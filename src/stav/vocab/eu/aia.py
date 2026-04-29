# SPDX-FileCopyrightText: 2026-present Arthit Suriyawongkul
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0
#
# AUTO-GENERATED — do not edit manually.
# Source: STAV — EU AI Act concepts and obligations
# Generated: 2026-04-29T22:30:24Z
# Regenerate: python -m stav.codegen.generate tools/recipes/stav_eu_ai.json

"""Vocabulary from STAV — EU AI Act concepts and obligations.

63 term constants (accessible as ``module.TermName``); grouped enums: :class:`AIRole`, :class:`AIActObligation`, :class:`AIActDocumentation`."""

from __future__ import annotations

from stav._registry import _register
from stav.term import _StavVocabEnum

__stav_namespace__ = "vocab.eu.aia"

# ── Individual term constants ─────────────────────────────────────────────────────
# Plain string IRIs — use directly with MLflow, Pitloom, SBOM serialisers.
# Metadata (label, definition, broader) via: stav.label(NaturalPerson) etc.
Action = "http://www.w3.org/ns/odrl/2/Action"
AiActChapter3Article18ReqColl = "http://tair.adaptcentre.ie/ontologies/tair/AiActChapter3Article18ReqColl"
AiActRequirement = "http://tair.adaptcentre.ie/ontologies/tair/AiActRequirement"
AiaPrReq_16_1_R1c = "http://tair.adaptcentre.ie/ontologies/tair/AiaPrReq_16.1_R1c"
AiaPrReq_16_1_R1f = "http://tair.adaptcentre.ie/ontologies/tair/AiaPrReq_16.1_R1f"
AiaPrReq_51_1_R1 = "http://tair.adaptcentre.ie/ontologies/tair/AiaPrReq_51.1_R1"
AIDeployer = "https://w3id.org/stav#AIDeployer"  # AI Deployer
AIProvider = "https://w3id.org/stav#AIProvider"  # AI Provider
AISystem = "https://w3id.org/stav#AISystem"  # AI System
AISystemStatus = "https://w3id.org/stav#AISystemStatus"
AppliedStandards = "https://w3id.org/stav#AppliedStandards"  # Applied Standards
Asset = "http://www.w3.org/ns/odrl/2/Asset"
AssetCollection = "http://www.w3.org/ns/odrl/2/AssetCollection"
AuthorisedRepresentative = "https://w3id.org/stav#AuthorisedRepresentative"  # Authorised Representative
BaselineProcessDescription = "https://w3id.org/stav#BaselineProcessDescription"  # Baseline Process Description
BeingNotHighRiskCriteria = "https://w3id.org/stav#BeingNotHighRiskCriteria"  # Being Not High-Risk Criteria
BeingNotHighRiskGrounds = "https://w3id.org/stav#BeingNotHighRiskGrounds"  # Being Not High-Risk Grounds
ComponentsAndFunctionsSupportedDescription = (
    "https://w3id.org/stav#ComponentsAndFunctionsSupportedDescription"  # Components And Functions Supported Description
)
ConformityDeclaration = "https://w3id.org/stav#ConformityDeclaration"  # Conformity Declaration
CurrentAndPotentialFutureImpacts = (
    "https://w3id.org/stav#CurrentAndPotentialFutureImpacts"  # Current and Potential Future Impacts
)
DataMinimizationPractices = "https://w3id.org/stav#DataMinimizationPractices"  # Data Minimization Practices
DataProtectionImpactAssessmentDocumentation = "https://w3id.org/stav#DataProtectionImpactAssessmentDocumentation"  # Data Protection Impact Assessment Documentation
DeploymentContext = "https://w3id.org/stav#DeploymentContext"  # Deployment Context
EUAIAAIDatabaseRegisterationObligation = "https://w3id.org/stav-eu-aia#EUAIAAIDatabaseRegisterationObligation"  # AI Database Registeration Obligation (EU AI Act)
EUAIAQualityManagementSystemDocumentationObligation = "https://w3id.org/stav-eu-aia#EUAIAQualityManagementSystemDocumentationObligation"  # Quality Management System Documentation Obligation (EU AI Act)
EUAIATechnicalDocumentationObligation = "https://w3id.org/stav-eu-aia#EUAIATechnicalDocumentationObligation"  # Technical Documentation Obligation (EU AI Act)
ExternalInteractionDescription = (
    "https://w3id.org/stav#ExternalInteractionDescription"  # External Interaction Description
)
FundamentalRightsImpactAssessmentDocumentation = "https://w3id.org/stav#FundamentalRightsImpactAssessmentDocumentation"  # Fundamental Rights Impact Assessment Documentation
ImpactAssessmentDocumentation = "https://w3id.org/stav#ImpactAssessmentDocumentation"  # Impact Assessment Documentation
InformationCreationObligation = "https://w3id.org/stap#InformationCreationObligation"
InformationSecurityMeasures = "https://w3id.org/stav#InformationSecurityMeasures"  # Information Security Measures
InformationSubmissionObligation = "https://w3id.org/stap#InformationSubmissionObligation"
InformationSubmissionRepresentative = (
    "https://w3id.org/stav#InformationSubmissionRepresentative"  # Information Submission Representative
)
InformationUsedBySystemDescription = (
    "https://w3id.org/stav#InformationUsedBySystemDescription"  # Information Used By the System Description
)
InstallationInstructions = "https://w3id.org/stav#InstallationInstructions"  # Installation Instructions
InstructionsForUse = "https://w3id.org/stav#InstructionsForUse"  # Instructions for Use
IntendedBenefitsOverPreviouslyExistingProcess = "https://w3id.org/stav#IntendedBenefitsOverPreviouslyExistingProcess"  # Intended Benefits Over Previously Existing Process
IntendedHardwareDescription = "https://w3id.org/stav#IntendedHardwareDescription"  # Intended Hardware Description
IntendedPurposes = "https://w3id.org/stav#IntendedPurposes"  # Intended Purposes
Log = "https://w3id.org/stav#Log"
MakingAvailableOnTheMarket = "https://w3id.org/stav#MakingAvailableOnTheMarket"  # making available on the market
MarketSurveillenceAuthority = "https://w3id.org/stav#MarketSurveillenceAuthority"  # Market Surveillence Authority
Party = "http://www.w3.org/ns/odrl/2/Party"
PlacingOnTheMarket = "https://w3id.org/stav#PlacingOnTheMarket"  # placing on the market
PostMarketEvaluationSystemDescription = (
    "https://w3id.org/stav#PostMarketEvaluationSystemDescription"  # Post-Market Evaluation System Description
)
PreviouslyExistingProcessEvaluationDocumentation = "https://w3id.org/stav#PreviouslyExistingProcessEvaluationDocumentation"  # Previously Existing Process Evaluation Documentation
PreviouslyExistingProcessKnownNegativeImpactInformation = "https://w3id.org/stav#PreviouslyExistingProcessKnownNegativeImpactInformation"  # Previously Existing Process Known Negative Impact Information
PrivacyRisksAndPrivacyMeasuresEvaluationDocumentation = "https://w3id.org/stav#PrivacyRisksAndPrivacyMeasuresEvaluationDocumentation"  # Privacy Risks and Privacy Measures Evaluation Documentation
ProductServiceDescription = "https://w3id.org/stav#ProductServiceDescription"  # Product Service Descriptipn
ProductVisualImage = "https://w3id.org/stav#ProductVisualImage"  # Product Visual Image
PuttingIntoService = "https://w3id.org/stav#PuttingIntoService"  # putting into service
QualityManagementSystemDocumentationObligation = "https://w3id.org/stav#QualityManagementSystemDocumentationObligation"  # Quality Management System Documentation Obligation
RealWorldConditionsTestingPlan = (
    "https://w3id.org/stav#RealWorldConditionsTestingPlan"  # Real World Conditions Testing Plan
)
RealWorldConditionsTestingSuspensionOrTerminationInformation = "https://w3id.org/stav#RealWorldConditionsTestingSuspensionOrTerminationInformation"  # Real World Conditions Testing Suspension Or Termination Information
RealWorldConditionsTestingUser = (
    "https://w3id.org/stav#RealWorldConditionsTestingUser"  # Real World Conditions Testing User
)
RegisterationObligation = "https://w3id.org/stav#RegisterationObligation"  # Registeration Obligation
RiskManagementSystemDescription = (
    "https://w3id.org/stav#RiskManagementSystemDescription"  # Risk Management System Description
)
SoftwareDependencies = "https://w3id.org/stav#SoftwareDependencies"  # Software Dependencies
SystemDetailedDescription = "https://w3id.org/stav#SystemDetailedDescription"  # System Detailed Description
SystemEvaluationDocumentation = "https://w3id.org/stav#SystemEvaluationDocumentation"  # System Evaluation Documentation
SystemGeneralDescription = "https://w3id.org/stav#SystemGeneralDescription"  # System General Description
TechnicalDocumentation = "https://w3id.org/stav#TechnicalDocumentation"  # Technical Documentation
TechnicalDocumentationObligation = (
    "https://w3id.org/stav#TechnicalDocumentationObligation"  # Technical Documentation Obligation
)


