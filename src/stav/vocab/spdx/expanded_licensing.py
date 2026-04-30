# SPDX-FileCopyrightText: 2026-present Arthit Suriyawongkul
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0
#
# AUTO-GENERATED — do not edit manually.
# Source: SPDX 3.0.1 ExpandedLicensing profile
# Generated: 2026-04-30T08:53:35Z
# Regenerate: python -m stav.codegen.generate tools/recipes/spdx_expanded_licensing.json

"""Vocabulary from SPDX 3.0.1 ExpandedLicensing profile.

31 term constants (accessible as ``module.TermName``)."""

from __future__ import annotations

from stav._registry import _register
from stav.term import _StavVocabEnum

__stav_namespace__ = "vocab.spdx.expanded_licensing"

# ── Individual term constants ─────────────────────────────────────────────────────
# Plain string IRIs — use directly with MLflow, Pitloom, SBOM serialisers.
# Metadata (label, definition, broader) via: stav.label(NaturalPerson) etc.
additionText = 'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/additionText'
ConjunctiveLicenseSet = 'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/ConjunctiveLicenseSet'
CustomLicense = 'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/CustomLicense'
CustomLicenseAddition = 'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/CustomLicenseAddition'
deprecatedVersion = 'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/deprecatedVersion'
DisjunctiveLicenseSet = 'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/DisjunctiveLicenseSet'
ExtendableLicense = 'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/ExtendableLicense'
IndividualLicensingInfo = 'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/IndividualLicensingInfo'
isDeprecatedAdditionId = 'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/isDeprecatedAdditionId'
isDeprecatedLicenseId = 'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/isDeprecatedLicenseId'
isFsfLibre = 'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/isFsfLibre'
isOsiApproved = 'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/isOsiApproved'
License = 'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/License'
LicenseAddition = 'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/LicenseAddition'
licenseXml = 'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/licenseXml'
ListedLicense = 'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/ListedLicense'
ListedLicenseException = 'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/ListedLicenseException'
listVersionAdded = 'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/listVersionAdded'
member = 'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/member'
NoAssertionLicense = 'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/NoAssertionLicense'
NoneLicense = 'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/NoneLicense'
obsoletedBy = 'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/obsoletedBy'
OrLaterOperator = 'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/OrLaterOperator'
seeAlso = 'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/seeAlso'
standardAdditionTemplate = 'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/standardAdditionTemplate'
standardLicenseHeader = 'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/standardLicenseHeader'
standardLicenseTemplate = 'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/standardLicenseTemplate'
subjectAddition = 'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/subjectAddition'
subjectExtendableLicense = 'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/subjectExtendableLicense'
subjectLicense = 'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/subjectLicense'
WithAdditionOperator = 'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/WithAdditionOperator'

