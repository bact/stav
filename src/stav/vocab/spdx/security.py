# SPDX-FileCopyrightText: 2026-present Arthit Suriyawongkul
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0
#
# AUTO-GENERATED — do not edit manually.
# Source: SPDX 3.0.1 Security profile
# Generated: 2026-04-30T08:53:34Z
# Regenerate: python -m stav.codegen.generate tools/recipes/spdx_security.json

"""Vocabulary from SPDX 3.0.1 Security profile.

33 term constants (accessible as ``module.TermName``); grouped enums: :class:`CvssSeverityType`, :class:`ExploitCatalogType`, :class:`SsvcDecisionType`, :class:`VexJustificationType`."""

from __future__ import annotations

from stav._registry import _register
from stav.term import _StavVocabEnum

__stav_namespace__ = "vocab.spdx.security"

# ── Individual term constants ─────────────────────────────────────────────────────
# Plain string IRIs — use directly with MLflow, Pitloom, SBOM serialisers.
# Metadata (label, definition, broader) via: stav.label(NaturalPerson) etc.
actionStatement = 'https://spdx.org/rdf/3.0.1/terms/Security/actionStatement'
actionStatementTime = 'https://spdx.org/rdf/3.0.1/terms/Security/actionStatementTime'
assessedElement = 'https://spdx.org/rdf/3.0.1/terms/Security/assessedElement'
catalogType = 'https://spdx.org/rdf/3.0.1/terms/Security/catalogType'
CvssV2VulnAssessmentRelationship = 'https://spdx.org/rdf/3.0.1/terms/Security/CvssV2VulnAssessmentRelationship'
CvssV3VulnAssessmentRelationship = 'https://spdx.org/rdf/3.0.1/terms/Security/CvssV3VulnAssessmentRelationship'
CvssV4VulnAssessmentRelationship = 'https://spdx.org/rdf/3.0.1/terms/Security/CvssV4VulnAssessmentRelationship'
decisionType = 'https://spdx.org/rdf/3.0.1/terms/Security/decisionType'
EpssVulnAssessmentRelationship = 'https://spdx.org/rdf/3.0.1/terms/Security/EpssVulnAssessmentRelationship'
ExploitCatalogVulnAssessmentRelationship = 'https://spdx.org/rdf/3.0.1/terms/Security/ExploitCatalogVulnAssessmentRelationship'
exploited = 'https://spdx.org/rdf/3.0.1/terms/Security/exploited'
impactStatement = 'https://spdx.org/rdf/3.0.1/terms/Security/impactStatement'
impactStatementTime = 'https://spdx.org/rdf/3.0.1/terms/Security/impactStatementTime'
justificationType = 'https://spdx.org/rdf/3.0.1/terms/Security/justificationType'
locator = 'https://spdx.org/rdf/3.0.1/terms/Security/locator'
modifiedTime = 'https://spdx.org/rdf/3.0.1/terms/Security/modifiedTime'
percentile = 'https://spdx.org/rdf/3.0.1/terms/Security/percentile'
probability = 'https://spdx.org/rdf/3.0.1/terms/Security/probability'
publishedTime = 'https://spdx.org/rdf/3.0.1/terms/Security/publishedTime'
score = 'https://spdx.org/rdf/3.0.1/terms/Security/score'
severity = 'https://spdx.org/rdf/3.0.1/terms/Security/severity'
SsvcVulnAssessmentRelationship = 'https://spdx.org/rdf/3.0.1/terms/Security/SsvcVulnAssessmentRelationship'
statusNotes = 'https://spdx.org/rdf/3.0.1/terms/Security/statusNotes'
vectorString = 'https://spdx.org/rdf/3.0.1/terms/Security/vectorString'
VexAffectedVulnAssessmentRelationship = 'https://spdx.org/rdf/3.0.1/terms/Security/VexAffectedVulnAssessmentRelationship'
VexFixedVulnAssessmentRelationship = 'https://spdx.org/rdf/3.0.1/terms/Security/VexFixedVulnAssessmentRelationship'
VexNotAffectedVulnAssessmentRelationship = 'https://spdx.org/rdf/3.0.1/terms/Security/VexNotAffectedVulnAssessmentRelationship'
VexUnderInvestigationVulnAssessmentRelationship = 'https://spdx.org/rdf/3.0.1/terms/Security/VexUnderInvestigationVulnAssessmentRelationship'
vexVersion = 'https://spdx.org/rdf/3.0.1/terms/Security/vexVersion'
VexVulnAssessmentRelationship = 'https://spdx.org/rdf/3.0.1/terms/Security/VexVulnAssessmentRelationship'
VulnAssessmentRelationship = 'https://spdx.org/rdf/3.0.1/terms/Security/VulnAssessmentRelationship'
Vulnerability = 'https://spdx.org/rdf/3.0.1/terms/Security/Vulnerability'
withdrawnTime = 'https://spdx.org/rdf/3.0.1/terms/Security/withdrawnTime'

