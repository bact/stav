# SPDX-FileCopyrightText: 2026-present Arthit Suriyawongkul
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""Python source code emitter for enum vocab modules."""

from __future__ import annotations

import keyword
import textwrap
from datetime import datetime, timezone

from stav.codegen.model import EnumSpec, VocabModule, VocabTerm


def _safe_name(name: str) -> str:
    """Append ``_`` to names that are Python keywords (e.g. ``from`` → ``from_``)."""
    return f"{name}_" if keyword.iskeyword(name) else name

_BANNER = """\
# SPDX-FileCopyrightText: 2026-present Arthit Suriyawongkul
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0
#
# AUTO-GENERATED — do not edit manually.
# Source: {source_desc}
# Generated: {timestamp}
# Regenerate: python -m stav.codegen.generate {recipe}
"""

_MODULE_DOCSTRING = '"""{module_doc}"""\n'

_IMPORTS = """\
from __future__ import annotations

from stav._registry import _register
from stav.term import _StavVocabEnum
"""

_NAMESPACE_VAR = '__stav_namespace__ = "{submodule}"\n'

_CLASS_TEMPLATE = """\
class {class_name}(_StavVocabEnum):
{docstring}
{members}
"""


def emit(module: VocabModule, recipe_path: str = "", submodule: str = "") -> str:
    """Render a :class:`VocabModule` as Python source code.

    Constants are plain strings (IRIs) so they work directly as MLflow tags,
    Pitloom setter arguments, f-strings, and SBOM values with no wrapping.
    Metadata (label, definition, broader, datatype) is registered in the
    global IRI registry at import time and accessed via :mod:`stav._registry`.

    Args:
        module: The module specification with enums to emit.
        recipe_path: Path to the recipe file; shown in the regeneration hint.
        submodule: Python dotted submodule path (e.g. ``"vocab.dpv.ai"``);
            written as ``__stav_namespace__``.

    Returns:
        Full Python source code as a string.
    """
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    sections: list[str] = [
        _BANNER.format(
            source_desc=module.source_desc,
            timestamp=now,
            recipe=recipe_path or "<recipe.json>",
        ),
        _MODULE_DOCSTRING.format(module_doc=_module_doc(module)),
        _IMPORTS,
    ]

    if submodule:
        sections.append(_NAMESPACE_VAR.format(submodule=submodule))

    if module.emit_constants and module.all_terms:
        sections.append(_emit_constants(module.all_terms))

    for spec in module.enums:
        sections.append(_emit_class(spec))

    # Metadata registry — constants + enum members, deduped by IRI
    sections.append(_emit_register(module))

    # __all__: constants first, then enum class names
    const_names = _constant_names(module.all_terms) if module.emit_constants else []
    enum_names = [spec.class_name for spec in module.enums]
    all_names = const_names + enum_names
    all_list = ", ".join(f'"{n}"' for n in all_names)
    sections.append(f"__all__ = [{all_list}]\n")

    return "\n".join(sections)


def _module_doc(module: VocabModule) -> str:
    has_consts = module.emit_constants and module.all_terms
    has_enums = bool(module.enums)
    parts = []
    if has_consts:
        parts.append(f"{len(module.all_terms)} term constants (accessible as ``module.TermName``)")
    if has_enums:
        names = ", ".join(f":class:`{s.class_name}`" for s in module.enums)
        parts.append(f"grouped enums: {names}")
    summary = "; ".join(parts) if parts else "Vocabulary terms."
    return f"Vocabulary from {module.source_desc}.\n\n{summary}."


def _emit_constants(terms: list[VocabTerm]) -> str:
    """Emit module-level plain string IRI constants for every term."""
    lines = [
        "# ── Individual term constants ─────────────────────────────────────────────────────",
        "# Plain string IRIs — use directly with MLflow, Pitloom, SBOM serialisers.",
        "# Metadata (label, definition, broader) via: stav.label(NaturalPerson) etc.",
    ]
    seen: dict[str, int] = {}
    for term in sorted(terms, key=lambda t: t.name.lower()):
        name = _safe_name(term.name)
        if name in seen:
            seen[name] += 1
            name = f"{name}_{seen[name]}"
        else:
            seen[name] = 0
        comment = f"  # {term.label}" if term.label and term.label != term.name else ""
        lines.append(f"{name} = {term.iri!r}{comment}")
    return "\n".join(lines) + "\n"


def _constant_names(terms: list[VocabTerm]) -> list[str]:
    """Return deduplicated Python names for the constants section."""
    names: list[str] = []
    seen: dict[str, int] = {}
    for term in sorted(terms, key=lambda t: t.name.lower()):
        name = _safe_name(term.name)
        if name in seen:
            seen[name] += 1
            name = f"{name}_{seen[name]}"
        else:
            seen[name] = 0
        names.append(name)
    return names


def _emit_class(spec: EnumSpec) -> str:
    if not spec.terms:
        return f"# {spec.class_name}: no terms matched the filter — skipped.\n"

    docstring = _format_docstring(spec.docstring or f"{spec.class_name} vocabulary.")

    seen_names: dict[str, int] = {}
    members_lines: list[str] = []

    for term in sorted(spec.terms, key=lambda t: t.name.lower()):
        raw = term.name
        if raw in seen_names:
            seen_names[raw] += 1
            raw = f"{raw}_{seen_names[raw]}"
        else:
            seen_names[raw] = 0
        raw = _safe_name(raw)
        comment = f"  # {term.label}" if term.label and term.label != raw else ""
        members_lines.append(f"    {raw} = {term.iri!r}{comment}")

    members = "\n".join(members_lines)
    return _CLASS_TEMPLATE.format(
        class_name=spec.class_name,
        docstring=docstring,
        members=members,
    )


def _emit_register(module: VocabModule) -> str:
    """Emit the _register({...}) call that populates metadata at import time.

    Collects all_terms (constants) plus every term in every enum spec so the
    registry is complete even when enum members are excluded from the constants
    block (e.g. SPDX profile modules where vocab members live only in enums).
    """
    all_to_register: list[VocabTerm] = list(module.all_terms)
    seen_iris: set[str] = {t.iri for t in all_to_register}
    for spec in module.enums:
        for t in spec.terms:
            if t.iri not in seen_iris:
                all_to_register.append(t)
                seen_iris.add(t.iri)

    if not all_to_register:
        return ""

    lines = [
        "# ── Metadata registry ──────────────────────────────────────────────────────────────",
        "# Populated at import time so stav.label() / .definition() / .broader() work.",
        "_register({",
    ]
    for term in sorted(all_to_register, key=lambda t: t.iri):
        entry_parts = []
        if term.label:
            entry_parts.append(f'"label": {term.label!r}')
        if term.definition:
            defn = term.definition.replace("\n", " ").strip()
            if len(defn) > 300:
                defn = defn[:297] + "..."
            entry_parts.append(f'"definition": {defn!r}')
        if term.broader:
            blist = ", ".join(repr(b) for b in term.broader)
            entry_parts.append(f'"broader": ({blist},)' if len(term.broader) == 1 else f'"broader": ({blist})')
        if term.source_vocab:
            entry_parts.append(f'"source_vocab": {term.source_vocab!r}')
        inner = ", ".join(entry_parts)
        lines.append(f"    {term.iri!r}: {{{inner}}},")
    lines.append("})\n")
    return "\n".join(lines)


def _format_docstring(text: str) -> str:
    """Wrap text as an indented docstring block."""
    lines = textwrap.wrap(text, width=88)
    if not lines:
        return '    """"""'
    if len(lines) == 1:
        return f'    """{lines[0]}"""'
    body = "\n".join("    " + ln for ln in lines)
    return f'    """\n{body}\n    """'