# ── Metadata registry ──────────────────────────────────────────────────────────────
# Populated at import time so stav.label() / .definition() / .broader() work.
_register({
    'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/ConjunctiveLicenseSet': {"label": 'ConjunctiveLicenseSet', "definition": 'Portion of an AnyLicenseInfo representing a set of licensing information where all elements apply.', "broader": ('https://spdx.org/rdf/3.0.1/terms/SimpleLicensing/AnyLicenseInfo',), "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/CustomLicense': {"label": 'CustomLicense', "definition": 'A license that is not listed on the SPDX License List.', "broader": ('https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/License',), "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/CustomLicenseAddition': {"label": 'CustomLicenseAddition', "definition": 'A license addition that is not listed on the SPDX Exceptions List.', "broader": ('https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/LicenseAddition',), "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/DisjunctiveLicenseSet': {"label": 'DisjunctiveLicenseSet', "definition": 'Portion of an AnyLicenseInfo representing a set of licensing information where only one of the elements applies.', "broader": ('https://spdx.org/rdf/3.0.1/terms/SimpleLicensing/AnyLicenseInfo',), "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/ExtendableLicense': {"label": 'ExtendableLicense', "definition": 'Abstract class representing a License or an OrLaterOperator.', "broader": ('https://spdx.org/rdf/3.0.1/terms/SimpleLicensing/AnyLicenseInfo',), "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/IndividualLicensingInfo': {"label": 'IndividualLicensingInfo', "definition": 'A concrete subclass of AnyLicenseInfo used by Individuals in the ExpandedLicensing profile.', "broader": ('https://spdx.org/rdf/3.0.1/terms/SimpleLicensing/AnyLicenseInfo',), "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/License': {"label": 'License', "definition": 'Abstract class for the portion of an AnyLicenseInfo representing a license.', "broader": ('https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/ExtendableLicense',), "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/LicenseAddition': {"label": 'LicenseAddition', "definition": 'Abstract class for additional text intended to be added to a License, but which is not itself a standalone License.', "broader": ('https://spdx.org/rdf/3.0.1/terms/Core/Element',), "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/ListedLicense': {"label": 'ListedLicense', "definition": 'A license that is listed on the SPDX License List.', "broader": ('https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/License',), "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/ListedLicenseException': {"label": 'ListedLicenseException', "definition": 'A license exception that is listed on the SPDX Exceptions list.', "broader": ('https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/LicenseAddition',), "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/NoAssertionLicense': {"label": 'NoAssertionLicense', "definition": 'An Individual Value for License when no assertion can be made about its actual value.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/NoneLicense': {"label": 'NoneLicense', "definition": 'An Individual Value for License where the SPDX data creator determines that no license is present.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/OrLaterOperator': {"label": 'OrLaterOperator', "definition": 'Portion of an AnyLicenseInfo representing this version, or any later version, of the indicated License.', "broader": ('https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/ExtendableLicense',), "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/WithAdditionOperator': {"label": 'WithAdditionOperator', "definition": 'Portion of an AnyLicenseInfo representing a License which has additional text applied to it.', "broader": ('https://spdx.org/rdf/3.0.1/terms/SimpleLicensing/AnyLicenseInfo',), "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/additionText': {"label": 'additionText', "definition": 'Identifies the full text of a LicenseAddition.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/deprecatedVersion': {"label": 'deprecatedVersion', "definition": 'Specifies the SPDX License List version in which this license or exception identifier was deprecated.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/isDeprecatedAdditionId': {"label": 'isDeprecatedAdditionId', "definition": 'Specifies whether an additional text identifier has been marked as deprecated.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/isDeprecatedLicenseId': {"label": 'isDeprecatedLicenseId', "definition": 'Specifies whether a license or additional text identifier has been marked as deprecated.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/isFsfLibre': {"label": 'isFsfLibre', "definition": 'Specifies whether the License is listed as free by the Free Software Foundation (FSF).', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/isOsiApproved': {"label": 'isOsiApproved', "definition": 'Specifies whether the License is listed as approved by the Open Source Initiative (OSI).', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/licenseXml': {"label": 'licenseXml', "definition": 'Identifies all the text and metadata associated with a license in the license XML format.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/listVersionAdded': {"label": 'listVersionAdded', "definition": 'Specifies the SPDX License List version in which this ListedLicense or ListedLicenseException identifier was first added.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/member': {"label": 'member', "definition": 'A license expression participating in a license set.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/obsoletedBy': {"label": 'obsoletedBy', "definition": 'Specifies the licenseId that is preferred to be used in place of a deprecated License or LicenseAddition.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/seeAlso': {"label": 'seeAlso', "definition": 'Contains a URL where the License or LicenseAddition can be found in use.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/standardAdditionTemplate': {"label": 'standardAdditionTemplate', "definition": 'Identifies the full text of a LicenseAddition, in SPDX templating format.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/standardLicenseHeader': {"label": 'standardLicenseHeader', "definition": "Provides a License author's preferred text to indicate that a file is covered by the License.", "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/standardLicenseTemplate': {"label": 'standardLicenseTemplate', "definition": 'Identifies the full text of a License, in SPDX templating format.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/subjectAddition': {"label": 'subjectAddition', "definition": "A LicenseAddition participating in a 'with addition' model.", "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/subjectExtendableLicense': {"label": 'subjectExtendableLicense', "definition": "A License participating in a 'with addition' model.", "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/subjectLicense': {"label": 'subjectLicense', "definition": "A License participating in an 'or later' model.", "source_vocab": 'SPDX-3.0.1'},
})

__all__ = ["additionText", "ConjunctiveLicenseSet", "CustomLicense", "CustomLicenseAddition", "deprecatedVersion", "DisjunctiveLicenseSet", "ExtendableLicense", "IndividualLicensingInfo", "isDeprecatedAdditionId", "isDeprecatedLicenseId", "isFsfLibre", "isOsiApproved", "License", "LicenseAddition", "licenseXml", "ListedLicense", "ListedLicenseException", "listVersionAdded", "member", "NoAssertionLicense", "NoneLicense", "obsoletedBy", "OrLaterOperator", "seeAlso", "standardAdditionTemplate", "standardLicenseHeader", "standardLicenseTemplate", "subjectAddition", "subjectExtendableLicense", "subjectLicense", "WithAdditionOperator"]
