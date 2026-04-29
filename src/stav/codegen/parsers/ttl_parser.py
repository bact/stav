# SPDX-FileCopyrightText: 2026-present Arthit Suriyawongkul
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""Turtle / RDF parser (requires ``rdflib``)."""

from __future__ import annotations

import re
from pathlib import Path

from stav.codegen.model import VocabTerm

try:
    import rdflib
    from rdflib import Graph, Literal, URIRef
    from rdflib.namespace import OWL, RDF, RDFS, SKOS

    _RDFLIB = True
except ImportError:
    _RDFLIB = False

_SKOS_BROADER = "http://www.w3.org/2004/02/skos/core#broader"
_SKOS_DEF = "http://www.w3.org/2004/02/skos/core#definition"
_SKOS_PREF = "http://www.w3.org/2004/02/skos/core#prefLabel"
_HAS_BROADER = "https://w3id.org/dpv#hasbroader"  # DPV object prop (lower-case col)


def parse(path: str, source_vocab: str = "", **_) -> list[VocabTerm]:
    """Parse a Turtle file into :class:`~stav.codegen.model.VocabTerm` objects.

    Extracts:

    * ``owl:NamedIndividual`` — for SPDX-style enumeration values.
    * ``owl:Class`` / ``rdfs:Class`` — for ontology classes (DPV, STAV, …).
    * ``skos:Concept`` — for SKOS vocabularies.

    Each term gets its ``broader`` list populated from ``rdfs:subClassOf``,
    ``skos:broader``, and the DPV-style ``hasbroader`` object property.

    Args:
        path: Path to the ``.ttl`` (or ``.n3``) file.
        source_vocab: Human-readable source label; defaults to the filename stem.

    Returns:
        Flat list of :class:`VocabTerm`.
    """
    if not _RDFLIB:
        raise ImportError("rdflib is required for Turtle parsing. Install it: pip install rdflib")

    p = Path(path)
    vocab = source_vocab or p.stem

    g = Graph()
    g.parse(str(p), format="turtle")

    terms: list[VocabTerm] = []
    seen: set[str] = set()

    target_types = {
        str(OWL.NamedIndividual),
        str(OWL.Class),
        str(RDFS.Class),
        "http://www.w3.org/2004/02/skos/core#Concept",
    }

    for subj in g.subjects():
        if not isinstance(subj, URIRef):
            continue
        iri = str(subj)
        if iri in seen:
            continue

        rdf_types = {str(t) for t in g.objects(subj, RDF.type)}
        if not rdf_types.intersection(target_types):
            continue

        name = _local_name(iri)
        if not name or not name[0].isalpha():
            continue

        label = _first_literal(g, subj, [RDFS.label, URIRef(_SKOS_PREF)]) or name
        definition = (
            _first_literal(
                g,
                subj,
                [
                    URIRef(_SKOS_DEF),
                    RDFS.comment,
                ],
            )
            or ""
        )

        broader: list[str] = []
        for pred in [RDFS.subClassOf, URIRef(_SKOS_BROADER)]:
            for obj in g.objects(subj, pred):
                if isinstance(obj, URIRef):
                    broader.append(str(obj))

        seen.add(iri)
        terms.append(
            VocabTerm(
                name=name,
                iri=iri,
                label=label,
                definition=definition,
                broader=broader,
                types=list(rdf_types),
                source_vocab=vocab,
            )
        )

    return terms


def _local_name(iri: str) -> str:
    """Extract and sanitize the local name into a valid Python identifier."""
    raw = iri.rsplit("#", maxsplit=1)[-1] if "#" in iri else iri.rstrip("/").split("/")[-1]
    # Replace anything not alphanumeric/underscore with underscore
    s = re.sub(r"[^A-Za-z0-9_]", "_", raw)
    if s and s[0].isdigit():
        s = "_" + s
    # Collapse consecutive underscores
    s = re.sub(r"_+", "_", s).strip("_")
    return s


def _first_literal(g, subj, predicates) -> str:
    """Return the string value of the first matching literal, preferring English."""
    candidates: list[str] = []
    for pred in predicates:
        for obj in g.objects(subj, pred):
            if isinstance(obj, Literal):
                val = str(obj).strip()
                if obj.language in (None, "en", "en-US"):
                    return val
                candidates.append(val)
    return candidates[0] if candidates else ""
