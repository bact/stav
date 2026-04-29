# SPDX-FileCopyrightText: 2026-present Arthit Suriyawongkul
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""Global IRI → metadata registry and public vocabulary utility functions."""

from __future__ import annotations

_REGISTRY: dict = {}


def _register(meta: dict) -> None:
    """Register IRI → metadata entries from a generated vocab module.

    Called automatically at import time by each generated vocab file.
    Callers should not call this directly — use the recipe-based codegen.
    """
    _REGISTRY.update(meta)


def label(iri: str) -> str:
    """Return the human-readable label for *iri*, or empty string if unknown."""
    return _REGISTRY.get(iri, {}).get("label", "")


def definition(iri: str) -> str:
    """Return the definition text for *iri*, or empty string if unknown."""
    return _REGISTRY.get(iri, {}).get("definition", "")


def datatype(iri: str) -> str:
    """Return the expected XSD datatype for *iri*.

    Defaults to ``"xsd:anyURI"`` for ontology class/individual terms — they
    are IRI references.  Data properties may carry a more specific type such
    as ``"xsd:string"``, ``"xsd:integer"``, or ``"xsd:date"``.
    """
    return _REGISTRY.get(iri, {}).get("datatype", "xsd:anyURI")


def broader(iri: str) -> tuple:
    """Return parent-term IRIs for *iri* (``skos:broader`` / ``rdfs:subClassOf``)."""
    return _REGISTRY.get(iri, {}).get("broader", ())


def source_vocab(iri: str) -> str:
    """Return the source vocabulary identifier for *iri*, or empty string."""
    return _REGISTRY.get(iri, {}).get("source_vocab", "")


def validate(iri: str, value: object) -> bool:
    """Return True if *value* is compatible with the expected ``datatype`` for *iri*.

    Uses simple XSD type-mapping rules:

    * ``xsd:string`` / ``xsd:anyURI`` / ``xsd:normalizedString`` → ``str``
    * ``xsd:integer`` / ``xsd:int`` / ``xsd:positiveInteger`` / ``xsd:nonNegativeInteger`` → ``int``
    * ``xsd:boolean`` → ``bool``
    * unknown / missing datatype → always ``True`` (no constraint enforced)
    """
    dt = datatype(iri)
    if dt in ("xsd:string", "xsd:anyURI", "xsd:normalizedString"):
        return isinstance(value, str)
    if dt in ("xsd:integer", "xsd:int", "xsd:positiveInteger", "xsd:nonNegativeInteger"):
        return isinstance(value, int)
    if dt == "xsd:boolean":
        return isinstance(value, bool)
    return True