class AIRole(_StavVocabEnum):
    """
    Roles of actors in AI systems as defined in the EU AI Act (via STAV). Covers providers,
    deployers, and oversight bodies.
    """

    AIDeployer = "https://w3id.org/stav#AIDeployer"  # AI Deployer
    AIProvider = "https://w3id.org/stav#AIProvider"  # AI Provider
    AuthorisedRepresentative = "https://w3id.org/stav#AuthorisedRepresentative"  # Authorised Representative
    InformationSubmissionRepresentative = (
        "https://w3id.org/stav#InformationSubmissionRepresentative"  # Information Submission Representative
    )
    MarketSurveillenceAuthority = "https://w3id.org/stav#MarketSurveillenceAuthority"  # Market Surveillence Authority


class AIActObligation(_StavVocabEnum):
    """Documentation and compliance obligations under the EU AI Act (via STAV)."""

    EUAIAAIDatabaseRegisterationObligation = "https://w3id.org/stav-eu-aia#EUAIAAIDatabaseRegisterationObligation"  # AI Database Registeration Obligation (EU AI Act)
    EUAIAQualityManagementSystemDocumentationObligation = "https://w3id.org/stav-eu-aia#EUAIAQualityManagementSystemDocumentationObligation"  # Quality Management System Documentation Obligation (EU AI Act)
    EUAIATechnicalDocumentationObligation = "https://w3id.org/stav-eu-aia#EUAIATechnicalDocumentationObligation"  # Technical Documentation Obligation (EU AI Act)
    QualityManagementSystemDocumentationObligation = "https://w3id.org/stav#QualityManagementSystemDocumentationObligation"  # Quality Management System Documentation Obligation
    RegisterationObligation = "https://w3id.org/stav#RegisterationObligation"  # Registeration Obligation
    TechnicalDocumentationObligation = (
        "https://w3id.org/stav#TechnicalDocumentationObligation"  # Technical Documentation Obligation
    )


