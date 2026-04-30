# SPDX-FileCopyrightText: 2026-present Arthit Suriyawongkul
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0
#
# AUTO-GENERATED — do not edit manually.
# Source: SPDX 3.0.1 SimpleLicensing profile
# Generated: 2026-04-30T08:53:35Z
# Regenerate: python -m stav.codegen.generate tools/recipes/spdx_simple_licensing.json

"""Vocabulary from SPDX 3.0.1 SimpleLicensing profile.

7 term constants (accessible as ``module.TermName``)."""

from __future__ import annotations

from stav._registry import _register
from stav.term import _StavVocabEnum

__stav_namespace__ = "vocab.spdx.simple_licensing"

# ── Individual term constants ─────────────────────────────────────────────────────
# Plain string IRIs — use directly with MLflow, Pitloom, SBOM serialisers.
# Metadata (label, definition, broader) via: stav.label(NaturalPerson) etc.
AnyLicenseInfo = 'https://spdx.org/rdf/3.0.1/terms/SimpleLicensing/AnyLicenseInfo'
customIdToUri = 'https://spdx.org/rdf/3.0.1/terms/SimpleLicensing/customIdToUri'
LicenseExpression = 'https://spdx.org/rdf/3.0.1/terms/SimpleLicensing/LicenseExpression'
licenseExpression = 'https://spdx.org/rdf/3.0.1/terms/SimpleLicensing/licenseExpression'
licenseListVersion = 'https://spdx.org/rdf/3.0.1/terms/SimpleLicensing/licenseListVersion'
licenseText = 'https://spdx.org/rdf/3.0.1/terms/SimpleLicensing/licenseText'
SimpleLicensingText = 'https://spdx.org/rdf/3.0.1/terms/SimpleLicensing/SimpleLicensingText'

# ── Metadata registry ──────────────────────────────────────────────────────────────
# Populated at import time so stav.label() / .definition() / .broader() work.
_register({
    'https://spdx.org/rdf/3.0.1/terms/SimpleLicensing/AnyLicenseInfo': {"label": 'AnyLicenseInfo', "definition": 'Abstract class representing a license combination consisting of one or more licenses.', "broader": ('https://spdx.org/rdf/3.0.1/terms/Core/Element',), "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/SimpleLicensing/LicenseExpression': {"label": 'LicenseExpression', "definition": 'An SPDX Element containing an SPDX license expression string.', "broader": ('https://spdx.org/rdf/3.0.1/terms/SimpleLicensing/AnyLicenseInfo',), "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/SimpleLicensing/SimpleLicensingText': {"label": 'SimpleLicensingText', "definition": 'A license or addition that is not listed on the SPDX License List.', "broader": ('https://spdx.org/rdf/3.0.1/terms/Core/Element',), "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/SimpleLicensing/customIdToUri': {"label": 'customIdToUri', "definition": 'Maps a LicenseRef or AdditionRef string for a Custom License or a Custom License Addition to its URI ID.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/SimpleLicensing/licenseExpression': {"label": 'licenseExpression', "definition": 'A string in the license expression format.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/SimpleLicensing/licenseListVersion': {"label": 'licenseListVersion', "definition": 'The version of the SPDX License List used in the license expression.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/SimpleLicensing/licenseText': {"label": 'licenseText', "definition": 'Identifies the full text of a License or Addition.', "source_vocab": 'SPDX-3.0.1'},
})

__all__ = ["AnyLicenseInfo", "customIdToUri", "LicenseExpression", "licenseExpression", "licenseListVersion", "licenseText", "SimpleLicensingText"]
