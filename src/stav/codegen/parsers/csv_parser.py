# SPDX-FileCopyrightText: 2026-present Arthit Suriyawongkul
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""CSV vocabulary parser.

Handles the DPV CSV format (columns: term, type, iri, label, definition,
dpvtype, subclassof, hasbroader, scopenote, created, modified, vocab,
namespace) and any simpler CSV with at least ``name`` and ``iri`` columns.
"""

from __future__ import annotations

import csv
import re
from pathlib import Path

from stav.codegen.model import VocabTerm

# DPV exports IRIs separated by semicolons in multi-value fields.
_SEPARATOR = re.compile(r"\s*;\s*")

# Columns present in the DPV export format.
_DPV_COLS = {"term", "iri", "label", "definition", "hasbroader", "subclassof", "vocab"}


def parse(path: str, source_vocab: str = "", **_) -> list[VocabTerm]:
    """Parse a CSV file into :class:`~stav.codegen.model.VocabTerm` objects.

    Supports:
    * DPV-style exports (auto-detected by column names).
    * Generic CSVs with at minimum ``name``/``term`` and ``iri`` columns.

    Args:
        path: Path to the CSV file.
        source_vocab: Override for the ``source_vocab`` label; defaults to the
            ``vocab`` column value or the filename stem.

    Returns:
        List of terms.  Terms whose ``type`` column is not ``"class"`` or
        ``"property"`` (e.g. ``"individual"``) are included — callers filter
        by broader/type as needed.
    """
    p = Path(path)
    terms: list[VocabTerm] = []

    with p.open(newline="", encoding="utf-8") as fh:
        sample = fh.read(2048)
        fh.seek(0)
        dialect = csv.Sniffer().sniff(sample, delimiters=",\t")
        reader = csv.DictReader(fh, dialect=dialect)

        for row in reader:
            row = {k.strip().strip('"'): v.strip().strip('"') for k, v in row.items() if k}
            term = _extract(path, row, source_vocab or p.stem)
            if term is not None:
                terms.append(term)

    return terms


def _extract(path: str, row: dict[str, str], default_vocab: str) -> VocabTerm | None:
    # Determine column names (DPV vs generic)
    is_dpv = _DPV_COLS.issubset(set(row.keys()))

    name_raw = row.get("term") or row.get("name") or row.get("id") or ""
    iri = row.get("iri") or row.get("uri") or row.get("@id") or ""

    if not name_raw or not iri:
        return None

    name = _to_identifier(name_raw)
    label = row.get("label") or row.get("prefLabel") or name_raw
    definition = row.get("definition") or row.get("comment") or row.get("scopenote") or ""

    broader_raw = row.get("hasbroader") or row.get("broader") or row.get("subclassof") or ""
    broader = [b.strip() for b in _SEPARATOR.split(broader_raw) if b.strip()]

    vocab = row.get("vocab") or default_vocab

    return VocabTerm(
        name=name,
        iri=iri,
        label=label,
        definition=definition,
        broader=broader,
        source_vocab=vocab,
    )


def _to_identifier(raw: str) -> str:
    """Convert a raw term name to a valid Python identifier."""
    # Replace spaces/hyphens/dots with underscores, strip leading digits
    s = re.sub(r"[^A-Za-z0-9_]", "_", raw)
    if s and s[0].isdigit():
        s = "_" + s
    return s