class CvssSeverityType(_StavVocabEnum):
    """CVSS severity levels from SPDX 3.0.1 Security profile."""
    critical = 'https://spdx.org/rdf/3.0.1/terms/Security/CvssSeverityType/critical'
    high = 'https://spdx.org/rdf/3.0.1/terms/Security/CvssSeverityType/high'
    low = 'https://spdx.org/rdf/3.0.1/terms/Security/CvssSeverityType/low'
    medium = 'https://spdx.org/rdf/3.0.1/terms/Security/CvssSeverityType/medium'
    none = 'https://spdx.org/rdf/3.0.1/terms/Security/CvssSeverityType/none'

class ExploitCatalogType(_StavVocabEnum):
    """Exploit catalog types from SPDX 3.0.1 Security profile."""
    kev = 'https://spdx.org/rdf/3.0.1/terms/Security/ExploitCatalogType/kev'
    other = 'https://spdx.org/rdf/3.0.1/terms/Security/ExploitCatalogType/other'

class SsvcDecisionType(_StavVocabEnum):
    """SSVC decision types from SPDX 3.0.1 Security profile."""
    act = 'https://spdx.org/rdf/3.0.1/terms/Security/SsvcDecisionType/act'
    attend = 'https://spdx.org/rdf/3.0.1/terms/Security/SsvcDecisionType/attend'
    track = 'https://spdx.org/rdf/3.0.1/terms/Security/SsvcDecisionType/track'
    trackStar = 'https://spdx.org/rdf/3.0.1/terms/Security/SsvcDecisionType/trackStar'

class VexJustificationType(_StavVocabEnum):
    """VEX not-affected justification types from SPDX 3.0.1 Security profile."""
    componentNotPresent = 'https://spdx.org/rdf/3.0.1/terms/Security/VexJustificationType/componentNotPresent'
    inlineMitigationsAlreadyExist = 'https://spdx.org/rdf/3.0.1/terms/Security/VexJustificationType/inlineMitigationsAlreadyExist'
    vulnerableCodeCannotBeControlledByAdversary = 'https://spdx.org/rdf/3.0.1/terms/Security/VexJustificationType/vulnerableCodeCannotBeControlledByAdversary'
    vulnerableCodeNotInExecutePath = 'https://spdx.org/rdf/3.0.1/terms/Security/VexJustificationType/vulnerableCodeNotInExecutePath'
    vulnerableCodeNotPresent = 'https://spdx.org/rdf/3.0.1/terms/Security/VexJustificationType/vulnerableCodeNotPresent'

