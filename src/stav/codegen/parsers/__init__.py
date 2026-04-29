# SPDX-FileCopyrightText: 2026-present Arthit Suriyawongkul
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""Format-dispatching parser entry point."""

from __future__ import annotations

from pathlib import Path

from stav.codegen.model import VocabTerm


def parse(path: str, fmt: str | None = None, **kwargs) -> list[VocabTerm]:
    """Parse a vocabulary file and return a flat list of :class:`VocabTerm`.

    Args:
        path: Path to the source file.
        fmt:  Format override — one of ``"csv"``, ``"ttl"``, ``"jsonld"``,
              ``"yaml"``.  When *None* the format is inferred from the file
              extension.
        **kwargs: Passed through to the format-specific parser.

    Returns:
        Flat list of all terms found in the source.
    """
    p = Path(path)
    detected = fmt or _detect(p)

    if detected == "csv":
        from stav.codegen.parsers.csv_parser import parse as _parse

        return _parse(path, **kwargs)
    if detected in ("ttl", "n3", "turtle"):
        from stav.codegen.parsers.ttl_parser import parse as _parse

        return _parse(path, **kwargs)
    if detected in ("jsonld", "json"):
        from stav.codegen.parsers.jsonld_parser import parse as _parse

        return _parse(path, **kwargs)
    if detected in ("yaml", "yml"):
        from stav.codegen.parsers.yaml_parser import parse as _parse

        return _parse(path, **kwargs)

    raise ValueError(f"Cannot determine parser for '{p.name}'. Pass fmt='csv'|'ttl'|'jsonld'|'yaml' explicitly.")


def _detect(p: Path) -> str:
    ext = p.suffix.lower().lstrip(".")
    _map = {
        "csv": "csv",
        "ttl": "ttl",
        "n3": "n3",
        "jsonld": "jsonld",
        "json": "json",
        "yaml": "yaml",
        "yml": "yaml",
    }
    return _map.get(ext, ext)
