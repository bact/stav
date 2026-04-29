# SPDX-FileCopyrightText: 2026-present Arthit Suriyawongkul
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""CLI entry point for STAV vocabulary code generation.

Two usage modes
---------------

**Recipe mode** — process a JSON recipe file that fully specifies sources,
filters, and output path (suitable for automated regeneration)::

    python -m stav.codegen.generate tools/recipes/dpv_ai.json
    python -m stav.codegen.generate tools/recipes/dpv_ai.json tools/recipes/spdx_ai.json

**Interactive mode** — point directly at a vocabulary source file; the CLI
detects the namespace and prompts for a submodule name::

    python -m stav.codegen.generate my_vocab.ttl
    python -m stav.codegen.generate my_vocab.csv --submodule custom.terms

Recipe schema
-------------
.. code-block:: json

    {
      "source_desc": "W3C DPV AI Extension v2.3",
      "submodule": "dpv.ai",
      "output": "../../src/stav/dpv/ai.py",
      "sources": [
        {"path": "../../../dpv/2.3/ai/ai.csv", "format": "csv", "source_vocab": "DPV-AI"}
      ],
      "enums": [
        {
          "name": "AITechnique",
          "doc": "AI technique types.",
          "filter": {
            "broader_in": ["https://w3id.org/dpv/ai#Technique"],
            "include_roots": true
          }
        }
      ]
    }

Filter modes (exactly one per enum)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
``broader_in``
    Transitive ancestor match on the ``broader`` / ``hasbroader`` field.
    ``include_roots`` (default *true*) also includes the listed root terms.

``types_in``
    Match by ``rdf:type`` IRI — for SPDX-style ``NamedIndividual`` enums.

``iris``
    Explicit allowlist of IRIs (ordered).
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from textwrap import indent

from stav.codegen import parsers
from stav.codegen.emitter import emit
from stav.codegen.grouper import (
    build_ancestor_map,
    filter_by_broader,
    filter_by_iris,
    filter_by_types,
)
from stav.codegen.model import EnumSpec, VocabModule, VocabTerm
from stav.codegen.namespace import NamespaceHint
from stav.codegen.namespace import detect as detect_namespace

# ── helpers ────────────────────────────────────────────────────────────────


def _is_recipe(path: str) -> bool:
    """Return True when *path* looks like a JSON recipe rather than a vocab source."""
    p = Path(path)
    if p.suffix.lower() != ".json":
        return False
    try:
        doc = json.loads(p.read_text(encoding="utf-8"))
        # Recipes have "enums" and "sources" keys; raw JSON-LD has "@graph"
        return isinstance(doc, dict) and "enums" in doc and "sources" in doc
    except Exception:
        return False


def _scaffold_package(pkg_dir: Path, submodule: str) -> None:
    """Create a minimal ``__init__.py`` for an intermediate namespace package.

    Each namespace level (e.g. ``stav/dpv/__init__.py``) gets a
    ``__stav_namespace__`` marker so tools can introspect the hierarchy.

    Does *not* overwrite an existing ``__init__.py``.
    """
    init = pkg_dir / "__init__.py"
    if init.exists():
        return
    # submodule = "dpv.ai" → parent namespace of the leaf = "dpv"
    ns = submodule.rsplit(".", 1)[0] if "." in submodule else submodule
    init.write_text(
        "# SPDX-FileCopyrightText: 2026-present Arthit Suriyawongkul\n"
        "# SPDX-License-Identifier: Apache-2.0\n"
        f'"""STAV vocabulary namespace: {ns}."""\n\n'
        f'__stav_namespace__ = "{ns}"\n',
        encoding="utf-8",
    )
    print(f"  Scaffolded: {init}", file=sys.stderr)


def _prompt_submodule(hint: NamespaceHint, src_path: Path) -> str:
    """Interactively ask the user for a Python submodule name.

    Displays any namespace / title detected from the source file, shows the
    suggested dotted name derived from the IRI, and reads a line from stdin.
    Pressing Enter accepts the suggestion.

    Returns the chosen submodule name (e.g. ``"dpv.ai"``).
    """
    print(file=sys.stderr)
    print("─" * 60, file=sys.stderr)
    print(f"Source file : {src_path.name}", file=sys.stderr)
    if hint.title:
        print(f"Title       : {hint.title}", file=sys.stderr)
    if hint.namespace_iri:
        print(f"Namespace   : {hint.namespace_iri}", file=sys.stderr)
    if hint.version:
        print(f"Version     : {hint.version}", file=sys.stderr)
    suggestion = hint.suggested_submodule or src_path.stem.replace("-", "_").lower()
    print(f"Suggested   : {suggestion}", file=sys.stderr)
    print("─" * 60, file=sys.stderr)

    try:
        entered = input(f"Submodule name [Enter = '{suggestion}']: ").strip()
    except (EOFError, KeyboardInterrupt):
        print("\nAborted.", file=sys.stderr)
        sys.exit(1)

    return entered if entered else suggestion


