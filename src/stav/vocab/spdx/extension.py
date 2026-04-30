# SPDX-FileCopyrightText: 2026-present Arthit Suriyawongkul
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0
#
# AUTO-GENERATED — do not edit manually.
# Source: SPDX 3.0.1 Extension profile
# Generated: 2026-04-30T08:53:35Z
# Regenerate: python -m stav.codegen.generate tools/recipes/spdx_extension.json

"""Vocabulary from SPDX 3.0.1 Extension profile.

6 term constants (accessible as ``module.TermName``)."""

from __future__ import annotations

from stav._registry import _register
from stav.term import _StavVocabEnum

__stav_namespace__ = "vocab.spdx.extension"

# ── Individual term constants ─────────────────────────────────────────────────────
# Plain string IRIs — use directly with MLflow, Pitloom, SBOM serialisers.
# Metadata (label, definition, broader) via: stav.label(NaturalPerson) etc.
CdxPropertiesExtension = 'https://spdx.org/rdf/3.0.1/terms/Extension/CdxPropertiesExtension'
cdxProperty = 'https://spdx.org/rdf/3.0.1/terms/Extension/cdxProperty'
CdxPropertyEntry = 'https://spdx.org/rdf/3.0.1/terms/Extension/CdxPropertyEntry'
cdxPropName = 'https://spdx.org/rdf/3.0.1/terms/Extension/cdxPropName'
cdxPropValue = 'https://spdx.org/rdf/3.0.1/terms/Extension/cdxPropValue'
Extension = 'https://spdx.org/rdf/3.0.1/terms/Extension/Extension'

# ── Metadata registry ──────────────────────────────────────────────────────────────
# Populated at import time so stav.label() / .definition() / .broader() work.
_register({
    'https://spdx.org/rdf/3.0.1/terms/Extension/CdxPropertiesExtension': {"label": 'CdxPropertiesExtension', "definition": 'A type of extension consisting of a list of name value pairs.', "broader": ('https://spdx.org/rdf/3.0.1/terms/Extension/Extension',), "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Extension/CdxPropertyEntry': {"label": 'CdxPropertyEntry', "definition": 'A property name with an associated value.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Extension/Extension': {"label": 'Extension', "definition": 'A characterization of some aspect of an Element that is associated with the Element in a generalized fashion.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Extension/cdxPropName': {"label": 'cdxPropName', "definition": 'A name used in a CdxPropertyEntry name-value pair.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Extension/cdxPropValue': {"label": 'cdxPropValue', "definition": 'A value used in a CdxPropertyEntry name-value pair.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Extension/cdxProperty': {"label": 'cdxProperty', "definition": 'Provides a map of a property names to a values.', "source_vocab": 'SPDX-3.0.1'},
})

__all__ = ["CdxPropertiesExtension", "cdxProperty", "CdxPropertyEntry", "cdxPropName", "cdxPropValue", "Extension"]