class AIActDocumentation(_StavVocabEnum):
    """Documentation artifacts required or recommended by the EU AI Act (via STAV)."""

    DataProtectionImpactAssessmentDocumentation = "https://w3id.org/stav#DataProtectionImpactAssessmentDocumentation"  # Data Protection Impact Assessment Documentation
    FundamentalRightsImpactAssessmentDocumentation = "https://w3id.org/stav#FundamentalRightsImpactAssessmentDocumentation"  # Fundamental Rights Impact Assessment Documentation
    ImpactAssessmentDocumentation = (
        "https://w3id.org/stav#ImpactAssessmentDocumentation"  # Impact Assessment Documentation
    )
    InstructionsForUse = "https://w3id.org/stav#InstructionsForUse"  # Instructions for Use
    IntendedPurposes = "https://w3id.org/stav#IntendedPurposes"  # Intended Purposes
    Log = "https://w3id.org/stav#Log"
    RiskManagementSystemDescription = (
        "https://w3id.org/stav#RiskManagementSystemDescription"  # Risk Management System Description
    )
    SystemEvaluationDocumentation = (
        "https://w3id.org/stav#SystemEvaluationDocumentation"  # System Evaluation Documentation
    )
    SystemGeneralDescription = "https://w3id.org/stav#SystemGeneralDescription"  # System General Description
    TechnicalDocumentation = "https://w3id.org/stav#TechnicalDocumentation"  # Technical Documentation