def _submodule_to_output(submodule: str, repo_root: Path) -> Path:
    """Convert ``"dpv.ai"`` to ``<repo_root>/src/stav/dpv/ai.py``."""
    parts = submodule.split(".")
    return repo_root / "src" / "stav" / Path(*parts).with_suffix(".py")


# ── recipe mode ────────────────────────────────────────────────────────────


def run_recipe(recipe_path: str) -> None:
    """Process a JSON recipe file and write the generated Python module."""
    rp = Path(recipe_path).resolve()
    recipe = json.loads(rp.read_text(encoding="utf-8"))

    submodule = recipe.get("submodule", "")

    # Load all source terms
    all_terms: list[VocabTerm] = []
    for src in recipe.get("sources", []):
        src_path = (rp.parent / src["path"]).resolve()
        fmt = src.get("format")
        vocab = src.get("source_vocab", "")
        terms = parsers.parse(str(src_path), fmt=fmt, source_vocab=vocab)
        all_terms.extend(terms)
        print(f"  Loaded {len(terms):>4} terms from {src_path.name}", file=sys.stderr)

    ancestor_map = build_ancestor_map(all_terms)
    enum_specs = _build_enum_specs(recipe.get("enums", []), all_terms, ancestor_map)

    emit_constants = recipe.get("emit_constants", True)
    module = VocabModule(
        output_path=recipe["output"],
        source_desc=recipe.get("source_desc", rp.stem),
        enums=enum_specs,
        all_terms=all_terms if emit_constants else [],
        emit_constants=emit_constants,
    )

    out_path = (rp.parent / recipe["output"]).resolve()
    out_path.parent.mkdir(parents=True, exist_ok=True)

    # Scaffold intermediate __init__.py files
    if submodule:
        _scaffold_intermediates(out_path.parent, submodule, rp)

    rel_recipe = _try_relative(rp)
    source = emit(module, recipe_path=str(rel_recipe), submodule=submodule)
    out_path.write_text(source, encoding="utf-8")
    print(f"  Written: {out_path}", file=sys.stderr)


def _build_enum_specs(
    enum_defs: list[dict],
    all_terms: list[VocabTerm],
    ancestor_map: dict[str, set[str]],
) -> list[EnumSpec]:
    specs: list[EnumSpec] = []
    for edef in enum_defs:
        class_name = edef["name"]
        doc = edef.get("doc", f"{class_name} vocabulary.")
        flt = edef.get("filter", {})

        if "broader_in" in flt:
            matched = filter_by_broader(
                all_terms,
                flt["broader_in"],
                include_roots=flt.get("include_roots", True),
                ancestor_map=ancestor_map,
            )
        elif "types_in" in flt:
            matched = filter_by_types(all_terms, flt["types_in"])
        elif "iris" in flt:
            matched = filter_by_iris(all_terms, flt["iris"])
        else:
            print(f"  WARNING: enum '{class_name}' has no recognised filter — skipped.", file=sys.stderr)
            continue

        print(f"  {class_name}: {len(matched)} terms", file=sys.stderr)
        specs.append(EnumSpec(class_name=class_name, terms=matched, docstring=doc))

    return specs


def _scaffold_intermediates(out_dir: Path, submodule: str, rp: Path) -> None:
    """Walk up from the output dir and scaffold missing __init__.py files.

    Stops when we reach the ``src/stav`` package root (which already has one).
    """
    # Find src/stav root by looking for the stav package marker
    stav_root = out_dir
    for _ in range(6):  # reasonable depth limit
        if (stav_root / "__about__.py").exists() or stav_root.name == "stav":
            break
        stav_root = stav_root.parent

    # Collect all dirs between stav_root and out_dir (exclusive of both)
    dirs_to_check: list[Path] = []
    d = out_dir
    while d != stav_root and d != d.parent:
        dirs_to_check.append(d)
        d = d.parent

    # Build the namespace prefix for each level
    parts = submodule.split(".")
    for i, pkg_dir in enumerate(reversed(dirs_to_check)):
        ns = ".".join(parts[: i + 1])
        _scaffold_package(pkg_dir, ns)


# ── interactive mode ───────────────────────────────────────────────────────


