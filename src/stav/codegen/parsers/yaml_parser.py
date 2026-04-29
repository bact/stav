# SPDX-FileCopyrightText: 2026-present Arthit Suriyawongkul
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""YAML vocabulary parser (requires ``pyyaml``)."""

from __future__ import annotations

import re
from pathlib import Path

from stav.codegen.model import VocabTerm

try:
    import yaml as _yaml

    _PYYAML = True
except ImportError:
    _PYYAML = False


def parse(path: str, source_vocab: str = "", **_) -> list[VocabTerm]:
    """Parse a YAML vocabulary file into :class:`~stav.codegen.model.VocabTerm` objects.

    Expected YAML schema::

        vocab: my-vocab            # optional — used as source_vocab fallback
        namespace: https://example.com/vocab#   # base IRI; prepended when iri is absent
        terms:
          - name: MyTerm
            iri: https://example.com/vocab#MyTerm   # optional if namespace set
            label: My Term
            definition: A thing that does something.
            broader:
              - https://example.com/vocab#ParentTerm

    ``iri`` is optional when a ``namespace`` key is present at the root or
    term level; the IRI is then constructed as ``namespace + name``.

    Args:
        path: Path to the ``.yaml`` / ``.yml`` file.
        source_vocab: Human-readable source label; defaults to the ``vocab``
            key in the YAML or the filename stem.

    Returns:
        Flat list of :class:`VocabTerm`.
    """
    if not _PYYAML:
        raise ImportError("pyyaml is required for YAML parsing. Install it: pip install pyyaml")

    p = Path(path)
    with p.open(encoding="utf-8") as fh:
        doc = _yaml.safe_load(fh)

    if not isinstance(doc, dict):
        raise ValueError(f"YAML file '{p}' must have a mapping at the top level.")

    vocab = source_vocab or doc.get("vocab") or p.stem
    root_ns = doc.get("namespace", "")
    raw_terms = doc.get("terms", [])

    terms: list[VocabTerm] = []
    for entry in raw_terms:
        if not isinstance(entry, dict):
            continue

        name_raw = str(entry.get("name") or entry.get("id") or "")
        if not name_raw:
            continue

        ns = entry.get("namespace", root_ns)
        iri = entry.get("iri") or entry.get("uri") or (ns + name_raw if ns else "")
        if not iri:
            continue

        name = _to_identifier(name_raw)
        label = entry.get("label") or name_raw
        definition = entry.get("definition") or entry.get("description") or ""

        broader_raw = entry.get("broader") or entry.get("subclassOf") or []
        if isinstance(broader_raw, str):
            broader_raw = [broader_raw]
        broader = [str(b).strip() for b in broader_raw if b]

        terms.append(
            VocabTerm(
                name=name,
                iri=iri,
                label=label,
                definition=definition,
                broader=broader,
                source_vocab=vocab,
            )
        )

    return terms


def _to_identifier(raw: str) -> str:
    s = re.sub(r"[^A-Za-z0-9_]", "_", raw)
    if s and s[0].isdigit():
        s = "_" + s
    return s
