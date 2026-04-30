# SPDX-FileCopyrightText: 2026-present Arthit Suriyawongkul
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""Helpers for grouping flat VocabTerm lists into enum buckets."""

from __future__ import annotations

from stav.codegen.model import VocabTerm


def build_ancestor_map(terms: list[VocabTerm]) -> dict[str, set[str]]:
    """Build a map: iri → {all transitive ancestor IRIs}.

    Uses the ``broader`` field of each term.  Terms that lack an IRI in the
    corpus are still tracked as string anchors (e.g. when the broader IRI
    points to a term defined outside the parsed file).
    """
    direct: dict[str, set[str]] = {}
    for t in terms:
        direct.setdefault(t.iri, set()).update(t.broader)

    # Iterative closure
    changed = True
    while changed:
        changed = False
        for iri, parents in list(direct.items()):
            new = set()
            for p in parents:
                new |= direct.get(p, set())
            if not new.issubset(parents):
                direct[iri] |= new
                changed = True

    return direct


def filter_by_broader(
    terms: list[VocabTerm],
    roots: list[str],
    *,
    include_roots: bool = True,
    ancestor_map: dict[str, set[str]] | None = None,
) -> list[VocabTerm]:
    """Return terms whose transitive ancestors include any IRI in *roots*.

    Args:
        terms: Full corpus.
        roots: List of broader IRIs that define the scope of the enum.
        include_roots: If *True*, terms whose own IRI is in *roots* are
            included even when they have no further descendants.
        ancestor_map: Pre-built map from :func:`build_ancestor_map`; computed
            on the fly when absent.

    Returns:
        Filtered, deduplicated list preserving original order.
    """
    if ancestor_map is None:
        ancestor_map = build_ancestor_map(terms)

    root_set = set(roots)
    result: list[VocabTerm] = []
    seen: set[str] = set()

    for t in terms:
        if t.iri in seen:
            continue
        ancestors = ancestor_map.get(t.iri, set())
        is_root = t.iri in root_set
        matches_root = bool(ancestors & root_set)

        if matches_root or (include_roots and is_root):
            result.append(t)
            seen.add(t.iri)

    return result


def filter_by_types(
    terms: list[VocabTerm],
    type_iris: list[str],
) -> list[VocabTerm]:
    """Return terms whose ``types`` list contains any IRI in *type_iris*."""
    type_set = set(type_iris)
    return [t for t in terms if type_set.intersection(t.types)]


def filter_by_iris(
    terms: list[VocabTerm],
    iris: list[str],
) -> list[VocabTerm]:
    """Return terms whose IRI is in the explicit *iris* allowlist (ordered)."""
    iri_map = {t.iri: t for t in terms}
    result: list[VocabTerm] = []
    seen: set[str] = set()
    for iri in iris:
        t = iri_map.get(iri)
        if t and iri not in seen:
            result.append(t)
            seen.add(iri)
    return result


def filter_by_iri_prefix(
    terms: list[VocabTerm],
    prefix: str,
) -> list[VocabTerm]:
    """Return terms whose IRI starts with *prefix*.

    Used to isolate terms belonging to a single ontology profile, e.g.
    ``"https://spdx.org/rdf/3.0.1/terms/AI/"`` to restrict to the SPDX AI
    profile without cross-contamination from Dataset or Core terms.
    """
    return [t for t in terms if t.iri.startswith(prefix)]
