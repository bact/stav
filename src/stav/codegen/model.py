# SPDX-FileCopyrightText: 2026-present Arthit Suriyawongkul
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""Intermediate representation for vocabulary terms."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class VocabTerm:
    """One term from a vocabulary source."""

    name: str
    """Python-safe CamelCase or lowerCamelCase identifier (enum member name)."""

    iri: str
    """Full IRI — used as the enum value so SBOMs link back to the standard."""

    label: str = ""
    """Human-readable label (rdfs:label or CSV label column)."""

    definition: str = ""
    """Definition text (skos:definition or CSV definition column)."""

    broader: list[str] = field(default_factory=list)
    """Direct broader term IRIs (hasbroader / skos:broader / rdfs:subClassOf)."""

    types: list[str] = field(default_factory=list)
    """RDF types of this term (rdf:type IRIs) — used for NamedIndividual grouping."""

    source_vocab: str = ""
    """Human-readable identifier for the source ontology/vocabulary."""


@dataclass
class EnumSpec:
    """Specification for one generated Python enum class."""

    class_name: str
    """Python class name, e.g. ``AITechnique``."""

    terms: list[VocabTerm]
    """Ordered list of terms that become enum members."""

    docstring: str = ""
    """Docstring placed on the generated class."""

    source: str = ""
    """Source description shown in the generated file header comment."""


@dataclass
class VocabModule:
    """One generated Python source file containing several enum classes."""

    output_path: str
    """Destination path relative to the repo root."""

    source_desc: str
    """Human-readable description of the source data (goes into the file header)."""

    enums: list[EnumSpec]
    """Enum classes to emit, in order."""

    all_terms: list[VocabTerm] = field(default_factory=list)
    """All terms from all sources — emitted as module-level IRI string constants
    so the entire vocabulary is accessible by name (e.g. ``dpv.NaturalPerson``)."""

    emit_constants: bool = True
    """When True, emit module-level IRI constants for every term in ``all_terms``."""