# ── Metadata registry ──────────────────────────────────────────────────────────────
# Populated at import time so stav.label() / .definition() / .broader() work.
_register(
    {
        "http://tair.adaptcentre.ie/ontologies/tair/AiActChapter3Article18ReqColl": {
            "label": "AiActChapter3Article18ReqColl",
            "source_vocab": "STAV-EU-AIA",
        },
        "http://tair.adaptcentre.ie/ontologies/tair/AiActRequirement": {
            "label": "AiActRequirement",
            "source_vocab": "STAV-EU-AIA",
        },
        "http://tair.adaptcentre.ie/ontologies/tair/AiaPrReq_16.1_R1c": {
            "label": "AiaPrReq_16_1_R1c",
            "source_vocab": "STAV-EU-AIA",
        },
        "http://tair.adaptcentre.ie/ontologies/tair/AiaPrReq_16.1_R1f": {
            "label": "AiaPrReq_16_1_R1f",
            "source_vocab": "STAV-EU-AIA",
        },
        "http://tair.adaptcentre.ie/ontologies/tair/AiaPrReq_51.1_R1": {
            "label": "AiaPrReq_51_1_R1",
            "source_vocab": "STAV-EU-AIA",
        },
        "http://www.w3.org/ns/odrl/2/Action": {"label": "Action", "source_vocab": "STAV"},
        "http://www.w3.org/ns/odrl/2/Asset": {"label": "Asset", "source_vocab": "STAV"},
        "http://www.w3.org/ns/odrl/2/AssetCollection": {"label": "AssetCollection", "source_vocab": "STAV"},
        "http://www.w3.org/ns/odrl/2/Party": {"label": "Party", "source_vocab": "STAV"},
        "https://w3id.org/stap#InformationCreationObligation": {
            "label": "InformationCreationObligation",
            "source_vocab": "STAV",
        },
        "https://w3id.org/stap#InformationSubmissionObligation": {
            "label": "InformationSubmissionObligation",
            "source_vocab": "STAV",
        },
        "https://w3id.org/stav#AIDeployer": {
            "label": "AI Deployer",
            "broader": ("http://www.w3.org/ns/odrl/2/Party",),
            "source_vocab": "STAV",
        },
        "https://w3id.org/stav#AIProvider": {
            "label": "AI Provider",
            "broader": ("http://www.w3.org/ns/odrl/2/Party",),
            "source_vocab": "STAV",
        },
        "https://w3id.org/stav#AISystem": {
            "label": "AI System",
            "broader": ("http://www.w3.org/ns/odrl/2/Asset",),
            "source_vocab": "STAV",
        },
        "https://w3id.org/stav#AISystemStatus": {
            "label": "AISystemStatus",
            "broader": ("http://www.w3.org/ns/odrl/2/Asset",),
            "source_vocab": "STAV",
        },
        "https://w3id.org/stav#AppliedStandards": {
            "label": "Applied Standards",
            "definition": "Annex IV (6)",
            "broader": ("http://www.w3.org/ns/odrl/2/Asset",),
            "source_vocab": "STAV",
        },
        "https://w3id.org/stav#AuthorisedRepresentative": {
            "label": "Authorised Representative",
            "broader": ("http://www.w3.org/ns/odrl/2/Party",),
            "source_vocab": "STAV",
        },
        "https://w3id.org/stav#BaselineProcessDescription": {
            "label": "Baseline Process Description",
            "definition": "Desciption of a previously existing decision-making process prior to the deployment of an AI/augmented decision process.",
            "broader": ("http://www.w3.org/ns/odrl/2/Asset",),
            "source_vocab": "STAV",
        },
        "https://w3id.org/stav#BeingNotHighRiskCriteria": {
            "label": "Being Not High-Risk Criteria",
            "definition": "Based on which criterion or criteria provided in Article 6(2a) the AI system is considered as not high-risk",
            "broader": ("http://www.w3.org/ns/odrl/2/Asset",),
            "source_vocab": "STAV",
        },
        "https://w3id.org/stav#BeingNotHighRiskGrounds": {
            "label": "Being Not High-Risk Grounds",
            "definition": "Short summary of the grounds for considering the AI system as not high-risk in application of the procedure under Article 6(2a)",
            "broader": ("http://www.w3.org/ns/odrl/2/Asset",),
            "source_vocab": "STAV",
        },
        "https://w3id.org/stav#ComponentsAndFunctionsSupportedDescription": {
            "label": "Components And Functions Supported Description",
            "definition": "Description of the components and functions supported through this AI system",
            "broader": ("http://www.w3.org/ns/odrl/2/Asset",),
            "source_vocab": "STAV",
        },
        "https://w3id.org/stav#ConformityDeclaration": {
            "label": "Conformity Declaration",
            "definition": "Annex IV (7) EU AI Act  Can a text or an URL",
            "broader": ("http://www.w3.org/ns/odrl/2/Asset",),
            "source_vocab": "STAV",
        },
        "https://w3id.org/stav#CurrentAndPotentialFutureImpacts": {
            "label": "Current and Potential Future Impacts",
            "definition": "Assessment and documentation of the current and potential future or downstream positive and negative impacts of a system or process.",
            "broader": ("http://www.w3.org/ns/odrl/2/Asset",),
            "source_vocab": "STAV",
        },
        "https://w3id.org/stav#DataMinimizationPractices": {
            "label": "Data Minimization Practices",
            "definition": "Assessment and documentation of the data minimization practices of a system or process and the duration for which the relevant identifying information and any resulting critical decision is stored.",
            "broader": ("http://www.w3.org/ns/odrl/2/Asset",),
            "source_vocab": "STAV",
        },
        "https://w3id.org/stav#DataProtectionImpactAssessmentDocumentation": {
            "label": "Data Protection Impact Assessment Documentation",
            "definition": "A summary of the data protection impact assessment carried out in accordance with Article 35 of Regulation (EU) 2016/679 or Article 27 of Directive (EU) 2016/680 as specified in paragraph 6 of Article 29 of this Regulation, where applicable.",
            "broader": ("https://w3id.org/stav#ImpactAssessmentDocumentation",),
            "source_vocab": "STAV",
        },
        "https://w3id.org/stav#DeploymentContext": {
            "label": "Deployment Context",
            "definition": "Sec. 203. (a) (2) (C) S. 3312: Artificial Intelligence Research, Innovation, and Accountability Act of 2023 https://www.govtrack.us/congress/bills/118/s3312/text/is#link=II_203_a_2_C&nearest=id07706866948d4dc59792b34859a3afdf",
            "broader": ("http://www.w3.org/ns/odrl/2/Asset",),
            "source_vocab": "STAV",
        },
        "https://w3id.org/stav#ExternalInteractionDescription": {
            "label": "External Interaction Description",
            "definition": "How the AI system interacts or can be used to interact with hardware or software that is not part of the AI system itself, where applicable.",
            "broader": ("http://www.w3.org/ns/odrl/2/Asset",),
            "source_vocab": "STAV",
        },
        "https://w3id.org/stav#FundamentalRightsImpactAssessmentDocumentation": {
            "label": "Fundamental Rights Impact Assessment Documentation",
            "definition": "A summary of the findings of the fundamental rights impact assessment conducted in accordance with Article 29a.",
            "broader": ("https://w3id.org/stav#ImpactAssessmentDocumentation",),
            "source_vocab": "STAV",
        },
        "https://w3id.org/stav#ImpactAssessmentDocumentation": {
            "label": "Impact Assessment Documentation",
            "definition": "S. 2892: Algorithmic Accountability Act of 2023 Defined in Sec. 2. (12) https://www.govtrack.us/congress/bills/118/s2892/text/is#link=2_12 and detailed in Sec. 4. (a) https://www.govtrack.us/congress/bills/118/s2892/text/is#link=4_a  S. 3312: Artificial Intelligence Research, Innovation, and Acco...",
            "broader": ("http://www.w3.org/ns/odrl/2/AssetCollection",),
            "source_vocab": "STAV",
        },
        "https://w3id.org/stav#InformationSecurityMeasures": {
            "label": "Information Security Measures",
            "definition": "Assessment of information security measures with respect to a system or process.",
            "broader": ("http://www.w3.org/ns/odrl/2/Asset",),
            "source_vocab": "STAV",
        },
        "https://w3id.org/stav#InformationSubmissionRepresentative": {
            "label": "Information Submission Representative",
            "broader": ("http://www.w3.org/ns/odrl/2/Party",),
            "source_vocab": "STAV",
        },
        "https://w3id.org/stav#InformationUsedBySystemDescription": {
            "label": "Information Used By the System Description",
            "definition": "A basic and concise description of the information used by the system (data, inputs) and its operating logic",
            "broader": ("http://www.w3.org/ns/odrl/2/Asset",),
            "source_vocab": "STAV",
        },
        "https://w3id.org/stav#InstallationInstructions": {
            "label": "Installation Instructions",
            "broader": ("http://www.w3.org/ns/odrl/2/Asset",),
            "source_vocab": "STAV",
        },
        "https://w3id.org/stav#InstructionsForUse": {
            "label": "Instructions for Use",
            "definition": "‘instructions for use’ or ‘instructions of use’ means the information provided by the provider to inform the user of in particular an AI system’s intended purpose and proper use, inclusive of the specific geographical, behavioural or functional setting within which the high-risk AI system is inte...",
            "broader": ("http://www.w3.org/ns/odrl/2/Asset",),
            "source_vocab": "STAV",
        },
        "https://w3id.org/stav#IntendedBenefitsOverPreviouslyExistingProcess": {
            "label": "Intended Benefits Over Previously Existing Process",
            "definition": "Intended benefits of and need for the new process.",
            "broader": ("http://www.w3.org/ns/odrl/2/Asset",),
            "source_vocab": "STAV",
        },
        "https://w3id.org/stav#IntendedHardwareDescription": {
            "label": "Intended Hardware Description",
            "definition": "The description of hardware on which the AI system is intended to run.",
            "broader": ("http://www.w3.org/ns/odrl/2/Asset",),
            "source_vocab": "STAV",
        },
        "https://w3id.org/stav#IntendedPurposes": {
            "label": "Intended Purposes",
            "definition": '"intended purpose" EU AI Act Annex IV (1) (b) Annex VIII Section C (4) Annex VIII Section A (5) Annex VIIIa (3)  "purpose" Sec. 203. (a) (2) (A) S.3312 - Artificial Intelligence Research, Innovation, and Accountability Act of 2023 https://www.govtrack.us/congress/bills/118/s3312/text/is#link=II_2...',
            "broader": ("http://www.w3.org/ns/odrl/2/Asset",),
            "source_vocab": "STAV",
        },
        "https://w3id.org/stav#Log": {
            "label": "Log",
            "definition": "Automatic recording of events while the high-risk AI systems is operating. Those logging capabilities shall conform to recognised standards or common specifications. The logging capabilities shall ensure a level of traceability of the AI system’s functioning throughout its lifecycle that is appro...",
            "broader": ("http://www.w3.org/ns/odrl/2/Asset",),
            "source_vocab": "STAV",
        },
        "https://w3id.org/stav#MakingAvailableOnTheMarket": {
            "label": "making available on the market",
            "definition": "‘making available on the market’ means any supply of an AI system for distribution or use on the Union market in the course of a commercial activity, whether in return for payment or free of charge.",
            "broader": ("http://www.w3.org/ns/odrl/2/Action",),
            "source_vocab": "STAV",
        },
        "https://w3id.org/stav#MarketSurveillenceAuthority": {
            "label": "Market Surveillence Authority",
            "broader": ("http://www.w3.org/ns/odrl/2/Party",),
            "source_vocab": "STAV",
        },
        "https://w3id.org/stav#PlacingOnTheMarket": {
            "label": "placing on the market",
            "definition": "‘placing on the market’ means the first making available of an AI system on the Union market.",
            "broader": ("http://www.w3.org/ns/odrl/2/Action",),
            "source_vocab": "STAV",
        },
        "https://w3id.org/stav#PostMarketEvaluationSystemDescription": {
            "label": "Post-Market Evaluation System Description",
            "definition": "Annex IV (8) EU AI Act",
            "broader": ("http://www.w3.org/ns/odrl/2/Asset",),
            "source_vocab": "STAV",
        },
        "https://w3id.org/stav#PreviouslyExistingProcessEvaluationDocumentation": {
            "label": "Previously Existing Process Evaluation Documentation",
            "definition": "Any related documentation or information about previously existing process being enhanced or replaced by the new process. This also includes information about the new process for the comparison purpose with the previously existing process.",
            "broader": ("http://www.w3.org/ns/odrl/2/AssetCollection",),
            "source_vocab": "STAV",
        },
        "https://w3id.org/stav#PreviouslyExistingProcessKnownNegativeImpactInformation": {
            "label": "Previously Existing Process Known Negative Impact Information",
            "definition": "Any known harm, shortcoming, failure case, or material negative impact on consumers of the previously existing process used to make a decision.",
            "broader": ("http://www.w3.org/ns/odrl/2/Asset",),
            "source_vocab": "STAV",
        },
        "https://w3id.org/stav#PrivacyRisksAndPrivacyMeasuresEvaluationDocumentation": {
            "label": "Privacy Risks and Privacy Measures Evaluation Documentation",
            "broader": ("http://www.w3.org/ns/odrl/2/AssetCollection",),
            "source_vocab": "STAV",
        },
        "https://w3id.org/stav#ProductServiceDescription": {
            "label": "Product Service Descriptipn",
            "definition": "The description of the form in which the AI system is placed on the market or put into service.  One AI system can has more than one form of product or service.",
            "broader": ("http://www.w3.org/ns/odrl/2/Asset",),
            "source_vocab": "STAV",
        },
        "https://w3id.org/stav#ProductVisualImage": {
            "label": "Product Visual Image",
            "definition": "A photograph or an illustration showing external features, marking, and internal layout of a product that the AI system is part of.",
            "broader": ("http://www.w3.org/ns/odrl/2/Asset",),
            "source_vocab": "STAV",
        },
        "https://w3id.org/stav#PuttingIntoService": {
            "label": "putting into service",
            "definition": "‘putting into service’ means the supply of an AI system for first use directly to the user or for own use on the Union market for its intended purpose.",
            "broader": ("http://www.w3.org/ns/odrl/2/Action",),
            "source_vocab": "STAV",
        },
        "https://w3id.org/stav#QualityManagementSystemDocumentationObligation": {
            "label": "Quality Management System Documentation Obligation",
            "definition": "A quality management system ensures compliance of an AI system. A quality management system documentation shall be in the form of written policies, procedures and instructions. It shall include a strategy for regulatory compliance; techniques, procedures and systematic actions to be used for the ...",
            "broader": ("https://w3id.org/stap#InformationCreationObligation",),
            "source_vocab": "STAV",
        },
        "https://w3id.org/stav#RealWorldConditionsTestingPlan": {
            "label": "Real World Conditions Testing Plan",
            "definition": "A summary of the main characteristics of the plan for testing in real world conditions.",
            "broader": ("http://www.w3.org/ns/odrl/2/Asset",),
            "source_vocab": "STAV",
        },
        "https://w3id.org/stav#RealWorldConditionsTestingSuspensionOrTerminationInformation": {
            "label": "Real World Conditions Testing Suspension Or Termination Information",
            "definition": "Information on the suspension or termination of the testing in real world conditions.",
            "broader": ("http://www.w3.org/ns/odrl/2/Asset",),
            "source_vocab": "STAV",
        },
        "https://w3id.org/stav#RealWorldConditionsTestingUser": {
            "label": "Real World Conditions Testing User",
            "definition": "users involved in the testing in real world conditions.",
            "broader": ("http://www.w3.org/ns/odrl/2/Party",),
            "source_vocab": "STAV",
        },
        "https://w3id.org/stav#RegisterationObligation": {
            "label": "Registeration Obligation",
            "definition": "A registration to a database containing information about AI systems.",
            "broader": ("https://w3id.org/stap#InformationSubmissionObligation",),
            "source_vocab": "STAV",
        },
        "https://w3id.org/stav#RiskManagementSystemDescription": {
            "label": "Risk Management System Description",
            "broader": ("http://www.w3.org/ns/odrl/2/Asset",),
            "source_vocab": "STAV",
        },
        "https://w3id.org/stav#SoftwareDependencies": {
            "label": "Software Dependencies",
            "definition": "The versions of relevant software or firmware and any requirement related to version update.",
            "broader": ("http://www.w3.org/ns/odrl/2/Asset",),
            "source_vocab": "STAV",
        },
        "https://w3id.org/stav#SystemDetailedDescription": {
            "label": "System Detailed Description",
            "broader": ("http://www.w3.org/ns/odrl/2/AssetCollection",),
            "source_vocab": "STAV",
        },
        "https://w3id.org/stav#SystemEvaluationDocumentation": {
            "label": "System Evaluation Documentation",
            "broader": ("http://www.w3.org/ns/odrl/2/AssetCollection",),
            "source_vocab": "STAV",
        },
        "https://w3id.org/stav#SystemGeneralDescription": {
            "label": "System General Description",
            "definition": "A general description of the AI system.",
            "broader": ("http://www.w3.org/ns/odrl/2/AssetCollection",),
            "source_vocab": "STAV",
        },
        "https://w3id.org/stav#TechnicalDocumentation": {
            "label": "Technical Documentation",
            "definition": "The technical documentation shall be drawn up in such a way to demonstrate that the high-risk AI system complies with the requirements set out in Title III Chapter 2 and provide national competent authorities and notified bodies with all the necessary information to assess the compliance of the A...",
            "broader": ("http://www.w3.org/ns/odrl/2/AssetCollection",),
            "source_vocab": "STAV",
        },
        "https://w3id.org/stav#TechnicalDocumentationObligation": {
            "label": "Technical Documentation Obligation",
            "definition": "The technical documentation of an AI system contains information including its intended purpose and limitations, risk management process, data governance, and instructions of use.",
            "broader": ("https://w3id.org/stap#InformationCreationObligation",),
            "source_vocab": "STAV",
        },
        "https://w3id.org/stav-eu-aia#EUAIAAIDatabaseRegisterationObligation": {
            "label": "AI Database Registeration Obligation (EU AI Act)",
            "broader": (
                "http://tair.adaptcentre.ie/ontologies/tair/AiActRequirement",
                "https://w3id.org/stav#RegisterationObligation",
            ),
            "source_vocab": "STAV-EU-AIA",
        },
        "https://w3id.org/stav-eu-aia#EUAIAQualityManagementSystemDocumentationObligation": {
            "label": "Quality Management System Documentation Obligation (EU AI Act)",
            "definition": "Article 17  Providers of high-risk AI systems shall put a quality management system in place that ensures compliance with this Regulation. That system shall be documented in a systematic and orderly manner in the form of written policies, procedures and instructions, and shall include at least th...",
            "broader": (
                "http://tair.adaptcentre.ie/ontologies/tair/AiActRequirement",
                "https://w3id.org/stav#QualityManagementSystemDocumentationObligation",
            ),
            "source_vocab": "STAV-EU-AIA",
        },
        "https://w3id.org/stav-eu-aia#EUAIATechnicalDocumentationObligation": {
            "label": "Technical Documentation Obligation (EU AI Act)",
            "definition": "The technical documentation shall be drawn up in such a way to demonstrate that the high-risk AI system compiles with the requirements set out in Chapter 2 and provide national competent authorities and notified bodies with all the necessary information to assess the compliance of the AI system w...",
            "broader": (
                "http://tair.adaptcentre.ie/ontologies/tair/AiActRequirement",
                "https://w3id.org/stav#TechnicalDocumentationObligation",
            ),
            "source_vocab": "STAV-EU-AIA",
        },
    }
)

