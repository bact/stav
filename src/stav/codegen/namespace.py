# SPDX-FileCopyrightText: 2026-present Arthit Suriyawongkul
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""Detect preferred namespace / submodule name from a vocabulary source file.

The result is used to suggest a Python submodule path (e.g. ``dpv.ai``) when
the user runs the generator in interactive mode.
"""

from __future__ import annotations

import csv
import json
import re
from dataclasses import dataclass
from pathlib import Path

# ─── Well-known IRI base → Python prefix map ───────────────────────────────

_IRI_STRIP_PREFIXES = [
    "https://w3id.org/",
    "http://w3id.org/",
    "https://spdx.org/rdf/3.0.1/terms/",
    "http://spdx.org/rdf/3.0.1/terms/",
    "https://www.w3.org/ns/",
    "http://www.w3.org/ns/",
    "https://schema.org/",
    "http://schema.org/",
    "http://purl.org/dc/",
]

# Characters that are invalid in a Python identifier segment
_INVALID_ID = re.compile(r"[^A-Za-z0-9_]")


@dataclass
class NamespaceHint:
    """Information extracted from a vocabulary source file."""

    namespace_iri: str = ""
    """The base IRI / namespace URI of the vocabulary."""

    title: str = ""
    """Human-readable title of the vocabulary."""

    version: str = ""
    """Version string, if found."""

    suggested_submodule: str = ""
    """Best-guess Python submodule path derived from the IRI (e.g. ``dpv.ai``)."""


def detect(path: str, fmt: str | None = None) -> NamespaceHint:
    """Detect namespace information from a vocabulary source file.

    Args:
        path: Path to the vocabulary file.
        fmt: Format override — ``"csv"``, ``"ttl"``, ``"jsonld"``, ``"yaml"``.
             Auto-detected from extension when *None*.

    Returns:
        :class:`NamespaceHint` with as much information as could be extracted.
    """
    p = Path(path)
    detected_fmt = fmt or _ext_to_fmt(p.suffix.lower().lstrip("."))

    hint = NamespaceHint()

    try:
        if detected_fmt == "csv":
            _from_csv(p, hint)
        elif detected_fmt in ("ttl", "turtle", "n3"):
            _from_ttl(p, hint)
        elif detected_fmt in ("jsonld", "json"):
            _from_jsonld(p, hint)
        elif detected_fmt in ("yaml", "yml"):
            _from_yaml(p, hint)
    except Exception:
        pass

    if hint.namespace_iri and not hint.suggested_submodule:
        hint.suggested_submodule = iri_to_submodule(hint.namespace_iri)

    return hint


def iri_to_submodule(iri: str) -> str:
    """Derive a Python dotted submodule path from a namespace IRI.

    Examples::

        "https://w3id.org/dpv/ai#"   → "dpv.ai"
        "https://spdx.org/rdf/3.0.1/terms/Dataset/"  → "spdx.dataset"
        "http://schema.org/"         → "schema"
    """
    s = iri.rstrip("#/")
    for prefix in _IRI_STRIP_PREFIXES:
        if s.startswith(prefix):
            s = s[len(prefix) :]
            break
    else:
        # strip scheme + authority
        s = re.sub(r"^https?://[^/]+/", "", s)

    parts = [p for p in s.split("/") if p]

    # Clean each segment into a valid Python identifier
    clean: list[str] = []
    for seg in parts[:4]:  # max 4 levels deep
        seg = _INVALID_ID.sub("_", seg)
        seg = seg.strip("_")
        if seg and re.match(r"^[A-Za-z]", seg):
            clean.append(seg.lower())

    return ".".join(clean) if clean else ""


# ─── Per-format extractors ─────────────────────────────────────────────────


def _from_csv(p: Path, hint: NamespaceHint) -> None:
    with p.open(newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        for row in reader:
            row = {k.strip().strip('"'): v.strip().strip('"') for k, v in row.items() if k}
            ns = row.get("namespace") or row.get("ns") or ""
            vocab = row.get("vocab") or ""
            if ns:
                hint.namespace_iri = ns
                # Vocab column gives us a short name; use as leaf
                if vocab and vocab not in ns:
                    hint.suggested_submodule = (
                        iri_to_submodule(ns).rsplit(".", 1)[0] + "." + vocab if "." in iri_to_submodule(ns) else vocab
                    )
                break  # first data row is enough


def _from_ttl(p: Path, hint: NamespaceHint) -> None:
    text = p.read_text(encoding="utf-8", errors="replace")

    # Base prefix: @prefix : <...> or @base <...>
    m = re.search(r"@prefix\s+:\s+<([^>]+)>", text)
    if not m:
        m = re.search(r"@base\s+<([^>]+)>", text)
    if m:
        hint.namespace_iri = m.group(1)

    # Ontology IRI from <...> rdf:type owl:Ontology block
    m2 = re.search(r"<(https?://[^>]+)>\s+(?:a|rdf:type)\s+owl:Ontology", text)
    if m2 and not hint.namespace_iri:
        hint.namespace_iri = m2.group(1)

    # dct:title
    m3 = re.search(r'dct:title\s+"([^"]+)"', text)
    if m3:
        hint.title = m3.group(1)

    # owl:versionInfo
    m4 = re.search(r"owl:versionInfo\s+(\S+)", text)
    if m4:
        hint.version = m4.group(1).strip('"')


def _from_jsonld(p: Path, hint: NamespaceHint) -> None:
    with p.open(encoding="utf-8") as fh:
        doc = json.load(fh)

    # @context prefixes
    ctx = doc.get("@context", {}) if isinstance(doc, dict) else {}
    if isinstance(ctx, list):
        ctx = {k: v for item in ctx if isinstance(item, dict) for k, v in item.items()}
    base = ctx.get("@base", "") or ctx.get(":", "")
    if base:
        hint.namespace_iri = base

    # @graph → find ontology node
    nodes = doc if isinstance(doc, list) else doc.get("@graph", [])
    for node in nodes:
        if not isinstance(node, dict):
            continue
        types = node.get("@type", [])
        if isinstance(types, str):
            types = [types]
        if any("Ontology" in t for t in types):
            hint.namespace_iri = hint.namespace_iri or node.get("@id", "")
            for key in ("dct:title", "http://purl.org/dc/terms/title", "title"):
                if key in node:
                    v = node[key]
                    hint.title = v.get("@value", v) if isinstance(v, dict) else str(v)
                    break
            break


def _from_yaml(p: Path, hint: NamespaceHint) -> None:
    try:
        import yaml
    except ImportError:
        return
    with p.open(encoding="utf-8") as fh:
        doc = yaml.safe_load(fh)
    if not isinstance(doc, dict):
        return
    hint.namespace_iri = doc.get("namespace", "")
    hint.title = doc.get("title", "") or doc.get("vocab", "")
    hint.version = str(doc.get("version", ""))


def _ext_to_fmt(ext: str) -> str:
    return {
        "csv": "csv",
        "ttl": "ttl",
        "n3": "n3",
        "jsonld": "jsonld",
        "json": "json",
        "yaml": "yaml",
        "yml": "yaml",
    }.get(ext, ext)