def run_interactive(
    source_path: str,
    submodule_override: str | None,
    repo_root: Path,
    enum_names: list[str] | None = None,
) -> None:
    """Interactive single-file mode: detect namespace, prompt, generate a stub recipe.

    This does NOT attempt to auto-group enums (that requires domain knowledge).
    Instead it generates a template recipe JSON and a placeholder Python file
    so the user can then edit the recipe and re-run.

    Args:
        source_path: Path to the vocabulary source file.
        submodule_override: Dotted submodule name if passed via ``--submodule``.
        repo_root: Root of the stav repository.
        enum_names: List of enum class names to create (asked interactively when absent).
    """
    sp = Path(source_path).resolve()
    hint = detect_namespace(str(sp))

    # Determine submodule name
    if submodule_override:
        submodule = submodule_override
        print(f"  Using submodule: {submodule}", file=sys.stderr)
    else:
        submodule = _prompt_submodule(hint, sp)

    # Validate Python path
    for part in submodule.split("."):
        if not part.isidentifier():
            print(f"  ERROR: '{part}' is not a valid Python identifier.", file=sys.stderr)
            sys.exit(1)

    out_py = _submodule_to_output(submodule, repo_root)
    recipe_path = repo_root / "tools" / "recipes" / (submodule.replace(".", "_") + ".json")

    print(f"\n  Submodule : stav.{submodule}", file=sys.stderr)
    print(f"  Output    : {out_py}", file=sys.stderr)
    print(f"  Recipe    : {recipe_path}", file=sys.stderr)

    # Parse source to get a term count and a sample of top-level broader groups
    terms = parsers.parse(str(sp))
    broader_set: set[str] = set()
    for t in terms:
        broader_set.update(t.broader)
    broader_sample = sorted(broader_set)[:8]

    print(f"\n  Found {len(terms)} terms in source.", file=sys.stderr)
    if broader_sample:
        print("  Sample 'broader' values (use in filter.broader_in):", file=sys.stderr)
        for b in broader_sample:
            print(f"    {b}", file=sys.stderr)

    # Build recipe template
    rel_src = _try_relative(sp, start=recipe_path.parent)
    recipe_doc = {
        "source_desc": hint.title or sp.stem,
        "submodule": submodule,
        "output": str(_try_relative(out_py, start=recipe_path.parent)),
        "sources": [
            {
                "path": str(rel_src),
                "format": sp.suffix.lstrip(".") or "csv",
                "source_vocab": submodule.split(".")[-1].upper(),
            }
        ],
        "enums": [
            {
                "name": "MyEnum",
                "_comment": "Rename and duplicate this block for each enum class you want.",
                "doc": "Terms from this vocabulary.",
                "filter": {
                    "broader_in": broader_sample[:3] if broader_sample else [],
                    "include_roots": True,
                },
            }
        ],
    }

    recipe_path.parent.mkdir(parents=True, exist_ok=True)
    recipe_path.write_text(json.dumps(recipe_doc, indent=2), encoding="utf-8")
    print(f"\n  Recipe template written to: {recipe_path}", file=sys.stderr)
    print(
        f"  Edit the recipe, then run:\n    python -m stav.codegen.generate {_try_relative(recipe_path)}",
        file=sys.stderr,
    )


# ── utility ────────────────────────────────────────────────────────────────


def _try_relative(path: Path, start: Path | None = None) -> Path:
    try:
        return path.relative_to(start or Path.cwd())
    except ValueError:
        return path


# ── entry point ────────────────────────────────────────────────────────────


def _build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="python -m stav.codegen.generate",
        description="Generate Python vocab enums from ontology / taxonomy files.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Examples:\n"
            "  # Recipe mode (automated regeneration):\n"
            "  python -m stav.codegen.generate tools/recipes/dpv_ai.json\n\n"
            "  # Interactive mode (new vocabulary):\n"
            "  python -m stav.codegen.generate my_vocab.ttl\n"
            "  python -m stav.codegen.generate my_vocab.csv --submodule custom.terms\n"
        ),
    )
    p.add_argument(
        "inputs",
        nargs="+",
        metavar="FILE",
        help="Recipe JSON file(s) or vocabulary source file (TTL/CSV/JSON-LD/YAML).",
    )
    p.add_argument(
        "--submodule",
        "-s",
        metavar="DOTTED.NAME",
        default=None,
        help=(
            "Python submodule path for the generated module (e.g. dpv.ai). "
            "Only applies when a single vocabulary source file is given. "
            "If omitted, the CLI will prompt interactively."
        ),
    )
    p.add_argument(
        "--repo-root",
        metavar="DIR",
        default=None,
        help=(
            "Root of the stav repository. Used to resolve output paths in "
            "interactive mode. Defaults to the current working directory."
        ),
    )
    return p


def main(argv: list[str] | None = None) -> None:
    parser = _build_parser()
    args = parser.parse_args(argv)

    repo_root = Path(args.repo_root).resolve() if args.repo_root else Path.cwd()

    for inp in args.inputs:
        if _is_recipe(inp):
            print(f"Recipe: {inp}", file=sys.stderr)
            run_recipe(inp)
        else:
            print(f"Source file: {inp}", file=sys.stderr)
            if len(args.inputs) > 1 and args.submodule:
                print(
                    "  WARNING: --submodule applies to a single source file; ignoring for multi-file runs.",
                    file=sys.stderr,
                )
            run_interactive(
                inp,
                submodule_override=args.submodule if len(args.inputs) == 1 else None,
                repo_root=repo_root,
            )


if __name__ == "__main__":
    main()
