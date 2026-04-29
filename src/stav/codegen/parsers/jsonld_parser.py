# SPDX-FileCopyrightText: 2026-present Arthit Suriyawongkul
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""JSON-LD vocabulary parser (stdlib only)."""

from __future__ import annotations

import json
import re
from pathlib import Path

from stav.codegen.model import VocabTerm

_OWL_NAMED_INDIVIDUAL = "http://www.w3.org/2002/07/owl#NamedIndividual"
_OWL_CLASS = "http://www.w3.org/2002/07/owl#Class"
_RDFS_CLASS = "http://www.w3.org/2000/01/rdf-schema#Class"
_SKOS_CONCEPT = "http://www.w3.org/2004/02/skos/core#Concept"
_RDFS_LABEL = "http://www.w3.org/2000/01/rdf-schema#label"
_RDFS_COMMENT = "http://www.w3.org/2000/01/rdf-schema#comment"
_RDFS_SUBCLASS = "http://www.w3.org/2000/01/rdf-schema#subClassOf"
_SKOS_DEF = "http://www.w3.org/2004/02/skos/core#definition"
_SKOS_BROADER = "http://www.w3.org/2004/02/skos/core#broader"
_SKOS_PREF = "http://www.w3.org/2004/02/skos/core#prefLabel"

_TERM_TYPES = {_OWL_NAMED_INDIVIDUAL, _OWL_CLASS, _RDFS_CLASS, _SKOS_CONCEPT}


def parse(path: str, source_vocab: str = "", **_) -> list[VocabTerm]:
    """Parse a JSON-LD file into :class:`~stav.codegen.model.VocabTerm` objects.

    Supports both expanded and compacted JSON-LD.  The SPDX ``spdx-model.json-ld``
    and DPV ``ai.jsonld`` formats are both handled.

    Args:
        path: Path to the ``.jsonld`` or ``.json`` file.
        source_vocab: Human-readable source label; defaults to the filename stem.

    Returns:
        Flat list of :class:`VocabTerm`.
    """
    p = Path(path)
    vocab = source_vocab or p.stem

    with p.open(encoding="utf-8") as fh:
        doc = json.load(fh)

    # Collect @context prefix map for IRI expansion
    context = _collect_context(doc)

    # Gather nodes: top-level doc, or items in @graph
    nodes = doc if isinstance(doc, list) else doc.get("@graph", [doc])

    terms: list[VocabTerm] = []
    seen: set[str] = set()

    for node in nodes:
        if not isinstance(node, dict):
            continue
        term = _node_to_term(node, context, vocab)
        if term and term.iri not in seen:
            seen.add(term.iri)
            terms.append(term)

    return terms


def _node_to_term(node: dict, context: dict[str, str], vocab: str) -> VocabTerm | None:
    iri = _expand(node.get("@id", ""), context)
    if not iri or iri.startswith("_:"):
        return None

    raw_types = node.get("@type", [])
    if isinstance(raw_types, str):
        raw_types = [raw_types]
    types = [_expand(t, context) for t in raw_types]

    if not any(t in _TERM_TYPES for t in types):
        return None

    name = _local_name(iri)
    if not name or not re.match(r"^[A-Za-z_]", name):
        return None

    label = _get_literal(node, [_RDFS_LABEL, _SKOS_PREF], context) or name
    definition = _get_literal(node, [_SKOS_DEF, _RDFS_COMMENT], context) or ""

    broader: list[str] = []
    for pred in [_RDFS_SUBCLASS, _SKOS_BROADER]:
        val = node.get(pred) or node.get(_compact(pred, context), [])
        if isinstance(val, str):
            broader.append(_expand(val, context))
        elif isinstance(val, dict):
            broader.append(_expand(val.get("@id", ""), context))
        elif isinstance(val, list):
            for item in val:
                if isinstance(item, str):
                    broader.append(_expand(item, context))
                elif isinstance(item, dict):
                    broader.append(_expand(item.get("@id", ""), context))

    return VocabTerm(
        name=name,
        iri=iri,
        label=label,
        definition=definition,
        broader=[b for b in broader if b],
        types=types,
        source_vocab=vocab,
    )


def _collect_context(doc: dict | list) -> dict[str, str]:
    """Build a prefix → IRI expansion map from @context."""
    ctx: dict[str, str] = {}
    if isinstance(doc, list):
        return ctx
    raw = doc.get("@context", {})
    if isinstance(raw, str):
        return ctx
    if isinstance(raw, list):
        raw = {k: v for item in raw if isinstance(item, dict) for k, v in item.items()}
    for k, v in raw.items():
        if isinstance(v, str) and not k.startswith("@"):
            ctx[k] = v
    return ctx


def _expand(iri: str, context: dict[str, str]) -> str:
    """Expand a prefixed IRI or return as-is if already absolute."""
    if not iri:
        return ""
    if iri.startswith("http://") or iri.startswith("https://"):
        return iri
    if ":" in iri:
        prefix, local = iri.split(":", 1)
        if prefix in context:
            return context[prefix] + local
    return iri


def _compact(iri: str, context: dict[str, str]) -> str:
    """Try to compact a full IRI to a prefixed form (best-effort)."""
    for prefix, base in context.items():
        if iri.startswith(base):
            return prefix + ":" + iri[len(base) :]
    return iri


def _local_name(iri: str) -> str:
    raw = iri.rsplit("#", maxsplit=1)[-1] if "#" in iri else iri.rstrip("/").split("/")[-1]
    s = re.sub(r"[^A-Za-z0-9_]", "_", raw)
    if s and s[0].isdigit():
        s = "_" + s
    s = re.sub(r"_+", "_", s).strip("_")
    return s


def _get_literal(node: dict, predicates: list[str], context: dict[str, str]) -> str:
    for pred in predicates:
        for key in [pred, _compact(pred, context)]:
            val = node.get(key)
            if val is None:
                continue
            if isinstance(val, str):
                return val
            if isinstance(val, list):
                for item in val:
                    if isinstance(item, str):
                        return item
                    if isinstance(item, dict):
                        v = item.get("@value", "")
                        lang = item.get("@language", "")
                        if lang in ("", "en", "en-US"):
                            return v
            if isinstance(val, dict):
                return val.get("@value", "")
    return ""