# ── Metadata registry ──────────────────────────────────────────────────────────────
# Populated at import time so stav.label() / .definition() / .broader() work.
_register({
    'https://spdx.org/rdf/3.0.1/terms/Security/CvssSeverityType/critical': {"label": 'critical', "definition": 'When a CVSS score is between 9.0 - 10.0', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Security/CvssSeverityType/high': {"label": 'high', "definition": 'When a CVSS score is between 7.0 - 8.9', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Security/CvssSeverityType/low': {"label": 'low', "definition": 'When a CVSS score is between 0.1 - 3.9', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Security/CvssSeverityType/medium': {"label": 'medium', "definition": 'When a CVSS score is between 4.0 - 6.9', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Security/CvssSeverityType/none': {"label": 'none', "definition": 'When a CVSS score is 0.0', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Security/CvssV2VulnAssessmentRelationship': {"label": 'CvssV2VulnAssessmentRelationship', "definition": 'Provides a CVSS version 2.0 assessment for a vulnerability.', "broader": ('https://spdx.org/rdf/3.0.1/terms/Security/VulnAssessmentRelationship',), "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Security/CvssV3VulnAssessmentRelationship': {"label": 'CvssV3VulnAssessmentRelationship', "definition": 'Provides a CVSS version 3 assessment for a vulnerability.', "broader": ('https://spdx.org/rdf/3.0.1/terms/Security/VulnAssessmentRelationship',), "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Security/CvssV4VulnAssessmentRelationship': {"label": 'CvssV4VulnAssessmentRelationship', "definition": 'Provides a CVSS version 4 assessment for a vulnerability.', "broader": ('https://spdx.org/rdf/3.0.1/terms/Security/VulnAssessmentRelationship',), "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Security/EpssVulnAssessmentRelationship': {"label": 'EpssVulnAssessmentRelationship', "definition": 'Provides an EPSS assessment for a vulnerability.', "broader": ('https://spdx.org/rdf/3.0.1/terms/Security/VulnAssessmentRelationship',), "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Security/ExploitCatalogType/kev': {"label": 'kev', "definition": "CISA's Known Exploited Vulnerability (KEV) Catalog", "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Security/ExploitCatalogType/other': {"label": 'other', "definition": 'Other exploit catalogs', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Security/ExploitCatalogVulnAssessmentRelationship': {"label": 'ExploitCatalogVulnAssessmentRelationship', "definition": 'Provides an exploit assessment of a vulnerability.', "broader": ('https://spdx.org/rdf/3.0.1/terms/Security/VulnAssessmentRelationship',), "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Security/SsvcDecisionType/act': {"label": 'act', "definition": "The vulnerability requires attention from the organization's internal, supervisory-level and leadership-level individuals. Necessary actions include requesting assistance or information about the vulnerability, as well as publishing a notification either internally and/or externally. Typically, i...", "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Security/SsvcDecisionType/attend': {"label": 'attend', "definition": "The vulnerability requires attention from the organization's internal, supervisory-level individuals. Necessary actions include requesting assistance or information about the vulnerability, and may involve publishing a notification either internally and/or externally. CISA recommends remediating ...", "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Security/SsvcDecisionType/track': {"label": 'track', "definition": 'The vulnerability does not require action at this time. The organization would continue to track the vulnerability and reassess it if new information becomes available. CISA recommends remediating Track vulnerabilities within standard update timelines.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Security/SsvcDecisionType/trackStar': {"label": 'trackStar', "definition": '("Track\\*" in the SSVC spec) The vulnerability contains specific characteristics that may require closer monitoring for changes. CISA recommends remediating Track\\* vulnerabilities within standard update timelines.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Security/SsvcVulnAssessmentRelationship': {"label": 'SsvcVulnAssessmentRelationship', "definition": 'Provides an SSVC assessment for a vulnerability.', "broader": ('https://spdx.org/rdf/3.0.1/terms/Security/VulnAssessmentRelationship',), "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Security/VexAffectedVulnAssessmentRelationship': {"label": 'VexAffectedVulnAssessmentRelationship', "definition": 'Connects a vulnerability and an element designating the element as a product affected by the vulnerability.', "broader": ('https://spdx.org/rdf/3.0.1/terms/Security/VexVulnAssessmentRelationship',), "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Security/VexFixedVulnAssessmentRelationship': {"label": 'VexFixedVulnAssessmentRelationship', "definition": 'Links a vulnerability and elements representing products (in the VEX sense) where a fix has been applied and are no longer affected.', "broader": ('https://spdx.org/rdf/3.0.1/terms/Security/VexVulnAssessmentRelationship',), "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Security/VexJustificationType/componentNotPresent': {"label": 'componentNotPresent', "definition": 'The software is not affected because the vulnerable component is not in the product.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Security/VexJustificationType/inlineMitigationsAlreadyExist': {"label": 'inlineMitigationsAlreadyExist', "definition": 'Built-in inline controls or mitigations prevent an adversary from leveraging the vulnerability.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Security/VexJustificationType/vulnerableCodeCannotBeControlledByAdversary': {"label": 'vulnerableCodeCannotBeControlledByAdversary', "definition": 'The vulnerable component is present, and the component contains the vulnerable code. However, vulnerable code is used in such a way that an attacker cannot mount any anticipated attack.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Security/VexJustificationType/vulnerableCodeNotInExecutePath': {"label": 'vulnerableCodeNotInExecutePath', "definition": 'The affected code is not reachable through the execution of the code, including non-anticipated states of the product.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Security/VexJustificationType/vulnerableCodeNotPresent': {"label": 'vulnerableCodeNotPresent', "definition": 'The product is not affected because the code underlying the vulnerability is not present in the product.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Security/VexNotAffectedVulnAssessmentRelationship': {"label": 'VexNotAffectedVulnAssessmentRelationship', "definition": 'Links a vulnerability and one or more elements designating the latter as products not affected by the vulnerability.', "broader": ('https://spdx.org/rdf/3.0.1/terms/Security/VexVulnAssessmentRelationship',), "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Security/VexUnderInvestigationVulnAssessmentRelationship': {"label": 'VexUnderInvestigationVulnAssessmentRelationship', "definition": 'Designates elements as products where the impact of a vulnerability is being investigated.', "broader": ('https://spdx.org/rdf/3.0.1/terms/Security/VexVulnAssessmentRelationship',), "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Security/VexVulnAssessmentRelationship': {"label": 'VexVulnAssessmentRelationship', "definition": 'Abstract ancestor class for all VEX relationships', "broader": ('https://spdx.org/rdf/3.0.1/terms/Security/VulnAssessmentRelationship',), "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Security/VulnAssessmentRelationship': {"label": 'VulnAssessmentRelationship', "definition": 'Abstract ancestor class for all vulnerability assessments', "broader": ('https://spdx.org/rdf/3.0.1/terms/Core/Relationship',), "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Security/Vulnerability': {"label": 'Vulnerability', "definition": 'Specifies a vulnerability and its associated information.', "broader": ('https://spdx.org/rdf/3.0.1/terms/Core/Artifact',), "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Security/actionStatement': {"label": 'actionStatement', "definition": 'Provides advise on how to mitigate or remediate a vulnerability when a VEX product is affected by it.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Security/actionStatementTime': {"label": 'actionStatementTime', "definition": 'Records the time when a recommended action was communicated in a VEX statement to mitigate a vulnerability.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Security/assessedElement': {"label": 'assessedElement', "definition": 'Specifies an Element contained in a piece of software where a vulnerability was found.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Security/catalogType': {"label": 'catalogType', "definition": 'Specifies the exploit catalog type.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Security/decisionType': {"label": 'decisionType', "definition": 'Provide the enumeration of possible decisions in the [Stakeholder-Specific Vulnerability Categorization (SSVC) decision tree](https://www.cisa.gov/stakeholder-specific-vulnerability-categorization-ssvc).', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Security/exploited': {"label": 'exploited', "definition": "Describe that a CVE is known to have an exploit because it's been listed in an exploit catalog.", "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Security/impactStatement': {"label": 'impactStatement', "definition": 'Explains why a VEX product is not affected by a vulnerability. It is an alternative in VexNotAffectedVulnAssessmentRelationship to the machine-readable justification label.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Security/impactStatementTime': {"label": 'impactStatementTime', "definition": 'Timestamp of impact statement.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Security/justificationType': {"label": 'justificationType', "definition": 'Impact justification label to be used when linking a vulnerability to an element representing a VEX product with a VexNotAffectedVulnAssessmentRelationship relationship.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Security/locator': {"label": 'locator', "definition": 'Provides the location of an exploit catalog.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Security/modifiedTime': {"label": 'modifiedTime', "definition": 'Specifies a time when a vulnerability assessment was modified', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Security/percentile': {"label": 'percentile', "definition": 'The percentile of the current probability score.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Security/probability': {"label": 'probability', "definition": 'A probability score between 0 and 1 of a vulnerability being exploited.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Security/publishedTime': {"label": 'publishedTime', "definition": 'Specifies the time when a vulnerability was published.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Security/score': {"label": 'score', "definition": 'Provides a numerical (0-10) representation of the severity of a vulnerability.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Security/severity': {"label": 'severity', "definition": 'Specifies the CVSS qualitative severity rating of a vulnerability in relation to a piece of software.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Security/statusNotes': {"label": 'statusNotes', "definition": 'Conveys information about how VEX status was determined.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Security/vectorString': {"label": 'vectorString', "definition": 'Specifies the CVSS vector string for a vulnerability.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Security/vexVersion': {"label": 'vexVersion', "definition": 'Specifies the version of a VEX statement.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Security/withdrawnTime': {"label": 'withdrawnTime', "definition": 'Specified the time and date when a vulnerability was withdrawn.', "source_vocab": 'SPDX-3.0.1'},
})

__all__ = ["actionStatement", "actionStatementTime", "assessedElement", "catalogType", "CvssV2VulnAssessmentRelationship", "CvssV3VulnAssessmentRelationship", "CvssV4VulnAssessmentRelationship", "decisionType", "EpssVulnAssessmentRelationship", "ExploitCatalogVulnAssessmentRelationship", "exploited", "impactStatement", "impactStatementTime", "justificationType", "locator", "modifiedTime", "percentile", "probability", "publishedTime", "score", "severity", "SsvcVulnAssessmentRelationship", "statusNotes", "vectorString", "VexAffectedVulnAssessmentRelationship", "VexFixedVulnAssessmentRelationship", "VexNotAffectedVulnAssessmentRelationship", "VexUnderInvestigationVulnAssessmentRelationship", "vexVersion", "VexVulnAssessmentRelationship", "VulnAssessmentRelationship", "Vulnerability", "withdrawnTime", "CvssSeverityType", "ExploitCatalogType", "SsvcDecisionType", "VexJustificationType"]