__all__ = [
    "AIActDocumentation",
    "AIActObligation",
    "AIDeployer",
    "AIProvider",
    "AIRole",
    "AISystem",
    "AISystemStatus",
    "Action",
    "AiActChapter3Article18ReqColl",
    "AiActRequirement",
    "AiaPrReq_16_1_R1c",
    "AiaPrReq_16_1_R1f",
    "AiaPrReq_51_1_R1",
    "AppliedStandards",
    "Asset",
    "AssetCollection",
    "AuthorisedRepresentative",
    "BaselineProcessDescription",
    "BeingNotHighRiskCriteria",
    "BeingNotHighRiskGrounds",
    "ComponentsAndFunctionsSupportedDescription",
    "ConformityDeclaration",
    "CurrentAndPotentialFutureImpacts",
    "DataMinimizationPractices",
    "DataProtectionImpactAssessmentDocumentation",
    "DeploymentContext",
    "EUAIAAIDatabaseRegisterationObligation",
    "EUAIAQualityManagementSystemDocumentationObligation",
    "EUAIATechnicalDocumentationObligation",
    "ExternalInteractionDescription",
    "FundamentalRightsImpactAssessmentDocumentation",
    "ImpactAssessmentDocumentation",
    "InformationCreationObligation",
    "InformationSecurityMeasures",
    "InformationSubmissionObligation",
    "InformationSubmissionRepresentative",
    "InformationUsedBySystemDescription",
    "InstallationInstructions",
    "InstructionsForUse",
    "IntendedBenefitsOverPreviouslyExistingProcess",
    "IntendedHardwareDescription",
    "IntendedPurposes",
    "Log",
    "MakingAvailableOnTheMarket",
    "MarketSurveillenceAuthority",
    "Party",
    "PlacingOnTheMarket",
    "PostMarketEvaluationSystemDescription",
    "PreviouslyExistingProcessEvaluationDocumentation",
    "PreviouslyExistingProcessKnownNegativeImpactInformation",
    "PrivacyRisksAndPrivacyMeasuresEvaluationDocumentation",
    "ProductServiceDescription",
    "ProductVisualImage",
    "PuttingIntoService",
    "QualityManagementSystemDocumentationObligation",
    "RealWorldConditionsTestingPlan",
    "RealWorldConditionsTestingSuspensionOrTerminationInformation",
    "RealWorldConditionsTestingUser",
    "RegisterationObligation",
    "RiskManagementSystemDescription",
    "SoftwareDependencies",
    "SystemDetailedDescription",
    "SystemEvaluationDocumentation",
    "SystemGeneralDescription",
    "TechnicalDocumentation",
    "TechnicalDocumentationObligation",
]
