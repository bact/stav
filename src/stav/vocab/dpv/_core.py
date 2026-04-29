# SPDX-FileCopyrightText: 2026-present Arthit Suriyawongkul
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0
#
# AUTO-GENERATED — do not edit manually.
# Source: W3C Data Privacy Vocabulary (DPV) Core v2.3
# Generated: 2026-04-29T22:30:22Z
# Regenerate: python -m stav.codegen.generate tools/recipes/dpv_core.json

"""Vocabulary from W3C Data Privacy Vocabulary (DPV) Core v2.3.

1116 term constants (accessible as ``module.TermName``)."""

from __future__ import annotations

from stav._registry import _register
from stav.term import _StavVocabEnum

__stav_namespace__ = "vocab.dpv"

# ── Individual term constants ─────────────────────────────────────────────────────
# Plain string IRIs — use directly with MLflow, Pitloom, SBOM serialisers.
# Metadata (label, definition, broader) via: stav.label(NaturalPerson) etc.
AcademicResearch = "https://w3id.org/dpv#AcademicResearch"  # Academic Research
AcademicScientificOrganisation = (
    "https://w3id.org/dpv#AcademicScientificOrganisation"  # Academic or Scientific Organisation
)
AcceptableRule = "https://w3id.org/dpv#AcceptableRule"  # Acceptable Rule
AcceptableUsePolicy = "https://w3id.org/dpv#AcceptableUsePolicy"  # Acceptable Use Policy
AcceptContract = "https://w3id.org/dpv#AcceptContract"  # Accept Contract
Access = "https://w3id.org/dpv#Access"
AccessControlMethod = "https://w3id.org/dpv#AccessControlMethod"  # Access Control Method
AccountManagement = "https://w3id.org/dpv#AccountManagement"  # Account Management
Acquire = "https://w3id.org/dpv#Acquire"
ActivelyInvolved = "https://w3id.org/dpv#ActivelyInvolved"  # Actively Involved
ActiveRight = "https://w3id.org/dpv#ActiveRight"  # Active Right
ActivityCompleted = "https://w3id.org/dpv#ActivityCompleted"  # Activity Completed
ActivityHalted = "https://w3id.org/dpv#ActivityHalted"  # Activity Halted
ActivityMonitoring = "https://w3id.org/dpv#ActivityMonitoring"  # Activity Monitoring
ActivityNotCompleted = "https://w3id.org/dpv#ActivityNotCompleted"  # Activity Not Completed
ActivityOngoing = "https://w3id.org/dpv#ActivityOngoing"  # Activity Ongoing
ActivityPlanned = "https://w3id.org/dpv#ActivityPlanned"  # Activity Planned
ActivityProposed = "https://w3id.org/dpv#ActivityProposed"  # Activity Proposed
ActivityStatus = "https://w3id.org/dpv#ActivityStatus"  # Activity Status
Adapt = "https://w3id.org/dpv#Adapt"
Adult = "https://w3id.org/dpv#Adult"
Advertising = "https://w3id.org/dpv#Advertising"
Agent = "https://w3id.org/dpv#Agent"
AgeVerification = "https://w3id.org/dpv#AgeVerification"  # Age Verification
Aggregate = "https://w3id.org/dpv#Aggregate"
AIGovernance = "https://w3id.org/dpv#AIGovernance"  # AI Governance
AILiteracy = "https://w3id.org/dpv#AILiteracy"  # AI Literacy
AINotice = "https://w3id.org/dpv#AINotice"  # AI Notice
AlgorithmicLogic = "https://w3id.org/dpv#AlgorithmicLogic"  # Algorithmic Logic
Align = "https://w3id.org/dpv#Align"
Alter = "https://w3id.org/dpv#Alter"
AmbulanceProvider = "https://w3id.org/dpv#AmbulanceProvider"  # Ambulance Provider
Analyse = "https://w3id.org/dpv#Analyse"
Anonymisation = "https://w3id.org/dpv#Anonymisation"
Anonymise = "https://w3id.org/dpv#Anonymise"
AnonymisedData = "https://w3id.org/dpv#AnonymisedData"  # Anonymised Data
Applicability = "https://w3id.org/dpv#Applicability"
Applicant = "https://w3id.org/dpv#Applicant"
ApprovalProcedure = "https://w3id.org/dpv#ApprovalProcedure"  # Approval Procedure
Assess = "https://w3id.org/dpv#Assess"
Assessment = "https://w3id.org/dpv#Assessment"
AssetManagementProcedures = "https://w3id.org/dpv#AssetManagementProcedures"  # Asset Management Procedures
AssistiveAutomation = "https://w3id.org/dpv#AssistiveAutomation"  # Assistive Automation
AsylumSeeker = "https://w3id.org/dpv#AsylumSeeker"  # Asylum Seeker
AsymmetricCryptography = "https://w3id.org/dpv#AsymmetricCryptography"  # Asymmetric Cryptography
AsymmetricEncryption = "https://w3id.org/dpv#AsymmetricEncryption"  # Asymmetric Encryption
Audit = "https://w3id.org/dpv#Audit"
AuditApproved = "https://w3id.org/dpv#AuditApproved"  # Audit Approved
AuditConditionallyApproved = "https://w3id.org/dpv#AuditConditionallyApproved"  # Audit Conditionally Approved
AuditNotRequired = "https://w3id.org/dpv#AuditNotRequired"  # Audit Not Required
AuditRejected = "https://w3id.org/dpv#AuditRejected"  # Audit Rejected
AuditRequested = "https://w3id.org/dpv#AuditRequested"  # Audit Requested
AuditRequired = "https://w3id.org/dpv#AuditRequired"  # Audit Required
AuditStatus = "https://w3id.org/dpv#AuditStatus"  # Audit Status
Authentication_ABC = "https://w3id.org/dpv#Authentication-ABC"  # Authentication using ABC
Authentication_PABC = "https://w3id.org/dpv#Authentication-PABC"  # Authentication using PABC
AuthenticationProtocols = "https://w3id.org/dpv#AuthenticationProtocols"  # Authentication Protocols
AuthorisationProcedure = "https://w3id.org/dpv#AuthorisationProcedure"  # Authorisation Procedure
AuthorisationProtocols = "https://w3id.org/dpv#AuthorisationProtocols"  # Authorisation Protocols
Authority = "https://w3id.org/dpv#Authority"
AuthorityInformed = "https://w3id.org/dpv#AuthorityInformed"  # Authority Informed
AuthorityUninformed = "https://w3id.org/dpv#AuthorityUninformed"  # Authority Uninformed
AutomatedDecisionMaking = "https://w3id.org/dpv#AutomatedDecisionMaking"  # Automated Decision Making
AutomatedScoringOfIndividuals = "https://w3id.org/dpv#AutomatedScoringOfIndividuals"  # Automated Scoring of Individuals
AutomationLevel = "https://w3id.org/dpv#AutomationLevel"  # Automation Level
Autonomous = "https://w3id.org/dpv#Autonomous"
B2B2CContract = "https://w3id.org/dpv#B2B2CContract"  # Business-to-Business-to-Consumer Contract
B2BContract = "https://w3id.org/dpv#B2BContract"  # Business-to-Business Contract
B2CContract = "https://w3id.org/dpv#B2CContract"  # Business-to-Consumer Contract
BackgroundChecks = "https://w3id.org/dpv#BackgroundChecks"  # Background Checks
BiometricAuthentication = "https://w3id.org/dpv#BiometricAuthentication"  # Biometric Authentication
C2BContract = "https://w3id.org/dpv#C2BContract"  # Consumer-to-Business Contract
C2CContract = "https://w3id.org/dpv#C2CContract"  # Consumer-to-Consumer Contract
CannotChallengeProcess = "https://w3id.org/dpv#CannotChallengeProcess"  # Cannot Challenge Process
CannotChallengeProcessInput = "https://w3id.org/dpv#CannotChallengeProcessInput"  # Cannot Challenge Process Input
CannotChallengeProcessOutput = "https://w3id.org/dpv#CannotChallengeProcessOutput"  # Cannot Challenge Process Output
CannotCorrectProcess = "https://w3id.org/dpv#CannotCorrectProcess"  # Cannot Correct Process
CannotCorrectProcessInput = "https://w3id.org/dpv#CannotCorrectProcessInput"  # Cannot Correct Process Input
CannotCorrectProcessOutput = "https://w3id.org/dpv#CannotCorrectProcessOutput"  # Cannot Correct Process Output
CannotObjectToProcess = "https://w3id.org/dpv#CannotObjectToProcess"  # Cannot Object to Process
CannotOptInToProcess = "https://w3id.org/dpv#CannotOptInToProcess"  # Cannot Opt-in to Process
CannotOptOutFromProcess = "https://w3id.org/dpv#CannotOptOutFromProcess"  # Cannot Opt-out from Process
CannotReverseProcessEffects = "https://w3id.org/dpv#CannotReverseProcessEffects"  # Cannot Reverse Process Effects
CannotReverseProcessInput = "https://w3id.org/dpv#CannotReverseProcessInput"  # Cannot Reverse Process Input
CannotReverseProcessOutput = "https://w3id.org/dpv#CannotReverseProcessOutput"  # Cannot Reverse Process Output
CannotWithdrawFromProcess = "https://w3id.org/dpv#CannotWithdrawFromProcess"  # Cannot Withdraw from Process
Certification = "https://w3id.org/dpv#Certification"
CertificationSeal = "https://w3id.org/dpv#CertificationSeal"  # Certification and Seal
ChallengingProcess = "https://w3id.org/dpv#ChallengingProcess"  # Challenging Process
ChallengingProcessInput = "https://w3id.org/dpv#ChallengingProcessInput"  # Challenging Process Input
ChallengingProcessOutput = "https://w3id.org/dpv#ChallengingProcessOutput"  # Challenging Process Output
CharityOrganisation = "https://w3id.org/dpv#CharityOrganisation"  # Charity Organisation
Child = "https://w3id.org/dpv#Child"
Citizen = "https://w3id.org/dpv#Citizen"
City = "https://w3id.org/dpv#City"
Client = "https://w3id.org/dpv#Client"
Clinic = "https://w3id.org/dpv#Clinic"
CloudLocation = "https://w3id.org/dpv#CloudLocation"  # Cloud Location
CodeOfConduct = "https://w3id.org/dpv#CodeOfConduct"  # Code of Conduct
Collect = "https://w3id.org/dpv#Collect"
CollectedData = "https://w3id.org/dpv#CollectedData"  # Collected Data
CollectedPersonalData = "https://w3id.org/dpv#CollectedPersonalData"  # Collected Personal Data
CombatClimateChange = "https://w3id.org/dpv#CombatClimateChange"  # Combat Climate Change
Combine = "https://w3id.org/dpv#Combine"
CommerciallyConfidentialData = "https://w3id.org/dpv#CommerciallyConfidentialData"  # Commercially Confidential Data
CommercialPurpose = "https://w3id.org/dpv#CommercialPurpose"  # Commercial Purpose
CommercialResearch = "https://w3id.org/dpv#CommercialResearch"  # Commercial Research
CommunicationForCustomerCare = "https://w3id.org/dpv#CommunicationForCustomerCare"  # Communication for Customer Care
CommunicationManagement = "https://w3id.org/dpv#CommunicationManagement"  # Communication Management
CompatibilityUnknown = "https://w3id.org/dpv#CompatibilityUnknown"  # Compatibility Unknown
ComplianceAssessment = "https://w3id.org/dpv#ComplianceAssessment"  # Compliance Assessment
ComplianceIndeterminate = "https://w3id.org/dpv#ComplianceIndeterminate"  # Compliance Indeterminate
ComplianceMonitoring = "https://w3id.org/dpv#ComplianceMonitoring"  # Compliance Monitoring
ComplianceStatus = "https://w3id.org/dpv#ComplianceStatus"  # Compliance Status
ComplianceUnknown = "https://w3id.org/dpv#ComplianceUnknown"  # Compliance Unknown
ComplianceViolation = "https://w3id.org/dpv#ComplianceViolation"  # Compliance Violation
Compliant = "https://w3id.org/dpv#Compliant"
ConditionalAutomation = "https://w3id.org/dpv#ConditionalAutomation"  # Conditional Automation
ConfidentialData = "https://w3id.org/dpv#ConfidentialData"  # Confidential Data
ConfidentialityAgreement = "https://w3id.org/dpv#ConfidentialityAgreement"  # Confidentiality Agreement
ConformanceAssessment = "https://w3id.org/dpv#ConformanceAssessment"  # Conformance Assessment
ConformanceStatus = "https://w3id.org/dpv#ConformanceStatus"  # Conformance Status
Conformant = "https://w3id.org/dpv#Conformant"
Consent = "https://w3id.org/dpv#Consent"
ConsentControl = "https://w3id.org/dpv#ConsentControl"  # Consent Control
ConsentExpired = "https://w3id.org/dpv#ConsentExpired"  # Consent Expired
ConsentGiven = "https://w3id.org/dpv#ConsentGiven"  # Consent Given
ConsentInvalidated = "https://w3id.org/dpv#ConsentInvalidated"  # Consent Invalidated
ConsentManagement = "https://w3id.org/dpv#ConsentManagement"  # Consent Management
ConsentNotice = "https://w3id.org/dpv#ConsentNotice"  # Consent Notice
ConsentReceipt = "https://w3id.org/dpv#ConsentReceipt"  # Consent Receipt
ConsentRecord = "https://w3id.org/dpv#ConsentRecord"  # Consent Record
ConsentRefused = "https://w3id.org/dpv#ConsentRefused"  # Consent Refused
ConsentRequestDeferred = "https://w3id.org/dpv#ConsentRequestDeferred"  # Consent Request Deferred
ConsentRequested = "https://w3id.org/dpv#ConsentRequested"  # Consent Requested
ConsentRevoked = "https://w3id.org/dpv#ConsentRevoked"  # Consent Revoked
ConsentStatus = "https://w3id.org/dpv#ConsentStatus"  # Consent Status
ConsentStatusInvalidForProcessing = (
    "https://w3id.org/dpv#ConsentStatusInvalidForProcessing"  # Consent Status Invalid for Processing
)
ConsentStatusValidForProcessing = (
    "https://w3id.org/dpv#ConsentStatusValidForProcessing"  # Consent Status Valid for Processing
)
ConsentUnknown = "https://w3id.org/dpv#ConsentUnknown"  # Consent Unknown
ConsentWithdrawn = "https://w3id.org/dpv#ConsentWithdrawn"  # Consent Withdrawn
Consequence = "https://w3id.org/dpv#Consequence"
ConsequenceAsSideEffect = "https://w3id.org/dpv#ConsequenceAsSideEffect"  # Consequence as Side-Effect
ConsequenceOfFailure = "https://w3id.org/dpv#ConsequenceOfFailure"  # Consequence of Failure
ConsequenceOfSuccess = "https://w3id.org/dpv#ConsequenceOfSuccess"  # Consequence of Success
Consult = "https://w3id.org/dpv#Consult"
Consultation = "https://w3id.org/dpv#Consultation"
ConsultationWithAuthority = "https://w3id.org/dpv#ConsultationWithAuthority"  # Consultation with Authority
ConsultationWithDataSubject = "https://w3id.org/dpv#ConsultationWithDataSubject"  # Consultation with Data Subject
ConsultationWithDataSubjectRepresentative = (
    "https://w3id.org/dpv#ConsultationWithDataSubjectRepresentative"  # Consultation with Data Subject Representative
)
ConsultationWithDPO = "https://w3id.org/dpv#ConsultationWithDPO"  # Consultation with DPO
Consumer = "https://w3id.org/dpv#Consumer"
ConsumerStandardFormContract = "https://w3id.org/dpv#ConsumerStandardFormContract"  # Consumer Standard Form Contract
Context = "https://w3id.org/dpv#Context"
ContextuallyAnonymisedData = "https://w3id.org/dpv#ContextuallyAnonymisedData"  # Contextually Anonymised Data
ContinuousFrequency = "https://w3id.org/dpv#ContinuousFrequency"  # Continuous Frequency
Contract = "https://w3id.org/dpv#Contract"
ContractActivationStatus = "https://w3id.org/dpv#ContractActivationStatus"  # Contract Activation Status
ContractActive = "https://w3id.org/dpv#ContractActive"  # Contract Active
ContractAmended = "https://w3id.org/dpv#ContractAmended"  # Contract Amended
ContractAmendmentClause = "https://w3id.org/dpv#ContractAmendmentClause"  # Contract Amendment Clause
ContractApproved = "https://w3id.org/dpv#ContractApproved"  # Contract Approved
ContractBeingPerformed = "https://w3id.org/dpv#ContractBeingPerformed"  # Contract Being Performed
ContractBreached = "https://w3id.org/dpv#ContractBreached"  # Contract Breached
ContractByDomain = "https://w3id.org/dpv#ContractByDomain"  # Contract by Domain
ContractByEntityType = "https://w3id.org/dpv#ContractByEntityType"  # Contract by Entity Type
ContractByNegotiationType = "https://w3id.org/dpv#ContractByNegotiationType"  # Contract by Negotiation Type
ContractConfidentialityClause = "https://w3id.org/dpv#ContractConfidentialityClause"  # Contract Confidentiality Clause
ContractControl = "https://w3id.org/dpv#ContractControl"  # Contract Control
ContractDefinitions = "https://w3id.org/dpv#ContractDefinitions"  # Contract Definitions
ContractDisputed = "https://w3id.org/dpv#ContractDisputed"  # Contract Disputed
ContractDisputeResolutionClause = (
    "https://w3id.org/dpv#ContractDisputeResolutionClause"  # Contract DisputeResolution Clause
)
ContractDrafted = "https://w3id.org/dpv#ContractDrafted"  # Contract Drafted
ContractExecutionStatus = "https://w3id.org/dpv#ContractExecutionStatus"  # Contract Execution Status
ContractExpired = "https://w3id.org/dpv#ContractExpired"  # Contract Expired
ContractExtended = "https://w3id.org/dpv#ContractExtended"  # Contract Extended
ContractFulfilled = "https://w3id.org/dpv#ContractFulfilled"  # Contract Fulfilled
ContractFulfilmentStatus = "https://w3id.org/dpv#ContractFulfilmentStatus"  # Contract Fulfilment Status
ContractFullyExecuted = "https://w3id.org/dpv#ContractFullyExecuted"  # Contract Fully Executed
ContractFullySigned = "https://w3id.org/dpv#ContractFullySigned"  # Contract Fully Signed
ContractInactive = "https://w3id.org/dpv#ContractInactive"  # Contract Inactive
ContractJurisdictionClause = "https://w3id.org/dpv#ContractJurisdictionClause"  # Contract Jurisdiction Clause
ContractNegotiated = "https://w3id.org/dpv#ContractNegotiated"  # Contract Negotiated
ContractNotFulfilled = "https://w3id.org/dpv#ContractNotFulfilled"  # Contract Not Fulfilled
ContractOffered = "https://w3id.org/dpv#ContractOffered"  # Contract Offered
ContractPartiallyFulfilled = "https://w3id.org/dpv#ContractPartiallyFulfilled"  # Contract Partially Fulfilled
ContractPartiallySigned = "https://w3id.org/dpv#ContractPartiallySigned"  # Contract Partially Signed
ContractPerformance = "https://w3id.org/dpv#ContractPerformance"  # Contract Performance
ContractPerformanceStatus = "https://w3id.org/dpv#ContractPerformanceStatus"  # Contract Performance Status
ContractPreamble = "https://w3id.org/dpv#ContractPreamble"  # Contract Preamble
ContractPreparationStatus = "https://w3id.org/dpv#ContractPreparationStatus"  # Contract Preparation Status
ContractRejected = "https://w3id.org/dpv#ContractRejected"  # Contract Rejected
ContractRenewed = "https://w3id.org/dpv#ContractRenewed"  # Contract Renewed
ContractSignedByParty = "https://w3id.org/dpv#ContractSignedByParty"  # Contract Signed By Party
ContractStatus = "https://w3id.org/dpv#ContractStatus"  # Contract Status
ContractTemporarilySuspended = "https://w3id.org/dpv#ContractTemporarilySuspended"  # Contract Temporarily Suspended
ContractTerminated = "https://w3id.org/dpv#ContractTerminated"  # Contract Terminated
ContractTerminationClause = "https://w3id.org/dpv#ContractTerminationClause"  # Contract Termination Clause
ContractTerminationStatus = "https://w3id.org/dpv#ContractTerminationStatus"  # Contract Termination Status
ContractualClause = "https://w3id.org/dpv#ContractualClause"  # Contractual Clause
ContractualClauseFulfilled = "https://w3id.org/dpv#ContractualClauseFulfilled"  # Contractual Clause Fulfilled
ContractualClauseFulfilmentStatus = (
    "https://w3id.org/dpv#ContractualClauseFulfilmentStatus"  # Contractual Clause Fulfilment Status
)
ContractualClauseNotFulfilled = "https://w3id.org/dpv#ContractualClauseNotFulfilled"  # Contractual Clause Unfulfilled
ContractualClausePartiallyFulfilled = (
    "https://w3id.org/dpv#ContractualClausePartiallyFulfilled"  # Contractual Clause Partially Fulfilled
)
ContractualClauseViolated = "https://w3id.org/dpv#ContractualClauseViolated"  # Contractual Clause Breached
ContractualTerms = "https://w3id.org/dpv#ContractualTerms"  # Contractual Terms
ContractUnderNegotiation = "https://w3id.org/dpv#ContractUnderNegotiation"  # Contract Under Negotiation
ContractUnderReview = "https://w3id.org/dpv#ContractUnderReview"  # Contract Under Review
ContractViolated = "https://w3id.org/dpv#ContractViolated"  # Contract Violated
ControllerDataSubjectAgreement = (
    "https://w3id.org/dpv#ControllerDataSubjectAgreement"  # Controller-Data Subject Agreement
)
ControllerInformed = "https://w3id.org/dpv#ControllerInformed"  # Controller Informed
ControllerProcessorAgreement = "https://w3id.org/dpv#ControllerProcessorAgreement"  # Controller-Processor Agreement
ControllerUninformed = "https://w3id.org/dpv#ControllerUninformed"  # Controller Uninformed
Copy = "https://w3id.org/dpv#Copy"
CorrectingProcess = "https://w3id.org/dpv#CorrectingProcess"  # Correcting Process
CorrectingProcessInput = "https://w3id.org/dpv#CorrectingProcessInput"  # Correcting Process Input
CorrectingProcessOutput = "https://w3id.org/dpv#CorrectingProcessOutput"  # Correcting Process Output
CounterMoneyLaundering = "https://w3id.org/dpv#CounterMoneyLaundering"  # Counter Money Laundering
Counterterrorism = "https://w3id.org/dpv#Counterterrorism"
Country = "https://w3id.org/dpv#Country"
CredentialManagement = "https://w3id.org/dpv#CredentialManagement"  # Credential Management
CrossBorderTransfer = "https://w3id.org/dpv#CrossBorderTransfer"  # Cross-Border Transfer
CryptographicAuthentication = "https://w3id.org/dpv#CryptographicAuthentication"  # Cryptographic Authentication
CryptographicKeyManagement = "https://w3id.org/dpv#CryptographicKeyManagement"  # Cryptographic Key Management
CryptographicMethods = "https://w3id.org/dpv#CryptographicMethods"  # Cryptographic Methods
Customer = "https://w3id.org/dpv#Customer"
CustomerCare = "https://w3id.org/dpv#CustomerCare"  # Customer Care
CustomerClaimsManagement = "https://w3id.org/dpv#CustomerClaimsManagement"  # Customer Claims Management
CustomerManagement = "https://w3id.org/dpv#CustomerManagement"  # Customer Management
CustomerOrderManagement = "https://w3id.org/dpv#CustomerOrderManagement"  # Customer Order Management
CustomerRelationshipManagement = (
    "https://w3id.org/dpv#CustomerRelationshipManagement"  # Customer Relationship Management
)
CustomerSolvencyMonitoring = "https://w3id.org/dpv#CustomerSolvencyMonitoring"  # Customer Solvency Monitoring
CybersecurityAssessment = "https://w3id.org/dpv#CybersecurityAssessment"  # Cybersecurity Assessment
CybersecurityTraining = "https://w3id.org/dpv#CybersecurityTraining"  # Cybersecurity Training
DashboardNotice = "https://w3id.org/dpv#DashboardNotice"  # Dashboard Notice
Data = "https://w3id.org/dpv#Data"
DataAltruism = "https://w3id.org/dpv#DataAltruism"  # Data Altruism
DataAvailabilityAssessment = "https://w3id.org/dpv#DataAvailabilityAssessment"  # Data Availability Assessment
DataBackupProtocols = "https://w3id.org/dpv#DataBackupProtocols"  # Data Backup Protocols
DataBreachImpactAssessment = "https://w3id.org/dpv#DataBreachImpactAssessment"  # Data Breach Impact Assessment (DBIA)
DataBreachNotice = "https://w3id.org/dpv#DataBreachNotice"  # Data Breach Notice
DataBreachNotification = "https://w3id.org/dpv#DataBreachNotification"  # Data Breach Notification
DataBreachRecord = "https://w3id.org/dpv#DataBreachRecord"  # Data Breach Record
DataController = "https://w3id.org/dpv#DataController"  # Data Controller
DataControllerContract = "https://w3id.org/dpv#DataControllerContract"  # Data Controller Contract
DataControllerDataSource = "https://w3id.org/dpv#DataControllerDataSource"  # Data Controller as Data Source
DataDeletionPolicy = "https://w3id.org/dpv#DataDeletionPolicy"  # Data Deletion Policy
DataErasurePolicy = "https://w3id.org/dpv#DataErasurePolicy"  # Data Erasure Policy
DataExporter = "https://w3id.org/dpv#DataExporter"  # Data Exporter
DataGovernance = "https://w3id.org/dpv#DataGovernance"  # Data Governance
DataHandlingClause = "https://w3id.org/dpv#DataHandlingClause"  # Data Handling Clause
DataImporter = "https://w3id.org/dpv#DataImporter"  # Data Importer
DataInteroperabilityAssessment = (
    "https://w3id.org/dpv#DataInteroperabilityAssessment"  # Data Interoperability Assessment
)
DataInteroperabilityImprovement = (
    "https://w3id.org/dpv#DataInteroperabilityImprovement"  # Data Interoperability Improvement
)
DataInteroperabilityManagement = (
    "https://w3id.org/dpv#DataInteroperabilityManagement"  # Data Interoperability Management
)
DataInventoryManagement = "https://w3id.org/dpv#DataInventoryManagement"  # Data Inventory Management
DataJurisdictionPolicy = "https://w3id.org/dpv#DataJurisdictionPolicy"  # Data Jurisdiction Policy
DataLiteracy = "https://w3id.org/dpv#DataLiteracy"  # Data Literacy
DataProcessingAgreement = "https://w3id.org/dpv#DataProcessingAgreement"  # Data Processing Agreement
DataProcessingPolicy = "https://w3id.org/dpv#DataProcessingPolicy"  # Data Processing Policy
DataProcessingRecord = "https://w3id.org/dpv#DataProcessingRecord"  # Data Processing Record
DataProcessor = "https://w3id.org/dpv#DataProcessor"  # Data Processor
DataProcessorContract = "https://w3id.org/dpv#DataProcessorContract"  # Data Processor Contract
DataProtectionAuthority = "https://w3id.org/dpv#DataProtectionAuthority"  # Data Protection Authority
DataProtectionOfficer = "https://w3id.org/dpv#DataProtectionOfficer"  # Data Protection Officer
DataProtectionTraining = "https://w3id.org/dpv#DataProtectionTraining"  # Data Protection Training
DataPublishedByDataSubject = "https://w3id.org/dpv#DataPublishedByDataSubject"  # Data published by Data Subject
DataQualityAssessment = "https://w3id.org/dpv#DataQualityAssessment"  # Data Quality Assessment
DataQualityImprovement = "https://w3id.org/dpv#DataQualityImprovement"  # Data Quality Improvement
DataQualityManagement = "https://w3id.org/dpv#DataQualityManagement"  # Data Quality Management
DataRedaction = "https://w3id.org/dpv#DataRedaction"  # Data Redaction
DataRestorationPolicy = "https://w3id.org/dpv#DataRestorationPolicy"  # Data Restoration Policy
DataReusePolicy = "https://w3id.org/dpv#DataReusePolicy"  # Data Reuse Policy
DataSanitisationTechnique = "https://w3id.org/dpv#DataSanitisationTechnique"  # Data Sanitisation Technique
DataSecurityManagement = "https://w3id.org/dpv#DataSecurityManagement"  # Data Security Management
DataSource = "https://w3id.org/dpv#DataSource"  # Data Source
DataStoragePolicy = "https://w3id.org/dpv#DataStoragePolicy"  # Data Storage Policy
DataSubject = "https://w3id.org/dpv#DataSubject"  # Data Subject
DataSubjectContract = "https://w3id.org/dpv#DataSubjectContract"  # Data Subject Contract
DataSubjectDataSource = "https://w3id.org/dpv#DataSubjectDataSource"  # Data Subject as Data Source
DataSubjectInformed = "https://w3id.org/dpv#DataSubjectInformed"  # Data Subject Informed
DataSubjectRight = "https://w3id.org/dpv#DataSubjectRight"  # Data Subject Right
DataSubjectRightsManagement = "https://w3id.org/dpv#DataSubjectRightsManagement"  # Data Subject Rights Management
DataSubjectScale = "https://w3id.org/dpv#DataSubjectScale"  # Data Subject Scale
DataSubjectUninformed = "https://w3id.org/dpv#DataSubjectUninformed"  # Data Subject Uninformed
DataSubProcessor = "https://w3id.org/dpv#DataSubProcessor"  # Data Sub-Processor
DataSuitabilityAssessment = "https://w3id.org/dpv#DataSuitabilityAssessment"  # Data Suitability Assessment
DataTransferImpactAssessment = "https://w3id.org/dpv#DataTransferImpactAssessment"  # Data Transfer Impact Assessment
DataTransferLegalBasis = "https://w3id.org/dpv#DataTransferLegalBasis"  # Data Transfer Legal Basis
DataTransferNotice = "https://w3id.org/dpv#DataTransferNotice"  # Data Transfer Notice
DataTransferRecord = "https://w3id.org/dpv#DataTransferRecord"  # Data Transfer Record
DataVolume = "https://w3id.org/dpv#DataVolume"  # Data Volume
DecentralisedLocations = "https://w3id.org/dpv#DecentralisedLocations"  # Decentralised Locations
DecisionMaking = "https://w3id.org/dpv#DecisionMaking"  # Decision Making
Deidentification = "https://w3id.org/dpv#Deidentification"  # De-Identification
Delete = "https://w3id.org/dpv#Delete"
DeliveryOfGoods = "https://w3id.org/dpv#DeliveryOfGoods"  # Delivery of Goods
Derive = "https://w3id.org/dpv#Derive"
DerivedData = "https://w3id.org/dpv#DerivedData"  # Derived Data
DerivedPersonalData = "https://w3id.org/dpv#DerivedPersonalData"  # Derived Personal Data
DesignStandard = "https://w3id.org/dpv#DesignStandard"  # Design Standard
Destruct = "https://w3id.org/dpv#Destruct"
DeterministicPseudonymisation = "https://w3id.org/dpv#DeterministicPseudonymisation"  # Deterministic Pseudonymisation
Deterrence = "https://w3id.org/dpv#Deterrence"
DeterrenceFollowed = "https://w3id.org/dpv#DeterrenceFollowed"  # Deterrence Followed
DeterrenceNotFollowed = "https://w3id.org/dpv#DeterrenceNotFollowed"  # Deterrence Not Followed
DeviceNotice = "https://w3id.org/dpv#DeviceNotice"  # Device Notice
DifferentialPrivacy = "https://w3id.org/dpv#DifferentialPrivacy"  # Differential Privacy
DigitalLiteracy = "https://w3id.org/dpv#DigitalLiteracy"  # Digital Literacy
DigitalRightsManagement = "https://w3id.org/dpv#DigitalRightsManagement"  # Digital Rights Management
DigitalSignatures = "https://w3id.org/dpv#DigitalSignatures"  # Digital Signatures
DirectMarketing = "https://w3id.org/dpv#DirectMarketing"  # Direct Marketing
DisasterRecoveryProcedures = "https://w3id.org/dpv#DisasterRecoveryProcedures"  # Disaster Recovery Procedures
Disclose = "https://w3id.org/dpv#Disclose"
DiscloseByTransmission = "https://w3id.org/dpv#DiscloseByTransmission"  # Disclose by Transmission
Display = "https://w3id.org/dpv#Display"
DisputeManagement = "https://w3id.org/dpv#DisputeManagement"  # Dispute Management
Disseminate = "https://w3id.org/dpv#Disseminate"
DistributedSystemSecurity = "https://w3id.org/dpv#DistributedSystemSecurity"  # Distributed System Security
DistributionAgreement = "https://w3id.org/dpv#DistributionAgreement"  # Distribution Agreement
DocumentRandomisedPseudonymisation = (
    "https://w3id.org/dpv#DocumentRandomisedPseudonymisation"  # Document Randomised Pseudonymisation
)
DocumentSecurity = "https://w3id.org/dpv#DocumentSecurity"  # Document Security
Download = "https://w3id.org/dpv#Download"
DPIA = "https://w3id.org/dpv#DPIA"  # Data Protection Impact Assessment (DPIA)
Duration = "https://w3id.org/dpv#Duration"
EconomicUnion = "https://w3id.org/dpv#EconomicUnion"  # Economic Union
EducationalOrganisation = "https://w3id.org/dpv#EducationalOrganisation"  # Educational Organisation
EducationalTraining = "https://w3id.org/dpv#EducationalTraining"  # Educational Training
EffectivenessDeterminationProcedures = (
    "https://w3id.org/dpv#EffectivenessDeterminationProcedures"  # Effectiveness Determination Procedures
)
ElderlyDataSubject = "https://w3id.org/dpv#ElderlyDataSubject"  # Elderly Data Subject
ElderlyHuman = "https://w3id.org/dpv#ElderlyHuman"  # Elderly Human
EmergencyHealthcareProvider = "https://w3id.org/dpv#EmergencyHealthcareProvider"  # Emergency Healthcare Provider
EmergencyServiceProvider = "https://w3id.org/dpv#EmergencyServiceProvider"  # Emergency Service Provider
Employee = "https://w3id.org/dpv#Employee"
EmploymentContract = "https://w3id.org/dpv#EmploymentContract"  # Employment Contract
Encryption = "https://w3id.org/dpv#Encryption"
EncryptionAtRest = "https://w3id.org/dpv#EncryptionAtRest"  # Encryption at Rest
EncryptionInTransfer = "https://w3id.org/dpv#EncryptionInTransfer"  # Encryption in Transfer
EncryptionInUse = "https://w3id.org/dpv#EncryptionInUse"  # Encryption in Use
EndlessDuration = "https://w3id.org/dpv#EndlessDuration"  # Endless Duration
EndToEndEncryption = "https://w3id.org/dpv#EndToEndEncryption"  # End-to-End Encryption (E2EE)
EnforceAccessControl = "https://w3id.org/dpv#EnforceAccessControl"  # Enforce Access Control
EnforceSecurity = "https://w3id.org/dpv#EnforceSecurity"  # Enforce Security
EnterIntoContract = "https://w3id.org/dpv#EnterIntoContract"  # Enter Into Contract
Entity = "https://w3id.org/dpv#Entity"
EntityActiveInvolvement = "https://w3id.org/dpv#EntityActiveInvolvement"  # Entity Active Involvement
EntityInformed = "https://w3id.org/dpv#EntityInformed"  # Entity Informed
EntityInformedStatus = "https://w3id.org/dpv#EntityInformedStatus"  # Entity Informed Status
EntityIntendedInvolvement = "https://w3id.org/dpv#EntityIntendedInvolvement"  # Entity Intended Involvement
EntityInvolved = "https://w3id.org/dpv#EntityInvolved"  # Entity Involved
EntityInvolvement = "https://w3id.org/dpv#EntityInvolvement"  # Entity Involvement
EntityInvolvementStatus = "https://w3id.org/dpv#EntityInvolvementStatus"  # Entity Involvement Status
EntityNonInvolvement = "https://w3id.org/dpv#EntityNonInvolvement"  # Entity Non-Involvement
EntityNonPermissiveInvolvement = (
    "https://w3id.org/dpv#EntityNonPermissiveInvolvement"  # Entity Non-Permissive Involvement
)
EntityNotInvolved = "https://w3id.org/dpv#EntityNotInvolved"  # Entity Not Involved
EntityPassiveInvolvement = "https://w3id.org/dpv#EntityPassiveInvolvement"  # Entity Passive Involvement
EntityPermissiveInvolvement = "https://w3id.org/dpv#EntityPermissiveInvolvement"  # Entity Permissive Involvement
EntityUninformed = "https://w3id.org/dpv#EntityUninformed"  # Entity Uninformed
EntityUnintendedInvolvement = "https://w3id.org/dpv#EntityUnintendedInvolvement"  # Entity Unintended Involvement
EnvironmentalProtection = "https://w3id.org/dpv#EnvironmentalProtection"  # Environmental Protection
Erase = "https://w3id.org/dpv#Erase"
EstablishContractualAgreement = "https://w3id.org/dpv#EstablishContractualAgreement"  # Establish Contractual Agreement
EULA = "https://w3id.org/dpv#EULA"  # End User License Agreement (EULA)
EvaluationOfIndividuals = "https://w3id.org/dpv#EvaluationOfIndividuals"  # Evaluation of Individuals
EvaluationScoring = "https://w3id.org/dpv#EvaluationScoring"  # Evaluation and Scoring
ExpectationStatus = "https://w3id.org/dpv#ExpectationStatus"  # Expectation Status
Expected = "https://w3id.org/dpv#Expected"
ExplicitlyExpressedConsent = "https://w3id.org/dpv#ExplicitlyExpressedConsent"  # Explicitly Expressed Consent
Export = "https://w3id.org/dpv#Export"
ExpressedConsent = "https://w3id.org/dpv#ExpressedConsent"  # Expressed Consent
FailSafeProtocols = "https://w3id.org/dpv#FailSafeProtocols"  # Fail-Safe Protocols
FederatedLocations = "https://w3id.org/dpv#FederatedLocations"  # Federated Locations
FeeNotRequired = "https://w3id.org/dpv#FeeNotRequired"  # Fee Not Required
FeeRequired = "https://w3id.org/dpv#FeeRequired"  # Fee Required
FeeRequirement = "https://w3id.org/dpv#FeeRequirement"  # Fee Requirement
FileSystemSecurity = "https://w3id.org/dpv#FileSystemSecurity"  # File System Security
Filter = "https://w3id.org/dpv#Filter"
FireDepartment = "https://w3id.org/dpv#FireDepartment"  # Fire Department
FixedLocation = "https://w3id.org/dpv#FixedLocation"  # Fixed Location
FixedMultipleLocations = "https://w3id.org/dpv#FixedMultipleLocations"  # Fixed Multiple Locations
FixedOccurrencesDuration = "https://w3id.org/dpv#FixedOccurrencesDuration"  # Fixed Occurrences Duration
FixedSingularLocation = "https://w3id.org/dpv#FixedSingularLocation"  # Fixed Singular Location
Format = "https://w3id.org/dpv#Format"
ForProfitOrganisation = "https://w3id.org/dpv#ForProfitOrganisation"  # For-Profit Organisation
FraudPreventionAndDetection = "https://w3id.org/dpv#FraudPreventionAndDetection"  # Fraud Prevention and Detection
Frequency = "https://w3id.org/dpv#Frequency"
FRIA = "https://w3id.org/dpv#FRIA"  # Fundamental Rights Impact Assessment (FRIA)
FulfilmentOfContractualObligation = (
    "https://w3id.org/dpv#FulfilmentOfContractualObligation"  # Fulfilment of Contractual Obligation
)
FulfilmentOfObligation = "https://w3id.org/dpv#FulfilmentOfObligation"  # Fulfilment of Obligation
FullAutomation = "https://w3id.org/dpv#FullAutomation"  # Full Automation
FullyRandomisedPseudonymisation = (
    "https://w3id.org/dpv#FullyRandomisedPseudonymisation"  # Fully Randomised Pseudonymisation
)
G2BContract = "https://w3id.org/dpv#G2BContract"  # Government-to-Business Contract
G2CContract = "https://w3id.org/dpv#G2CContract"  # Government-to-Consumer Contract
G2GContract = "https://w3id.org/dpv#G2GContract"  # Government-to-Government Contract
Generate = "https://w3id.org/dpv#Generate"
GeneratedData = "https://w3id.org/dpv#GeneratedData"  # Generated Data
GeneratedPersonalData = "https://w3id.org/dpv#GeneratedPersonalData"  # Generated Personal Data
GeographicCoverage = "https://w3id.org/dpv#GeographicCoverage"  # Geographic Coverage
GlobalScale = "https://w3id.org/dpv#GlobalScale"  # Global Scale
GovernanceProcedures = "https://w3id.org/dpv#GovernanceProcedures"  # Governance Procedures
GovernmentalOrganisation = "https://w3id.org/dpv#GovernmentalOrganisation"  # Governmental Organisation
GraphicalNotice = "https://w3id.org/dpv#GraphicalNotice"  # Graphical Notice
GuardianOfDataSubject = "https://w3id.org/dpv#GuardianOfDataSubject"  # Guardian(s) of Data Subject
GuardianOfHuman = "https://w3id.org/dpv#GuardianOfHuman"  # Guardian(s) of Human
Guideline = "https://w3id.org/dpv#Guideline"
GuidelinesPrinciple = "https://w3id.org/dpv#GuidelinesPrinciple"  # Guidelines Principle
HardwareSecurityProtocols = "https://w3id.org/dpv#HardwareSecurityProtocols"  # Hardware Security Protocols
hasActiveEntity = "https://w3id.org/dpv#hasActiveEntity"  # has active entity
hasActivityStatus = "https://w3id.org/dpv#hasActivityStatus"  # has activity status
hasAddress = "https://w3id.org/dpv#hasAddress"  # has address
hasAlgorithmicLogic = "https://w3id.org/dpv#hasAlgorithmicLogic"  # has algorithmic logic
hasApplicability = "https://w3id.org/dpv#hasApplicability"  # has applicability
hasApplicableLaw = "https://w3id.org/dpv#hasApplicableLaw"  # has applicable law
hasAssessment = "https://w3id.org/dpv#hasAssessment"  # has assessment
hasAuditStatus = "https://w3id.org/dpv#hasAuditStatus"  # has audit status
hasAuthority = "https://w3id.org/dpv#hasAuthority"  # has authority
hasAutomationLevel = "https://w3id.org/dpv#hasAutomationLevel"  # has automation level
hasComplianceStatus = "https://w3id.org/dpv#hasComplianceStatus"  # has compliance status
hasConformanceStatus = "https://w3id.org/dpv#hasConformanceStatus"  # has conformance status
hasConsentControl = "https://w3id.org/dpv#hasConsentControl"  # has consent control
hasConsentStatus = "https://w3id.org/dpv#hasConsentStatus"  # has consent status
hasConsequence = "https://w3id.org/dpv#hasConsequence"  # has consequence
hasConsequenceOn = "https://w3id.org/dpv#hasConsequenceOn"  # has consequence on
hasContact = "https://w3id.org/dpv#hasContact"  # has contact
hasContext = "https://w3id.org/dpv#hasContext"  # has context
hasContractControl = "https://w3id.org/dpv#hasContractControl"  # has contract control
hasContractStatus = "https://w3id.org/dpv#hasContractStatus"  # has contract status
hasContractualClause = "https://w3id.org/dpv#hasContractualClause"  # has contractual clause
hasContractualFulfilmentStatus = (
    "https://w3id.org/dpv#hasContractualFulfilmentStatus"  # has contractual fulfilment status
)
hasCountry = "https://w3id.org/dpv#hasCountry"  # has country
hasData = "https://w3id.org/dpv#hasData"  # has data
hasDataController = "https://w3id.org/dpv#hasDataController"  # has data controller
hasDataExporter = "https://w3id.org/dpv#hasDataExporter"  # has data exporter
hasDataImporter = "https://w3id.org/dpv#hasDataImporter"  # has data importer
hasDataProcessor = "https://w3id.org/dpv#hasDataProcessor"  # has data processor
hasDataProtectionOfficer = "https://w3id.org/dpv#hasDataProtectionOfficer"  # has data protection officer
hasDataSource = "https://w3id.org/dpv#hasDataSource"  # has data source
hasDataSubject = "https://w3id.org/dpv#hasDataSubject"  # has data subject
hasDataSubjectScale = "https://w3id.org/dpv#hasDataSubjectScale"  # has data subject scale
hasDataVolume = "https://w3id.org/dpv#hasDataVolume"  # has data volume
hasDeterrence = "https://w3id.org/dpv#hasDeterrence"  # has deterrence
hasDuration = "https://w3id.org/dpv#hasDuration"  # has duration
hasEntity = "https://w3id.org/dpv#hasEntity"  # has entity
hasEntityControl = "https://w3id.org/dpv#hasEntityControl"  # has entity control
hasEntityInvolvement = "https://w3id.org/dpv#hasEntityInvolvement"  # has entity involvement
hasExpectation = "https://w3id.org/dpv#hasExpectation"  # has expectation
hasFee = "https://w3id.org/dpv#hasFee"  # has fee
hasFrequency = "https://w3id.org/dpv#hasFrequency"  # has frequency
hasFulfilmentStatus = "https://w3id.org/dpv#hasFulfilmentStatus"  # has fulfilment status
hasGeographicCoverage = "https://w3id.org/dpv#hasGeographicCoverage"  # has geographic coverage
HashFunctions = "https://w3id.org/dpv#HashFunctions"  # Hash Functions
HashMessageAuthenticationCode = (
    "https://w3id.org/dpv#HashMessageAuthenticationCode"  # Hash-based Message Authentication Code (HMAC)
)
hasHumanInvolvement = "https://w3id.org/dpv#hasHumanInvolvement"  # has human involvement
hasHumanSubject = "https://w3id.org/dpv#hasHumanSubject"  # has human subject
hasIdentifier = "https://w3id.org/dpv#hasIdentifier"  # has identifier
hasImpact = "https://w3id.org/dpv#hasImpact"  # has impact
hasImpactAssessment = "https://w3id.org/dpv#hasImpactAssessment"  # has impact assessment
hasImpactOn = "https://w3id.org/dpv#hasImpactOn"  # has impact on
hasImportance = "https://w3id.org/dpv#hasImportance"  # has importance
hasIndicationMethod = "https://w3id.org/dpv#hasIndicationMethod"  # has indication method
hasInformedStatus = "https://w3id.org/dpv#hasInformedStatus"  # has informed status
hasIntention = "https://w3id.org/dpv#hasIntention"  # has intention
hasInverseJurisdiction = "https://w3id.org/dpv#hasInverseJurisdiction"  # has inverse jurisdiction
hasInvolvement = "https://w3id.org/dpv#hasInvolvement"  # has involvement
hasJointDataControllers = "https://w3id.org/dpv#hasJointDataControllers"  # has joint data controllers
hasJurisdiction = "https://w3id.org/dpv#hasJurisdiction"  # has jurisdiction
hasJustification = "https://w3id.org/dpv#hasJustification"  # has justification
hasLawfulness = "https://w3id.org/dpv#hasLawfulness"  # has lawfulness
hasLegalBasis = "https://w3id.org/dpv#hasLegalBasis"  # has legal basis
hasLegalMeasure = "https://w3id.org/dpv#hasLegalMeasure"  # has legal measure
hasLikelihood = "https://w3id.org/dpv#hasLikelihood"  # has likelihood
hasLocation = "https://w3id.org/dpv#hasLocation"  # has location
hasName = "https://w3id.org/dpv#hasName"  # has name
hasNecessity = "https://w3id.org/dpv#hasNecessity"  # has necessity
hasNonInvolvedEntity = "https://w3id.org/dpv#hasNonInvolvedEntity"  # has non-involved entity
hasNonPersonalDataProcess = "https://w3id.org/dpv#hasNonPersonalDataProcess"  # has non-personal data process
hasNotice = "https://w3id.org/dpv#hasNotice"  # has notice
hasNoticeIcon = "https://w3id.org/dpv#hasNoticeIcon"  # has notice icon
hasNoticeLayer = "https://w3id.org/dpv#hasNoticeLayer"  # has notice layer
hasNoticeStatus = "https://w3id.org/dpv#hasNoticeStatus"  # has notice status
hasNotificationStatus = "https://w3id.org/dpv#hasNotificationStatus"  # has notification status
hasObligation = "https://w3id.org/dpv#hasObligation"  # has obligation
hasOrganisationalMeasure = "https://w3id.org/dpv#hasOrganisationalMeasure"  # has organisational measure
hasOrganisationalUnit = "https://w3id.org/dpv#hasOrganisationalUnit"  # has organisational unit
hasOutcome = "https://w3id.org/dpv#hasOutcome"  # has outcome
hasParty = "https://w3id.org/dpv#hasParty"  # has party
hasPassiveEntity = "https://w3id.org/dpv#hasPassiveEntity"  # has passive entity
hasPermission = "https://w3id.org/dpv#hasPermission"  # has permission
hasPersonalData = "https://w3id.org/dpv#hasPersonalData"  # has personal data
hasPersonalDataHandling = "https://w3id.org/dpv#hasPersonalDataHandling"  # has personal data handling
hasPersonalDataProcess = "https://w3id.org/dpv#hasPersonalDataProcess"  # has personal data process
hasPhysicalMeasure = "https://w3id.org/dpv#hasPhysicalMeasure"  # has physical measure
hasPolicy = "https://w3id.org/dpv#hasPolicy"  # has policy
hasProcess = "https://w3id.org/dpv#hasProcess"  # has process
hasProcessing = "https://w3id.org/dpv#hasProcessing"  # has processing
hasProcessingCondition = "https://w3id.org/dpv#hasProcessingCondition"  # has processing condition
hasProcessingScale = "https://w3id.org/dpv#hasProcessingScale"  # has processing scale
hasProhibition = "https://w3id.org/dpv#hasProhibition"  # has prohibition
hasPurpose = "https://w3id.org/dpv#hasPurpose"  # has purpose
hasRecipient = "https://w3id.org/dpv#hasRecipient"  # has recipient
hasRecipientDataController = "https://w3id.org/dpv#hasRecipientDataController"  # has recipient data controller
hasRecipientThirdParty = "https://w3id.org/dpv#hasRecipientThirdParty"  # has recipient third party
hasRecommendation = "https://w3id.org/dpv#hasRecommendation"  # has recommendation
hasRecordOfActivity = "https://w3id.org/dpv#hasRecordOfActivity"  # has record of activity
hasRelationWithDataSubject = "https://w3id.org/dpv#hasRelationWithDataSubject"  # has relation with data subject
hasRepresentative = "https://w3id.org/dpv#hasRepresentative"  # has representative
hasRequestStatus = "https://w3id.org/dpv#hasRequestStatus"  # has request status
hasResidualRisk = "https://w3id.org/dpv#hasResidualRisk"  # has residual risk
hasResponsibleEntity = "https://w3id.org/dpv#hasResponsibleEntity"  # has responsible entity
hasReuseCompatibility = "https://w3id.org/dpv#hasReuseCompatibility"  # has reuse compatibility
hasRight = "https://w3id.org/dpv#hasRight"  # has right
hasRisk = "https://w3id.org/dpv#hasRisk"  # has risk
hasRiskAssessment = "https://w3id.org/dpv#hasRiskAssessment"  # has risk assessment
hasRiskLevel = "https://w3id.org/dpv#hasRiskLevel"  # has risk level
hasRule = "https://w3id.org/dpv#hasRule"  # has rule
hasScale = "https://w3id.org/dpv#hasScale"  # has scale
hasScope = "https://w3id.org/dpv#hasScope"  # has scope
hasSector = "https://w3id.org/dpv#hasSector"  # has sector
hasSensitivityLevel = "https://w3id.org/dpv#hasSensitivityLevel"  # has sensitivity level
hasService = "https://w3id.org/dpv#hasService"  # has service
hasServiceConsumer = "https://w3id.org/dpv#hasServiceConsumer"  # has service consumer
hasServiceProvider = "https://w3id.org/dpv#hasServiceProvider"  # has service provider
hasSeverity = "https://w3id.org/dpv#hasSeverity"  # has severity
hasStatus = "https://w3id.org/dpv#hasStatus"  # has status
hasStorageCondition = "https://w3id.org/dpv#hasStorageCondition"  # has storage condition
hasSubsidiary = "https://w3id.org/dpv#hasSubsidiary"  # has subsidiary
hasTechnicalMeasure = "https://w3id.org/dpv#hasTechnicalMeasure"  # has technical measure
hasTechnicalOrganisationalMeasure = (
    "https://w3id.org/dpv#hasTechnicalOrganisationalMeasure"  # has technical and organisational measure
)
hasThirdCountry = "https://w3id.org/dpv#hasThirdCountry"  # has third country
hasThirdParty = "https://w3id.org/dpv#hasThirdParty"  # has third party
hasUncategorisedData = "https://w3id.org/dpv#hasUncategorisedData"  # has uncategorised data
hasUnstructuredData = "https://w3id.org/dpv#hasUnstructuredData"  # has unstructured data
HealthcareOrganisation = "https://w3id.org/dpv#HealthcareOrganisation"  # Healthcare Organisation
HighAutomation = "https://w3id.org/dpv#HighAutomation"  # High Automation
HomomorphicEncryption = "https://w3id.org/dpv#HomomorphicEncryption"  # Homomorphic Encryption
Hospital = "https://w3id.org/dpv#Hospital"
HugeDataVolume = "https://w3id.org/dpv#HugeDataVolume"  # Huge Data Volume
HugeScaleOfDataSubjects = "https://w3id.org/dpv#HugeScaleOfDataSubjects"  # Huge Scale Of Data Subjects
HumanInvolved = "https://w3id.org/dpv#HumanInvolved"  # Human involved
HumanInvolvement = "https://w3id.org/dpv#HumanInvolvement"  # Human Involvement
HumanInvolvementForControl = "https://w3id.org/dpv#HumanInvolvementForControl"  # Human Involvement for control
HumanInvolvementForDecision = "https://w3id.org/dpv#HumanInvolvementForDecision"  # Human Involvement for decision
HumanInvolvementForInput = "https://w3id.org/dpv#HumanInvolvementForInput"  # Human Involvement for Input
HumanInvolvementForIntervention = (
    "https://w3id.org/dpv#HumanInvolvementForIntervention"  # Human Involvement for intervention
)
HumanInvolvementForOversight = "https://w3id.org/dpv#HumanInvolvementForOversight"  # Human Involvement for Oversight
HumanInvolvementForVerification = (
    "https://w3id.org/dpv#HumanInvolvementForVerification"  # Human Involvement for Verification
)
HumanNotInvolved = "https://w3id.org/dpv#HumanNotInvolved"  # Human not involved
HumanOversight = "https://w3id.org/dpv#HumanOversight"  # Human Oversight
HumanResourceManagement = "https://w3id.org/dpv#HumanResourceManagement"  # Human Resource Management
HumanSubject = "https://w3id.org/dpv#HumanSubject"  # Human Subject
HybridPublicPrivateSpace = "https://w3id.org/dpv#HybridPublicPrivateSpace"  # Hybrid Public Private Space
IdentifyingPersonalData = "https://w3id.org/dpv#IdentifyingPersonalData"  # Identifying Personal Data
IdentityAuthentication = "https://w3id.org/dpv#IdentityAuthentication"  # Identity Authentication
IdentityManagementMethod = "https://w3id.org/dpv#IdentityManagementMethod"  # Identity Management Method
IdentityVerification = "https://w3id.org/dpv#IdentityVerification"  # Identity Verification
Immigrant = "https://w3id.org/dpv#Immigrant"
Impact = "https://w3id.org/dpv#Impact"
ImpactAssessment = "https://w3id.org/dpv#ImpactAssessment"  # Impact Assessment
ImpliedConsent = "https://w3id.org/dpv#ImpliedConsent"  # Implied Consent
Importance = "https://w3id.org/dpv#Importance"
ImproveExistingProductsAndServices = (
    "https://w3id.org/dpv#ImproveExistingProductsAndServices"  # Improve Existing Products and Services
)
ImproveHealthcare = "https://w3id.org/dpv#ImproveHealthcare"  # Improve Healthcare
ImproveInternalCRMProcesses = "https://w3id.org/dpv#ImproveInternalCRMProcesses"  # Improve Internal CRM Processes
ImprovePublicServices = "https://w3id.org/dpv#ImprovePublicServices"  # Improve Public Services
ImproveTransportMobility = "https://w3id.org/dpv#ImproveTransportMobility"  # Improve Transport and Mobility
IncidentManagementProcedures = "https://w3id.org/dpv#IncidentManagementProcedures"  # Incident Management Procedures
IncidentReportingCommunication = (
    "https://w3id.org/dpv#IncidentReportingCommunication"  # Incident Reporting Communication
)
IncorrectData = "https://w3id.org/dpv#IncorrectData"  # Incorrect Data
IncreaseServiceRobustness = "https://w3id.org/dpv#IncreaseServiceRobustness"  # Increase Service Robustness
IndeterminateDuration = "https://w3id.org/dpv#IndeterminateDuration"  # Indeterminate Duration
IndustryConsortium = "https://w3id.org/dpv#IndustryConsortium"  # Industry Consortium
Infer = "https://w3id.org/dpv#Infer"
InferredData = "https://w3id.org/dpv#InferredData"  # Inferred Data
InferredPersonalData = "https://w3id.org/dpv#InferredPersonalData"  # Inferred Personal Data
InformationAudit = "https://w3id.org/dpv#InformationAudit"  # Information Audit
InformationFlowControl = "https://w3id.org/dpv#InformationFlowControl"  # Information Flow Control
InformationSecurityPolicy = "https://w3id.org/dpv#InformationSecurityPolicy"  # Information Security Policy
InformedConsent = "https://w3id.org/dpv#InformedConsent"  # Informed Consent
InnovativeUseOfExistingTechnology = (
    "https://w3id.org/dpv#InnovativeUseOfExistingTechnology"  # Innovative Use of Existing Technologies
)
InnovativeUseOfNewTechnologies = (
    "https://w3id.org/dpv#InnovativeUseOfNewTechnologies"  # Innovative Use of New Technologies
)
InnovativeUseOfTechnology = "https://w3id.org/dpv#InnovativeUseOfTechnology"  # Innovative use of Technology
IntellectualPropertyData = "https://w3id.org/dpv#IntellectualPropertyData"  # Intellectual Property Data
Intended = "https://w3id.org/dpv#Intended"
IntentionStatus = "https://w3id.org/dpv#IntentionStatus"  # Intention Status
InternalResourceOptimisation = "https://w3id.org/dpv#InternalResourceOptimisation"  # Internal Resource Optimisation
InternationalOrganisation = "https://w3id.org/dpv#InternationalOrganisation"  # International Organisation
IntrusionDetectionSystem = "https://w3id.org/dpv#IntrusionDetectionSystem"  # Intrusion Detection System
InverseJurisdiction = "https://w3id.org/dpv#InverseJurisdiction"  # Inverse Jurisdiction
InvolvementStatus = "https://w3id.org/dpv#InvolvementStatus"  # Involvement Status
IPRManagement = "https://w3id.org/dpv#IPRManagement"  # Intellectual Property Rights Management
isAfter = "https://w3id.org/dpv#isAfter"  # is after
isApplicableFor = "https://w3id.org/dpv#isApplicableFor"  # is applicable for
isAuthorityFor = "https://w3id.org/dpv#isAuthorityFor"  # is authority for
isBefore = "https://w3id.org/dpv#isBefore"  # is before
isDeterminedByEntity = "https://w3id.org/dpv#isDeterminedByEntity"  # is determined by entity
isDuring = "https://w3id.org/dpv#isDuring"  # is during
isExercisedAt = "https://w3id.org/dpv#isExercisedAt"  # is exercised at
isImplementedByEntity = "https://w3id.org/dpv#isImplementedByEntity"  # is implemented by entity
isImplementedUsingTechnology = "https://w3id.org/dpv#isImplementedUsingTechnology"  # is implemented using technology
isIndicatedAtTime = "https://w3id.org/dpv#isIndicatedAtTime"  # is indicated at time
isIndicatedBy = "https://w3id.org/dpv#isIndicatedBy"  # is indicated by
isMitigatedByMeasure = "https://w3id.org/dpv#isMitigatedByMeasure"  # is mitigated by measure
isNotApplicableFor = "https://w3id.org/dpv#isNotApplicableFor"  # is not applicable for
isOrganisationalUnitOf = "https://w3id.org/dpv#isOrganisationalUnitOf"  # is organisational unit of
isOutsideOfLocation = "https://w3id.org/dpv#isOutsideOfLocation"  # is outside of location
isPolicyFor = "https://w3id.org/dpv#isPolicyFor"  # is policy for
isRepresentativeFor = "https://w3id.org/dpv#isRepresentativeFor"  # is representative for
isResidualRiskOf = "https://w3id.org/dpv#isResidualRiskOf"  # is residual risk of
isSubsidiaryOf = "https://w3id.org/dpv#isSubsidiaryOf"  # is subsidiary of
JITNotice = "https://w3id.org/dpv#JITNotice"  # Just-in-time Notice
JobApplicant = "https://w3id.org/dpv#JobApplicant"  # Job Applicant
JointDataControllers = "https://w3id.org/dpv#JointDataControllers"  # Joint Data Controllers
JointDataControllersAgreement = "https://w3id.org/dpv#JointDataControllersAgreement"  # Joint Data Controllers Agreement
JudicialOrganisation = "https://w3id.org/dpv#JudicialOrganisation"  # Judicial Organisation
Jurisdiction = "https://w3id.org/dpv#Jurisdiction"
Justification = "https://w3id.org/dpv#Justification"
LargeDataVolume = "https://w3id.org/dpv#LargeDataVolume"  # Large Data Volume
LargeScaleOfDataSubjects = "https://w3id.org/dpv#LargeScaleOfDataSubjects"  # Large Scale Of Data Subjects
LargeScaleProcessing = "https://w3id.org/dpv#LargeScaleProcessing"  # Large Scale Processing
Law = "https://w3id.org/dpv#Law"
LawEnforcementOrganisation = "https://w3id.org/dpv#LawEnforcementOrganisation"  # Law Enforcement Organisation
Lawful = "https://w3id.org/dpv#Lawful"
Lawfulness = "https://w3id.org/dpv#Lawfulness"
LawfulnessUnknown = "https://w3id.org/dpv#LawfulnessUnknown"  # Lawfulness Unknown
LayeredNotice = "https://w3id.org/dpv#LayeredNotice"  # Layered Notice
LegalAgent = "https://w3id.org/dpv#LegalAgent"  # Legal Agent
LegalAgreement = "https://w3id.org/dpv#LegalAgreement"  # Legal Agreement
LegalBasis = "https://w3id.org/dpv#LegalBasis"  # Legal Basis
LegalCompliance = "https://w3id.org/dpv#LegalCompliance"  # Legal Compliance
LegalComplianceAssessment = "https://w3id.org/dpv#LegalComplianceAssessment"  # Legal Compliance Assessment
LegalComplianceAudit = "https://w3id.org/dpv#LegalComplianceAudit"  # Legal Compliance Audit
LegalEntity = "https://w3id.org/dpv#LegalEntity"  # Legal Entity
LegalMeasure = "https://w3id.org/dpv#LegalMeasure"  # Legal Measure
LegalObligation = "https://w3id.org/dpv#LegalObligation"  # Legal Obligation
LegalObligationCompleted = "https://w3id.org/dpv#LegalObligationCompleted"  # Legal ObligationCompleted
LegalObligationOngoing = "https://w3id.org/dpv#LegalObligationOngoing"  # Legal ObligationOngoing
LegalObligationPending = "https://w3id.org/dpv#LegalObligationPending"  # Legal ObligationPending
LegalObligationStatus = "https://w3id.org/dpv#LegalObligationStatus"  # Legal ObligationStatus
LegitimateInterest = "https://w3id.org/dpv#LegitimateInterest"  # Legitimate Interest
LegitimateInterestAssessment = "https://w3id.org/dpv#LegitimateInterestAssessment"  # Legitimate Interest Assessment
LegitimateInterestInformed = "https://w3id.org/dpv#LegitimateInterestInformed"  # Legitimate InterestInformed
LegitimateInterestNotObjected = "https://w3id.org/dpv#LegitimateInterestNotObjected"  # Legitimate InterestNotObjected
LegitimateInterestObjected = "https://w3id.org/dpv#LegitimateInterestObjected"  # Legitimate InterestObjected
LegitimateInterestOfController = (
    "https://w3id.org/dpv#LegitimateInterestOfController"  # Legitimate Interest of Controller
)
LegitimateInterestOfDataSubject = (
    "https://w3id.org/dpv#LegitimateInterestOfDataSubject"  # Legitimate Interest of Data Subject
)
LegitimateInterestOfThirdParty = (
    "https://w3id.org/dpv#LegitimateInterestOfThirdParty"  # Legitimate Interest of Third Party
)
LegitimateInterestStatus = "https://w3id.org/dpv#LegitimateInterestStatus"  # Legitimate InterestStatus
LegitimateInterestUninformed = "https://w3id.org/dpv#LegitimateInterestUninformed"  # Legitimate InterestUninformed
LicenseAgreement = "https://w3id.org/dpv#LicenseAgreement"  # License Agreement
Likelihood = "https://w3id.org/dpv#Likelihood"
LocalEnvironmentScale = "https://w3id.org/dpv#LocalEnvironmentScale"  # Local Environment Scale
LocalityScale = "https://w3id.org/dpv#LocalityScale"  # Locality Scale
LocalLocation = "https://w3id.org/dpv#LocalLocation"  # Local Location
Location = "https://w3id.org/dpv#Location"
LocationFixture = "https://w3id.org/dpv#LocationFixture"  # Location Fixture
LocationLocality = "https://w3id.org/dpv#LocationLocality"  # Location Locality
LoggingPolicy = "https://w3id.org/dpv#LoggingPolicy"  # Logging Policy
MaintainFraudDatabase = "https://w3id.org/dpv#MaintainFraudDatabase"  # Maintain Fraud Database
MakeAvailable = "https://w3id.org/dpv#MakeAvailable"  # Make Available
ManageConsent = "https://w3id.org/dpv#ManageConsent"  # Manage Consent
ManagementStandard = "https://w3id.org/dpv#ManagementStandard"  # Management Standard
Marketing = "https://w3id.org/dpv#Marketing"
Match = "https://w3id.org/dpv#Match"
MediumDataVolume = "https://w3id.org/dpv#MediumDataVolume"  # Medium Data Volume
MediumScaleOfDataSubjects = "https://w3id.org/dpv#MediumScaleOfDataSubjects"  # Medium Scale Of Data Subjects
MediumScaleProcessing = "https://w3id.org/dpv#MediumScaleProcessing"  # Medium Scale Processing
Member = "https://w3id.org/dpv#Member"
MemberPartnerManagement = "https://w3id.org/dpv#MemberPartnerManagement"  # Members and Partners Management
MentallyVulnerableDataSubject = "https://w3id.org/dpv#MentallyVulnerableDataSubject"  # Mentally Vulnerable Data Subject
MentallyVulnerableHuman = "https://w3id.org/dpv#MentallyVulnerableHuman"  # Mentally Vulnerable Human
MessageAuthenticationCodes = "https://w3id.org/dpv#MessageAuthenticationCodes"  # Message Authentication Codes (MAC)
MetadataManagement = "https://w3id.org/dpv#MetadataManagement"  # Metadata Management
MisusePreventionAndDetection = "https://w3id.org/dpv#MisusePreventionAndDetection"  # Misuse, Prevention and Detection
mitigatesRisk = "https://w3id.org/dpv#mitigatesRisk"  # mitigates risk
MobilePlatformSecurity = "https://w3id.org/dpv#MobilePlatformSecurity"  # Mobile Platform Security
Modify = "https://w3id.org/dpv#Modify"
Monitor = "https://w3id.org/dpv#Monitor"
MonitoringPolicy = "https://w3id.org/dpv#MonitoringPolicy"  # Monitoring Policy
MonotonicCounterPseudonymisation = (
    "https://w3id.org/dpv#MonotonicCounterPseudonymisation"  # Monotonic Counter Pseudonymisation
)
Move = "https://w3id.org/dpv#Move"
MultiFactorAuthentication = "https://w3id.org/dpv#MultiFactorAuthentication"  # Multi-Factor Authentication (MFA)
MultiNationalScale = "https://w3id.org/dpv#MultiNationalScale"  # Multi National Scale
NationalAuthority = "https://w3id.org/dpv#NationalAuthority"  # National Authority
NationalScale = "https://w3id.org/dpv#NationalScale"  # National Scale
NaturalPerson = "https://w3id.org/dpv#NaturalPerson"  # Natural Person
NDA = "https://w3id.org/dpv#NDA"  # Non-Disclosure Agreement (NDA)
NearlyGlobalScale = "https://w3id.org/dpv#NearlyGlobalScale"  # Nearly Global Scale
Necessity = "https://w3id.org/dpv#Necessity"
NegotiateContract = "https://w3id.org/dpv#NegotiateContract"  # Negotiate Contract
NegotiatedContract = "https://w3id.org/dpv#NegotiatedContract"  # Negotiated Contract
NetworkProxyRouting = "https://w3id.org/dpv#NetworkProxyRouting"  # Network Proxy Routing
NetworkSecurityProtocols = "https://w3id.org/dpv#NetworkSecurityProtocols"  # Network Security Protocols
NonCitizen = "https://w3id.org/dpv#NonCitizen"  # Non-Citizen
NonCommercialPurpose = "https://w3id.org/dpv#NonCommercialPurpose"  # Non-commercial Purpose
NonCommercialResearch = "https://w3id.org/dpv#NonCommercialResearch"  # Non-Commercial Research
NonCompliant = "https://w3id.org/dpv#NonCompliant"  # Non Compliant
NonConformant = "https://w3id.org/dpv#NonConformant"
NonGovernmentalOrganisation = "https://w3id.org/dpv#NonGovernmentalOrganisation"  # Non-Governmental Organisation
NonPersonalData = "https://w3id.org/dpv#NonPersonalData"  # Non-Personal Data
NonPersonalDataProcess = "https://w3id.org/dpv#NonPersonalDataProcess"  # Non-Personal Data Process
NonProfitOrganisation = "https://w3id.org/dpv#NonProfitOrganisation"  # Non-Profit Organisation
NonPublicDataSource = "https://w3id.org/dpv#NonPublicDataSource"  # Non-Public Data Source
NotApplicable = "https://w3id.org/dpv#NotApplicable"  # Not Applicable
NotAutomated = "https://w3id.org/dpv#NotAutomated"  # Not Automated
NotAvailable = "https://w3id.org/dpv#NotAvailable"  # Not Available
Notice = "https://w3id.org/dpv#Notice"
NoticeCommunicated = "https://w3id.org/dpv#NoticeCommunicated"  # Notice Communicated
NoticeGenerated = "https://w3id.org/dpv#NoticeGenerated"  # Notice Generated
NoticeIcon = "https://w3id.org/dpv#NoticeIcon"  # Notice Icon
NoticeLatest = "https://w3id.org/dpv#NoticeLatest"  # Notice Latest
NoticeLayer = "https://w3id.org/dpv#NoticeLayer"  # Notice Layer
NoticeStale = "https://w3id.org/dpv#NoticeStale"  # Notice Stale
NoticeStatus = "https://w3id.org/dpv#NoticeStatus"  # Notice Status
NoticeUnused = "https://w3id.org/dpv#NoticeUnused"  # Notice Unused
NoticeUpdated = "https://w3id.org/dpv#NoticeUpdated"  # Notice Updated
NoticeUsed = "https://w3id.org/dpv#NoticeUsed"  # Notice Used
Notification = "https://w3id.org/dpv#Notification"
NotificationCompleted = "https://w3id.org/dpv#NotificationCompleted"  # Notification Completed
NotificationFailed = "https://w3id.org/dpv#NotificationFailed"  # Notification Failed
NotificationNotNeeded = "https://w3id.org/dpv#NotificationNotNeeded"  # Notification Not Needed
NotificationOngoing = "https://w3id.org/dpv#NotificationOngoing"  # Notification Ongoing
NotificationPlanned = "https://w3id.org/dpv#NotificationPlanned"  # Notification Planned
NotificationStatus = "https://w3id.org/dpv#NotificationStatus"  # Notification Status
NotInvolved = "https://w3id.org/dpv#NotInvolved"  # Not Involved
NotRequired = "https://w3id.org/dpv#NotRequired"  # Not Required
ObjectingToProcess = "https://w3id.org/dpv#ObjectingToProcess"  # Objecting to Process
Obligation = "https://w3id.org/dpv#Obligation"
ObligationFulfilled = "https://w3id.org/dpv#ObligationFulfilled"  # Obligation Fulfilled
ObligationUnfulfilled = "https://w3id.org/dpv#ObligationUnfulfilled"  # Obligation Unfulfilled
ObligationViolated = "https://w3id.org/dpv#ObligationViolated"  # Obligation Violated
Observe = "https://w3id.org/dpv#Observe"
ObservedData = "https://w3id.org/dpv#ObservedData"  # Observed Data
ObservedPersonalData = "https://w3id.org/dpv#ObservedPersonalData"  # Observed Personal Data
Obtain = "https://w3id.org/dpv#Obtain"
ObtainConsent = "https://w3id.org/dpv#ObtainConsent"  # Obtain Consent
OfferContract = "https://w3id.org/dpv#OfferContract"  # Offer Contract
OfficialAuthorityExerciseCompleted = (
    "https://w3id.org/dpv#OfficialAuthorityExerciseCompleted"  # Official Authority Exercise Completed
)
OfficialAuthorityExerciseOngoing = (
    "https://w3id.org/dpv#OfficialAuthorityExerciseOngoing"  # Official Authority Exercise Ongoing
)
OfficialAuthorityExercisePending = (
    "https://w3id.org/dpv#OfficialAuthorityExercisePending"  # Official Authority Exercise Pending
)
OfficialAuthorityExerciseStatus = (
    "https://w3id.org/dpv#OfficialAuthorityExerciseStatus"  # Official Authority Exercise Status
)
OfficialAuthorityOfController = "https://w3id.org/dpv#OfficialAuthorityOfController"  # Official Authority of Controller
OftenFrequency = "https://w3id.org/dpv#OftenFrequency"  # Often Frequency
OperatingSystemSecurity = "https://w3id.org/dpv#OperatingSystemSecurity"  # Operating System Security
OptimisationForConsumer = "https://w3id.org/dpv#OptimisationForConsumer"  # Optimisation for Consumer
OptimisationForController = "https://w3id.org/dpv#OptimisationForController"  # Optimisation for Controller
OptimiseUserInterface = "https://w3id.org/dpv#OptimiseUserInterface"  # Optimise User Interface
OptingInToProcess = "https://w3id.org/dpv#OptingInToProcess"  # Opting in to Process
OptingOutFromProcess = "https://w3id.org/dpv#OptingOutFromProcess"  # Opting out of Process
Optional = "https://w3id.org/dpv#Optional"
OralNotice = "https://w3id.org/dpv#OralNotice"  # Oral Notice
Organisation = "https://w3id.org/dpv#Organisation"
OrganisationalMeasure = "https://w3id.org/dpv#OrganisationalMeasure"  # Organisational Measure
OrganisationalUnit = "https://w3id.org/dpv#OrganisationalUnit"  # Organisational Unit
OrganisationComplianceManagement = (
    "https://w3id.org/dpv#OrganisationComplianceManagement"  # Organisation Compliance Management
)
OrganisationGovernance = "https://w3id.org/dpv#OrganisationGovernance"  # Organisation Governance
OrganisationRiskManagement = "https://w3id.org/dpv#OrganisationRiskManagement"  # Organisation Risk Management
Organise = "https://w3id.org/dpv#Organise"
ParentLegalEntity = "https://w3id.org/dpv#ParentLegalEntity"  # Parent Legal Entity
ParentOfDataSubject = "https://w3id.org/dpv#ParentOfDataSubject"  # Parent(s) of Data Subject
ParentOfHuman = "https://w3id.org/dpv#ParentOfHuman"  # Parent of Human
PartialAutomation = "https://w3id.org/dpv#PartialAutomation"  # Partial Automation
PartiallyCompliant = "https://w3id.org/dpv#PartiallyCompliant"  # Partially Compliant
Participant = "https://w3id.org/dpv#Participant"
PassivelyInvolved = "https://w3id.org/dpv#PassivelyInvolved"  # Passively Involved
PassiveRight = "https://w3id.org/dpv#PassiveRight"  # Passive Right
PasswordAuthentication = "https://w3id.org/dpv#PasswordAuthentication"  # Password Authentication
Patient = "https://w3id.org/dpv#Patient"
PaymentManagement = "https://w3id.org/dpv#PaymentManagement"  # Payment Management
PenetrationTestingMethods = "https://w3id.org/dpv#PenetrationTestingMethods"  # Penetration Testing Methods
Permission = "https://w3id.org/dpv#Permission"
PermissionManagement = "https://w3id.org/dpv#PermissionManagement"  # Permission Management
PermissionNotUtilised = "https://w3id.org/dpv#PermissionNotUtilised"  # Permission Not Utilised
PermissionUtilised = "https://w3id.org/dpv#PermissionUtilised"  # Permission Utilised
PersonalData = "https://w3id.org/dpv#PersonalData"  # Personal Data
PersonalDataAudit = "https://w3id.org/dpv#PersonalDataAudit"  # Personal Data Audit
PersonalDataHandling = "https://w3id.org/dpv#PersonalDataHandling"  # Personal Data Handling
PersonalDataProcess = "https://w3id.org/dpv#PersonalDataProcess"  # Personal Data Process
Personalisation = "https://w3id.org/dpv#Personalisation"
PersonalisedAdvertising = "https://w3id.org/dpv#PersonalisedAdvertising"  # Personalised Advertising
PersonalisedBenefits = "https://w3id.org/dpv#PersonalisedBenefits"  # Personalised Benefits
PersonalSpace = "https://w3id.org/dpv#PersonalSpace"  # Personal Space
PersonnelBehaviourMonitoring = "https://w3id.org/dpv#PersonnelBehaviourMonitoring"  # Personnel Behaviour Monitoring
PersonnelHiring = "https://w3id.org/dpv#PersonnelHiring"  # Personnel Hiring
PersonnelManagement = "https://w3id.org/dpv#PersonnelManagement"  # Personnel Management
PersonnelMonitoring = "https://w3id.org/dpv#PersonnelMonitoring"  # Personnel Monitoring
PersonnelOffboarding = "https://w3id.org/dpv#PersonnelOffboarding"  # Personnel Offboarding
PersonnelOnboarding = "https://w3id.org/dpv#PersonnelOnboarding"  # Personnel Onboarding
PersonnelPayment = "https://w3id.org/dpv#PersonnelPayment"  # Personnel Payment
PersonnelPerformanceEvaluation = (
    "https://w3id.org/dpv#PersonnelPerformanceEvaluation"  # Personnel Performance Evaluation
)
PersonnelPerformanceManagement = (
    "https://w3id.org/dpv#PersonnelPerformanceManagement"  # Personnel Performance Management
)
PersonnelPerformanceMonitoring = (
    "https://w3id.org/dpv#PersonnelPerformanceMonitoring"  # Personnel Performance Monitoring
)
PersonnelPerformancePrediction = (
    "https://w3id.org/dpv#PersonnelPerformancePrediction"  # Personnel Performance Prediction
)
PersonnelPromotionManagement = "https://w3id.org/dpv#PersonnelPromotionManagement"  # Personnel Promotion Management
PersonnelTerminationManagement = (
    "https://w3id.org/dpv#PersonnelTerminationManagement"  # Personnel Termination Management
)
PersonnelWorkloadManagement = "https://w3id.org/dpv#PersonnelWorkloadManagement"  # Personnel Workload Management
PhysicalAccessControlMethod = "https://w3id.org/dpv#PhysicalAccessControlMethod"  # Physical Access Control Method
PhysicalAuthentication = "https://w3id.org/dpv#PhysicalAuthentication"  # Physical Authentication
PhysicalAuthorisation = "https://w3id.org/dpv#PhysicalAuthorisation"  # Physical Authorisation
PhysicalDeviceSecurity = "https://w3id.org/dpv#PhysicalDeviceSecurity"  # Physical Device Security
PhysicalInterceptionProtection = (
    "https://w3id.org/dpv#PhysicalInterceptionProtection"  # Physical Interception Protection
)
PhysicalInterruptionProtection = (
    "https://w3id.org/dpv#PhysicalInterruptionProtection"  # Physical Interruption Protection
)
PhysicalMeasure = "https://w3id.org/dpv#PhysicalMeasure"  # Physical Measure
PhysicalNetworkSecurity = "https://w3id.org/dpv#PhysicalNetworkSecurity"  # Physical Network Security
PhysicalSecureStorage = "https://w3id.org/dpv#PhysicalSecureStorage"  # Physical Secure Storage
PhysicalSupplySecurity = "https://w3id.org/dpv#PhysicalSupplySecurity"  # Physical Supply Security
PhysicalSurveillance = "https://w3id.org/dpv#PhysicalSurveillance"  # Physical Surveillance
PIA = "https://w3id.org/dpv#PIA"  # Privacy Impact Assessment (PIA)
Policy = "https://w3id.org/dpv#Policy"
PoliticalCampaign = "https://w3id.org/dpv#PoliticalCampaign"  # Political Campaign
PostedNotice = "https://w3id.org/dpv#PostedNotice"  # Posted Notice
PostQuantumCryptography = "https://w3id.org/dpv#PostQuantumCryptography"  # Post-Quantum Cryptography
PrimaryImportance = "https://w3id.org/dpv#PrimaryImportance"  # Primary Importance
PrimaryUse = "https://w3id.org/dpv#PrimaryUse"  # Primary Use
Principle = "https://w3id.org/dpv#Principle"
PrintedNotice = "https://w3id.org/dpv#PrintedNotice"  # Printed Notice
PrivacyByDefault = "https://w3id.org/dpv#PrivacyByDefault"  # Privacy by Default
PrivacyByDesign = "https://w3id.org/dpv#PrivacyByDesign"  # Privacy by Design
PrivacyNotice = "https://w3id.org/dpv#PrivacyNotice"  # Privacy Notice
PrivacyPreservingProtocol = "https://w3id.org/dpv#PrivacyPreservingProtocol"  # Privacy Preserving Protocol
PrivateCommunalSpace = "https://w3id.org/dpv#PrivateCommunalSpace"  # Private Communal Space
PrivateInformationRetrieval = "https://w3id.org/dpv#PrivateInformationRetrieval"  # Private Information Retrieval
PrivateLocation = "https://w3id.org/dpv#PrivateLocation"  # Private Location (deprecated)
PrivatelyOperatedPublicSpace = "https://w3id.org/dpv#PrivatelyOperatedPublicSpace"  # Privately Operated Public Space
PrivatelyOwnedPublicSpace = "https://w3id.org/dpv#PrivatelyOwnedPublicSpace"  # Privately Owned Public Space
PrivatelyOwnedSpace = "https://w3id.org/dpv#PrivatelyOwnedSpace"  # Privately Owned Space
PrivateSectorBody = "https://w3id.org/dpv#PrivateSectorBody"  # Private Sector Body
PrivateSpace = "https://w3id.org/dpv#PrivateSpace"  # Private Space
Process = "https://w3id.org/dpv#Process"
Processing = "https://w3id.org/dpv#Processing"
ProcessingCondition = "https://w3id.org/dpv#ProcessingCondition"  # Processing Condition
ProcessingContext = "https://w3id.org/dpv#ProcessingContext"  # Processing Context
ProcessingDuration = "https://w3id.org/dpv#ProcessingDuration"  # Processing Duration
ProcessingLocation = "https://w3id.org/dpv#ProcessingLocation"  # Processing Location
ProcessingScale = "https://w3id.org/dpv#ProcessingScale"  # Processing Scale
ProfessionalConfidentialData = "https://w3id.org/dpv#ProfessionalConfidentialData"  # Professional Confidential Data
ProfessionalTraining = "https://w3id.org/dpv#ProfessionalTraining"  # Professional Training
Profiling = "https://w3id.org/dpv#Profiling"
Prohibition = "https://w3id.org/dpv#Prohibition"
ProhibitionUnviolated = "https://w3id.org/dpv#ProhibitionUnviolated"  # Prohibition Unviolated
ProhibitionViolated = "https://w3id.org/dpv#ProhibitionViolated"  # Prohibition Violated
ProtectionOfIPR = "https://w3id.org/dpv#ProtectionOfIPR"  # Protection of Intellectual Property Rights
ProtectionOfNationalSecurity = "https://w3id.org/dpv#ProtectionOfNationalSecurity"  # Protection of National Security
ProtectionOfPublicSecurity = "https://w3id.org/dpv#ProtectionOfPublicSecurity"  # Protection of Public Security
ProvideConsent = "https://w3id.org/dpv#ProvideConsent"  # Provide Consent
ProvidedData = "https://w3id.org/dpv#ProvidedData"  # Provided Data
ProvidedPersonalData = "https://w3id.org/dpv#ProvidedPersonalData"  # Provided Personal Data
ProvideEventRecommendations = "https://w3id.org/dpv#ProvideEventRecommendations"  # Provide Event Recommendations
ProvideOfficialStatistics = "https://w3id.org/dpv#ProvideOfficialStatistics"  # Provide Official Statistics
ProvidePersonalisedRecommendations = (
    "https://w3id.org/dpv#ProvidePersonalisedRecommendations"  # Provide Personalised Recommendations
)
ProvideProductRecommendations = "https://w3id.org/dpv#ProvideProductRecommendations"  # Provide Product Recommendations
ProviderStandardFormContract = "https://w3id.org/dpv#ProviderStandardFormContract"  # Provider Standard Form Contract
Pseudonymisation = "https://w3id.org/dpv#Pseudonymisation"
Pseudonymise = "https://w3id.org/dpv#Pseudonymise"
PseudonymisedData = "https://w3id.org/dpv#PseudonymisedData"  # Pseudonymised Data
PublicBenefit = "https://w3id.org/dpv#PublicBenefit"  # Public Benefit
PublicDataSource = "https://w3id.org/dpv#PublicDataSource"  # Public Data Source
PublicInterest = "https://w3id.org/dpv#PublicInterest"  # Public Interest
PublicInterestCompleted = "https://w3id.org/dpv#PublicInterestCompleted"  # Public Interest Completed
PublicInterestObjected = "https://w3id.org/dpv#PublicInterestObjected"  # Public Interest Objected
PublicInterestOngoing = "https://w3id.org/dpv#PublicInterestOngoing"  # Public Interest Ongoing
PublicInterestPending = "https://w3id.org/dpv#PublicInterestPending"  # Public Interest Pending
PublicInterestStatus = "https://w3id.org/dpv#PublicInterestStatus"  # Public Interest Status
PublicLocation = "https://w3id.org/dpv#PublicLocation"  # Public Location (deprecated)
PubliclyAccessibleSpace = "https://w3id.org/dpv#PubliclyAccessibleSpace"  # Publicly Accessible Space
PubliclyOwnedSpace = "https://w3id.org/dpv#PubliclyOwnedSpace"  # Publicly Owned Space
PublicPolicyMaking = "https://w3id.org/dpv#PublicPolicyMaking"  # Public Policy Making
PublicRegisterOfEntities = "https://w3id.org/dpv#PublicRegisterOfEntities"  # Public Register of Entities
PublicRelations = "https://w3id.org/dpv#PublicRelations"  # Public Relations
PublicSectorBody = "https://w3id.org/dpv#PublicSectorBody"  # Public Sector Body
PublicSpace = "https://w3id.org/dpv#PublicSpace"  # Public Space
Purpose = "https://w3id.org/dpv#Purpose"
QuantumCryptography = "https://w3id.org/dpv#QuantumCryptography"  # Quantum Cryptography
Query = "https://w3id.org/dpv#Query"
RandomLocation = "https://w3id.org/dpv#RandomLocation"  # Random Location
ReaffirmConsent = "https://w3id.org/dpv#ReaffirmConsent"  # Reaffirm Consent
RecertificationPolicy = "https://w3id.org/dpv#RecertificationPolicy"  # Recertification Policy
Recipient = "https://w3id.org/dpv#Recipient"
RecipientInformed = "https://w3id.org/dpv#RecipientInformed"  # Recipient Informed
RecipientUninformed = "https://w3id.org/dpv#RecipientUninformed"  # Recipient Uninformed
Recommendation = "https://w3id.org/dpv#Recommendation"
RecommendationFollowed = "https://w3id.org/dpv#RecommendationFollowed"  # Recommendation Followed
RecommendationNotFollowed = "https://w3id.org/dpv#RecommendationNotFollowed"  # Recommendation Not Followed
Record = "https://w3id.org/dpv#Record"
RecordManagement = "https://w3id.org/dpv#RecordManagement"  # Record Management
RecordsOfActivities = "https://w3id.org/dpv#RecordsOfActivities"  # Records of Activities
RecruitmentAdvertising = "https://w3id.org/dpv#RecruitmentAdvertising"  # Recruitment Advertising
RecruitmentApplicantBackgroundCheck = (
    "https://w3id.org/dpv#RecruitmentApplicantBackgroundCheck"  # Recruitment Applicant Background Check
)
RecruitmentApplicantCriminalBackgroundCheck = "https://w3id.org/dpv#RecruitmentApplicantCriminalBackgroundCheck"  # Recruitment Applicant Criminal Background Check
RecruitmentApplicantInformationAuthentication = "https://w3id.org/dpv#RecruitmentApplicantInformationAuthentication"  # Recruitment Applicant Information Authentication
RecruitmentApplicantSelection = "https://w3id.org/dpv#RecruitmentApplicantSelection"  # Recruitment Applicant Selection
RecruitmentApplicationAnalysis = (
    "https://w3id.org/dpv#RecruitmentApplicationAnalysis"  # Recruitment Application Analysis
)
RecruitmentApplicationManagement = (
    "https://w3id.org/dpv#RecruitmentApplicationManagement"  # Recruitment Application Management
)
RecruitmentApplicationScreening = (
    "https://w3id.org/dpv#RecruitmentApplicationScreening"  # Recruitment Application Screening
)
RecruitmentInterviewAnalysis = "https://w3id.org/dpv#RecruitmentInterviewAnalysis"  # Recruitment Interview Analysis
RecruitmentInterviewAssessment = (
    "https://w3id.org/dpv#RecruitmentInterviewAssessment"  # Recruitment Interview Assessment
)
RecruitmentInterviewManagement = (
    "https://w3id.org/dpv#RecruitmentInterviewManagement"  # Recruitment Interview Management
)
RecruitmentInterviewScheduling = (
    "https://w3id.org/dpv#RecruitmentInterviewScheduling"  # Recruitment Interview Scheduling
)
RecruitmentManagement = "https://w3id.org/dpv#RecruitmentManagement"  # Recruitment Management
RecruitmentTargetedAdvertising = (
    "https://w3id.org/dpv#RecruitmentTargetedAdvertising"  # Targeted Recruitment Advertising
)
Reformat = "https://w3id.org/dpv#Reformat"
RefuseConsent = "https://w3id.org/dpv#RefuseConsent"  # Refuse Consent
RefuseContract = "https://w3id.org/dpv#RefuseContract"  # Refuse Contract
Region = "https://w3id.org/dpv#Region"
RegionalAuthority = "https://w3id.org/dpv#RegionalAuthority"  # Regional Authority
RegionalScale = "https://w3id.org/dpv#RegionalScale"  # Regional Scale
RegulatorySandbox = "https://w3id.org/dpv#RegulatorySandbox"  # Regulatory Sandbox
ReligiousAssociations = "https://w3id.org/dpv#ReligiousAssociations"  # Religious Associations
RemoteLocation = "https://w3id.org/dpv#RemoteLocation"  # Remote Location
Remove = "https://w3id.org/dpv#Remove"
RenewedConsentGiven = "https://w3id.org/dpv#RenewedConsentGiven"  # Renewed Consent Given
RepairImpairments = "https://w3id.org/dpv#RepairImpairments"  # Repair Impairments
Representative = "https://w3id.org/dpv#Representative"
RequestAccepted = "https://w3id.org/dpv#RequestAccepted"  # Request Accepted
RequestAcknowledged = "https://w3id.org/dpv#RequestAcknowledged"  # Request Acknowledged
RequestActionDelayed = "https://w3id.org/dpv#RequestActionDelayed"  # Request Action Delayed
RequestedServiceProvision = "https://w3id.org/dpv#RequestedServiceProvision"  # Requested Service Provision
RequestFulfilled = "https://w3id.org/dpv#RequestFulfilled"  # Request Fulfilled
RequestInitiated = "https://w3id.org/dpv#RequestInitiated"  # Request Initiated
RequestRejected = "https://w3id.org/dpv#RequestRejected"  # Request Rejected
RequestRequiredActionPerformed = (
    "https://w3id.org/dpv#RequestRequiredActionPerformed"  # Request Required Action Performed
)
RequestRequiresAction = "https://w3id.org/dpv#RequestRequiresAction"  # Request Requires Action
RequestStatus = "https://w3id.org/dpv#RequestStatus"  # Request Status
RequestStatusQuery = "https://w3id.org/dpv#RequestStatusQuery"  # Request Status Query
RequestUnfulfilled = "https://w3id.org/dpv#RequestUnfulfilled"  # Request Unfulfilled
Required = "https://w3id.org/dpv#Required"
ResearchAndDevelopment = "https://w3id.org/dpv#ResearchAndDevelopment"  # Research and Development
ResidualRisk = "https://w3id.org/dpv#ResidualRisk"  # Residual Risk
Restrict = "https://w3id.org/dpv#Restrict"
Retrieve = "https://w3id.org/dpv#Retrieve"
ReuseCompatibility = "https://w3id.org/dpv#ReuseCompatibility"
ReversingProcessEffects = "https://w3id.org/dpv#ReversingProcessEffects"  # Reversing Process Effects
ReversingProcessInput = "https://w3id.org/dpv#ReversingProcessInput"  # Reversing Process Input
ReversingProcessOutput = "https://w3id.org/dpv#ReversingProcessOutput"  # Reversing Process Output
ReviewImpactAssessment = "https://w3id.org/dpv#ReviewImpactAssessment"  # Review Impact Assessment
ReviewProcedure = "https://w3id.org/dpv#ReviewProcedure"  # Review Procedure
Right = "https://w3id.org/dpv#Right"
RightExerciseActivity = "https://w3id.org/dpv#RightExerciseActivity"  # Right Exercise Activity
RightExerciseNotice = "https://w3id.org/dpv#RightExerciseNotice"  # Right Exercise Notice
RightExerciseRecord = "https://w3id.org/dpv#RightExerciseRecord"  # Right Exercise Record
RightFulfilmentNotice = "https://w3id.org/dpv#RightFulfilmentNotice"  # Right Fulfilment Notice
RightNonFulfilmentNotice = "https://w3id.org/dpv#RightNonFulfilmentNotice"  # Right Non-Fulfilment Notice
RightNotice = "https://w3id.org/dpv#RightNotice"  # Right Notice
RightsFulfilment = "https://w3id.org/dpv#RightsFulfilment"  # Rights Fulfilment
RightsImpactAssessment = "https://w3id.org/dpv#RightsImpactAssessment"  # Rights Impact Assessment
RightsManagement = "https://w3id.org/dpv#RightsManagement"  # Rights Management
Risk = "https://w3id.org/dpv#Risk"
RiskAssessment = "https://w3id.org/dpv#RiskAssessment"  # Risk Assessment
RiskConcept = "https://w3id.org/dpv#RiskConcept"  # Risk Concept
RiskLevel = "https://w3id.org/dpv#RiskLevel"  # Risk Level
RiskMitigationMeasure = "https://w3id.org/dpv#RiskMitigationMeasure"  # Risk Mitigation Measure
RNGPseudonymisation = "https://w3id.org/dpv#RNGPseudonymisation"  # RNG Pseudonymisation
ROPA = "https://w3id.org/dpv#ROPA"  # Records of Processing Activities
Rule = "https://w3id.org/dpv#Rule"
RuleFulfilled = "https://w3id.org/dpv#RuleFulfilled"  # Rule Fulfilled
RuleFulfilmentStatus = "https://w3id.org/dpv#RuleFulfilmentStatus"  # Rule Fulfilment Status
RuleUnfulfilled = "https://w3id.org/dpv#RuleUnfulfilled"  # Rule Unfulfilled
RuleViolated = "https://w3id.org/dpv#RuleViolated"  # Rule Violated
Safeguard = "https://w3id.org/dpv#Safeguard"
SafeguardForDataTransfer = "https://w3id.org/dpv#SafeguardForDataTransfer"  # Safeguard for Data Transfer
Scale = "https://w3id.org/dpv#Scale"
ScientificResearch = "https://w3id.org/dpv#ScientificResearch"  # Scientific Research
Scope = "https://w3id.org/dpv#Scope"
ScoringOfIndividuals = "https://w3id.org/dpv#ScoringOfIndividuals"  # Scoring of Individuals
Screen = "https://w3id.org/dpv#Screen"
Seal = "https://w3id.org/dpv#Seal"
SearchFunctionalities = "https://w3id.org/dpv#SearchFunctionalities"  # Search Functionalities
SecondaryImportance = "https://w3id.org/dpv#SecondaryImportance"  # Secondary Importance
SecondaryUse = "https://w3id.org/dpv#SecondaryUse"  # Secondary Use
SecretSharingSchemes = "https://w3id.org/dpv#SecretSharingSchemes"  # Secret Sharing Schemes
Sector = "https://w3id.org/dpv#Sector"
SecureMultiPartyComputation = "https://w3id.org/dpv#SecureMultiPartyComputation"  # Secure Multi-Party Computation
SecureProcessingEnvironment = "https://w3id.org/dpv#SecureProcessingEnvironment"  # Secure Processing Environment
SecurityAssessment = "https://w3id.org/dpv#SecurityAssessment"  # Security Assessment
SecurityAudit = "https://w3id.org/dpv#SecurityAudit"  # Security Audit
SecurityIncidentNotice = "https://w3id.org/dpv#SecurityIncidentNotice"  # Security Incident Notice
SecurityIncidentNotification = "https://w3id.org/dpv#SecurityIncidentNotification"  # Security Incident Notification
SecurityIncidentRecord = "https://w3id.org/dpv#SecurityIncidentRecord"  # Security Incident Record
SecurityKnowledgeTraining = "https://w3id.org/dpv#SecurityKnowledgeTraining"  # Security Knowledge Training
SecurityMethod = "https://w3id.org/dpv#SecurityMethod"  # Security Method
SecurityProcedure = "https://w3id.org/dpv#SecurityProcedure"  # Security Procedure
SecurityRoleProcedures = "https://w3id.org/dpv#SecurityRoleProcedures"  # Security Role Procedures
SellDataToThirdParties = "https://w3id.org/dpv#SellDataToThirdParties"  # Sell Data to Third Parties
SellInsightsFromData = "https://w3id.org/dpv#SellInsightsFromData"  # Sell Insights from Data
SellProducts = "https://w3id.org/dpv#SellProducts"  # Sell Products
SellProductsToDataSubject = "https://w3id.org/dpv#SellProductsToDataSubject"  # Sell Products to Data Subject
SemiPrivateSpace = "https://w3id.org/dpv#SemiPrivateSpace"  # Semi Private Space
SensitiveData = "https://w3id.org/dpv#SensitiveData"  # Sensitive Data
SensitiveNonPersonalData = "https://w3id.org/dpv#SensitiveNonPersonalData"  # Sensitive Non Personal Data
SensitivePersonalData = "https://w3id.org/dpv#SensitivePersonalData"  # Sensitive Personal Data
SensitivityLevel = "https://w3id.org/dpv#SensitivityLevel"  # Sensitivity Level
Service = "https://w3id.org/dpv#Service"
ServiceAccessDetermination = "https://w3id.org/dpv#ServiceAccessDetermination"  # Service Access Determination
ServiceConsumer = "https://w3id.org/dpv#ServiceConsumer"  # Service Consumer
ServiceLevelAgreement = "https://w3id.org/dpv#ServiceLevelAgreement"  # Service Level Agreement (SLA)
ServiceManagement = "https://w3id.org/dpv#ServiceManagement"  # Service Management
ServiceMonitoring = "https://w3id.org/dpv#ServiceMonitoring"  # Service Monitoring
ServiceOptimisation = "https://w3id.org/dpv#ServiceOptimisation"  # Service Optimisation
ServicePersonalisation = "https://w3id.org/dpv#ServicePersonalisation"  # Service Personalisation
ServiceProvider = "https://w3id.org/dpv#ServiceProvider"  # Service Provider
ServiceProvision = "https://w3id.org/dpv#ServiceProvision"  # Service Provision
ServiceRegistration = "https://w3id.org/dpv#ServiceRegistration"  # Service Registration
ServiceUsageAnalytics = "https://w3id.org/dpv#ServiceUsageAnalytics"  # Service Usage Analytics
Severity = "https://w3id.org/dpv#Severity"
Share = "https://w3id.org/dpv#Share"
SingleSignOn = "https://w3id.org/dpv#SingleSignOn"  # Single Sign On
SingularDataVolume = "https://w3id.org/dpv#SingularDataVolume"  # Singular Data Volume
SingularFrequency = "https://w3id.org/dpv#SingularFrequency"  # Singular Frequency
SingularScaleOfDataSubjects = "https://w3id.org/dpv#SingularScaleOfDataSubjects"  # Singular Scale Of Data Subjects
SmallDataVolume = "https://w3id.org/dpv#SmallDataVolume"  # Small Data Volume
SmallScaleOfDataSubjects = "https://w3id.org/dpv#SmallScaleOfDataSubjects"  # Small Scale Of Data Subjects
SmallScaleProcessing = "https://w3id.org/dpv#SmallScaleProcessing"  # Small Scale Processing
SMEOrganisation = "https://w3id.org/dpv#SMEOrganisation"  # SME Organisation
SocialMediaMarketing = "https://w3id.org/dpv#SocialMediaMarketing"  # Social Media Marketing
SpecialCategoryPersonalData = "https://w3id.org/dpv#SpecialCategoryPersonalData"  # Special Category Personal Data
SporadicDataVolume = "https://w3id.org/dpv#SporadicDataVolume"  # Sporadic Data Volume
SporadicFrequency = "https://w3id.org/dpv#SporadicFrequency"  # Sporadic Frequency
SporadicScaleOfDataSubjects = "https://w3id.org/dpv#SporadicScaleOfDataSubjects"  # Sporadic Scale Of Data Subjects
StaffTraining = "https://w3id.org/dpv#StaffTraining"  # Staff Training
Standard = "https://w3id.org/dpv#Standard"
StandardFormContract = "https://w3id.org/dpv#StandardFormContract"  # Standard Form Contract
StandardsConformance = "https://w3id.org/dpv#StandardsConformance"  # Standards Conformance
StartupOrganisation = "https://w3id.org/dpv#StartupOrganisation"  # Startup Organisation
StatisticalConfidentialityAgreement = (
    "https://w3id.org/dpv#StatisticalConfidentialityAgreement"  # Statistical Confidentiality Agreement
)
StatisticallyConfidentialData = "https://w3id.org/dpv#StatisticallyConfidentialData"  # Statistically Confidential Data
Status = "https://w3id.org/dpv#Status"
StorageCondition = "https://w3id.org/dpv#StorageCondition"  # Storage Condition
StorageDeletion = "https://w3id.org/dpv#StorageDeletion"  # Storage Deletion
StorageDuration = "https://w3id.org/dpv#StorageDuration"  # Storage Duration
StorageLocation = "https://w3id.org/dpv#StorageLocation"  # Storage Location
StorageRestoration = "https://w3id.org/dpv#StorageRestoration"  # Storage Restoration
Store = "https://w3id.org/dpv#Store"
Structure = "https://w3id.org/dpv#Structure"
Student = "https://w3id.org/dpv#Student"
SubProcessorAgreement = "https://w3id.org/dpv#SubProcessorAgreement"  # Sub-Processor Agreement
Subscriber = "https://w3id.org/dpv#Subscriber"
SubsidiaryLegalEntity = "https://w3id.org/dpv#SubsidiaryLegalEntity"  # Subsidiary Legal Entity
SupportContractNegotiation = "https://w3id.org/dpv#SupportContractNegotiation"  # Support Contract Negotiation
SupportEntityDecisionMaking = "https://w3id.org/dpv#SupportEntityDecisionMaking"  # Support Entity Decision Making
SupportExchangeOfViews = "https://w3id.org/dpv#SupportExchangeOfViews"  # Support Exchange of Views
SupportInformedConsentDecision = (
    "https://w3id.org/dpv#SupportInformedConsentDecision"  # Support Informed Consent Decision
)
supportsComplianceWith = "https://w3id.org/dpv#supportsComplianceWith"  # supports Compliance With
SupraNationalAuthority = "https://w3id.org/dpv#SupraNationalAuthority"  # Supranational Authority
SupraNationalUnion = "https://w3id.org/dpv#SupraNationalUnion"  # Supranational Union
SymmetricCryptography = "https://w3id.org/dpv#SymmetricCryptography"  # Symmetric Cryptography
SymmetricEncryption = "https://w3id.org/dpv#SymmetricEncryption"  # Symmetric Encryption
SyntheticData = "https://w3id.org/dpv#SyntheticData"  # Synthetic Data
SystematicMonitoring = "https://w3id.org/dpv#SystematicMonitoring"  # Systematic Monitoring
TargetedAdvertising = "https://w3id.org/dpv#TargetedAdvertising"  # Targeted Advertising
TechnicalMeasure = "https://w3id.org/dpv#TechnicalMeasure"  # Technical Measure
TechnicalOrganisationalMeasure = (
    "https://w3id.org/dpv#TechnicalOrganisationalMeasure"  # Technical and Organisational Measure
)
TechnicalServiceProvision = "https://w3id.org/dpv#TechnicalServiceProvision"  # Technical Service Provision
TechnicalStandard = "https://w3id.org/dpv#TechnicalStandard"  # Technical Standard
Technology = "https://w3id.org/dpv#Technology"
TemporalDuration = "https://w3id.org/dpv#TemporalDuration"  # Temporal Duration
TerminateContract = "https://w3id.org/dpv#TerminateContract"  # Terminate Contract
TermsOfService = "https://w3id.org/dpv#TermsOfService"  # Terms of Service
ThirdCountry = "https://w3id.org/dpv#ThirdCountry"  # Third Country
ThirdParty = "https://w3id.org/dpv#ThirdParty"  # Third Party
ThirdPartyAgreement = "https://w3id.org/dpv#ThirdPartyAgreement"  # Third-Party Agreement
ThirdPartyContract = "https://w3id.org/dpv#ThirdPartyContract"  # Third Party Contract
ThirdPartyDataSource = "https://w3id.org/dpv#ThirdPartyDataSource"  # Third Party as Data Source
ThirdPartySecurityProcedures = "https://w3id.org/dpv#ThirdPartySecurityProcedures"  # Third Party Security Procedures
Tourist = "https://w3id.org/dpv#Tourist"
Tracking = "https://w3id.org/dpv#Tracking"
TrackingByFirstParty = "https://w3id.org/dpv#TrackingByFirstParty"  # Tracking by First Party
TrackingByThirdParty = "https://w3id.org/dpv#TrackingByThirdParty"  # Tracking by Third Party
Transfer = "https://w3id.org/dpv#Transfer"
Transform = "https://w3id.org/dpv#Transform"
Transmit = "https://w3id.org/dpv#Transmit"
TrustedComputing = "https://w3id.org/dpv#TrustedComputing"  # Trusted Computing
TrustedExecutionEnvironment = "https://w3id.org/dpv#TrustedExecutionEnvironment"  # Trusted Execution Environment
UnacceptableRule = "https://w3id.org/dpv#UnacceptableRule"  # Unacceptable Rule
UncategorisedData = "https://w3id.org/dpv#UncategorisedData"  # Uncategorised Data
Unexpected = "https://w3id.org/dpv#Unexpected"
UninformedConsent = "https://w3id.org/dpv#UninformedConsent"  # Uninformed Consent
Unintended = "https://w3id.org/dpv#Unintended"
UnknownApplicability = "https://w3id.org/dpv#UnknownApplicability"  # Unknown Applicability
Unlawful = "https://w3id.org/dpv#Unlawful"
UnstructuredData = "https://w3id.org/dpv#UnstructuredData"  # Unstructured Data
UntilEventDuration = "https://w3id.org/dpv#UntilEventDuration"  # Until Event Duration
UntilTimeDuration = "https://w3id.org/dpv#UntilTimeDuration"  # Until Time Duration
UnverifiedData = "https://w3id.org/dpv#UnverifiedData"  # Unverified Data
UsageControl = "https://w3id.org/dpv#UsageControl"  # Usage Control
Use = "https://w3id.org/dpv#Use"
User = "https://w3id.org/dpv#User"
UserInterfacePersonalisation = "https://w3id.org/dpv#UserInterfacePersonalisation"  # User Interface Personalisation
UseSyntheticData = "https://w3id.org/dpv#UseSyntheticData"  # Use of Synthetic Data
VariableLocation = "https://w3id.org/dpv#VariableLocation"  # Variable Location
VendorManagement = "https://w3id.org/dpv#VendorManagement"  # Vendor Management
VendorPayment = "https://w3id.org/dpv#VendorPayment"  # Vendor Payment
VendorRecordsManagement = "https://w3id.org/dpv#VendorRecordsManagement"  # Vendor Records Management
VendorSelectionAssessment = "https://w3id.org/dpv#VendorSelectionAssessment"  # Vendor Selection Assessment
Verification = "https://w3id.org/dpv#Verification"
VerifiedData = "https://w3id.org/dpv#VerifiedData"  # Verified Data
VirtualisationSecurity = "https://w3id.org/dpv#VirtualisationSecurity"  # Virtualisation Security
Visitor = "https://w3id.org/dpv#Visitor"
VitalInterest = "https://w3id.org/dpv#VitalInterest"  # Vital Interest
VitalInterestCompleted = "https://w3id.org/dpv#VitalInterestCompleted"  # Vital Interest Completed
VitalInterestObjected = "https://w3id.org/dpv#VitalInterestObjected"  # Vital Interest Objected
VitalInterestOfDataSubject = "https://w3id.org/dpv#VitalInterestOfDataSubject"  # Vital Interest of Data Subject
VitalInterestOfNaturalPerson = "https://w3id.org/dpv#VitalInterestOfNaturalPerson"  # Vital Interest of Natural Person
VitalInterestOngoing = "https://w3id.org/dpv#VitalInterestOngoing"  # Vital Interest Ongoing
VitalInterestPending = "https://w3id.org/dpv#VitalInterestPending"  # Vital Interest Pending
VitalInterestStatus = "https://w3id.org/dpv#VitalInterestStatus"  # Vital Interest Status
VulnerabilityTestingMethods = "https://w3id.org/dpv#VulnerabilityTestingMethods"  # Vulnerability Testing Methods
VulnerableDataSubject = "https://w3id.org/dpv#VulnerableDataSubject"  # Vulnerable Data Subject
VulnerableHuman = "https://w3id.org/dpv#VulnerableHuman"  # Vulnerable Human
WebBrowserSecurity = "https://w3id.org/dpv#WebBrowserSecurity"  # WebBrowser Security
WebSecurityProtocols = "https://w3id.org/dpv#WebSecurityProtocols"  # Web Security Protocols
WirelessSecurityProtocols = "https://w3id.org/dpv#WirelessSecurityProtocols"  # Wireless Security Protocols
WithdrawConsent = "https://w3id.org/dpv#WithdrawConsent"  # Withdraw Consent
WithdrawingFromProcess = "https://w3id.org/dpv#WithdrawingFromProcess"  # Withdrawing from Process
WithinDevice = "https://w3id.org/dpv#WithinDevice"  # Within Device (deprecated)
WithinPhysicalEnvironment = "https://w3id.org/dpv#WithinPhysicalEnvironment"  # Within Physical Environment
WithinVirtualEnvironment = "https://w3id.org/dpv#WithinVirtualEnvironment"  # Within Virtual Environment
ZeroKnowledgeAuthentication = "https://w3id.org/dpv#ZeroKnowledgeAuthentication"  # Zero Knowledge Authentication

# ── Metadata registry ──────────────────────────────────────────────────────────────
# Populated at import time so stav.label() / .definition() / .broader() work.
_register(
    {
        "https://w3id.org/dpv#AIGovernance": {
            "label": "AI Governance",
            "definition": "Procedures related to governance of AI, including its procurement, development, deployment, and assessments",
            "broader": ("https://w3id.org/dpv#GovernanceProcedures",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#AILiteracy": {
            "label": "AI Literacy",
            "definition": "Providing skills, knowledge, and understanding to enable reading, writing, analysing, reasoning, and communicating regarding AI",
            "broader": ("https://w3id.org/dpv#DigitalLiteracy",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#AINotice": {
            "label": "AI Notice",
            "definition": "A notice providing information regarding the particulars of an AI system such as its intended purpose and proper use",
            "broader": ("https://w3id.org/dpv#Notice",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#AcademicResearch": {
            "label": "Academic Research",
            "definition": "Purposes associated with conducting or assisting with research conducted in an academic context e.g. within universities",
            "broader": ("https://w3id.org/dpv#ResearchAndDevelopment",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#AcademicScientificOrganisation": {
            "label": "Academic or Scientific Organisation",
            "definition": "Organisations related to academia or scientific pursuits e.g. Universities, Schools, Research Bodies",
            "broader": ("https://w3id.org/dpv#Organisation",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#AcceptContract": {
            "label": "Accept Contract",
            "definition": "Control for accepting a contract",
            "broader": ("https://w3id.org/dpv#ContractControl",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#AcceptableRule": {
            "label": "Acceptable Rule",
            "definition": "A rule that is acceptable where it is either desirable if it occurs or it is not unacceptable if it does",
            "broader": ("https://w3id.org/dpv#Rule",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#AcceptableUsePolicy": {
            "label": "Acceptable Use Policy",
            "definition": "Acceptable Use Policy (AUP) refers to conditions, contexts, or uses which are considered acceptable with the implication that those not covered by such a policy are to be considered unacceptable",
            "broader": ("https://w3id.org/dpv#Policy",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Access": {
            "label": "Access",
            "definition": "to access data",
            "broader": ("https://w3id.org/dpv#Use",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#AccessControlMethod": {
            "label": "Access Control Method",
            "definition": "Methods which restrict access to a place or resource",
            "broader": ("https://w3id.org/dpv#TechnicalMeasure",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#AccountManagement": {
            "label": "Account Management",
            "definition": "Account Management refers to purposes associated with account management, such as to create, provide, maintain, and manage accounts",
            "broader": ("https://w3id.org/dpv#Purpose",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Acquire": {
            "label": "Acquire",
            "definition": "to come into possession or control of the data",
            "broader": ("https://w3id.org/dpv#Obtain",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ActiveRight": {
            "label": "Active Right",
            "definition": "The right(s) applicable, provided, or expected that need to be (actively) exercised",
            "broader": ("https://w3id.org/dpv#Right",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ActivelyInvolved": {
            "label": "Actively Involved",
            "definition": "Status indicating the specified context is 'actively' involved",
            "broader": ("https://w3id.org/dpv#InvolvementStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ActivityCompleted": {
            "label": "Activity Completed",
            "definition": "State of an activity that has completed i.e. is fully in the past",
            "broader": ("https://w3id.org/dpv#ActivityStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ActivityHalted": {
            "label": "Activity Halted",
            "definition": "State of an activity that was occurring in the past, and has been halted or paused or stopped",
            "broader": ("https://w3id.org/dpv#ActivityStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ActivityMonitoring": {
            "label": "Activity Monitoring",
            "definition": "Monitoring of activities including assessing whether they have been successfully initiated and completed",
            "broader": ("https://w3id.org/dpv#TechnicalMeasure",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ActivityNotCompleted": {
            "label": "Activity Not Completed",
            "definition": "State of an activity that could not be completed, but has reached some end state",
            "broader": ("https://w3id.org/dpv#ActivityStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ActivityOngoing": {
            "label": "Activity Ongoing",
            "definition": "State of an activity occurring in continuation i.e. currently ongoing",
            "broader": ("https://w3id.org/dpv#ActivityStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ActivityPlanned": {
            "label": "Activity Planned",
            "definition": "State of an activity being planned with concrete plans for implementation",
            "broader": ("https://w3id.org/dpv#ActivityStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ActivityProposed": {
            "label": "Activity Proposed",
            "definition": "State of an activity being proposed without any concrete plans for implementation",
            "broader": ("https://w3id.org/dpv#ActivityStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ActivityStatus": {
            "label": "Activity Status",
            "definition": "Status associated with activity operations and lifecycles",
            "broader": ("https://w3id.org/dpv#Status",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Adapt": {
            "label": "Adapt",
            "definition": "to modify the data, often rewritten into a new form for a new use",
            "broader": ("https://w3id.org/dpv#Transform",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Adult": {
            "label": "Adult",
            "definition": "A natural person that is not a child i.e. has attained some legally specified age of adulthood",
            "broader": ("https://w3id.org/dpv#HumanSubject",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Advertising": {
            "label": "Advertising",
            "definition": "Purposes associated with conducting advertising i.e. process or artefact used to call attention to a product, service, etc. through announcements, notices, or other forms of communication",
            "broader": ("https://w3id.org/dpv#Marketing",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#AgeVerification": {
            "label": "Age Verification",
            "definition": "Purposes associated with verifying or authenticating age or age related information as a form of security",
            "broader": ("https://w3id.org/dpv#Verification",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Agent": {
            "label": "Agent",
            "definition": "An Agent is a dpv:Entity that is (a) acting on behalf of another Entity; and (b) is authorised to do so by that Entity",
            "broader": ("https://w3id.org/dpv#Entity",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Aggregate": {
            "label": "Aggregate",
            "definition": "to aggregate data",
            "broader": ("https://w3id.org/dpv#Alter",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#AlgorithmicLogic": {
            "label": "Algorithmic Logic",
            "definition": "The algorithmic logic applied or used",
            "broader": ("https://w3id.org/dpv#ProcessingContext",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Align": {
            "label": "Align",
            "definition": "to adjust the data to be in relation to another data",
            "broader": ("https://w3id.org/dpv#Transform",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Alter": {
            "label": "Alter",
            "definition": "to change the data without changing it into something else",
            "broader": ("https://w3id.org/dpv#Transform",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#AmbulanceProvider": {
            "label": "Ambulance Provider",
            "definition": "An organisation that that offers transportation and medical care to patients requiring urgent medical attention",
            "broader": ("https://w3id.org/dpv#EmergencyServiceProvider",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Analyse": {
            "label": "Analyse",
            "definition": "to study or examine the data in detail",
            "broader": ("https://w3id.org/dpv#Use",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Anonymisation": {
            "label": "Anonymisation",
            "definition": "Anonymisation is the process by which data is irreversibly altered in such a way that a data subject can no longer be identified directly or indirectly, either by the entity holding the data alone or in collaboration with other entities and information sources",
            "broader": ("https://w3id.org/dpv#Deidentification",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Anonymise": {
            "label": "Anonymise",
            "definition": "to irreversibly alter personal data in such a way that an unique data subject can no longer be identified directly or indirectly or in combination with other data",
            "broader": ("https://w3id.org/dpv#Transform",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#AnonymisedData": {
            "label": "Anonymised Data",
            "definition": "Personal Data that has been (fully and completely) anonymised so that it is no longer considered Personal Data",
            "broader": ("https://w3id.org/dpv#NonPersonalData",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Applicability": {
            "label": "Applicability",
            "definition": "Concept provided to represent indication of cases where the information or context is not applicable (N/A) or not available or this is not known or determined yet. If the information is applicable and available, this concept should not be used.",
            "broader": ("https://w3id.org/dpv#Context",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Applicant": {
            "label": "Applicant",
            "definition": "Humans that are applicants in some context",
            "broader": ("https://w3id.org/dpv#HumanSubject",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ApprovalProcedure": {
            "label": "Approval Procedure",
            "definition": "A procedure or process for determining and managing approvals for activities as part of governance",
            "broader": ("https://w3id.org/dpv#GovernanceProcedures",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Assess": {
            "label": "Assess",
            "definition": "to assess data for some criteria",
            "broader": ("https://w3id.org/dpv#Use",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Assessment": {
            "label": "Assessment",
            "definition": "The document, plan, or process for assessment or determination towards a purpose e.g. assessment of legality or impact assessments",
            "broader": ("https://w3id.org/dpv#OrganisationalMeasure",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#AssetManagementProcedures": {
            "label": "Asset Management Procedures",
            "definition": "Procedures related to management of assets",
            "broader": ("https://w3id.org/dpv#GovernanceProcedures",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#AssistiveAutomation": {
            "label": "Assistive Automation",
            "definition": "Level of automation corresponding to Level 1 in ISO/IEC 22989:2022 where automation is limited to parts of the system or a specific part of the system in a manner that does not change the control of the human in using/driving the system",
            "broader": ("https://w3id.org/dpv#AutomationLevel",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#AsylumSeeker": {
            "label": "Asylum Seeker",
            "definition": "Humans that are asylum seekers",
            "broader": ("https://w3id.org/dpv#VulnerableHuman",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#AsymmetricCryptography": {
            "label": "Asymmetric Cryptography",
            "definition": "Use of public-key cryptography or asymmetric cryptography involving a public and private pair of keys",
            "broader": ("https://w3id.org/dpv#CryptographicMethods",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#AsymmetricEncryption": {
            "label": "Asymmetric Encryption",
            "definition": "Use of asymmetric cryptography to encrypt data",
            "broader": ("https://w3id.org/dpv#Encryption",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Audit": {
            "label": "Audit",
            "definition": "An audit is a systematic examination or evaluation of records, processes, or systems towards a specific objective such as to assess accuracy, compliance, effectiveness, or performance",
            "broader": ("https://w3id.org/dpv#OrganisationalMeasure",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#AuditApproved": {
            "label": "Audit Approved",
            "definition": "State of being approved through the audit",
            "broader": ("https://w3id.org/dpv#AuditStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#AuditConditionallyApproved": {
            "label": "Audit Conditionally Approved",
            "definition": "State of being conditionally approved through the audit",
            "broader": ("https://w3id.org/dpv#AuditStatus",),
            "source_vocab": "2022-06-29",
        },
        "https://w3id.org/dpv#AuditNotRequired": {
            "label": "Audit Not Required",
            "definition": "State where an audit is determined as not being required",
            "broader": ("https://w3id.org/dpv#AuditStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#AuditRejected": {
            "label": "Audit Rejected",
            "definition": "State of not being approved or being rejected through the audit",
            "broader": ("https://w3id.org/dpv#AuditStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#AuditRequested": {
            "label": "Audit Requested",
            "definition": "State of an audit being requested whose outcome is not yet known",
            "broader": ("https://w3id.org/dpv#AuditStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#AuditRequired": {
            "label": "Audit Required",
            "definition": "State where an audit is determined as being required but has not been conducted",
            "broader": ("https://w3id.org/dpv#AuditStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#AuditStatus": {
            "label": "Audit Status",
            "definition": "Status associated with Auditing or Investigation",
            "broader": ("https://w3id.org/dpv#Status",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Authentication-ABC": {
            "label": "Authentication using ABC",
            "definition": "Use of Attribute Based Credentials (ABC) to perform and manage authentication",
            "broader": ("https://w3id.org/dpv#CryptographicAuthentication",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Authentication-PABC": {
            "label": "Authentication using PABC",
            "definition": "Use of Privacy-enhancing Attribute Based Credentials (ABC) to perform and manage authentication",
            "broader": ("https://w3id.org/dpv#CryptographicAuthentication",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#AuthenticationProtocols": {
            "label": "Authentication Protocols",
            "definition": "Protocols involving validation of identity i.e. authentication of a person or information",
            "broader": ("https://w3id.org/dpv#TechnicalMeasure",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#AuthorisationProcedure": {
            "label": "Authorisation Procedure",
            "definition": "Procedures for determining authorisation through permission or authority",
            "broader": ("https://w3id.org/dpv#SecurityProcedure",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#AuthorisationProtocols": {
            "label": "Authorisation Protocols",
            "definition": "Protocols involving authorisation of roles or profiles to determine permission, rights, or privileges",
            "broader": ("https://w3id.org/dpv#TechnicalMeasure",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Authority": {
            "label": "Authority",
            "definition": "An authority with the power to create or enforce laws, or determine their compliance.",
            "broader": ("https://w3id.org/dpv#GovernmentalOrganisation",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#AuthorityInformed": {
            "label": "Authority Informed",
            "definition": "Status indicating Authority has been informed about the specified context",
            "broader": ("https://w3id.org/dpv#EntityInformed",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#AuthorityUninformed": {
            "label": "Authority Uninformed",
            "definition": "Status indicating Authority is uninformed i.e. has not been informed about the specified context",
            "broader": ("https://w3id.org/dpv#EntityUninformed",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#AutomatedDecisionMaking": {
            "label": "Automated Decision Making",
            "definition": "Processing that involves automated decision making",
            "broader": ("https://w3id.org/dpv#DecisionMaking",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#AutomatedScoringOfIndividuals": {
            "label": "Automated Scoring of Individuals",
            "definition": "Processing that involves automated scoring of individuals",
            "broader": ("https://w3id.org/dpv#ScoringOfIndividuals",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#AutomationLevel": {
            "label": "Automation Level",
            "definition": "Indication of degree or level of automation associated with specified context",
            "broader": ("https://w3id.org/dpv#ProcessingContext",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Autonomous": {
            "label": "Autonomous",
            "definition": "Level of automation corresponding to Level 6 in ISO/IEC 22989:2022 where the automation in system is capable of modifying its operation domain or its goals without external intervention, control or oversight",
            "broader": ("https://w3id.org/dpv#AutomationLevel",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#B2B2CContract": {
            "label": "Business-to-Business-to-Consumer Contract",
            "definition": "A contract between two businesses who partner together to provide services to a consumer",
            "broader": ("https://w3id.org/dpv#B2BContract", "https://w3id.org/dpv#B2CContract"),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#B2BContract": {
            "label": "Business-to-Business Contract",
            "definition": "A contract between two businesses",
            "broader": ("https://w3id.org/dpv#ContractByEntityType",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#B2CContract": {
            "label": "Business-to-Consumer Contract",
            "definition": "A contract between a business and a consumer where the business provides goods or services to the consumer",
            "broader": ("https://w3id.org/dpv#ContractByEntityType",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#BackgroundChecks": {
            "label": "Background Checks",
            "definition": "Procedure where the background of an entity is assessed to identity vulnerabilities and threats due to their current or intended role",
            "broader": ("https://w3id.org/dpv#SecurityProcedure",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#BiometricAuthentication": {
            "label": "Biometric Authentication",
            "definition": "Use of biometric data for authentication",
            "broader": ("https://w3id.org/dpv#AuthenticationProtocols",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#C2BContract": {
            "label": "Consumer-to-Business Contract",
            "definition": "A contract between a consumer and a business where the business purchases goods or services from the consumer",
            "broader": ("https://w3id.org/dpv#ContractByEntityType",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#C2CContract": {
            "label": "Consumer-to-Consumer Contract",
            "definition": "A contract between two consumers",
            "broader": ("https://w3id.org/dpv#ContractByEntityType",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#CannotChallengeProcess": {
            "label": "Cannot Challenge Process",
            "definition": "Involvement where entity cannot challenge the process of specified context",
            "broader": ("https://w3id.org/dpv#EntityNonPermissiveInvolvement",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#CannotChallengeProcessInput": {
            "label": "Cannot Challenge Process Input",
            "definition": "Involvement where entity cannot challenge input of specified context",
            "broader": ("https://w3id.org/dpv#EntityNonPermissiveInvolvement",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#CannotChallengeProcessOutput": {
            "label": "Cannot Challenge Process Output",
            "definition": "Involvement where entity cannot challenge the output of specified context",
            "broader": ("https://w3id.org/dpv#EntityNonPermissiveInvolvement",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#CannotCorrectProcess": {
            "label": "Cannot Correct Process",
            "definition": "Involvement where entity cannot correct the process of specified context",
            "broader": ("https://w3id.org/dpv#EntityNonPermissiveInvolvement",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#CannotCorrectProcessInput": {
            "label": "Cannot Correct Process Input",
            "definition": "Involvement where entity cannot correct input of specified context",
            "broader": ("https://w3id.org/dpv#EntityNonPermissiveInvolvement",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#CannotCorrectProcessOutput": {
            "label": "Cannot Correct Process Output",
            "definition": "Involvement where entity cannot correct the output of specified context",
            "broader": ("https://w3id.org/dpv#EntityNonPermissiveInvolvement",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#CannotObjectToProcess": {
            "label": "Cannot Object to Process",
            "definition": "Involvement where entity cannot object to process of specified context",
            "broader": ("https://w3id.org/dpv#EntityNonPermissiveInvolvement",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#CannotOptInToProcess": {
            "label": "Cannot Opt-in to Process",
            "definition": "Involvement where entity cannot opt-in to specified context",
            "broader": ("https://w3id.org/dpv#EntityNonPermissiveInvolvement",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#CannotOptOutFromProcess": {
            "label": "Cannot Opt-out from Process",
            "definition": "Involvement where entity cannot opt-out from specified context",
            "broader": ("https://w3id.org/dpv#EntityNonPermissiveInvolvement",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#CannotReverseProcessEffects": {
            "label": "Cannot Reverse Process Effects",
            "definition": "Involvement where entity cannot reverse effects of specified context",
            "broader": ("https://w3id.org/dpv#EntityNonPermissiveInvolvement",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#CannotReverseProcessInput": {
            "label": "Cannot Reverse Process Input",
            "definition": "Involvement where entity cannot reverse input of specified context",
            "broader": ("https://w3id.org/dpv#EntityNonPermissiveInvolvement",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#CannotReverseProcessOutput": {
            "label": "Cannot Reverse Process Output",
            "definition": "Involvement where entity cannot reverse output of specified context",
            "broader": ("https://w3id.org/dpv#EntityNonPermissiveInvolvement",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#CannotWithdrawFromProcess": {
            "label": "Cannot Withdraw from Process",
            "definition": "Involvement where entity cannot withdraw a previously given assent from specified context",
            "broader": ("https://w3id.org/dpv#EntityNonPermissiveInvolvement",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Certification": {
            "label": "Certification",
            "definition": "Certification mechanisms, seals, and marks for the purpose of demonstrating compliance",
            "broader": ("https://w3id.org/dpv#CertificationSeal",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#CertificationSeal": {
            "label": "Certification and Seal",
            "definition": "Certifications, seals, and marks indicating compliance to regulations or practices",
            "broader": ("https://w3id.org/dpv#OrganisationalMeasure",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ChallengingProcess": {
            "label": "Challenging Process",
            "definition": "Involvement where entity can challenge the process of specified context",
            "broader": ("https://w3id.org/dpv#EntityPermissiveInvolvement",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ChallengingProcessInput": {
            "label": "Challenging Process Input",
            "definition": "Involvement where entity can challenge input of specified context",
            "broader": ("https://w3id.org/dpv#EntityPermissiveInvolvement",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ChallengingProcessOutput": {
            "label": "Challenging Process Output",
            "definition": "Involvement where entity can challenge the output of specified context",
            "broader": ("https://w3id.org/dpv#EntityPermissiveInvolvement",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#CharityOrganisation": {
            "label": "Charity Organisation",
            "definition": "A nonprofit entity dedicated to providing assistance or raising funds for social, educational, religious, or other philanthropic purposes",
            "broader": ("https://w3id.org/dpv#LegalEntity",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Child": {
            "label": "Child",
            "definition": "A 'child' is a natural legal person who is below a certain legal age depending on the legal jurisdiction.",
            "broader": ("https://w3id.org/dpv#VulnerableHuman",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Citizen": {
            "label": "Citizen",
            "definition": "Humans that are citizens (for a jurisdiction)",
            "broader": ("https://w3id.org/dpv#HumanSubject",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#City": {
            "label": "City",
            "definition": "A region consisting of urban population and commerce",
            "broader": ("https://w3id.org/dpv#Region",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Client": {
            "label": "Client",
            "definition": "Humans that are clients or recipients of services",
            "broader": ("https://w3id.org/dpv#Customer",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Clinic": {
            "label": "Clinic",
            "definition": "An organisation that is a smaller healthcare facility offering outpatient medical services for diagnosis and treatment",
            "broader": ("https://w3id.org/dpv#Organisation",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#CloudLocation": {
            "label": "Cloud Location",
            "definition": "Location that is in the 'cloud' i.e. a logical location operated over the internet",
            "broader": ("https://w3id.org/dpv#RemoteLocation",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#CodeOfConduct": {
            "label": "Code of Conduct",
            "definition": "A set of rules or procedures outlining the norms and practices for conducting activities",
            "broader": ("https://w3id.org/dpv#GuidelinesPrinciple",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Collect": {
            "label": "Collect",
            "definition": "to gather data from someone",
            "broader": ("https://w3id.org/dpv#Obtain",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#CollectedData": {
            "label": "Collected Data",
            "definition": "Data that has been obtained by collecting it from a source",
            "broader": ("https://w3id.org/dpv#Data",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#CollectedPersonalData": {
            "label": "Collected Personal Data",
            "definition": "Personal Data that has been collected from another source such as the Data Subject",
            "broader": ("https://w3id.org/dpv#CollectedData", "https://w3id.org/dpv#PersonalData"),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#CombatClimateChange": {
            "label": "Combat Climate Change",
            "definition": "Purposes associated with combating the causes and consequences of climate change, including reducing gas emissions and fighting emergencies such as floods or wildfires",
            "broader": ("https://w3id.org/dpv#PublicBenefit",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Combine": {
            "label": "Combine",
            "definition": "to join or merge data",
            "broader": ("https://w3id.org/dpv#Transform",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#CommercialPurpose": {
            "label": "Commercial Purpose",
            "definition": "Purposes associated with processing activities performed in a commercial setting or with intention to commercialise",
            "broader": ("https://w3id.org/dpv#Purpose",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#CommercialResearch": {
            "label": "Commercial Research",
            "definition": "Purposes associated with conducting research in a commercial setting or with intention to commercialise e.g. in a company or sponsored by a company",
            "broader": ("https://w3id.org/dpv#CommercialPurpose", "https://w3id.org/dpv#ResearchAndDevelopment"),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#CommerciallyConfidentialData": {
            "label": "Commercially Confidential Data",
            "definition": "Data that is considered confidential due to business/trade secrets, confidentiality agreements, or company secrets",
            "broader": ("https://w3id.org/dpv#ConfidentialData",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#CommunicationForCustomerCare": {
            "label": "Communication for Customer Care",
            "definition": "Customer Care Communication refers to purposes associated with communicating with customers for assisting them, resolving issues, ensuring satisfaction, etc. in relation to services provided",
            "broader": ("https://w3id.org/dpv#CommunicationManagement", "https://w3id.org/dpv#CustomerCare"),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#CommunicationManagement": {
            "label": "Communication Management",
            "definition": "Communication Management refers to purposes associated with providing or managing communication activities e.g. to send an email for notifying some information",
            "broader": ("https://w3id.org/dpv#Purpose",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#CompatibilityUnknown": {
            "label": "Compatibility Unknown",
            "definition": "Status indicating the compatibility of the context with an earlier context is currently unknown",
            "broader": ("https://w3id.org/dpv#ReuseCompatibility",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ComplianceAssessment": {
            "label": "Compliance Assessment",
            "definition": "Assessment regarding compliance (e.g. internal policy, regulations)",
            "broader": ("https://w3id.org/dpv#Assessment",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ComplianceIndeterminate": {
            "label": "Compliance Indeterminate",
            "definition": "State where the status of compliance has not been fully assessed, evaluated, or determined",
            "broader": ("https://w3id.org/dpv#ComplianceStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ComplianceMonitoring": {
            "label": "Compliance Monitoring",
            "definition": "Monitoring of compliance (e.g. internal policy, regulations)",
            "broader": ("https://w3id.org/dpv#GovernanceProcedures",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ComplianceStatus": {
            "label": "Compliance Status",
            "definition": "Status associated with Compliance with some norms, objectives, or requirements",
            "broader": ("https://w3id.org/dpv#Status",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ComplianceUnknown": {
            "label": "Compliance Unknown",
            "definition": "State where the status of compliance is unknown",
            "broader": ("https://w3id.org/dpv#ComplianceStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ComplianceViolation": {
            "label": "Compliance Violation",
            "definition": "State where compliance cannot be achieved due to requirements being violated",
            "broader": ("https://w3id.org/dpv#ComplianceStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Compliant": {
            "label": "Compliant",
            "definition": "State of being fully compliant",
            "broader": ("https://w3id.org/dpv#ComplianceStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ConditionalAutomation": {
            "label": "Conditional Automation",
            "definition": "Level of automation corresponding to Level 3 in ISO/IEC 22989:2022 where the automation is sufficient to perform most tasks of the system with the human present to take over where necessary",
            "broader": ("https://w3id.org/dpv#AutomationLevel",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ConfidentialData": {
            "label": "Confidential Data",
            "definition": "Data deemed confidential",
            "broader": ("https://w3id.org/dpv#Data",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ConfidentialityAgreement": {
            "label": "Confidentiality Agreement",
            "definition": "Agreements that enforce confidentiality for e.g. to protect business, professional, or company secrets",
            "broader": ("https://w3id.org/dpv#LegalAgreement",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ConformanceAssessment": {
            "label": "Conformance Assessment",
            "definition": "Assessment regarding conformance with standards or norms or guidelines or similar instruments",
            "broader": ("https://w3id.org/dpv#Assessment",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ConformanceStatus": {
            "label": "Conformance Status",
            "definition": "Status associated with conformance to a standard, guideline, code, or recommendation",
            "broader": ("https://w3id.org/dpv#Status",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Conformant": {
            "label": "Conformant",
            "definition": "State of being conformant",
            "broader": ("https://w3id.org/dpv#ConformanceStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Consent": {
            "label": "Consent",
            "definition": "Consent of the Data Subject for specified process or activity",
            "broader": ("https://w3id.org/dpv#LegalBasis",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ConsentControl": {
            "label": "Consent Control",
            "definition": "The control or activity associated with obtaining, providing, withdrawing, or reaffirming consent",
            "broader": ("https://w3id.org/dpv#EntityInvolvement",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ConsentExpired": {
            "label": "Consent Expired",
            "definition": "The state where the temporal or contextual validity of consent has 'expired'",
            "broader": ("https://w3id.org/dpv#ConsentStatusInvalidForProcessing",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ConsentGiven": {
            "label": "Consent Given",
            "definition": "The state where consent has been given",
            "broader": ("https://w3id.org/dpv#ConsentStatusValidForProcessing",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ConsentInvalidated": {
            "label": "Consent Invalidated",
            "definition": "The state where consent has been deemed to be invalid",
            "broader": ("https://w3id.org/dpv#ConsentStatusInvalidForProcessing",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ConsentManagement": {
            "label": "Consent Management",
            "definition": "Methods to obtain, provide, modify, and withdraw consent along with maintaining a record of consent, retrieving records, and processing changes in consent states",
            "broader": ("https://w3id.org/dpv#PermissionManagement",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ConsentNotice": {
            "label": "Consent Notice",
            "definition": "A Notice for information provision associated with Consent",
            "broader": ("https://w3id.org/dpv#PrivacyNotice",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ConsentReceipt": {
            "label": "Consent Receipt",
            "definition": "A record of consent or consent related activities that is provided to another entity",
            "broader": ("https://w3id.org/dpv#ConsentRecord",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ConsentRecord": {
            "label": "Consent Record",
            "definition": "A Record of Consent or Consent related activities",
            "broader": ("https://w3id.org/dpv#DataProcessingRecord",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ConsentRefused": {
            "label": "Consent Refused",
            "definition": "The state where consent has been refused",
            "broader": ("https://w3id.org/dpv#ConsentStatusInvalidForProcessing",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ConsentRequestDeferred": {
            "label": "Consent Request Deferred",
            "definition": "State where a request for consent has been deferred without a decision",
            "broader": ("https://w3id.org/dpv#ConsentStatusInvalidForProcessing",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ConsentRequested": {
            "label": "Consent Requested",
            "definition": "State where a request for consent has been made and is awaiting a decision",
            "broader": ("https://w3id.org/dpv#ConsentStatusInvalidForProcessing",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ConsentRevoked": {
            "label": "Consent Revoked",
            "definition": "The state where the consent is revoked by an entity other than the data subject and which prevents it from being further used as a valid state",
            "broader": ("https://w3id.org/dpv#ConsentStatusInvalidForProcessing",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ConsentStatus": {
            "label": "Consent Status",
            "definition": "The state or status of 'consent' that provides information reflecting its operational status and validity for processing data",
            "broader": ("https://w3id.org/dpv#Status",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ConsentStatusInvalidForProcessing": {
            "label": "Consent Status Invalid for Processing",
            "definition": "States of consent that cannot be used as valid justifications for processing data",
            "broader": ("https://w3id.org/dpv#ConsentStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ConsentStatusValidForProcessing": {
            "label": "Consent Status Valid for Processing",
            "definition": "States of consent that can be used as valid justifications for processing data",
            "broader": ("https://w3id.org/dpv#ConsentStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ConsentUnknown": {
            "label": "Consent Unknown",
            "definition": "State where information about consent is not available or is unknown",
            "broader": ("https://w3id.org/dpv#ConsentStatusInvalidForProcessing",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ConsentWithdrawn": {
            "label": "Consent Withdrawn",
            "definition": "The state where the consent is withdrawn or revoked specifically by the data subject and which prevents it from being further used as a valid state",
            "broader": ("https://w3id.org/dpv#ConsentStatusInvalidForProcessing",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Consequence": {
            "label": "Consequence",
            "definition": "The consequence(s) possible or arising from specified context",
            "broader": ("https://w3id.org/dpv#RiskConcept",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ConsequenceAsSideEffect": {
            "label": "Consequence as Side-Effect",
            "definition": "The consequence(s) possible or arising as a side-effect of specified context",
            "broader": ("https://w3id.org/dpv#Consequence",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ConsequenceOfFailure": {
            "label": "Consequence of Failure",
            "definition": "The consequence(s) possible or arising from failure of specified context",
            "broader": ("https://w3id.org/dpv#Consequence",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ConsequenceOfSuccess": {
            "label": "Consequence of Success",
            "definition": "The consequence(s) possible or arising from success of specified context",
            "broader": ("https://w3id.org/dpv#Consequence",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Consult": {
            "label": "Consult",
            "definition": "to consult or query data",
            "broader": ("https://w3id.org/dpv#Use",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Consultation": {
            "label": "Consultation",
            "definition": "Consultation is a process of receiving feedback, advice, or opinion from an external agency",
            "broader": ("https://w3id.org/dpv#OrganisationalMeasure",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ConsultationWithAuthority": {
            "label": "Consultation with Authority",
            "definition": "Consultation with an authority or authoritative entity",
            "broader": ("https://w3id.org/dpv#Consultation",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ConsultationWithDPO": {
            "label": "Consultation with DPO",
            "definition": "Consultation with Data Protection Officer(s)",
            "broader": ("https://w3id.org/dpv#Consultation",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ConsultationWithDataSubject": {
            "label": "Consultation with Data Subject",
            "definition": "Consultation with data subject(s) or their representative(s)",
            "broader": ("https://w3id.org/dpv#Consultation",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ConsultationWithDataSubjectRepresentative": {
            "label": "Consultation with Data Subject Representative",
            "definition": "Consultation with representative of data subject(s)",
            "broader": ("https://w3id.org/dpv#ConsultationWithDataSubject",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Consumer": {
            "label": "Consumer",
            "definition": "Humans that consume goods or services for direct use",
            "broader": ("https://w3id.org/dpv#HumanSubject",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ConsumerStandardFormContract": {
            "label": "Consumer Standard Form Contract",
            "definition": "A contract where the terms and conditions are determined by parties in the role of a 'consumer' - whether an entity or an individual, and the other parties have negligible or no ability to negotiate the terms and conditions",
            "broader": ("https://w3id.org/dpv#StandardFormContract",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Context": {
            "label": "Context",
            "definition": "Contextually relevant information",
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ContextuallyAnonymisedData": {
            "label": "Contextually Anonymised Data",
            "definition": "Data that can be considered as being fully anonymised within the context but in actuality is not fully anonymised and is still personal data as it can be de-anonymised outside that context",
            "broader": ("https://w3id.org/dpv#PseudonymisedData",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ContinuousFrequency": {
            "label": "Continuous Frequency",
            "definition": "Frequency where occurrences are continuous",
            "broader": ("https://w3id.org/dpv#Frequency",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Contract": {
            "label": "Contract",
            "definition": "Creation, completion, fulfilment, or performance of a contract involving specified processing of data or technologies",
            "broader": ("https://w3id.org/dpv#LegalBasis",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ContractActivationStatus": {
            "label": "Contract Activation Status",
            "definition": "Status associated with activation of a contract i.e. whether its terms are active and are required to be performed",
            "broader": ("https://w3id.org/dpv#ContractStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ContractActive": {
            "label": "Contract Active",
            "definition": "Status representing contract that has been fully executed and whose terms are considered active i.e. they are applicable and are required to be performed",
            "broader": ("https://w3id.org/dpv#ContractActivationStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ContractAmended": {
            "label": "Contract Amended",
            "definition": "Status representing contract that has been fully executed and whose terms have been amended through mutual agreement or other means such that the contract is still required to be performed",
            "broader": ("https://w3id.org/dpv#ContractPerformanceStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ContractAmendmentClause": {
            "label": "Contract Amendment Clause",
            "definition": "A provision describing how changes or modifications to the contract can be made and the process for implementing them",
            "broader": ("https://w3id.org/dpv#ContractualClause",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ContractApproved": {
            "label": "Contract Approved",
            "definition": "Status representing contract has been approved and can be used for signing",
            "broader": ("https://w3id.org/dpv#ContractPreparationStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ContractBeingPerformed": {
            "label": "Contract Being Performed",
            "definition": "Status representing contract that has been fully executed and whose terms are being carried out i.e. the contract is being performed",
            "broader": ("https://w3id.org/dpv#ContractPerformanceStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ContractBreached": {
            "label": "Contract Breached",
            "definition": "Status representing contract being breached where its terms are not fulfilled or are violated with legal consequences",
            "broader": ("https://w3id.org/dpv#ContractTerminationStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ContractByDomain": {
            "label": "Contract by Domain",
            "definition": "A generic concept representing contracts categorised by specific domains which dictate the drafting and interpretation of contracts",
            "broader": ("https://w3id.org/dpv#Contract",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ContractByEntityType": {
            "label": "Contract by Entity Type",
            "definition": "A generic concept representing contracts categorised by the type of entities involved - such as Businesses (B), Consumers (C), and Governments (G)",
            "broader": ("https://w3id.org/dpv#Contract",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ContractByNegotiationType": {
            "label": "Contract by Negotiation Type",
            "definition": "A generic concept representing contracts categorised based on their use or absence of negotiation in the contract forming process",
            "broader": ("https://w3id.org/dpv#Contract",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ContractConfidentialityClause": {
            "label": "Contract Confidentiality Clause",
            "definition": "A provision requiring parties to keep certain information confidential and not disclose it to third parties",
            "broader": ("https://w3id.org/dpv#ContractualClause",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ContractControl": {
            "label": "Contract Control",
            "definition": "The control or activity associated with accepting, refusing, and other actions associated with a contract",
            "broader": ("https://w3id.org/dpv#EntityInvolvement",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ContractDefinitions": {
            "label": "Contract Definitions",
            "definition": "A section specifying the meanings of key terms and phrases used throughout the contract",
            "broader": ("https://w3id.org/dpv#ContractualClause",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ContractDisputeResolutionClause": {
            "label": "Contract DisputeResolution Clause",
            "definition": "A provision detailing the methods and procedures for resolving disagreements or conflicts arising from the contract",
            "broader": ("https://w3id.org/dpv#ContractualClause",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ContractDisputed": {
            "label": "Contract Disputed",
            "definition": "Status representing contract being disputed where one or more parties have an issue regarding the interpretation and performance of the contract",
            "broader": ("https://w3id.org/dpv#ContractTerminationStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ContractDrafted": {
            "label": "Contract Drafted",
            "definition": "Status representing the drafting of contract text has been completed and it can now be offered for signing",
            "broader": ("https://w3id.org/dpv#ContractPreparationStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ContractExecutionStatus": {
            "label": "Contract Execution Status",
            "definition": "Status associated with execution of a contract (i.e. signing and procedural aspects before the contract terms come in to effect)",
            "broader": ("https://w3id.org/dpv#ContractStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ContractExpired": {
            "label": "Contract Expired",
            "definition": "Status representing reaching the expiry defined in the contract, such as when the stated duration or the stated obligations have been completed",
            "broader": ("https://w3id.org/dpv#ContractTerminationStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ContractExtended": {
            "label": "Contract Extended",
            "definition": "Status representing the duration associated with a contract being extended through mutual agreement or by a party",
            "broader": ("https://w3id.org/dpv#ContractTerminationStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ContractFulfilled": {
            "label": "Contract Fulfilled",
            "definition": "Status representing contract where all its terms have been fulfilled in a manner that does not constitute a violation or breach of the contract",
            "broader": ("https://w3id.org/dpv#ContractFulfilmentStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ContractFulfilmentStatus": {
            "label": "Contract Fulfilment Status",
            "definition": "Status associated with fulfilment of a contract",
            "broader": ("https://w3id.org/dpv#ContractStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ContractFullyExecuted": {
            "label": "Contract Fully Executed",
            "definition": "Status representing contract has been fully executed i.e. it has been signed by all parties and all other procedural aspects such as exchange of signed contract copies have been completed",
            "broader": ("https://w3id.org/dpv#ContractExecutionStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ContractFullySigned": {
            "label": "Contract Fully Signed",
            "definition": "Status representing contract has been signed by all concerned parties",
            "broader": ("https://w3id.org/dpv#ContractExecutionStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ContractInactive": {
            "label": "Contract Inactive",
            "definition": "Status representing contract that has been fully executed and whose terms are not yet active i.e. they need to be performed at a later time",
            "broader": ("https://w3id.org/dpv#ContractActivationStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ContractJurisdictionClause": {
            "label": "Contract Jurisdiction Clause",
            "definition": "A provision specifying the legal jurisdiction or court where disputes related to the contract will be resolved",
            "broader": ("https://w3id.org/dpv#ContractualClause",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ContractNegotiated": {
            "label": "Contract Negotiated",
            "definition": "Status representing contract has been successfully negotiated by involved parties",
            "broader": ("https://w3id.org/dpv#ContractPreparationStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ContractNotFulfilled": {
            "label": "Contract Not Fulfilled",
            "definition": "Status representing contract where none of its terms have been fulfilled in a manner that does not constitute a violation or breach of the contract i.e. there is still time and opportunity to complete the terms",
            "broader": ("https://w3id.org/dpv#ContractFulfilmentStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ContractOffered": {
            "label": "Contract Offered",
            "definition": "Status representing contract has been offered to a party or to parties for reviewing and signing",
            "broader": ("https://w3id.org/dpv#ContractPreparationStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ContractPartiallyFulfilled": {
            "label": "Contract Partially Fulfilled",
            "definition": "Status representing contract where some of its terms have been fulfilled, and others are yet to be fulfilled in a manner that does not constitute a violation or breach of the contract i.e. there is still time and opportunity to complete the terms",
            "broader": ("https://w3id.org/dpv#ContractFulfilmentStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ContractPartiallySigned": {
            "label": "Contract Partially Signed",
            "definition": "Status representing contract has been partially signed by parties i.e. some parties have signed the contract and others are yet to make a decision to sign it",
            "broader": ("https://w3id.org/dpv#ContractExecutionStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ContractPerformance": {
            "label": "Contract Performance",
            "definition": "Fulfilment or performance of a contract involving specified processing of data or technologies",
            "broader": ("https://w3id.org/dpv#Contract",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ContractPerformanceStatus": {
            "label": "Contract Performance Status",
            "definition": "Status associated with performance of a contract",
            "broader": ("https://w3id.org/dpv#ContractStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ContractPreamble": {
            "label": "Contract Preamble",
            "definition": "An introductory section outlining the background, context, and purpose of the contract",
            "broader": ("https://w3id.org/dpv#ContractualClause",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ContractPreparationStatus": {
            "label": "Contract Preparation Status",
            "definition": "Status associated with preparation of contracts before they are signed or accepted or executed",
            "broader": ("https://w3id.org/dpv#ContractStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ContractRejected": {
            "label": "Contract Rejected",
            "definition": "Status representing contract has been rejected and cannot be used for signing",
            "broader": ("https://w3id.org/dpv#ContractPreparationStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ContractRenewed": {
            "label": "Contract Renewed",
            "definition": "Status representing contract being renewed with new duration and/or applicability where the contract has been fully executed in the past",
            "broader": ("https://w3id.org/dpv#ContractPerformanceStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ContractSignedByParty": {
            "label": "Contract Signed By Party",
            "definition": "Status representing contract has been signed by the indicated signing party",
            "broader": ("https://w3id.org/dpv#ContractExecutionStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ContractStatus": {
            "label": "Contract Status",
            "definition": "Status associated with a contract",
            "broader": ("https://w3id.org/dpv#Status",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ContractTemporarilySuspended": {
            "label": "Contract Temporarily Suspended",
            "definition": "Status representing contract that has been temporarily suspended through mutual agreement or by some parties",
            "broader": ("https://w3id.org/dpv#ContractPerformanceStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ContractTerminated": {
            "label": "Contract Terminated",
            "definition": "Status representing contract being terminated by one or more parties",
            "broader": ("https://w3id.org/dpv#ContractTerminationStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ContractTerminationClause": {
            "label": "Contract Termination Clause",
            "definition": "A provision outlining the conditions under which the contract can be terminated before its completion, including any penalties or obligations",
            "broader": ("https://w3id.org/dpv#ContractualClause",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ContractTerminationStatus": {
            "label": "Contract Termination Status",
            "definition": "Status associated with termination of a contract",
            "broader": ("https://w3id.org/dpv#ContractStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ContractUnderNegotiation": {
            "label": "Contract Under Negotiation",
            "definition": "Status representing contract is under negotiation between parties",
            "broader": ("https://w3id.org/dpv#ContractPreparationStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ContractUnderReview": {
            "label": "Contract Under Review",
            "definition": "Status representing contract is under review and is being considered for signing",
            "broader": ("https://w3id.org/dpv#ContractPreparationStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ContractViolated": {
            "label": "Contract Violated",
            "definition": "Status representing contract where one or more terms have not been fulfilled or have been fulfilled, where either is considered a violation of the terms",
            "broader": ("https://w3id.org/dpv#ContractFulfilmentStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ContractualClause": {
            "label": "Contractual Clause",
            "definition": "A part or component within a contract that outlines its specifics",
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ContractualClauseFulfilled": {
            "label": "Contractual Clause Fulfilled",
            "definition": "Status indicating the terms of the contractual clause are fulfilled i.e. they have been successfully completed without violation",
            "broader": ("https://w3id.org/dpv#ContractualClauseFulfilmentStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ContractualClauseFulfilmentStatus": {
            "label": "Contractual Clause Fulfilment Status",
            "definition": "Status associated with fulfilment of a contractual clause",
            "broader": ("https://w3id.org/dpv#ContractStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ContractualClauseNotFulfilled": {
            "label": "Contractual Clause Unfulfilled",
            "definition": "Status indicating the terms of the contractual clause have not yet been fulfilled in a manner that does not constitute a violation i.e. there is still an opportunity to complete them",
            "broader": ("https://w3id.org/dpv#ContractualClauseFulfilmentStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ContractualClausePartiallyFulfilled": {
            "label": "Contractual Clause Partially Fulfilled",
            "definition": "Status indicating some of the terms of the contractual clause have been fulfilled, and others have not yet been fulfilled in a manner that does not constitute a violation i.e. there is still an opportunity to complete them",
            "broader": ("https://w3id.org/dpv#ContractualClauseFulfilmentStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ContractualClauseViolated": {
            "label": "Contractual Clause Breached",
            "definition": "Status indicating the terms of the contractual clause have been violated",
            "broader": ("https://w3id.org/dpv#ContractualClauseFulfilmentStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ContractualTerms": {
            "label": "Contractual Terms",
            "definition": "Contractual terms governing data handling within or with an entity",
            "broader": ("https://w3id.org/dpv#LegalMeasure",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ControllerDataSubjectAgreement": {
            "label": "Controller-Data Subject Agreement",
            "definition": "An agreement outlining conditions, criteria, obligations, responsibilities, and specifics for carrying out processing of data between a Data Controller and a Data Subject",
            "broader": ("https://w3id.org/dpv#DataSubjectContract",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ControllerInformed": {
            "label": "Controller Informed",
            "definition": "Status indicating Controller has been informed about the specified context",
            "broader": ("https://w3id.org/dpv#EntityInformed",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ControllerProcessorAgreement": {
            "label": "Controller-Processor Agreement",
            "definition": "An agreement outlining conditions, criteria, obligations, responsibilities, and specifics for carrying out processing of data between a Data Controller and a Data Processor",
            "broader": ("https://w3id.org/dpv#DataProcessorContract",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ControllerUninformed": {
            "label": "Controller Uninformed",
            "definition": "Status indicating Controller is uninformed i.e. has not been informed about the specified context",
            "broader": ("https://w3id.org/dpv#EntityUninformed",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Copy": {
            "label": "Copy",
            "definition": "to produce an exact reproduction of the data",
            "broader": ("https://w3id.org/dpv#Processing",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#CorrectingProcess": {
            "label": "Correcting Process",
            "definition": "Involvement where entity can correct the process of specified context",
            "broader": ("https://w3id.org/dpv#EntityPermissiveInvolvement",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#CorrectingProcessInput": {
            "label": "Correcting Process Input",
            "definition": "Involvement where entity can correct input of specified context",
            "broader": ("https://w3id.org/dpv#EntityPermissiveInvolvement",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#CorrectingProcessOutput": {
            "label": "Correcting Process Output",
            "definition": "Involvement where entity can correct the output of specified context",
            "broader": ("https://w3id.org/dpv#EntityPermissiveInvolvement",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#CounterMoneyLaundering": {
            "label": "Counter Money Laundering",
            "definition": "Purposes associated with detection, prevention, and mitigation of mitigate money laundering",
            "broader": ("https://w3id.org/dpv#FraudPreventionAndDetection",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Counterterrorism": {
            "label": "Counterterrorism",
            "definition": "Purposes associated with activities that detect, prevent, mitigate, or otherwise perform activities to combat or eliminate terrorism (also referred to as anti-terrorism)",
            "broader": ("https://w3id.org/dpv#PublicBenefit",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Country": {
            "label": "Country",
            "definition": "A political entity indicative of a sovereign or non-sovereign territorial state comprising of distinct geographical areas",
            "broader": ("https://w3id.org/dpv#Jurisdiction",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#CredentialManagement": {
            "label": "Credential Management",
            "definition": "Management of credentials and their use in authorisations",
            "broader": ("https://w3id.org/dpv#AuthorisationProcedure",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#CrossBorderTransfer": {
            "label": "Cross-Border Transfer",
            "definition": "to move data from one jurisdiction (border) to another",
            "broader": ("https://w3id.org/dpv#Transfer",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#CryptographicAuthentication": {
            "label": "Cryptographic Authentication",
            "definition": "Use of cryptography for authentication",
            "broader": ("https://w3id.org/dpv#AuthenticationProtocols", "https://w3id.org/dpv#CryptographicMethods"),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#CryptographicKeyManagement": {
            "label": "Cryptographic Key Management",
            "definition": "Management of cryptographic keys, including their generation, storage, assessment, and safekeeping",
            "broader": ("https://w3id.org/dpv#CryptographicMethods",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#CryptographicMethods": {
            "label": "Cryptographic Methods",
            "definition": "Use of cryptographic methods to perform tasks",
            "broader": ("https://w3id.org/dpv#TechnicalMeasure",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Customer": {
            "label": "Customer",
            "definition": "Humans that purchase goods or services",
            "broader": ("https://w3id.org/dpv#HumanSubject",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#CustomerCare": {
            "label": "Customer Care",
            "definition": "Customer Care refers to purposes associated with purposes for providing assistance, resolving issues, ensuring satisfaction, etc. in relation to services provided",
            "broader": ("https://w3id.org/dpv#CustomerManagement",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#CustomerClaimsManagement": {
            "label": "Customer Claims Management",
            "definition": "Customer Claims Management refers to purposes associated with managing claims, including repayment of monies owed",
            "broader": ("https://w3id.org/dpv#CustomerManagement",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#CustomerManagement": {
            "label": "Customer Management",
            "definition": "Customer Management refers to purposes associated with managing activities related with past, current, and future customers",
            "broader": ("https://w3id.org/dpv#Purpose",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#CustomerOrderManagement": {
            "label": "Customer Order Management",
            "definition": "Customer Order Management refers to purposes associated with managing customer orders i.e. processing of an order related to customer's purchase of good or services",
            "broader": ("https://w3id.org/dpv#CustomerManagement",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#CustomerRelationshipManagement": {
            "label": "Customer Relationship Management",
            "definition": "Customer Relationship Management refers to purposes associated with managing and analysing interactions with past, current, and potential customers",
            "broader": ("https://w3id.org/dpv#CustomerManagement",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#CustomerSolvencyMonitoring": {
            "label": "Customer Solvency Monitoring",
            "definition": "Customer Solvency Monitoring refers to purposes associated with monitor solvency of customers for financial diligence",
            "broader": ("https://w3id.org/dpv#CustomerManagement",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#CybersecurityAssessment": {
            "label": "Cybersecurity Assessment",
            "definition": "Assessment of cybersecurity capabilities in terms of vulnerabilities and effectiveness of controls",
            "broader": ("https://w3id.org/dpv#SecurityAssessment",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#CybersecurityTraining": {
            "label": "Cybersecurity Training",
            "definition": "Training methods related to cybersecurity",
            "broader": ("https://w3id.org/dpv#StaffTraining",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#DPIA": {
            "label": "Data Protection Impact Assessment (DPIA)",
            "definition": "Impact assessment determining the potential and actual impact of processing activities on individuals or groups of individuals and taking into account the impacts of activities on their rights and freedoms",
            "broader": ("https://w3id.org/dpv#RightsImpactAssessment",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#DashboardNotice": {
            "label": "Dashboard Notice",
            "definition": "A notice that is provided within a dashboard also used for other purposes",
            "broader": ("https://w3id.org/dpv#Notice",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Data": {
            "label": "Data",
            "definition": "A broad concept representing 'data' or 'information'",
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#DataAltruism": {
            "label": "Data Altruism",
            "definition": "Purposes associated with the voluntary sharing of data for the general interest of the public, such as healthcare or combating climate change",
            "broader": ("https://w3id.org/dpv#PublicBenefit",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#DataAvailabilityAssessment": {
            "label": "Data Availability Assessment",
            "definition": "Measures associated with assessment of availability of data for specific task(s)",
            "broader": ("https://w3id.org/dpv#DataGovernance",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#DataBackupProtocols": {
            "label": "Data Backup Protocols",
            "definition": "Protocols or plans for backing up of data",
            "broader": ("https://w3id.org/dpv#TechnicalMeasure",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#DataBreachImpactAssessment": {
            "label": "Data Breach Impact Assessment (DBIA)",
            "definition": "Impact Assessment concerning the consequences and impacts of a data breach",
            "broader": ("https://w3id.org/dpv#RightsImpactAssessment",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#DataBreachNotice": {
            "label": "Data Breach Notice",
            "definition": "A notice providing information about data breach(es) i.e. unauthorised transfer, access, use, or modification of data",
            "broader": ("https://w3id.org/dpv#SecurityIncidentNotice",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#DataBreachNotification": {
            "label": "Data Breach Notification",
            "definition": "Notification of information about data breach(es) i.e. unauthorised transfer, access, use, or modification of data",
            "broader": ("https://w3id.org/dpv#SecurityIncidentNotification",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#DataBreachRecord": {
            "label": "Data Breach Record",
            "definition": "Record of a data breach incident",
            "broader": ("https://w3id.org/dpv#RecordsOfActivities",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#DataController": {
            "label": "Data Controller",
            "definition": "The individual or organisation that decides (or controls) the purpose(s) of processing personal data.",
            "broader": ("https://w3id.org/dpv#LegalEntity",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#DataControllerContract": {
            "label": "Data Controller Contract",
            "definition": "Creation, completion, fulfilment, or performance of a contract, with Data Controllers as parties being Joint Data Controllers, and involving specified processing of data or technologies. NOTE: This concept is being deprecated - use dpv:JointDataControllersAgreement which has a more explicit defin...",
            "broader": ("https://w3id.org/dpv#DataProcessingAgreement",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#DataControllerDataSource": {
            "label": "Data Controller as Data Source",
            "definition": "Data Sourced from Data Controller(s), e.g. a Controller inferring data or generating data",
            "broader": ("https://w3id.org/dpv#DataSource",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#DataDeletionPolicy": {
            "label": "Data Deletion Policy",
            "definition": "Policy regarding deletion of data",
            "broader": ("https://w3id.org/dpv#DataProcessingPolicy",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#DataErasurePolicy": {
            "label": "Data Erasure Policy",
            "definition": "Policy regarding erasure of data",
            "broader": ("https://w3id.org/dpv#DataProcessingPolicy",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#DataExporter": {
            "label": "Data Exporter",
            "definition": "An entity that 'exports' data where exporting is considered a form of data transfer",
            "broader": ("https://w3id.org/dpv#LegalEntity",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#DataGovernance": {
            "label": "Data Governance",
            "definition": "Measures associated with topics typically considered to be part of 'Data Governance'",
            "broader": ("https://w3id.org/dpv#OrganisationGovernance",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#DataHandlingClause": {
            "label": "Data Handling Clause",
            "definition": "Contractual clauses governing handling of data within or by an entity",
            "broader": ("https://w3id.org/dpv#ContractualTerms",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#DataImporter": {
            "label": "Data Importer",
            "definition": "An entity that 'imports' data where importing is considered a form of data transfer",
            "broader": ("https://w3id.org/dpv#Recipient",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#DataInteroperabilityAssessment": {
            "label": "Data Interoperability Assessment",
            "definition": "Measures associated with assessment of data interoperability",
            "broader": ("https://w3id.org/dpv#Assessment", "https://w3id.org/dpv#DataInteroperabilityManagement"),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#DataInteroperabilityImprovement": {
            "label": "Data Interoperability Improvement",
            "definition": "Measures associated with improvement of data interoperability",
            "broader": ("https://w3id.org/dpv#DataInteroperabilityManagement",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#DataInteroperabilityManagement": {
            "label": "Data Interoperability Management",
            "definition": "Measures associated with management of data interoperability",
            "broader": ("https://w3id.org/dpv#DataGovernance",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#DataInventoryManagement": {
            "label": "Data Inventory Management",
            "definition": "Measures associated with management of data inventory or a data asset list",
            "broader": ("https://w3id.org/dpv#DataGovernance",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#DataJurisdictionPolicy": {
            "label": "Data Jurisdiction Policy",
            "definition": "Policy specifying jurisdictional requirements for data processing",
            "broader": ("https://w3id.org/dpv#DataProcessingPolicy",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#DataLiteracy": {
            "label": "Data Literacy",
            "definition": "Providing skills, knowledge, and understanding to enable reading, writing, analysing, reasoning, and communicating regarding data",
            "broader": ("https://w3id.org/dpv#DigitalLiteracy",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#DataProcessingAgreement": {
            "label": "Data Processing Agreement",
            "definition": "An agreement outlining conditions, criteria, obligations, responsibilities, and specifics for carrying out processing of data",
            "broader": ("https://w3id.org/dpv#Contract",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#DataProcessingPolicy": {
            "label": "Data Processing Policy",
            "definition": "Policy regarding data processing activities",
            "broader": ("https://w3id.org/dpv#Policy",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#DataProcessingRecord": {
            "label": "Data Processing Record",
            "definition": "Record of data processing, whether ex-ante or ex-post",
            "broader": ("https://w3id.org/dpv#RecordsOfActivities",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#DataProcessor": {
            "label": "Data Processor",
            "definition": "A ‘processor’ means a natural or legal person, public authority, agency or other body which processes data on behalf of the controller.",
            "broader": ("https://w3id.org/dpv#Recipient",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#DataProcessorContract": {
            "label": "Data Processor Contract",
            "definition": "Creation, completion, fulfilment, or performance of a contract, with the Data Controller and Data Processor as parties, and involving specified processing of data or technologies. NOTE: This concept is being deprecated - use dpv:ControllerProcessorAgreement which has a more explicit definition of...",
            "broader": ("https://w3id.org/dpv#DataProcessingAgreement",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#DataProtectionAuthority": {
            "label": "Data Protection Authority",
            "definition": "An authority tasked with overseeing legal compliance regarding privacy and data protection laws.",
            "broader": ("https://w3id.org/dpv#Authority",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#DataProtectionOfficer": {
            "label": "Data Protection Officer",
            "definition": "An entity within or authorised by an organisation to monitor internal compliance, inform and advise on data protection obligations and act as a contact point for data subjects and the supervisory authority.",
            "broader": ("https://w3id.org/dpv#Representative",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#DataProtectionTraining": {
            "label": "Data Protection Training",
            "definition": "Training intended to increase knowledge regarding data protection",
            "broader": ("https://w3id.org/dpv#StaffTraining",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#DataPublishedByDataSubject": {
            "label": "Data published by Data Subject",
            "definition": "Data is published by the data subject",
            "broader": ("https://w3id.org/dpv#DataSubjectDataSource",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#DataQualityAssessment": {
            "label": "Data Quality Assessment",
            "definition": "Measures associated with assessment of data quality",
            "broader": ("https://w3id.org/dpv#Assessment", "https://w3id.org/dpv#DataQualityManagement"),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#DataQualityImprovement": {
            "label": "Data Quality Improvement",
            "definition": "Measures associated with improvement of data quality",
            "broader": ("https://w3id.org/dpv#DataQualityManagement",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#DataQualityManagement": {
            "label": "Data Quality Management",
            "definition": "Measures associated with management of data quality",
            "broader": ("https://w3id.org/dpv#DataGovernance",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#DataRedaction": {
            "label": "Data Redaction",
            "definition": "Removal of sensitive information from a data or document",
            "broader": ("https://w3id.org/dpv#DataSanitisationTechnique",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#DataRestorationPolicy": {
            "label": "Data Restoration Policy",
            "definition": "Policy regarding restoration of data",
            "broader": ("https://w3id.org/dpv#DataProcessingPolicy",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#DataReusePolicy": {
            "label": "Data Reuse Policy",
            "definition": "Policy regarding reuse of data i.e. using data for purposes other than its initial purpose",
            "broader": ("https://w3id.org/dpv#DataProcessingPolicy",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#DataSanitisationTechnique": {
            "label": "Data Sanitisation Technique",
            "definition": "Cleaning or any removal or re-organisation of elements in data based on selective criteria",
            "broader": ("https://w3id.org/dpv#TechnicalMeasure",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#DataSecurityManagement": {
            "label": "Data Security Management",
            "definition": "Measures associated with management of data security",
            "broader": ("https://w3id.org/dpv#DataGovernance", "https://w3id.org/dpv#SecurityProcedure"),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#DataSource": {
            "label": "Data Source",
            "definition": "The source or origin of data",
            "broader": ("https://w3id.org/dpv#ProcessingContext",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#DataStoragePolicy": {
            "label": "Data Storage Policy",
            "definition": "Policy regarding storage of data, including the manner, duration, location, and conditions for storage",
            "broader": ("https://w3id.org/dpv#DataProcessingPolicy",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#DataSubProcessor": {
            "label": "Data Sub-Processor",
            "definition": "A 'sub-processor' is a processor engaged by another processor",
            "broader": ("https://w3id.org/dpv#DataProcessor",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#DataSubject": {
            "label": "Data Subject",
            "definition": "The individual (or category of individuals) whose personal data is being processed",
            "broader": ("https://w3id.org/dpv#HumanSubject",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#DataSubjectContract": {
            "label": "Data Subject Contract",
            "definition": "Creation, completion, fulfilment, or performance of a contract, with the Data Controller and Data Subject as parties, and involving specified processing of data or technologies. NOTE: This concept is being deprecated - use dpv:ControllerDataSubjectAgreement which has a more explicit definition of...",
            "broader": ("https://w3id.org/dpv#DataProcessingAgreement",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#DataSubjectDataSource": {
            "label": "Data Subject as Data Source",
            "definition": "Data Sourced from Data Subject(s), e.g. when data is collected via a form or observed from their activities",
            "broader": ("https://w3id.org/dpv#DataSource",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#DataSubjectInformed": {
            "label": "Data Subject Informed",
            "definition": "Status indicating DataSubject has been informed about the specified context",
            "broader": ("https://w3id.org/dpv#EntityInformed",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#DataSubjectRight": {
            "label": "Data Subject Right",
            "definition": "The rights applicable or provided to a Data Subject",
            "broader": ("https://w3id.org/dpv#Right",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#DataSubjectRightsManagement": {
            "label": "Data Subject Rights Management",
            "definition": "Methods to provide, implement, and exercise data subjects' rights",
            "broader": ("https://w3id.org/dpv#RightsManagement",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#DataSubjectScale": {
            "label": "Data Subject Scale",
            "definition": "Scale of Data Subject(s)",
            "broader": ("https://w3id.org/dpv#Scale",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#DataSubjectUninformed": {
            "label": "Data Subject Uninformed",
            "definition": "Status indicating DataSubject is uninformed i.e. has not been informed about the specified context",
            "broader": ("https://w3id.org/dpv#EntityUninformed",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#DataSuitabilityAssessment": {
            "label": "Data Suitability Assessment",
            "definition": "Measures associated with assessment of suitability of data for specific task(s)",
            "broader": ("https://w3id.org/dpv#DataQualityAssessment",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#DataTransferImpactAssessment": {
            "label": "Data Transfer Impact Assessment",
            "definition": "Impact Assessment for conducting data transfers",
            "broader": ("https://w3id.org/dpv#ImpactAssessment",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#DataTransferLegalBasis": {
            "label": "Data Transfer Legal Basis",
            "definition": "Specific or special categories and instances of legal basis intended for justifying data transfers",
            "broader": ("https://w3id.org/dpv#LegalBasis",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#DataTransferNotice": {
            "label": "Data Transfer Notice",
            "definition": "Notice for the legal entity for the transfer of its data",
            "broader": ("https://w3id.org/dpv#Notice",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#DataTransferRecord": {
            "label": "Data Transfer Record",
            "definition": "Record of data transfer activities",
            "broader": ("https://w3id.org/dpv#DataProcessingRecord",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#DataVolume": {
            "label": "Data Volume",
            "definition": "Volume or Scale of Data",
            "broader": ("https://w3id.org/dpv#Scale",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#DecentralisedLocations": {
            "label": "Decentralised Locations",
            "definition": "Location that is spread across multiple separate areas with no distinction between their importance",
            "broader": ("https://w3id.org/dpv#LocationFixture",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#DecisionMaking": {
            "label": "Decision Making",
            "definition": "Processing that involves decision making",
            "broader": ("https://w3id.org/dpv#ProcessingContext",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Deidentification": {
            "label": "De-Identification",
            "definition": "Removal of identity or information to reduce identifiability",
            "broader": ("https://w3id.org/dpv#DataSanitisationTechnique",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Delete": {
            "label": "Delete",
            "definition": "to remove data in a logical fashion i.e. with the possibility of retrieval",
            "broader": ("https://w3id.org/dpv#Remove",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#DeliveryOfGoods": {
            "label": "Delivery of Goods",
            "definition": "Purposes associated with delivering goods and services requested or asked by consumer",
            "broader": ("https://w3id.org/dpv#RequestedServiceProvision",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Derive": {
            "label": "Derive",
            "definition": "to create new derivative data from the original data",
            "broader": ("https://w3id.org/dpv#Obtain",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#DerivedData": {
            "label": "Derived Data",
            "definition": "Data that has been obtained through derivations of other data",
            "broader": ("https://w3id.org/dpv#Data",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#DerivedPersonalData": {
            "label": "Derived Personal Data",
            "definition": "Personal Data that is obtained or derived from other data",
            "broader": ("https://w3id.org/dpv#DerivedData", "https://w3id.org/dpv#PersonalData"),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#DesignStandard": {
            "label": "Design Standard",
            "definition": "A set of rules or guidelines outlining criterias for design",
            "broader": ("https://w3id.org/dpv#Standard",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Destruct": {
            "label": "Destruct",
            "definition": "to process data in a way it no longer exists or cannot be repaired",
            "broader": ("https://w3id.org/dpv#Remove",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#DeterministicPseudonymisation": {
            "label": "Deterministic Pseudonymisation",
            "definition": "Pseudonymisation achieved through a deterministic function",
            "broader": ("https://w3id.org/dpv#Pseudonymisation",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Deterrence": {
            "label": "Deterrence",
            "definition": "A rule describing a deterrence for performing an activity",
            "broader": ("https://w3id.org/dpv#UnacceptableRule",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#DeterrenceFollowed": {
            "label": "Deterrence Followed",
            "definition": "Status indicating a deterrence has been followed i.e. the activity stated as being deterred has not been carried out",
            "broader": ("https://w3id.org/dpv#RuleFulfilled",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#DeterrenceNotFollowed": {
            "label": "Deterrence Not Followed",
            "definition": "Status indicating a deterrence has not been followed i.e. the activity stated as being deterred has been carried out",
            "broader": ("https://w3id.org/dpv#RuleUnfulfilled",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#DeviceNotice": {
            "label": "Device Notice",
            "definition": "A notice provided using the functionality provided by a device e.g. using the popup or alert feature",
            "broader": ("https://w3id.org/dpv#Notice",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#DifferentialPrivacy": {
            "label": "Differential Privacy",
            "definition": "Utilisation of differential privacy where information is shared as patterns or groups to withhold individual elements",
            "broader": ("https://w3id.org/dpv#CryptographicMethods",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#DigitalLiteracy": {
            "label": "Digital Literacy",
            "definition": "Providing skills, knowledge, and understanding to enable reading, writing, analysing, reasoning, and communicating regarding digital technologies and their implications",
            "broader": ("https://w3id.org/dpv#OrganisationalMeasure",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#DigitalRightsManagement": {
            "label": "Digital Rights Management",
            "definition": "Management of access, use, and other operations associated with digital content",
            "broader": ("https://w3id.org/dpv#TechnicalMeasure",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#DigitalSignatures": {
            "label": "Digital Signatures",
            "definition": "Expression and authentication of identity through digital information containing cryptographic signatures",
            "broader": ("https://w3id.org/dpv#CryptographicMethods",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#DirectMarketing": {
            "label": "Direct Marketing",
            "definition": "Purposes associated with conducting direct marketing i.e. marketing communicated directly to the individual",
            "broader": ("https://w3id.org/dpv#Marketing",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#DisasterRecoveryProcedures": {
            "label": "Disaster Recovery Procedures",
            "definition": "Procedures related to management of disasters and recovery",
            "broader": ("https://w3id.org/dpv#GovernanceProcedures",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Disclose": {
            "label": "Disclose",
            "definition": "to make data known",
            "broader": ("https://w3id.org/dpv#Processing",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#DiscloseByTransmission": {
            "label": "Disclose by Transmission",
            "definition": "to disclose data by means of transmission",
            "broader": ("https://w3id.org/dpv#Disclose",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Display": {
            "label": "Display",
            "definition": "to present or show data",
            "broader": ("https://w3id.org/dpv#Disclose",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#DisputeManagement": {
            "label": "Dispute Management",
            "definition": "Purposes associated with activities that manage disputes by natural persons, private bodies, or public authorities relevant to organisation",
            "broader": ("https://w3id.org/dpv#OrganisationGovernance",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Disseminate": {
            "label": "Disseminate",
            "definition": "to spread data throughout",
            "broader": ("https://w3id.org/dpv#Disclose",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#DistributedSystemSecurity": {
            "label": "Distributed System Security",
            "definition": "Security implementations provided using or over a distributed system",
            "broader": ("https://w3id.org/dpv#SecurityMethod",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#DistributionAgreement": {
            "label": "Distribution Agreement",
            "definition": "A contract regarding supply of data or technologies between a distributor and a supplier",
            "broader": ("https://w3id.org/dpv#ContractByDomain",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#DocumentRandomisedPseudonymisation": {
            "label": "Document Randomised Pseudonymisation",
            "definition": "Use of randomised pseudonymisation where the same elements are assigned different values in the same document or database",
            "broader": ("https://w3id.org/dpv#Pseudonymisation",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#DocumentSecurity": {
            "label": "Document Security",
            "definition": "Security measures enacted over documents to protect against tampering or restrict access",
            "broader": ("https://w3id.org/dpv#SecurityMethod",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Download": {
            "label": "Download",
            "definition": "to provide a copy or to receive a copy of data over a network or internet",
            "broader": ("https://w3id.org/dpv#Disclose",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Duration": {
            "label": "Duration",
            "definition": "The duration or temporal limitation",
            "broader": ("https://w3id.org/dpv#Context",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#EULA": {
            "label": "End User License Agreement (EULA)",
            "definition": "End User License Agreement is a contract entered into between a software (or service) developer or provider with the (end-)user",
            "broader": ("https://w3id.org/dpv#LicenseAgreement",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#EconomicUnion": {
            "label": "Economic Union",
            "definition": "A political union of two or more countries based on economic or trade agreements",
            "broader": ("https://w3id.org/dpv#Jurisdiction",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#EducationalOrganisation": {
            "label": "Educational Organisation",
            "definition": "An organisation focused on delivering formal or informal education, training, or research",
            "broader": ("https://w3id.org/dpv#Organisation",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#EducationalTraining": {
            "label": "Educational Training",
            "definition": "Training methods that are intended to provide education on topic(s)",
            "broader": ("https://w3id.org/dpv#StaffTraining",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#EffectivenessDeterminationProcedures": {
            "label": "Effectiveness Determination Procedures",
            "definition": "Procedures intended to determine effectiveness of other measures",
            "broader": ("https://w3id.org/dpv#Assessment",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ElderlyDataSubject": {
            "label": "Elderly Data Subject",
            "definition": "Data subjects that are considered elderly (i.e. based on age)",
            "broader": ("https://w3id.org/dpv#VulnerableDataSubject",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ElderlyHuman": {
            "label": "Elderly Human",
            "definition": "Humans that are considered elderly (i.e. based on age)",
            "broader": ("https://w3id.org/dpv#VulnerableHuman",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#EmergencyHealthcareProvider": {
            "label": "Emergency Healthcare Provider",
            "definition": "An organisation that is an emergency service provider focused on delivering immediate medical care to patients in critical or life-threatening situations",
            "broader": ("https://w3id.org/dpv#EmergencyServiceProvider",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#EmergencyServiceProvider": {
            "label": "Emergency Service Provider",
            "definition": "An organisation tasked with providing emergency services such as by responding rapidly to urgent situations to protect lives, property, and the environment",
            "broader": ("https://w3id.org/dpv#Organisation",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Employee": {
            "label": "Employee",
            "definition": "Humans that are employees",
            "broader": ("https://w3id.org/dpv#HumanSubject",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#EmploymentContract": {
            "label": "Employment Contract",
            "definition": "A contract regarding employment between an employer and an employee",
            "broader": ("https://w3id.org/dpv#ContractByDomain",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Encryption": {
            "label": "Encryption",
            "definition": "Technical measures consisting of encryption",
            "broader": ("https://w3id.org/dpv#TechnicalMeasure",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#EncryptionAtRest": {
            "label": "Encryption at Rest",
            "definition": "Encryption of data when being stored (persistent encryption)",
            "broader": ("https://w3id.org/dpv#Encryption",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#EncryptionInTransfer": {
            "label": "Encryption in Transfer",
            "definition": "Encryption of data in transit e.g. when being transferred from one location to another, including sharing",
            "broader": ("https://w3id.org/dpv#Encryption",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#EncryptionInUse": {
            "label": "Encryption in Use",
            "definition": "Encryption of data when it is being used",
            "broader": ("https://w3id.org/dpv#Encryption",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#EndToEndEncryption": {
            "label": "End-to-End Encryption (E2EE)",
            "definition": "Encrypted communications where data is encrypted by the sender and decrypted by the intended receiver to prevent access to any third party",
            "broader": ("https://w3id.org/dpv#Encryption",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#EndlessDuration": {
            "label": "Endless Duration",
            "definition": "Duration that is (known or intended to be) open ended or without an end",
            "broader": ("https://w3id.org/dpv#Duration",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#EnforceAccessControl": {
            "label": "Enforce Access Control",
            "definition": "Purposes associated with conducting or enforcing access control as a form of security",
            "broader": ("https://w3id.org/dpv#EnforceSecurity",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#EnforceSecurity": {
            "label": "Enforce Security",
            "definition": "Purposes associated with ensuring and enforcing security for data, personnel, or other related matters",
            "broader": ("https://w3id.org/dpv#Purpose",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#EnterIntoContract": {
            "label": "Enter Into Contract",
            "definition": "Processing necessary to enter into contract",
            "broader": ("https://w3id.org/dpv#Contract",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Entity": {
            "label": "Entity",
            "definition": "A human or non-human 'thing' that constitutes as an entity",
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#EntityActiveInvolvement": {
            "label": "Entity Active Involvement",
            "definition": "Involvement where entity is 'actively' involved",
            "broader": ("https://w3id.org/dpv#EntityInvolvement",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#EntityInformed": {
            "label": "Entity Informed",
            "definition": "Status indicating entity has been informed about specified context",
            "broader": ("https://w3id.org/dpv#EntityInformedStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#EntityInformedStatus": {
            "label": "Entity Informed Status",
            "definition": "Status indicating whether an entity is informed or uninformed about specified context",
            "broader": ("https://w3id.org/dpv#Status",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#EntityIntendedInvolvement": {
            "label": "Entity Intended Involvement",
            "definition": "Status indicating the involvement of the entity is intended",
            "broader": ("https://w3id.org/dpv#EntityInvolvement", "https://w3id.org/dpv#Intended"),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#EntityInvolved": {
            "label": "Entity Involved",
            "definition": "Status indicating the entity is involved",
            "broader": ("https://w3id.org/dpv#EntityInvolvementStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#EntityInvolvement": {
            "label": "Entity Involvement",
            "definition": "Involvement of an entity in specific context",
            "broader": ("https://w3id.org/dpv#ProcessingContext",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#EntityInvolvementStatus": {
            "label": "Entity Involvement Status",
            "definition": "Status indicating whether an entity is involved",
            "broader": ("https://w3id.org/dpv#EntityInvolvement", "https://w3id.org/dpv#Status"),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#EntityNonInvolvement": {
            "label": "Entity Non-Involvement",
            "definition": "Indicating entity is not involved",
            "broader": ("https://w3id.org/dpv#EntityInvolvement",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#EntityNonPermissiveInvolvement": {
            "label": "Entity Non-Permissive Involvement",
            "definition": "Involvement of an entity in specific context where it is not permitted or able to do something",
            "broader": ("https://w3id.org/dpv#EntityInvolvement",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#EntityNotInvolved": {
            "label": "Entity Not Involved",
            "definition": "Status indicating the entity is not involved",
            "broader": ("https://w3id.org/dpv#EntityInvolvementStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#EntityPassiveInvolvement": {
            "label": "Entity Passive Involvement",
            "definition": "Involvement where entity is 'passively' or 'not actively' involved",
            "broader": ("https://w3id.org/dpv#EntityInvolvement",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#EntityPermissiveInvolvement": {
            "label": "Entity Permissive Involvement",
            "definition": "Involvement of an entity in specific context where it is permitted or able to do something",
            "broader": ("https://w3id.org/dpv#EntityInvolvement",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#EntityUninformed": {
            "label": "Entity Uninformed",
            "definition": "Status indicating entity is uninformed i.e. has been not been informed about specified context",
            "broader": ("https://w3id.org/dpv#EntityInformedStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#EntityUnintendedInvolvement": {
            "label": "Entity Unintended Involvement",
            "definition": "Status indicating the involvement of the entity is not intended",
            "broader": ("https://w3id.org/dpv#EntityInvolvement", "https://w3id.org/dpv#Unintended"),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#EnvironmentalProtection": {
            "label": "Environmental Protection",
            "definition": "Physical protection against environmental threats such as fire, floods, storms, etc.",
            "broader": ("https://w3id.org/dpv#PhysicalMeasure",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Erase": {
            "label": "Erase",
            "definition": "to remove data from existence i.e. without the possibility of retrieval",
            "broader": ("https://w3id.org/dpv#Remove",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#EstablishContractualAgreement": {
            "label": "Establish Contractual Agreement",
            "definition": "Purposes associated with carrying out data processing to establish an agreement, such as for entering into a contract",
            "broader": ("https://w3id.org/dpv#Purpose",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#EvaluationOfIndividuals": {
            "label": "Evaluation of Individuals",
            "definition": "Processing that involves evaluation of individuals",
            "broader": ("https://w3id.org/dpv#EvaluationScoring",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#EvaluationScoring": {
            "label": "Evaluation and Scoring",
            "definition": "Processing that involves evaluation and scoring of individuals",
            "broader": ("https://w3id.org/dpv#ProcessingContext",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ExpectationStatus": {
            "label": "Expectation Status",
            "definition": "Status indicating whether the specified context was intended or unintended",
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Expected": {
            "label": "Expected",
            "definition": "Status indicating the specified context was expected",
            "broader": ("https://w3id.org/dpv#ExpectationStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ExplicitlyExpressedConsent": {
            "label": "Explicitly Expressed Consent",
            "definition": "Consent that is expressed through an explicit action solely conveying a consenting decision",
            "broader": ("https://w3id.org/dpv#ExpressedConsent",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Export": {
            "label": "Export",
            "definition": "to provide a copy of data from one system to another",
            "broader": ("https://w3id.org/dpv#Disclose",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ExpressedConsent": {
            "label": "Expressed Consent",
            "definition": "Consent that is expressed through an action intended to convey a consenting decision",
            "broader": ("https://w3id.org/dpv#InformedConsent",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#FRIA": {
            "label": "Fundamental Rights Impact Assessment (FRIA)",
            "definition": "Impact assessment which assesses the potential and actual impact on fundamental rights occurring due to processing activities",
            "broader": ("https://w3id.org/dpv#RightsImpactAssessment",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#FailSafeProtocols": {
            "label": "Fail-Safe Protocols",
            "definition": "Use of fail-safe measures and protocols",
            "broader": ("https://w3id.org/dpv#TechnicalMeasure",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#FederatedLocations": {
            "label": "Federated Locations",
            "definition": "Location that is federated across multiple separate areas with designation of a primary or central location",
            "broader": ("https://w3id.org/dpv#LocationFixture",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#FeeNotRequired": {
            "label": "Fee Not Required",
            "definition": "Concept indicating a fee is not required. This is distinct from a Fee of zero as it indicates a fee is not applicable in the context",
            "broader": ("https://w3id.org/dpv#FeeRequirement",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#FeeRequired": {
            "label": "Fee Required",
            "definition": "Concept indicating a fee is required. The value of the fee should be specified using rdf:value or an another relevant means",
            "broader": ("https://w3id.org/dpv#FeeRequirement",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#FeeRequirement": {
            "label": "Fee Requirement",
            "definition": "Concept indicating whether a fee is required",
            "broader": ("https://w3id.org/dpv#Context",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#FileSystemSecurity": {
            "label": "File System Security",
            "definition": "Security implemented over a file system",
            "broader": ("https://w3id.org/dpv#SecurityMethod",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Filter": {
            "label": "Filter",
            "definition": "to filter or keep data for some criteria",
            "broader": ("https://w3id.org/dpv#Transform",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#FireDepartment": {
            "label": "Fire Department",
            "definition": "An organisation that is an emergency service provider for fire prevention, firefighting, and rescue services",
            "broader": ("https://w3id.org/dpv#EmergencyServiceProvider",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#FixedLocation": {
            "label": "Fixed Location",
            "definition": "Location that is fixed i.e. known to occur at a specific place",
            "broader": ("https://w3id.org/dpv#LocationFixture",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#FixedMultipleLocations": {
            "label": "Fixed Multiple Locations",
            "definition": "Location that is fixed with multiple places e.g. multiple cities",
            "broader": ("https://w3id.org/dpv#FixedLocation",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#FixedOccurrencesDuration": {
            "label": "Fixed Occurrences Duration",
            "definition": "Duration that takes place a fixed number of times e.g. 3 times",
            "broader": ("https://w3id.org/dpv#Duration",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#FixedSingularLocation": {
            "label": "Fixed Singular Location",
            "definition": "Location that is fixed at a specific place e.g. a city",
            "broader": ("https://w3id.org/dpv#FixedLocation",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ForProfitOrganisation": {
            "label": "For-Profit Organisation",
            "definition": "An organisation that aims to achieve profit as its primary goal",
            "broader": ("https://w3id.org/dpv#Organisation",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Format": {
            "label": "Format",
            "definition": "to arrange or structure data in a specific form",
            "broader": ("https://w3id.org/dpv#Structure",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#FraudPreventionAndDetection": {
            "label": "Fraud Prevention and Detection",
            "definition": "Purposes associated with fraud detection, prevention, and mitigation",
            "broader": ("https://w3id.org/dpv#MisusePreventionAndDetection",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Frequency": {
            "label": "Frequency",
            "definition": "The frequency or information about periods and repetitions in terms of recurrence.",
            "broader": ("https://w3id.org/dpv#Context",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#FulfilmentOfContractualObligation": {
            "label": "Fulfilment of Contractual Obligation",
            "definition": "Purposes associated with carrying out data processing to fulfill a contractual obligation",
            "broader": ("https://w3id.org/dpv#FulfilmentOfObligation",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#FulfilmentOfObligation": {
            "label": "Fulfilment of Obligation",
            "definition": "Purposes associated with carrying out data processing to fulfill an obligation",
            "broader": ("https://w3id.org/dpv#Purpose",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#FullAutomation": {
            "label": "Full Automation",
            "definition": "Level of automation corresponding to Level 5 in ISO/IEC 22989:2022 where the automation in system is capable of performing all its tasks regardless of the conditions without human involvement",
            "broader": ("https://w3id.org/dpv#AutomationLevel",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#FullyRandomisedPseudonymisation": {
            "label": "Fully Randomised Pseudonymisation",
            "definition": "Use of randomised pseudonymisation where the same elements are assigned different values each time they occur",
            "broader": ("https://w3id.org/dpv#Pseudonymisation",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#G2BContract": {
            "label": "Government-to-Business Contract",
            "definition": "A contract between a government and a business",
            "broader": ("https://w3id.org/dpv#ContractByEntityType",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#G2CContract": {
            "label": "Government-to-Consumer Contract",
            "definition": "A contract between a government and consumers",
            "broader": ("https://w3id.org/dpv#ContractByEntityType",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#G2GContract": {
            "label": "Government-to-Government Contract",
            "definition": "A contract between two governments or government departments or units",
            "broader": ("https://w3id.org/dpv#ContractByEntityType",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Generate": {
            "label": "Generate",
            "definition": "to generate or create data",
            "broader": ("https://w3id.org/dpv#Obtain",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#GeneratedData": {
            "label": "Generated Data",
            "definition": "Data that is generated or brought into existence without relation to existing data i.e. it is not derived or inferred from other data",
            "broader": ("https://w3id.org/dpv#Data",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#GeneratedPersonalData": {
            "label": "Generated Personal Data",
            "definition": "Personal Data that is generated or brought into existence without relation to existing data i.e. it is not derived or inferred from other data",
            "broader": ("https://w3id.org/dpv#PersonalData",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#GeographicCoverage": {
            "label": "Geographic Coverage",
            "definition": "Indicate of scale in terms of geographic coverage",
            "broader": ("https://w3id.org/dpv#Scale",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#GlobalScale": {
            "label": "Global Scale",
            "definition": "Geographic coverage spanning the entire globe",
            "broader": ("https://w3id.org/dpv#GeographicCoverage",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#GovernanceProcedures": {
            "label": "Governance Procedures",
            "definition": "Procedures related to governance (e.g. organisation, unit, team, process, system)",
            "broader": ("https://w3id.org/dpv#OrganisationalMeasure",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#GovernmentalOrganisation": {
            "label": "Governmental Organisation",
            "definition": "An organisation managed or part of government",
            "broader": ("https://w3id.org/dpv#Organisation",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#GraphicalNotice": {
            "label": "Graphical Notice",
            "definition": "A notice that uses graphical elements such as visualisations and icons",
            "broader": ("https://w3id.org/dpv#Notice",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#GuardianOfDataSubject": {
            "label": "Guardian(s) of Data Subject",
            "definition": "Guardian(s) of data subjects such as children",
            "broader": ("https://w3id.org/dpv#GuardianOfHuman",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#GuardianOfHuman": {
            "label": "Guardian(s) of Human",
            "definition": "Guardian(s) of humans",
            "broader": ("https://w3id.org/dpv#HumanSubject",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Guideline": {
            "label": "Guideline",
            "definition": "Practices that specify how activities must be conducted",
            "broader": ("https://w3id.org/dpv#GuidelinesPrinciple",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#GuidelinesPrinciple": {
            "label": "Guidelines Principle",
            "definition": "Guidelines or Principles regarding processing and operational measures",
            "broader": ("https://w3id.org/dpv#OrganisationalMeasure",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#HardwareSecurityProtocols": {
            "label": "Hardware Security Protocols",
            "definition": "Security protocols implemented at or within hardware",
            "broader": ("https://w3id.org/dpv#SecurityMethod",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#HashFunctions": {
            "label": "Hash Functions",
            "definition": "Use of hash functions to map information or to retrieve a prior categorisation",
            "broader": ("https://w3id.org/dpv#CryptographicMethods",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#HashMessageAuthenticationCode": {
            "label": "Hash-based Message Authentication Code (HMAC)",
            "definition": "Use of HMAC where message authentication code (MAC) utilise a cryptographic hash function and a secret cryptographic key",
            "broader": ("https://w3id.org/dpv#CryptographicAuthentication",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#HealthcareOrganisation": {
            "label": "Healthcare Organisation",
            "definition": "An organisation that delivers medical services, promotes health, and provides care for individuals and communities",
            "broader": ("https://w3id.org/dpv#Organisation",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#HighAutomation": {
            "label": "High Automation",
            "definition": "Level of automation corresponding to Level 4 in ISO/IEC 22989:2022 where the automation in system is capable of performing all its tasks within specific controlled conditions without human involvement",
            "broader": ("https://w3id.org/dpv#AutomationLevel",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#HomomorphicEncryption": {
            "label": "Homomorphic Encryption",
            "definition": "Use of Homomorphic encryption that permits computations on encrypted data without decrypting it",
            "broader": ("https://w3id.org/dpv#CryptographicMethods",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Hospital": {
            "label": "Hospital",
            "definition": "An organisation that provides comprehensive medical treatment, including emergency care, surgeries, and inpatient services",
            "broader": ("https://w3id.org/dpv#Organisation",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#HugeDataVolume": {
            "label": "Huge Data Volume",
            "definition": "Data volume that is considered huge or more than large within the context",
            "broader": ("https://w3id.org/dpv#DataVolume",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#HugeScaleOfDataSubjects": {
            "label": "Huge Scale Of Data Subjects",
            "definition": "Scale of data subjects considered huge or more than large within the context",
            "broader": ("https://w3id.org/dpv#DataSubjectScale",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#HumanInvolved": {
            "label": "Human involved",
            "definition": "Humans are involved in the specified context",
            "broader": ("https://w3id.org/dpv#HumanInvolvement",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#HumanInvolvement": {
            "label": "Human Involvement",
            "definition": "The involvement of humans in specified context",
            "broader": ("https://w3id.org/dpv#EntityInvolvement",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#HumanInvolvementForControl": {
            "label": "Human Involvement for control",
            "definition": "Human involvement for the purposes of exercising control over the specified operations in context",
            "broader": ("https://w3id.org/dpv#HumanInvolvement",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#HumanInvolvementForDecision": {
            "label": "Human Involvement for decision",
            "definition": "Human involvement for the purposes of exercising decisions over the specified operations in context",
            "broader": ("https://w3id.org/dpv#HumanInvolvement",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#HumanInvolvementForInput": {
            "label": "Human Involvement for Input",
            "definition": "Human involvement for the purposes of providing inputs to the specified context",
            "broader": ("https://w3id.org/dpv#HumanInvolvement",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#HumanInvolvementForIntervention": {
            "label": "Human Involvement for intervention",
            "definition": "Human involvement for the purposes of exercising interventions over the specified operations in context",
            "broader": ("https://w3id.org/dpv#HumanInvolvement",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#HumanInvolvementForOversight": {
            "label": "Human Involvement for Oversight",
            "definition": "Human involvement for the purposes of having oversight over the specified context regarding its operations, inputs, or outputs",
            "broader": ("https://w3id.org/dpv#HumanInvolvement",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#HumanInvolvementForVerification": {
            "label": "Human Involvement for Verification",
            "definition": "Human involvement for the purposes of verification of specified context to ensure its operations, inputs, or outputs are correct or are acceptable.",
            "broader": ("https://w3id.org/dpv#HumanInvolvement",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#HumanNotInvolved": {
            "label": "Human not involved",
            "definition": "Humans are not involved in the specified context",
            "broader": ("https://w3id.org/dpv#HumanInvolvement",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#HumanOversight": {
            "label": "Human Oversight",
            "definition": "Procedures related to implementing and ensuring human oversight, which includes ability for humans to oversee, understand, control, and reverse processes, and to have sufficient monitoring capability to detect and address anomalies, dysfunctions, or unexpected performance",
            "broader": ("https://w3id.org/dpv#GovernanceProcedures",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#HumanResourceManagement": {
            "label": "Human Resource Management",
            "definition": "Purposes associated with managing humans and 'human resources' within the organisation for effective and efficient operations.",
            "broader": ("https://w3id.org/dpv#Purpose",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#HumanSubject": {
            "label": "Human Subject",
            "definition": "The individual (or category of individuals) that is the subject within some context such as personal data (dpv:DataSubject) or technology (tech:Subject)",
            "broader": ("https://w3id.org/dpv#LegalEntity",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#HybridPublicPrivateSpace": {
            "label": "Hybrid Public Private Space",
            "definition": "A space that is a hybrid space i.e it has both public and private components - such as by having part of it be a private space or which is operated privately",
            "broader": ("https://w3id.org/dpv#PrivateSpace", "https://w3id.org/dpv#PublicSpace"),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#IPRManagement": {
            "label": "Intellectual Property Rights Management",
            "definition": "Management of Intellectual Property Rights with a view to identify and safeguard and enforce them",
            "broader": ("https://w3id.org/dpv#RightsManagement",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#IdentifyingPersonalData": {
            "label": "Identifying Personal Data",
            "definition": "Personal Data that explicitly and by itself is sufficient to identify a person",
            "broader": ("https://w3id.org/dpv#PersonalData",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#IdentityAuthentication": {
            "label": "Identity Authentication",
            "definition": "Purposes associated with performing authentication based on identity as a form of security",
            "broader": ("https://w3id.org/dpv#EnforceSecurity",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#IdentityManagementMethod": {
            "label": "Identity Management Method",
            "definition": "Management of identity and identity-based processes",
            "broader": ("https://w3id.org/dpv#AuthorisationProcedure",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#IdentityVerification": {
            "label": "Identity Verification",
            "definition": "Purposes associated with verifying or authenticating identity as a form of security",
            "broader": ("https://w3id.org/dpv#Verification",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Immigrant": {
            "label": "Immigrant",
            "definition": "Humans that are immigrants (for a jurisdiction)",
            "broader": ("https://w3id.org/dpv#HumanSubject",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Impact": {
            "label": "Impact",
            "definition": "The impact(s) possible or arising as a consequence from specified context",
            "broader": ("https://w3id.org/dpv#Consequence",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ImpactAssessment": {
            "label": "Impact Assessment",
            "definition": "Calculating or determining the likelihood of impact of an existing or proposed process, which can involve risks or detriments.",
            "broader": ("https://w3id.org/dpv#RiskAssessment",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ImpliedConsent": {
            "label": "Implied Consent",
            "definition": "Consent that is implied indirectly through an action not associated solely with conveying a consenting decision",
            "broader": ("https://w3id.org/dpv#InformedConsent",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Importance": {
            "label": "Importance",
            "definition": "An indication of 'importance' within a context",
            "broader": ("https://w3id.org/dpv#Context",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ImproveExistingProductsAndServices": {
            "label": "Improve Existing Products and Services",
            "definition": "Purposes associated with improving existing products and services",
            "broader": ("https://w3id.org/dpv#OptimisationForController",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ImproveHealthcare": {
            "label": "Improve Healthcare",
            "definition": "Purposes associated with improving healthcare systems such as for personalised treatments and curing chronic diseases",
            "broader": ("https://w3id.org/dpv#PublicBenefit",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ImproveInternalCRMProcesses": {
            "label": "Improve Internal CRM Processes",
            "definition": "Purposes associated with improving customer-relationship management (CRM) processes",
            "broader": (
                "https://w3id.org/dpv#CustomerRelationshipManagement",
                "https://w3id.org/dpv#OptimisationForController",
            ),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ImprovePublicServices": {
            "label": "Improve Public Services",
            "definition": "Purposes associated with improving the provision of public services, such as public safety, education or law enforcement",
            "broader": ("https://w3id.org/dpv#PublicBenefit",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ImproveTransportMobility": {
            "label": "Improve Transport and Mobility",
            "definition": "Purposes associated with improving traffic, public transport systems or costs for drivers",
            "broader": ("https://w3id.org/dpv#PublicBenefit",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#IncidentManagementProcedures": {
            "label": "Incident Management Procedures",
            "definition": "Procedures related to management of incidents",
            "broader": ("https://w3id.org/dpv#GovernanceProcedures",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#IncidentReportingCommunication": {
            "label": "Incident Reporting Communication",
            "definition": "Procedures related to management of incident reporting",
            "broader": ("https://w3id.org/dpv#GovernanceProcedures",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#IncorrectData": {
            "label": "Incorrect Data",
            "definition": "Data that is known to be incorrect or inconsistent with some requirements",
            "broader": ("https://w3id.org/dpv#Data",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#IncreaseServiceRobustness": {
            "label": "Increase Service Robustness",
            "definition": "Purposes associated with improving robustness and resilience of services",
            "broader": ("https://w3id.org/dpv#OptimisationForController",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#IndeterminateDuration": {
            "label": "Indeterminate Duration",
            "definition": "Duration that is indeterminate or cannot be determined",
            "broader": ("https://w3id.org/dpv#Duration",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#IndustryConsortium": {
            "label": "Industry Consortium",
            "definition": "A consortium established and comprising on industry organisations",
            "broader": ("https://w3id.org/dpv#Organisation",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Infer": {
            "label": "Infer",
            "definition": "to infer data from existing data",
            "broader": ("https://w3id.org/dpv#Derive",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#InferredData": {
            "label": "Inferred Data",
            "definition": "Data that has been obtained through inferences of other data",
            "broader": ("https://w3id.org/dpv#DerivedData",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#InferredPersonalData": {
            "label": "Inferred Personal Data",
            "definition": "Personal Data that is obtained through inference from other data",
            "broader": ("https://w3id.org/dpv#DerivedPersonalData", "https://w3id.org/dpv#InferredData"),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#InformationAudit": {
            "label": "Information Audit",
            "definition": "An audit that systematically examines the existence and use of information along with its associated resources (e.g. where it is stored) and flows (e.g. where it originates and with whom it is being shared)",
            "broader": ("https://w3id.org/dpv#Audit",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#InformationFlowControl": {
            "label": "Information Flow Control",
            "definition": "Use of measures to control information flows",
            "broader": ("https://w3id.org/dpv#TechnicalMeasure",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#InformationSecurityPolicy": {
            "label": "Information Security Policy",
            "definition": "Policy regarding security of information",
            "broader": ("https://w3id.org/dpv#Policy",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#InformedConsent": {
            "label": "Informed Consent",
            "definition": "Consent that is informed i.e. with the requirement to provide sufficient information to make a consenting decision",
            "broader": ("https://w3id.org/dpv#Consent",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#InnovativeUseOfExistingTechnology": {
            "label": "Innovative Use of Existing Technologies",
            "definition": "Involvement of existing technologies used in an innovative manner",
            "broader": ("https://w3id.org/dpv#InnovativeUseOfTechnology",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#InnovativeUseOfNewTechnologies": {
            "label": "Innovative Use of New Technologies",
            "definition": "Involvement of a new (innovative) technologies",
            "broader": ("https://w3id.org/dpv#InnovativeUseOfTechnology",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#InnovativeUseOfTechnology": {
            "label": "Innovative use of Technology",
            "definition": "Indicates that technology is being used in an innovative manner",
            "broader": ("https://w3id.org/dpv#ProcessingContext",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#IntellectualPropertyData": {
            "label": "Intellectual Property Data",
            "definition": "Data protected by Intellectual Property rights and regulations",
            "broader": ("https://w3id.org/dpv#ConfidentialData",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Intended": {
            "label": "Intended",
            "definition": "Status indicating the specified context was intended",
            "broader": ("https://w3id.org/dpv#IntentionStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#IntentionStatus": {
            "label": "Intention Status",
            "definition": "Status indicating whether the specified context was intended or unintended",
            "broader": ("https://w3id.org/dpv#Status",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#InternalResourceOptimisation": {
            "label": "Internal Resource Optimisation",
            "definition": "Purposes associated with optimisation of internal resource availability and usage for organisation",
            "broader": ("https://w3id.org/dpv#OptimisationForController",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#InternationalOrganisation": {
            "label": "International Organisation",
            "definition": "An organisation and its subordinate bodies governed by public international law, or any other body which is set up by, or on the basis of, an agreement between two or more countries",
            "broader": ("https://w3id.org/dpv#Organisation",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#IntrusionDetectionSystem": {
            "label": "Intrusion Detection System",
            "definition": "Use of measures to detect intrusions and other unauthorised attempts to gain access to a system",
            "broader": ("https://w3id.org/dpv#SecurityMethod",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#InverseJurisdiction": {
            "label": "Inverse Jurisdiction",
            "definition": "An inverse jurisdiction for a specific jurisdiction is the set of all other jurisdictions that are not part of the specific jurisdiction",
            "broader": ("https://w3id.org/dpv#Jurisdiction",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#InvolvementStatus": {
            "label": "Involvement Status",
            "definition": "Status indicating whether the involvement of specified context",
            "broader": ("https://w3id.org/dpv#Status",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#JITNotice": {
            "label": "Just-in-time Notice",
            "definition": 'A notice that is provided "just in time"" when collecting information or performing an activity',
            "broader": ("https://w3id.org/dpv#Notice",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#JobApplicant": {
            "label": "Job Applicant",
            "definition": "Humans that apply for jobs or employments",
            "broader": ("https://w3id.org/dpv#HumanSubject",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#JointDataControllers": {
            "label": "Joint Data Controllers",
            "definition": "A group of Data Controllers that jointly determine the purposes and means of processing",
            "broader": ("https://w3id.org/dpv#DataController",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#JointDataControllersAgreement": {
            "label": "Joint Data Controllers Agreement",
            "definition": "An agreement outlining conditions, criteria, obligations, responsibilities, and specifics for carrying out processing of data between Controllers within a Joint Controllers relationship",
            "broader": ("https://w3id.org/dpv#DataControllerContract",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#JudicialOrganisation": {
            "label": "Judicial Organisation",
            "definition": "An organisation involved in interpreting and applying the law, resolving disputes, and administering justice as part of the judicial system",
            "broader": ("https://w3id.org/dpv#Organisation",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Jurisdiction": {
            "label": "Jurisdiction",
            "definition": "A jurisdiction represents the locations that define the extent of authority (or control) claimed, granted, or asserted by a legal entity (in particular a legal authority) to govern or enforce rules",
            "broader": ("https://w3id.org/dpv#Location",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Justification": {
            "label": "Justification",
            "definition": "A form of documentation providing reasons, explanations, or justifications",
            "broader": ("https://w3id.org/dpv#Context",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#LargeDataVolume": {
            "label": "Large Data Volume",
            "definition": "Data volume that is considered large within the context",
            "broader": ("https://w3id.org/dpv#DataVolume",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#LargeScaleOfDataSubjects": {
            "label": "Large Scale Of Data Subjects",
            "definition": "Scale of data subjects considered large within the context",
            "broader": ("https://w3id.org/dpv#DataSubjectScale",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#LargeScaleProcessing": {
            "label": "Large Scale Processing",
            "definition": "Processing that takes place at large scales (as specified by some criteria)",
            "broader": ("https://w3id.org/dpv#ProcessingScale",),
            "source_vocab": "this should be reflected by extending this term with the appropriate context.",
        },
        "https://w3id.org/dpv#Law": {
            "label": "Law",
            "definition": "A law is a set of rules created by government or authorities",
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#LawEnforcementOrganisation": {
            "label": "Law Enforcement Organisation",
            "definition": "An organisation that is an agency responsible for enforcing laws, maintaining public order, and ensuring public safety",
            "broader": ("https://w3id.org/dpv#Organisation",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Lawful": {
            "label": "Lawful",
            "definition": "State of being lawful or legally compliant",
            "broader": ("https://w3id.org/dpv#Lawfulness",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Lawfulness": {
            "label": "Lawfulness",
            "definition": "Status associated with expressing lawfulness or legal compliance",
            "broader": ("https://w3id.org/dpv#ComplianceStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#LawfulnessUnknown": {
            "label": "Lawfulness Unknown",
            "definition": "State of the lawfulness not being known",
            "broader": ("https://w3id.org/dpv#Lawfulness",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#LayeredNotice": {
            "label": "Layered Notice",
            "definition": "A notice that contains layered elements",
            "broader": ("https://w3id.org/dpv#Notice",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#LegalAgent": {
            "label": "Legal Agent",
            "definition": "A Legal Agent is a Legal Entity that is authorised to act on behalf of another entity",
            "broader": ("https://w3id.org/dpv#Agent", "https://w3id.org/dpv#LegalEntity"),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#LegalAgreement": {
            "label": "Legal Agreement",
            "definition": "A legally binding agreement",
            "broader": ("https://w3id.org/dpv#LegalMeasure",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#LegalBasis": {
            "label": "Legal Basis",
            "definition": "Legal basis used to justify processing of data or use of technology in accordance with a law",
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#LegalCompliance": {
            "label": "Legal Compliance",
            "definition": "Purposes associated with carrying out data processing to fulfill a legal or statutory obligation",
            "broader": ("https://w3id.org/dpv#FulfilmentOfObligation",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#LegalComplianceAssessment": {
            "label": "Legal Compliance Assessment",
            "definition": "Assessment regarding legal compliance",
            "broader": ("https://w3id.org/dpv#ComplianceAssessment",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#LegalComplianceAudit": {
            "label": "Legal Compliance Audit",
            "definition": "An audit that systematically examines the state of legal compliance by reviewing policies and procedures related to obligations and compliance requirements for specific laws and regulations",
            "broader": ("https://w3id.org/dpv#Audit",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#LegalEntity": {
            "label": "Legal Entity",
            "definition": "A human or non-human 'thing' that constitutes as an entity and which is recognised and defined in law",
            "broader": ("https://w3id.org/dpv#Entity",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#LegalMeasure": {
            "label": "Legal Measure",
            "definition": "Legal measures used to safeguard and ensure good practices in connection with data and technologies",
            "broader": ("https://w3id.org/dpv#TechnicalOrganisationalMeasure",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#LegalObligation": {
            "label": "Legal Obligation",
            "definition": "Legal Obligation to conduct the specified activities",
            "broader": ("https://w3id.org/dpv#LegalBasis",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#LegalObligationCompleted": {
            "label": "Legal ObligationCompleted",
            "definition": "Status where the legal obligation has been completed",
            "broader": ("https://w3id.org/dpv#LegalObligationStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#LegalObligationOngoing": {
            "label": "Legal ObligationOngoing",
            "definition": "Status where the legal obligation is being fulfilled",
            "broader": ("https://w3id.org/dpv#LegalObligationStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#LegalObligationPending": {
            "label": "Legal ObligationPending",
            "definition": "Status where the legal obligation has not been started",
            "broader": ("https://w3id.org/dpv#LegalObligationStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#LegalObligationStatus": {
            "label": "Legal ObligationStatus",
            "definition": "Status associated with use of Legal Obligation as a legal basis",
            "broader": ("https://w3id.org/dpv#Status",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#LegitimateInterest": {
            "label": "Legitimate Interest",
            "definition": "Legitimate Interests of a Party as justification for specified activities",
            "broader": ("https://w3id.org/dpv#LegalBasis",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#LegitimateInterestAssessment": {
            "label": "Legitimate Interest Assessment",
            "definition": "Indicates an assessment regarding the use of legitimate interest as a lawful basis by the data controller",
            "broader": ("https://w3id.org/dpv#Assessment",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#LegitimateInterestInformed": {
            "label": "Legitimate InterestInformed",
            "definition": "Status where the Legitimate Interest was informed to the data subject or other relevant entities",
            "broader": ("https://w3id.org/dpv#LegitimateInterestStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#LegitimateInterestNotObjected": {
            "label": "Legitimate InterestNotObjected",
            "definition": "Status where the use of Legitimate Interest was not objected to",
            "broader": ("https://w3id.org/dpv#LegitimateInterestStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#LegitimateInterestObjected": {
            "label": "Legitimate InterestObjected",
            "definition": "Status where the use of Legitimate Interest was objected to",
            "broader": ("https://w3id.org/dpv#LegitimateInterestStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#LegitimateInterestOfController": {
            "label": "Legitimate Interest of Controller",
            "definition": "Legitimate Interests of a Data Controller in conducting specified activities",
            "broader": ("https://w3id.org/dpv#LegitimateInterest",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#LegitimateInterestOfDataSubject": {
            "label": "Legitimate Interest of Data Subject",
            "definition": "Legitimate Interests of the Data Subject in conducting specified activities",
            "broader": ("https://w3id.org/dpv#LegitimateInterest",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#LegitimateInterestOfThirdParty": {
            "label": "Legitimate Interest of Third Party",
            "definition": "Legitimate Interests of a Third Party in conducting specified activities",
            "broader": ("https://w3id.org/dpv#LegitimateInterest",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#LegitimateInterestStatus": {
            "label": "Legitimate InterestStatus",
            "definition": "Status associated with use of Legitimate Interest as a legal basis",
            "broader": ("https://w3id.org/dpv#Status",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#LegitimateInterestUninformed": {
            "label": "Legitimate InterestUninformed",
            "definition": "Status where the Legitimate Interest was not informed to the data subject or other relevant entities",
            "broader": ("https://w3id.org/dpv#LegitimateInterestStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#LicenseAgreement": {
            "label": "License Agreement",
            "definition": "A Legal Document providing permission to utilise data or resource and outlining the conditions under which such use is considered valid",
            "broader": ("https://w3id.org/dpv#ContractByDomain",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Likelihood": {
            "label": "Likelihood",
            "definition": "The likelihood or probability or chance of something taking place or occurring",
            "source_vocab": "DPV",
        },
        "https://w3id.org/dpv#LocalEnvironmentScale": {
            "label": "Local Environment Scale",
            "definition": "Geographic coverage spanning a specific environment within the locality",
            "broader": ("https://w3id.org/dpv#GeographicCoverage",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#LocalLocation": {
            "label": "Local Location",
            "definition": "Location is local",
            "broader": ("https://w3id.org/dpv#LocationLocality",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#LocalityScale": {
            "label": "Locality Scale",
            "definition": "Geographic coverage spanning a specific locality",
            "broader": ("https://w3id.org/dpv#GeographicCoverage",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Location": {
            "label": "Location",
            "definition": "A location is a position, site, or area where something is located",
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#LocationFixture": {
            "label": "Location Fixture",
            "definition": "The fixture of location refers to whether the location is fixed",
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#LocationLocality": {
            "label": "Location Locality",
            "definition": "Locality refers to whether the specified location is local within some context, e.g. for the user",
            "broader": ("https://w3id.org/dpv#Location",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#LoggingPolicy": {
            "label": "Logging Policy",
            "definition": "Policy for logging of information",
            "broader": ("https://w3id.org/dpv#Policy",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#MaintainFraudDatabase": {
            "label": "Maintain Fraud Database",
            "definition": "Purposes associated with maintaining a database related to identifying and identified fraud risks and fraud incidents",
            "broader": ("https://w3id.org/dpv#FraudPreventionAndDetection",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#MakeAvailable": {
            "label": "Make Available",
            "definition": "to transform or publish data to be used",
            "broader": ("https://w3id.org/dpv#Disclose",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ManageConsent": {
            "label": "Manage Consent",
            "definition": "Control for managing a given consent in terms of providing, reaffirming, or withdrawing it",
            "broader": (
                "https://w3id.org/dpv#ProvideConsent",
                "https://w3id.org/dpv#ReaffirmConsent",
                "https://w3id.org/dpv#WithdrawConsent",
            ),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ManagementStandard": {
            "label": "Management Standard",
            "definition": "A management standard is a standard that establishes norms or requirements regarding the management operations and processes e.g. in an organisation",
            "broader": ("https://w3id.org/dpv#Standard",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Marketing": {
            "label": "Marketing",
            "definition": "Purposes associated with conducting marketing in relation to organisation or products or services e.g. promoting, selling, and distributing",
            "broader": ("https://w3id.org/dpv#Purpose",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Match": {
            "label": "Match",
            "definition": "to combine, compare, or match data from different sources",
            "broader": ("https://w3id.org/dpv#Use",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#MediumDataVolume": {
            "label": "Medium Data Volume",
            "definition": "Data volume that is considered medium i.e. neither large nor small within the context",
            "broader": ("https://w3id.org/dpv#DataVolume",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#MediumScaleOfDataSubjects": {
            "label": "Medium Scale Of Data Subjects",
            "definition": "Scale of data subjects considered medium i.e. neither large nor small within the context",
            "broader": ("https://w3id.org/dpv#DataSubjectScale",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#MediumScaleProcessing": {
            "label": "Medium Scale Processing",
            "definition": "Processing that takes place at medium scales (as specified by some criteria)",
            "broader": ("https://w3id.org/dpv#ProcessingScale",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Member": {
            "label": "Member",
            "definition": "Humans that are members of a group, organisation, or other collectives",
            "broader": ("https://w3id.org/dpv#HumanSubject",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#MemberPartnerManagement": {
            "label": "Members and Partners Management",
            "definition": "Purposes associated with maintaining a registry of shareholders, members, or partners for governance, administration, and management functions",
            "broader": ("https://w3id.org/dpv#OrganisationGovernance",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#MentallyVulnerableDataSubject": {
            "label": "Mentally Vulnerable Data Subject",
            "definition": "Data subjects that are considered mentally vulnerable",
            "broader": ("https://w3id.org/dpv#MentallyVulnerableHuman", "https://w3id.org/dpv#VulnerableDataSubject"),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#MentallyVulnerableHuman": {
            "label": "Mentally Vulnerable Human",
            "definition": "Humans that are considered mentally vulnerable within the context",
            "broader": ("https://w3id.org/dpv#VulnerableHuman",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#MessageAuthenticationCodes": {
            "label": "Message Authentication Codes (MAC)",
            "definition": "Use of cryptographic methods to authenticate messages",
            "broader": ("https://w3id.org/dpv#CryptographicAuthentication",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#MetadataManagement": {
            "label": "Metadata Management",
            "definition": "Measures associated with management of metadata",
            "broader": ("https://w3id.org/dpv#DataGovernance",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#MisusePreventionAndDetection": {
            "label": "Misuse, Prevention and Detection",
            "definition": "Prevention and Detection of Misuse or Abuse of services",
            "broader": ("https://w3id.org/dpv#EnforceSecurity",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#MobilePlatformSecurity": {
            "label": "Mobile Platform Security",
            "definition": "Security implemented over a mobile platform",
            "broader": ("https://w3id.org/dpv#SecurityMethod",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Modify": {
            "label": "Modify",
            "definition": "to modify or change data",
            "broader": ("https://w3id.org/dpv#Alter",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Monitor": {
            "label": "Monitor",
            "definition": "to monitor data for some criteria",
            "broader": ("https://w3id.org/dpv#Consult",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#MonitoringPolicy": {
            "label": "Monitoring Policy",
            "definition": "Policy for monitoring (e.g. progress, performance)",
            "broader": ("https://w3id.org/dpv#Policy",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#MonotonicCounterPseudonymisation": {
            "label": "Monotonic Counter Pseudonymisation",
            "definition": "A simple pseudonymisation method where identifiers are substituted by a number chosen by a monotonic counter",
            "broader": ("https://w3id.org/dpv#Pseudonymisation",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Move": {
            "label": "Move",
            "definition": "to move data from one location to another including deleting the original copy",
            "broader": ("https://w3id.org/dpv#Transfer",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#MultiFactorAuthentication": {
            "label": "Multi-Factor Authentication (MFA)",
            "definition": "An authentication system that uses two or more methods to authenticate",
            "broader": ("https://w3id.org/dpv#AuthenticationProtocols",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#MultiNationalScale": {
            "label": "Multi National Scale",
            "definition": "Geographic coverage spanning multiple nations",
            "broader": ("https://w3id.org/dpv#GeographicCoverage",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#NDA": {
            "label": "Non-Disclosure Agreement (NDA)",
            "definition": "Non-disclosure Agreements e.g. preserving confidentiality of information",
            "broader": ("https://w3id.org/dpv#LegalAgreement",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#NationalAuthority": {
            "label": "National Authority",
            "definition": "An authority tasked with overseeing legal compliance for a nation",
            "broader": ("https://w3id.org/dpv#Authority",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#NationalScale": {
            "label": "National Scale",
            "definition": "Geographic coverage spanning a nation",
            "broader": ("https://w3id.org/dpv#GeographicCoverage",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#NaturalPerson": {
            "label": "Natural Person",
            "definition": "A human",
            "broader": ("https://w3id.org/dpv#Entity",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#NearlyGlobalScale": {
            "label": "Nearly Global Scale",
            "definition": "Geographic coverage nearly spanning the entire globe",
            "broader": ("https://w3id.org/dpv#GeographicCoverage",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Necessity": {
            "label": "Necessity",
            "definition": "An indication of 'necessity' within a context",
            "broader": ("https://w3id.org/dpv#Context",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#NegotiateContract": {
            "label": "Negotiate Contract",
            "definition": "Control for negotiating a contract",
            "broader": ("https://w3id.org/dpv#ContractControl",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#NegotiatedContract": {
            "label": "Negotiated Contract",
            "definition": "A contract where the terms and conditions are determined with all parties having the ability to negotiate the terms and conditions",
            "broader": ("https://w3id.org/dpv#ContractByNegotiationType",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#NetworkProxyRouting": {
            "label": "Network Proxy Routing",
            "definition": "Use of network routing using proxy",
            "broader": ("https://w3id.org/dpv#SecurityMethod",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#NetworkSecurityProtocols": {
            "label": "Network Security Protocols",
            "definition": "Security implemented at or over networks protocols",
            "broader": ("https://w3id.org/dpv#SecurityMethod",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#NonCitizen": {
            "label": "Non-Citizen",
            "definition": "Humans that are not citizens (for a jurisdiction)",
            "broader": ("https://w3id.org/dpv#HumanSubject",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#NonCommercialPurpose": {
            "label": "Non-commercial Purpose",
            "definition": "Purposes associated with processing activities performed in a non-commercial setting or without intention to commercialise",
            "broader": ("https://w3id.org/dpv#Purpose",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#NonCommercialResearch": {
            "label": "Non-Commercial Research",
            "definition": "Purposes associated with conducting research in a non-commercial setting e.g. for a non-profit-organisation (NGO)",
            "broader": ("https://w3id.org/dpv#NonCommercialPurpose", "https://w3id.org/dpv#ResearchAndDevelopment"),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#NonCompliant": {
            "label": "Non Compliant",
            "definition": "State of non-compliance where objectives have not been met, but have not been violated",
            "broader": ("https://w3id.org/dpv#ComplianceStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#NonConformant": {
            "label": "NonConformant",
            "definition": "State of being non-conformant",
            "broader": ("https://w3id.org/dpv#ConformanceStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#NonGovernmentalOrganisation": {
            "label": "Non-Governmental Organisation",
            "definition": "An organisation not part of or independent from the government",
            "broader": ("https://w3id.org/dpv#Organisation",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#NonPersonalData": {
            "label": "Non-Personal Data",
            "definition": "Data that is not Personal Data",
            "broader": ("https://w3id.org/dpv#Data",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#NonPersonalDataProcess": {
            "label": "Non-Personal Data Process",
            "definition": "An action, activity, or method involving non-personal data, and asserting that no personal data is involved",
            "broader": ("https://w3id.org/dpv#Process",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#NonProfitOrganisation": {
            "label": "Non-Profit Organisation",
            "definition": "An organisation that does not aim to achieve profit as its primary goal",
            "broader": ("https://w3id.org/dpv#Organisation",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#NonPublicDataSource": {
            "label": "Non-Public Data Source",
            "definition": "A source of data that is not publicly accessible or available",
            "broader": ("https://w3id.org/dpv#DataSource",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#NotApplicable": {
            "label": "Not Applicable",
            "definition": "Concept indicating the information or context is not applicable",
            "broader": ("https://w3id.org/dpv#Applicability",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#NotAutomated": {
            "label": "Not Automated",
            "definition": "Level of automation corresponding to Level 0 in ISO/IEC 22989:2022 where there is no automation in the system",
            "broader": ("https://w3id.org/dpv#AutomationLevel",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#NotAvailable": {
            "label": "Not Available",
            "definition": "Concept indicating the information or context is applicable but information is not yet available",
            "broader": ("https://w3id.org/dpv#Applicability",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#NotInvolved": {
            "label": "Not Involved",
            "definition": "Status indicating the specified context is 'not' involved",
            "broader": ("https://w3id.org/dpv#InvolvementStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#NotRequired": {
            "label": "Not Required",
            "definition": "Indication of neither being required nor optional i.e. not relevant or needed",
            "broader": ("https://w3id.org/dpv#Necessity",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Notice": {
            "label": "Notice",
            "definition": "A notice is an artefact for providing information, choices, or controls",
            "broader": ("https://w3id.org/dpv#OrganisationalMeasure",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#NoticeCommunicated": {
            "label": "Notice Communicated",
            "definition": "Status indicating the notice has been communicated",
            "broader": ("https://w3id.org/dpv#NoticeStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#NoticeGenerated": {
            "label": "Notice Generated",
            "definition": "Status indicating the notice has been generated",
            "broader": ("https://w3id.org/dpv#NoticeStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#NoticeIcon": {
            "label": "Notice Icon",
            "definition": "An icon within a notice associated with specific information or elements",
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#NoticeLatest": {
            "label": "Notice Latest",
            "definition": "Status indicating the notice is currently at its latest iteration",
            "broader": ("https://w3id.org/dpv#NoticeStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#NoticeLayer": {
            "label": "Notice Layer",
            "definition": "A layer within a layered notice where the layer can be used for providing specific information or controls",
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#NoticeStale": {
            "label": "Notice Stale",
            "definition": "Status indicating the notice is stale or not up to date or not the latest version",
            "broader": ("https://w3id.org/dpv#NoticeStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#NoticeStatus": {
            "label": "Notice Status",
            "definition": "Status associated with notice provision, use, and management",
            "broader": ("https://w3id.org/dpv#Status",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#NoticeUnused": {
            "label": "Notice Unused",
            "definition": "Status indicating the notice has been communicated but has not yet been used e.g. the recipient has not acknowledged it or has not taken the intended action",
            "broader": ("https://w3id.org/dpv#NoticeStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#NoticeUpdated": {
            "label": "Notice Updated",
            "definition": "Status indicating the notice has been updated and its contents or implications have changed",
            "broader": ("https://w3id.org/dpv#NoticeStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#NoticeUsed": {
            "label": "Notice Used",
            "definition": "Status indicating the notice has been communicated and has been used e.g. the recipient has acknowledged it or taken the intended action",
            "broader": ("https://w3id.org/dpv#NoticeStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Notification": {
            "label": "Notification",
            "definition": "Notification represents the provision of a notice i.e. notifying",
            "broader": ("https://w3id.org/dpv#OrganisationalMeasure",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#NotificationCompleted": {
            "label": "Notification Completed",
            "definition": "Status indicating notification(s) are completed",
            "broader": ("https://w3id.org/dpv#NotificationStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#NotificationFailed": {
            "label": "Notification Failed",
            "definition": "Status indicating notification(s) could not be completed due to a failure",
            "broader": ("https://w3id.org/dpv#NotificationStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#NotificationNotNeeded": {
            "label": "Notification Not Needed",
            "definition": "Status indicating notification(s) are not needed",
            "broader": ("https://w3id.org/dpv#NotificationStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#NotificationOngoing": {
            "label": "Notification Ongoing",
            "definition": "Status indicating notification(s) are ongoing",
            "broader": ("https://w3id.org/dpv#NotificationStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#NotificationPlanned": {
            "label": "Notification Planned",
            "definition": "Status indicating notification(s) are planned",
            "broader": ("https://w3id.org/dpv#NotificationStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#NotificationStatus": {
            "label": "Notification Status",
            "definition": "Status indicating whether notification(s) are planned, completed, or failed",
            "broader": ("https://w3id.org/dpv#Status",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ObjectingToProcess": {
            "label": "Objecting to Process",
            "definition": "Involvement where entity can object to process of specified context",
            "broader": ("https://w3id.org/dpv#EntityPermissiveInvolvement",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Obligation": {
            "label": "Obligation",
            "definition": "A rule describing an obligation for performing an activity",
            "broader": ("https://w3id.org/dpv#AcceptableRule",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ObligationFulfilled": {
            "label": "Obligation Fulfilled",
            "definition": "Status indicating an obligation has been fulfilled i.e. the activity stated as being required to be carried out has been successfully completed",
            "broader": ("https://w3id.org/dpv#RuleFulfilled",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ObligationUnfulfilled": {
            "label": "Obligation Unfulfilled",
            "definition": "Status indicating an obligation has not been fulfilled i.e. the activity stated as being required to be carried out has not been carried out but this is not considered as a violation e.g. there is still time to conduct the activity",
            "broader": ("https://w3id.org/dpv#RuleUnfulfilled",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ObligationViolated": {
            "label": "Obligation Violated",
            "definition": "Status indicating an obligation has been violated i.e. the activity stated as being required to be carried out has not been carried out and this is considered as a violation i.e. the activity can no longer be carried out to fulfil the obligation",
            "broader": ("https://w3id.org/dpv#RuleViolated",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Observe": {
            "label": "Observe",
            "definition": "to obtain data through observation",
            "broader": ("https://w3id.org/dpv#Obtain",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ObservedData": {
            "label": "Observed Data",
            "definition": "Data that has been obtained through observations of a source",
            "broader": ("https://w3id.org/dpv#CollectedData",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ObservedPersonalData": {
            "label": "Observed Personal Data",
            "definition": "Personal Data that has been collected through observation of the Data Subject(s)",
            "broader": ("https://w3id.org/dpv#CollectedPersonalData", "https://w3id.org/dpv#ObservedData"),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Obtain": {
            "label": "Obtain",
            "definition": "to solicit or gather data from someone",
            "broader": ("https://w3id.org/dpv#Processing",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ObtainConsent": {
            "label": "Obtain Consent",
            "definition": "Control for obtaining consent",
            "broader": ("https://w3id.org/dpv#ConsentControl",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#OfferContract": {
            "label": "Offer Contract",
            "definition": "Control for offering a contract",
            "broader": ("https://w3id.org/dpv#ContractControl",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#OfficialAuthorityExerciseCompleted": {
            "label": "Official Authority Exercise Completed",
            "definition": "Status where the official authority has been exercised to completion",
            "broader": ("https://w3id.org/dpv#OfficialAuthorityExerciseStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#OfficialAuthorityExerciseOngoing": {
            "label": "Official Authority Exercise Ongoing",
            "definition": "Status where the official authority is being exercised",
            "broader": ("https://w3id.org/dpv#OfficialAuthorityExerciseStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#OfficialAuthorityExercisePending": {
            "label": "Official Authority Exercise Pending",
            "definition": "Status where the official authority has not been exercised",
            "broader": ("https://w3id.org/dpv#OfficialAuthorityExerciseStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#OfficialAuthorityExerciseStatus": {
            "label": "Official Authority Exercise Status",
            "definition": "Status associated with use of Official Authority as a legal basis",
            "broader": ("https://w3id.org/dpv#Status",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#OfficialAuthorityOfController": {
            "label": "Official Authority of Controller",
            "definition": "Activities are necessary or authorised through the official authority granted to or vested in the Data Controller",
            "broader": ("https://w3id.org/dpv#LegalBasis",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#OftenFrequency": {
            "label": "Often Frequency",
            "definition": "Frequency where occurrences are often or frequent, but not continuous",
            "broader": ("https://w3id.org/dpv#Frequency",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#OperatingSystemSecurity": {
            "label": "Operating System Security",
            "definition": "Security implemented at or through operating systems",
            "broader": ("https://w3id.org/dpv#SecurityMethod",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#OptimisationForConsumer": {
            "label": "Optimisation for Consumer",
            "definition": "Purposes associated with optimisation of activities and services for consumer or user",
            "broader": ("https://w3id.org/dpv#ServiceOptimisation",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#OptimisationForController": {
            "label": "Optimisation for Controller",
            "definition": "Purposes associated with optimisation of activities and services for provider or controller",
            "broader": ("https://w3id.org/dpv#ServiceOptimisation",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#OptimiseUserInterface": {
            "label": "Optimise User Interface",
            "definition": "Purposes associated with optimisation of interfaces presented to the user",
            "broader": ("https://w3id.org/dpv#OptimisationForConsumer",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#OptingInToProcess": {
            "label": "Opting in to Process",
            "definition": "Involvement where entity can opt-in to specified context",
            "broader": ("https://w3id.org/dpv#EntityPermissiveInvolvement",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#OptingOutFromProcess": {
            "label": "Opting out of Process",
            "definition": "Involvement where entity can opt-out from specified context",
            "broader": ("https://w3id.org/dpv#EntityPermissiveInvolvement",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Optional": {
            "label": "Optional",
            "definition": "Indication of 'optional' or 'voluntary'",
            "broader": ("https://w3id.org/dpv#Necessity",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#OralNotice": {
            "label": "Oral Notice",
            "definition": "A notice provided orally or verbally",
            "broader": ("https://w3id.org/dpv#Notice",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Organisation": {
            "label": "Organisation",
            "definition": "A general term reflecting a company or a business or a group acting as a unit",
            "broader": ("https://w3id.org/dpv#LegalEntity",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#OrganisationComplianceManagement": {
            "label": "Organisation Compliance Management",
            "definition": "Purposes associated with managing compliance for organisation in relation to internal policies",
            "broader": ("https://w3id.org/dpv#OrganisationGovernance",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#OrganisationGovernance": {
            "label": "Organisation Governance",
            "definition": "Purposes associated with conducting activities and functions for governance of an organisation",
            "broader": ("https://w3id.org/dpv#Purpose",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#OrganisationRiskManagement": {
            "label": "Organisation Risk Management",
            "definition": "Purposes associated with managing risk for organisation's activities",
            "broader": ("https://w3id.org/dpv#OrganisationGovernance",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#OrganisationalMeasure": {
            "label": "Organisational Measure",
            "definition": "Organisational measures used to safeguard and ensure good practices in connection with data and technologies",
            "broader": ("https://w3id.org/dpv#TechnicalOrganisationalMeasure",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#OrganisationalUnit": {
            "label": "Organisational Unit",
            "definition": "Entity within an organisation that does not constitute as a separate legal entity",
            "broader": ("https://w3id.org/dpv#Entity",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Organise": {
            "label": "Organise",
            "definition": "to organize data for arranging or classifying",
            "broader": ("https://w3id.org/dpv#Processing",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#PIA": {
            "label": "Privacy Impact Assessment (PIA)",
            "definition": "Impact assessment regarding privacy risks",
            "broader": ("https://w3id.org/dpv#ImpactAssessment",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ParentLegalEntity": {
            "label": "Parent Legal Entity",
            "definition": "A legal entity that has one or more subsidiary entities operating under it",
            "broader": ("https://w3id.org/dpv#Organisation",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ParentOfDataSubject": {
            "label": "Parent(s) of Data Subject",
            "definition": "Parent(s) of data subjects such as children",
            "broader": ("https://w3id.org/dpv#ParentOfHuman",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ParentOfHuman": {
            "label": "Parent of Human",
            "definition": "Parent(s) of humans",
            "broader": ("https://w3id.org/dpv#HumanSubject",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#PartialAutomation": {
            "label": "Partial Automation",
            "definition": "Level of automation corresponding to Level 2 in ISO/IEC 22989:2022 where the automation is present in multiple parts of the system or in a manner that does not require the human to control/use these parts while still retaining control over the system",
            "broader": ("https://w3id.org/dpv#AutomationLevel",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#PartiallyCompliant": {
            "label": "Partially Compliant",
            "definition": "State of partially being compliant i.e. only some objectives have been met, and others have not been in violation",
            "broader": ("https://w3id.org/dpv#ComplianceStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Participant": {
            "label": "Participant",
            "definition": "Humans that participate in some context such as volunteers in a function",
            "broader": ("https://w3id.org/dpv#HumanSubject",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#PassiveRight": {
            "label": "Passive Right",
            "definition": "The right(s) applicable, provided, or expected that are always (passively) applicable",
            "broader": ("https://w3id.org/dpv#Right",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#PassivelyInvolved": {
            "label": "Passively Involved",
            "definition": "Status indicating the specified context is 'passively' involved",
            "broader": ("https://w3id.org/dpv#InvolvementStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#PasswordAuthentication": {
            "label": "Password Authentication",
            "definition": "Use of passwords to perform authentication",
            "broader": ("https://w3id.org/dpv#AuthenticationProtocols",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Patient": {
            "label": "Patient",
            "definition": "Humans that receive medical attention, treatment, care, advice, or other health related services",
            "broader": ("https://w3id.org/dpv#HumanSubject",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#PaymentManagement": {
            "label": "Payment Management",
            "definition": "Purposes associated with processing and managing payment in relation to service, including invoicing and records",
            "broader": ("https://w3id.org/dpv#ServiceManagement",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#PenetrationTestingMethods": {
            "label": "Penetration Testing Methods",
            "definition": "Use of penetration testing to identify weaknesses and vulnerabilities through simulations",
            "broader": ("https://w3id.org/dpv#SecurityMethod",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Permission": {
            "label": "Permission",
            "definition": "A rule describing a permission to perform an activity",
            "broader": ("https://w3id.org/dpv#AcceptableRule",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#PermissionManagement": {
            "label": "Permission Management",
            "definition": "Methods to obtain, provide, modify, and withdraw permissions along with maintaining a record of permissions, retrieving records, and processing changes in permission states",
            "broader": ("https://w3id.org/dpv#RightsManagement",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#PermissionNotUtilised": {
            "label": "Permission Not Utilised",
            "definition": "Status indicating a permission has not been utilised i.e. the activity stated as being permitted has not been carried out",
            "broader": ("https://w3id.org/dpv#RuleFulfilled",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#PermissionUtilised": {
            "label": "Permission Utilised",
            "definition": "Status indicating a permission has been utilised i.e. the activity stated as being permitted has been carried out",
            "broader": ("https://w3id.org/dpv#RuleFulfilled",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#PersonalData": {
            "label": "Personal Data",
            "definition": "Data directly or indirectly associated or related to an individual",
            "broader": ("https://w3id.org/dpv#Data",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#PersonalDataAudit": {
            "label": "Personal Data Audit",
            "definition": "An audit that systematically examines the existence and use of personal data along with its associated resources (e.g. where it is stored) and flows (e.g. where it originates and with whom it is being shared)",
            "broader": ("https://w3id.org/dpv#InformationAudit",),
            "source_vocab": "2024-12-17",
        },
        "https://w3id.org/dpv#PersonalDataHandling": {
            "label": "Personal Data Handling",
            "definition": "An abstract concept describing 'personal data handling'",
            "broader": ("https://w3id.org/dpv#Process",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#PersonalDataProcess": {
            "label": "Personal Data Process",
            "definition": "An action, activity, or method involving personal data",
            "broader": ("https://w3id.org/dpv#Process",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#PersonalSpace": {
            "label": "Personal Space",
            "definition": "A private space associated with an individual in a personal capacity - such as their home or the space around their physical person e.g. my home or my room",
            "broader": ("https://w3id.org/dpv#PrivateSpace",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Personalisation": {
            "label": "Personalisation",
            "definition": "Purposes associated with creating and providing customisation based on attributes and/or needs of person(s) or context(s).",
            "broader": ("https://w3id.org/dpv#Purpose",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#PersonalisedAdvertising": {
            "label": "Personalised Advertising",
            "definition": "Purposes associated with creating and providing personalised advertising",
            "broader": ("https://w3id.org/dpv#Advertising", "https://w3id.org/dpv#Personalisation"),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#PersonalisedBenefits": {
            "label": "Personalised Benefits",
            "definition": "Purposes associated with creating and providing personalised benefits for a service",
            "broader": ("https://w3id.org/dpv#ServicePersonalisation",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#PersonnelBehaviourMonitoring": {
            "label": "Personnel Behaviour Monitoring",
            "definition": "Purposes associated with monitoring behaviour of personnel",
            "broader": ("https://w3id.org/dpv#PersonnelMonitoring",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#PersonnelHiring": {
            "label": "Personnel Hiring",
            "definition": "Purposes associated with management and execution of hiring processes of personnel",
            "broader": ("https://w3id.org/dpv#PersonnelManagement",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#PersonnelManagement": {
            "label": "Personnel Management",
            "definition": "Purposes associated with management of personnel associated with the organisation e.g. evaluation and management of employees and intermediaries",
            "broader": ("https://w3id.org/dpv#HumanResourceManagement",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#PersonnelMonitoring": {
            "label": "Personnel Monitoring",
            "definition": "Purposes associated with monitoring of personnel",
            "broader": ("https://w3id.org/dpv#PersonnelManagement",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#PersonnelOffboarding": {
            "label": "Personnel Offboarding",
            "definition": "Purposes associated with offboarding of personnel i.e. activities and processes carried out when the person is exiting the company or role",
            "broader": ("https://w3id.org/dpv#PersonnelManagement",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#PersonnelOnboarding": {
            "label": "Personnel Onboarding",
            "definition": "Purposes associated with onboarding and integration of personnel within an organisation",
            "broader": ("https://w3id.org/dpv#PersonnelHiring",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#PersonnelPayment": {
            "label": "Personnel Payment",
            "definition": "Purposes associated with management and execution of payment of personnel",
            "broader": ("https://w3id.org/dpv#PersonnelManagement",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#PersonnelPerformanceEvaluation": {
            "label": "Personnel Performance Evaluation",
            "definition": "Purposes associated with evaluation or assessment of performance of employees",
            "broader": ("https://w3id.org/dpv#PersonnelPerformanceManagement",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#PersonnelPerformanceManagement": {
            "label": "Personnel Performance Management",
            "definition": "Purposes associated with management of performance of personnel",
            "broader": ("https://w3id.org/dpv#PersonnelManagement", "https://w3id.org/dpv#PersonnelMonitoring"),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#PersonnelPerformanceMonitoring": {
            "label": "Personnel Performance Monitoring",
            "definition": "Purposes associated with monitoring of performance of personnel",
            "broader": (
                "https://w3id.org/dpv#PersonnelMonitoring",
                "https://w3id.org/dpv#PersonnelPerformanceManagement",
            ),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#PersonnelPerformancePrediction": {
            "label": "Personnel Performance Prediction",
            "definition": "Purposes associated with prediction of performance of personnel",
            "broader": ("https://w3id.org/dpv#PersonnelPerformanceManagement",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#PersonnelPromotionManagement": {
            "label": "Personnel Promotion Management",
            "definition": "Purposes associated with determination and management of promotion of personnel",
            "broader": ("https://w3id.org/dpv#PersonnelManagement",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#PersonnelTerminationManagement": {
            "label": "Personnel Termination Management",
            "definition": "Purposes associated with determination and management of termination of personnel",
            "broader": ("https://w3id.org/dpv#PersonnelManagement",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#PersonnelWorkloadManagement": {
            "label": "Personnel Workload Management",
            "definition": "Purposes assocaited with determination, scheduling, planning, and carrying out workload management of personnel",
            "broader": ("https://w3id.org/dpv#PersonnelManagement",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#PhysicalAccessControlMethod": {
            "label": "Physical Access Control Method",
            "definition": "Access control applied for physical access e.g. premises or equipment",
            "broader": ("https://w3id.org/dpv#AccessControlMethod",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#PhysicalAuthentication": {
            "label": "Physical Authentication",
            "definition": "Physical implementation of authentication e.g. by matching the person to their ID card",
            "broader": ("https://w3id.org/dpv#PhysicalMeasure",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#PhysicalAuthorisation": {
            "label": "Physical Authorisation",
            "definition": "Physical implementation of authorisation e.g. by stamping a visitor pass",
            "broader": ("https://w3id.org/dpv#PhysicalMeasure",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#PhysicalDeviceSecurity": {
            "label": "Physical Device Security",
            "definition": "Physical protection for devices and equipment",
            "broader": ("https://w3id.org/dpv#PhysicalMeasure",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#PhysicalInterceptionProtection": {
            "label": "Physical Interception Protection",
            "definition": "Physical protection against interception e.g. by posting a guard",
            "broader": ("https://w3id.org/dpv#PhysicalMeasure",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#PhysicalInterruptionProtection": {
            "label": "Physical Interruption Protection",
            "definition": "Physical protection against interruptions e.g. electrical supply interruption",
            "broader": ("https://w3id.org/dpv#PhysicalMeasure",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#PhysicalMeasure": {
            "label": "Physical Measure",
            "definition": "Physical measures used to safeguard and ensure good practices in connection with data and technologies",
            "broader": ("https://w3id.org/dpv#TechnicalOrganisationalMeasure",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#PhysicalNetworkSecurity": {
            "label": "Physical Network Security",
            "definition": "Physical protection for networks and networking related infrastructure e.g. by isolating networking equipments",
            "broader": ("https://w3id.org/dpv#PhysicalMeasure",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#PhysicalSecureStorage": {
            "label": "Physical Secure Storage",
            "definition": "Physical protection for storage of information or equipment e.g. secure storage for files",
            "broader": ("https://w3id.org/dpv#PhysicalMeasure",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#PhysicalSupplySecurity": {
            "label": "Physical Supply Security",
            "definition": "Physically securing the supply of resources",
            "broader": ("https://w3id.org/dpv#PhysicalMeasure",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#PhysicalSurveillance": {
            "label": "Physical Surveillance",
            "definition": "Physically monitoring areas via surveillance",
            "broader": ("https://w3id.org/dpv#PhysicalMeasure",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Policy": {
            "label": "Policy",
            "definition": "A guidance document outlining any of: procedures, plans, principles, decisions, intent, or protocols.",
            "broader": ("https://w3id.org/dpv#GovernanceProcedures",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#PoliticalCampaign": {
            "label": "Political Campaign",
            "definition": "Purposes associated with political campaign activities related to promotion and advertisement of positions and candidates in elections at local, state or regional, or national and international levels",
            "broader": ("https://w3id.org/dpv#Advertising", "https://w3id.org/dpv#Personalisation"),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#PostQuantumCryptography": {
            "label": "Post-Quantum Cryptography",
            "definition": "Use of algorithms that are intended to be secure against cryptanalytic attack by a quantum computer",
            "broader": ("https://w3id.org/dpv#CryptographicMethods",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#PostedNotice": {
            "label": "Posted Notice",
            "definition": "A notice that is posted as a sign or banner",
            "broader": ("https://w3id.org/dpv#Notice",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#PrimaryImportance": {
            "label": "Primary Importance",
            "definition": "Indication of 'primary' or 'main' or 'core' importance",
            "broader": ("https://w3id.org/dpv#Importance",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#PrimaryUse": {
            "label": "Primary Use",
            "definition": "Status indicating compatibility based on the use being either the original context or something that is compatible with it",
            "broader": ("https://w3id.org/dpv#ReuseCompatibility",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Principle": {
            "label": "Principle",
            "definition": "A representation of values or norms that must be taken into consideration when conducting activities",
            "broader": ("https://w3id.org/dpv#GuidelinesPrinciple",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#PrintedNotice": {
            "label": "Printed Notice",
            "definition": "A notice that is provided in a printed form on or along with a device",
            "broader": ("https://w3id.org/dpv#Notice",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#PrivacyByDefault": {
            "label": "Privacy by Default",
            "definition": "Practices regarding setting the default configurations of information and services to implement data protection and privacy (synonymous with Data Protection by Default)",
            "broader": ("https://w3id.org/dpv#GuidelinesPrinciple",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#PrivacyByDesign": {
            "label": "Privacy by Design",
            "definition": "Practices regarding incorporating data protection and privacy in the design of information and services (synonymous with Data Protection by Design)",
            "broader": ("https://w3id.org/dpv#GuidelinesPrinciple",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#PrivacyNotice": {
            "label": "Privacy Notice",
            "definition": "Represents a notice or document outlining information regarding privacy",
            "broader": ("https://w3id.org/dpv#Notice",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#PrivacyPreservingProtocol": {
            "label": "Privacy Preserving Protocol",
            "definition": "Use of protocols designed with the intention of provided additional guarantees regarding privacy",
            "broader": ("https://w3id.org/dpv#CryptographicMethods",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#PrivateCommunalSpace": {
            "label": "Private Communal Space",
            "definition": "A space that is accessible to a group or a community within a private space and where members of the public do not have access to it e.g. society amenities such as gyms and pools",
            "broader": ("https://w3id.org/dpv#PrivateSpace",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#PrivateInformationRetrieval": {
            "label": "Private Information Retrieval",
            "definition": "Use of cryptographic methods to retrieve a record from a system without revealing which record is retrieved",
            "broader": ("https://w3id.org/dpv#CryptographicMethods",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#PrivateLocation": {
            "label": "Private Location (deprecated)",
            "definition": "Location that is not or cannot be accessed by the public and is controlled as a private space",
            "broader": ("https://w3id.org/dpv#LocalLocation",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#PrivateSectorBody": {
            "label": "Private Sector Body",
            "definition": "An organisation owned and operated by private individuals or companies",
            "broader": ("https://w3id.org/dpv#LegalEntity",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#PrivateSpace": {
            "label": "Private Space",
            "definition": "A space that is owned or controlled by a private entity and where access to members of the public is restricted",
            "broader": ("https://w3id.org/dpv#Location",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#PrivatelyOperatedPublicSpace": {
            "label": "Privately Operated Public Space",
            "definition": "A space that is operated or managed by a private entity but which is accessible to the public e.g. a public bus station operated by a specific company",
            "broader": (
                "https://w3id.org/dpv#HybridPublicPrivateSpace",
                "https://w3id.org/dpv#PubliclyAccessibleSpace",
            ),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#PrivatelyOwnedPublicSpace": {
            "label": "Privately Owned Public Space",
            "definition": "A space that is privately owned but which is accessible and usable by the public - whether freely or through a process which is open to all members of the public e.g. hotel lobby, shopping mall atriums",
            "broader": ("https://w3id.org/dpv#HybridPublicPrivateSpace", "https://w3id.org/dpv#PrivatelyOwnedSpace"),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#PrivatelyOwnedSpace": {
            "label": "Privately Owned Space",
            "definition": "A place that is privately owned e.g. offices, malls",
            "broader": ("https://w3id.org/dpv#PrivateSpace",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Process": {
            "label": "Process",
            "definition": "An action, activity, or method",
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Processing": {
            "label": "Processing",
            "definition": "Operations or 'processing' performed on data",
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ProcessingCondition": {
            "label": "Processing Condition",
            "definition": "Conditions required or followed regarding processing of data or use of technologies",
            "broader": ("https://w3id.org/dpv#ProcessingContext",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ProcessingContext": {
            "label": "Processing Context",
            "definition": "Context or conditions within which processing takes place",
            "broader": ("https://w3id.org/dpv#Context",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ProcessingDuration": {
            "label": "Processing Duration",
            "definition": "Conditions regarding duration or temporal limitation for processing",
            "broader": ("https://w3id.org/dpv#Duration", "https://w3id.org/dpv#ProcessingCondition"),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ProcessingLocation": {
            "label": "Processing Location",
            "definition": "Conditions regarding location or geospatial scope where processing takes places",
            "broader": ("https://w3id.org/dpv#Location", "https://w3id.org/dpv#ProcessingCondition"),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ProcessingScale": {
            "label": "Processing Scale",
            "definition": "Scale of Processing",
            "broader": ("https://w3id.org/dpv#Scale",),
            "source_vocab": "this should be reflected by extending the scales provided with the appropriate context.",
        },
        "https://w3id.org/dpv#ProfessionalConfidentialData": {
            "label": "Professional Confidential Data",
            "definition": "Data protected by professional secrecy or confidentiality, including but not limited to data covered by professional privilege or secrecy obligations such as that covered by lawyer or doctor-patient confidentiality and other forms of recognised professional confidentiality obligations",
            "broader": ("https://w3id.org/dpv#ConfidentialData",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ProfessionalTraining": {
            "label": "Professional Training",
            "definition": "Training methods that are intended to provide professional knowledge and expertise",
            "broader": ("https://w3id.org/dpv#StaffTraining",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Profiling": {
            "label": "Profiling",
            "definition": "to create a profile that describes or represents a person",
            "broader": ("https://w3id.org/dpv#Use",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Prohibition": {
            "label": "Prohibition",
            "definition": "A rule describing a prohibition to perform an activity",
            "broader": ("https://w3id.org/dpv#UnacceptableRule",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ProhibitionUnviolated": {
            "label": "Prohibition Unviolated",
            "definition": "Status indicating a prohibition has not been violated i.e. the activity stated as being prohibited has not been carried out",
            "broader": ("https://w3id.org/dpv#RuleFulfilled",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ProhibitionViolated": {
            "label": "Prohibition Violated",
            "definition": "Status indicating a prohibition has been violated i.e. the activity stated as being prohibited has been carried out",
            "broader": ("https://w3id.org/dpv#RuleViolated",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ProtectionOfIPR": {
            "label": "Protection of Intellectual Property Rights",
            "definition": "Purposes associated with the protection of intellectual property rights",
            "broader": ("https://w3id.org/dpv#FulfilmentOfObligation",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ProtectionOfNationalSecurity": {
            "label": "Protection of National Security",
            "definition": "Purposes associated with the protection of national security",
            "broader": ("https://w3id.org/dpv#PublicBenefit",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ProtectionOfPublicSecurity": {
            "label": "Protection of Public Security",
            "definition": "Purposes associated with the protection of public security",
            "broader": ("https://w3id.org/dpv#PublicBenefit",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ProvideConsent": {
            "label": "Provide Consent",
            "definition": "Control for providing consent",
            "broader": ("https://w3id.org/dpv#ConsentControl", "https://w3id.org/dpv#OptingInToProcess"),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ProvideEventRecommendations": {
            "label": "Provide Event Recommendations",
            "definition": "Purposes associated with creating and providing personalised recommendations for events",
            "broader": ("https://w3id.org/dpv#ProvidePersonalisedRecommendations",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ProvideOfficialStatistics": {
            "label": "Provide Official Statistics",
            "definition": "Purposes associated with facilitating the development, production and dissemination of reliable official statistics",
            "broader": ("https://w3id.org/dpv#PublicBenefit",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ProvidePersonalisedRecommendations": {
            "label": "Provide Personalised Recommendations",
            "definition": "Purposes associated with creating and providing personalised recommendations",
            "broader": ("https://w3id.org/dpv#ServicePersonalisation",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ProvideProductRecommendations": {
            "label": "Provide Product Recommendations",
            "definition": "Purposes associated with creating and providing product recommendations e.g. suggest similar products",
            "broader": ("https://w3id.org/dpv#ProvidePersonalisedRecommendations",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ProvidedData": {
            "label": "Provided Data",
            "definition": "Data that has been provided by an entity",
            "broader": ("https://w3id.org/dpv#CollectedData",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ProvidedPersonalData": {
            "label": "Provided Personal Data",
            "definition": "Personal Data that has been provided by an entity such as the Data Subject",
            "broader": ("https://w3id.org/dpv#CollectedPersonalData", "https://w3id.org/dpv#ProvidedData"),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ProviderStandardFormContract": {
            "label": "Provider Standard Form Contract",
            "definition": "A contract where the terms and conditions are determined by parties in the role of a 'provider', and the other parties have negligible or no ability to negotiate the terms and conditions",
            "broader": ("https://w3id.org/dpv#StandardFormContract",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Pseudonymisation": {
            "label": "Pseudonymisation",
            "definition": "Pseudonymisation means the processing of personal data in such a manner that the personal data can no longer be attributed to a specific data subject without the use of additional information, provided that such additional information is kept separately and is subject to technical and organisatio...",
            "broader": ("https://w3id.org/dpv#Deidentification",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Pseudonymise": {
            "label": "Pseudonymise",
            "definition": "to replace personal identifiable information by artificial identifiers",
            "broader": ("https://w3id.org/dpv#Transform",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#PseudonymisedData": {
            "label": "Pseudonymised Data",
            "definition": "Pseudonymised Data is data that has gone a partial or incomplete anonymisation process by replacing the identifiable information with artificial identifiers or 'pseudonyms', and is still considered as personal data",
            "broader": ("https://w3id.org/dpv#PersonalData",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#PublicBenefit": {
            "label": "Public Benefit",
            "definition": "Purposes undertaken and intended to provide benefit to public or society",
            "broader": ("https://w3id.org/dpv#Purpose",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#PublicDataSource": {
            "label": "Public Data Source",
            "definition": "A source of data that is publicly accessible or available",
            "broader": ("https://w3id.org/dpv#DataSource",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#PublicInterest": {
            "label": "Public Interest",
            "definition": "Activities are necessary or beneficial for interest of the public or society at large",
            "broader": ("https://w3id.org/dpv#LegalBasis",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#PublicInterestCompleted": {
            "label": "Public Interest Completed",
            "definition": "Status where the public interest activity has been completed",
            "broader": ("https://w3id.org/dpv#PublicInterestStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#PublicInterestObjected": {
            "label": "Public Interest Objected",
            "definition": "Status where the public interest activity was objected to by the Data Subject or another relevant entity",
            "broader": ("https://w3id.org/dpv#PublicInterestStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#PublicInterestOngoing": {
            "label": "Public Interest Ongoing",
            "definition": "Status where the public interest activity is ongoing",
            "broader": ("https://w3id.org/dpv#PublicInterestStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#PublicInterestPending": {
            "label": "Public Interest Pending",
            "definition": "Status where the public interest activity has not started",
            "broader": ("https://w3id.org/dpv#PublicInterestStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#PublicInterestStatus": {
            "label": "Public Interest Status",
            "definition": "Status associated with use of Public Interest as a legal basis",
            "broader": ("https://w3id.org/dpv#Status",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#PublicLocation": {
            "label": "Public Location (deprecated)",
            "definition": "Location that is or can be accessed by the public",
            "broader": ("https://w3id.org/dpv#LocalLocation",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#PublicPolicyMaking": {
            "label": "Public Policy Making",
            "definition": "Purposes associated with public policy making, such as the development of new laws",
            "broader": ("https://w3id.org/dpv#PublicBenefit",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#PublicRegisterOfEntities": {
            "label": "Public Register of Entities",
            "definition": "A publicly available list of entities e.g. to indicate which entities perform a certain activity within a certain location or jurisdiction",
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#PublicRelations": {
            "label": "Public Relations",
            "definition": "Purposes associated with managing and conducting public relations processes, including creating goodwill for the organisation",
            "broader": ("https://w3id.org/dpv#Marketing",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#PublicSectorBody": {
            "label": "Public Sector Body",
            "definition": "A government-controlled organisation that provides services or goods to the public",
            "broader": ("https://w3id.org/dpv#LegalEntity",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#PublicSpace": {
            "label": "Public Space",
            "definition": "Any space that is accessible to the public or is owned by the public",
            "broader": ("https://w3id.org/dpv#Location",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#PubliclyAccessibleSpace": {
            "label": "Publicly Accessible Space",
            "definition": "A space that is accessible to all members of the public e.g. parks, malls, train stations",
            "broader": ("https://w3id.org/dpv#PublicSpace",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#PubliclyOwnedSpace": {
            "label": "Publicly Owned Space",
            "definition": "A space that is owned by the public e.g. national parks, forests",
            "broader": ("https://w3id.org/dpv#PublicSpace",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Purpose": {
            "label": "Purpose",
            "definition": "Purpose or (broader) Goal associated with data or technology",
            "source_vocab": "2024-04-14",
        },
        "https://w3id.org/dpv#QuantumCryptography": {
            "label": "Quantum Cryptography",
            "definition": "Cryptographic methods that utilise quantum mechanical properties to perform cryptographic tasks",
            "broader": ("https://w3id.org/dpv#CryptographicMethods",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Query": {
            "label": "Query",
            "definition": "to query or make enquiries over data",
            "broader": ("https://w3id.org/dpv#Consult",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#RNGPseudonymisation": {
            "label": "RNG Pseudonymisation",
            "definition": "A pseudonymisation method where identifiers are substituted by a number chosen by a Random Number Generator (RNG)",
            "broader": ("https://w3id.org/dpv#Pseudonymisation",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ROPA": {
            "label": "Records of Processing Activities",
            "definition": "A Record of Processing Activities (ROPA) is a document detailing processing activities",
            "broader": ("https://w3id.org/dpv#DataProcessingRecord",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#RandomLocation": {
            "label": "Random Location",
            "definition": "Location that is random or unknown",
            "broader": ("https://w3id.org/dpv#LocationFixture",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ReaffirmConsent": {
            "label": "Reaffirm Consent",
            "definition": "Control for affirming consent",
            "broader": ("https://w3id.org/dpv#ConsentControl",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#RecertificationPolicy": {
            "label": "Recertification Policy",
            "definition": "Policy regarding repetition or renewal of existing certification(s)",
            "broader": ("https://w3id.org/dpv#Policy",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Recipient": {
            "label": "Recipient",
            "definition": "Entities that receive data or technologies",
            "broader": ("https://w3id.org/dpv#LegalEntity",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#RecipientInformed": {
            "label": "Recipient Informed",
            "definition": "Status indicating Recipient has been informed about the specified context",
            "broader": ("https://w3id.org/dpv#EntityInformed",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#RecipientUninformed": {
            "label": "Recipient Uninformed",
            "definition": "Status indicating Recipient is uninformed i.e. has not been informed about the specified context",
            "broader": ("https://w3id.org/dpv#EntityUninformed",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Recommendation": {
            "label": "Recommendation",
            "definition": "A rule describing a recommendation for performing an activity",
            "broader": ("https://w3id.org/dpv#AcceptableRule",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#RecommendationFollowed": {
            "label": "Recommendation Followed",
            "definition": "Status indicating a recommendation has been followed i.e. the activity stated as being recommended has been carried out",
            "broader": ("https://w3id.org/dpv#RuleFulfilled",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#RecommendationNotFollowed": {
            "label": "Recommendation Not Followed",
            "definition": "Status indicating a recommendation has not been followed i.e. the activity stated as being recommended has not been carried out",
            "broader": ("https://w3id.org/dpv#RuleUnfulfilled",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Record": {
            "label": "Record",
            "definition": "to make a record (especially media)",
            "broader": ("https://w3id.org/dpv#Obtain",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#RecordManagement": {
            "label": "Record Management",
            "definition": "Purposes associated with manage creation, storage, and use of records relevant to operations, events, and processes e.g. to store logs or access requests",
            "broader": ("https://w3id.org/dpv#Purpose",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#RecordsOfActivities": {
            "label": "Records of Activities",
            "definition": "Records of activities within some context such as maintenance tasks or governance functions",
            "broader": ("https://w3id.org/dpv#OrganisationalMeasure",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#RecruitmentAdvertising": {
            "label": "Recruitment Advertising",
            "definition": "Purposes associated with advertisement for Recruitments and personnel hiring",
            "broader": ("https://w3id.org/dpv#Advertising", "https://w3id.org/dpv#PersonnelHiring"),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#RecruitmentApplicantBackgroundCheck": {
            "label": "Recruitment Applicant Background Check",
            "definition": "Purposes assocaited with conducting background checks for prospective and current job applicants for recruitment",
            "broader": ("https://w3id.org/dpv#RecruitmentManagement",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#RecruitmentApplicantCriminalBackgroundCheck": {
            "label": "Recruitment Applicant Criminal Background Check",
            "definition": "Purposes associated with conducting criminal background assessment for prospective and current job applicants for recruitment",
            "broader": ("https://w3id.org/dpv#RecruitmentManagement",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#RecruitmentApplicantInformationAuthentication": {
            "label": "Recruitment Applicant Information Authentication",
            "definition": "Purposes associated with authentication and verification of information as part of recruitment",
            "broader": ("https://w3id.org/dpv#RecruitmentManagement",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#RecruitmentApplicantSelection": {
            "label": "Recruitment Applicant Selection",
            "definition": "Purposes associated with determination or selection of candidates, whether for a specific job or job pool, or for a specific stage as part of recruitment",
            "broader": ("https://w3id.org/dpv#RecruitmentManagement",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#RecruitmentApplicationAnalysis": {
            "label": "Recruitment Application Analysis",
            "definition": "Purposes assocaited with analysis of job applications or job candidates for recruitment",
            "broader": ("https://w3id.org/dpv#RecruitmentApplicationManagement",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#RecruitmentApplicationManagement": {
            "label": "Recruitment Application Management",
            "definition": "Purposes associated with managing job applications for recruitment",
            "broader": ("https://w3id.org/dpv#RecruitmentManagement",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#RecruitmentApplicationScreening": {
            "label": "Recruitment Application Screening",
            "definition": "Purposes associated with screening and filtering of job applications or job candidates for recruitment",
            "broader": ("https://w3id.org/dpv#RecruitmentApplicationManagement",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#RecruitmentInterviewAnalysis": {
            "label": "Recruitment Interview Analysis",
            "definition": "Purposes associated with analysis of interviews, including the people and involved, for recruitment",
            "broader": ("https://w3id.org/dpv#RecruitmentInterviewManagement",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#RecruitmentInterviewAssessment": {
            "label": "Recruitment Interview Assessment",
            "definition": "Purposes associated with assessment of interviews, including assessment of people and information, for recruitment",
            "broader": ("https://w3id.org/dpv#RecruitmentInterviewManagement",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#RecruitmentInterviewManagement": {
            "label": "Recruitment Interview Management",
            "definition": "Purposes associated conducting and managing interviews for recruitment",
            "broader": ("https://w3id.org/dpv#RecruitmentManagement",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#RecruitmentInterviewScheduling": {
            "label": "Recruitment Interview Scheduling",
            "definition": "Purposes associated with scheduling interviews for recruitment",
            "broader": ("https://w3id.org/dpv#RecruitmentInterviewManagement",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#RecruitmentManagement": {
            "label": "Recruitment Management",
            "definition": "Purposes assocaited with recruitment of personnel, which includes identifying, sourcing, screening, filtering, shortlisting, and interviewing candidates",
            "broader": ("https://w3id.org/dpv#PersonnelHiring",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#RecruitmentTargetedAdvertising": {
            "label": "Targeted Recruitment Advertising",
            "definition": "Purposes associated with targeted advertisement for Recruitments and personnel hiring",
            "broader": ("https://w3id.org/dpv#RecruitmentAdvertising", "https://w3id.org/dpv#TargetedAdvertising"),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Reformat": {
            "label": "Reformat",
            "definition": "to rearrange or restructure data to change its form",
            "broader": ("https://w3id.org/dpv#Format",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#RefuseConsent": {
            "label": "Refuse Consent",
            "definition": "Control for refusing consent",
            "broader": ("https://w3id.org/dpv#ConsentControl",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#RefuseContract": {
            "label": "Refuse Contract",
            "definition": "Control for refusing a contract",
            "broader": ("https://w3id.org/dpv#ContractControl",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Region": {
            "label": "Region",
            "definition": "A region is an area or site that is considered a location",
            "broader": ("https://w3id.org/dpv#Country",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#RegionalAuthority": {
            "label": "Regional Authority",
            "definition": "An authority tasked with overseeing legal compliance for a region",
            "broader": ("https://w3id.org/dpv#Authority",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#RegionalScale": {
            "label": "Regional Scale",
            "definition": "Geographic coverage spanning a specific region or regions",
            "broader": ("https://w3id.org/dpv#GeographicCoverage",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#RegulatorySandbox": {
            "label": "Regulatory Sandbox",
            "definition": "Mechanism used by regulators and businesses for gauging the compatibility of regulations and innovative products, particularly in the context of digitalisation, in a controlled real-world environment with appropriate safeguards in place",
            "broader": ("https://w3id.org/dpv#Safeguard",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ReligiousAssociations": {
            "label": "Religious Associations",
            "definition": "An organisations that supports the practice, promotion, and management of religious activities and beliefs",
            "broader": ("https://w3id.org/dpv#Organisation",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#RemoteLocation": {
            "label": "Remote Location",
            "definition": "Location is remote i.e. not local",
            "broader": ("https://w3id.org/dpv#LocationLocality",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Remove": {
            "label": "Remove",
            "definition": "to destruct or erase data",
            "broader": ("https://w3id.org/dpv#Processing",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#RenewedConsentGiven": {
            "label": "Renewed Consent Given",
            "definition": "The state where a previously given consent has been 'renewed' or 'refreshed' or 'reaffirmed' to form a new instance of given consent",
            "broader": ("https://w3id.org/dpv#ConsentStatusValidForProcessing",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#RepairImpairments": {
            "label": "Repair Impairments",
            "definition": "Purposes associated with identifying, rectifying, or otherwise undertaking activities intended to fix or repair impairments to existing functionalities",
            "broader": ("https://w3id.org/dpv#ServiceManagement",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Representative": {
            "label": "Representative",
            "definition": "A representative of a legal entity",
            "broader": ("https://w3id.org/dpv#LegalEntity",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#RequestAccepted": {
            "label": "Request Accepted",
            "definition": "State of a request being accepted towards fulfilment",
            "broader": ("https://w3id.org/dpv#RequestStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#RequestAcknowledged": {
            "label": "Request Acknowledged",
            "definition": "State of a request being acknowledged",
            "broader": ("https://w3id.org/dpv#RequestStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#RequestActionDelayed": {
            "label": "Request Action Delayed",
            "definition": "State of a request being delayed towards fulfilment",
            "broader": ("https://w3id.org/dpv#RequestStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#RequestFulfilled": {
            "label": "Request Fulfilled",
            "definition": "State of a request being fulfilled",
            "broader": ("https://w3id.org/dpv#RequestStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#RequestInitiated": {
            "label": "Request Initiated",
            "definition": "State of a request being initiated",
            "broader": ("https://w3id.org/dpv#RequestStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#RequestRejected": {
            "label": "Request Rejected",
            "definition": "State of a request being rejected towards non-fulfilment",
            "broader": ("https://w3id.org/dpv#RequestStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#RequestRequiredActionPerformed": {
            "label": "Request Required Action Performed",
            "definition": "State of a request's required action having been performed by the other party",
            "broader": ("https://w3id.org/dpv#RequestStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#RequestRequiresAction": {
            "label": "Request Requires Action",
            "definition": "State of a request requiring an action to be performed from another party",
            "broader": ("https://w3id.org/dpv#RequestStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#RequestStatus": {
            "label": "Request Status",
            "definition": "Status associated with requests",
            "broader": ("https://w3id.org/dpv#Status",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#RequestStatusQuery": {
            "label": "Request Status Query",
            "definition": "State of a request's status being queried",
            "broader": ("https://w3id.org/dpv#RequestStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#RequestUnfulfilled": {
            "label": "Request Unfulfilled",
            "definition": "State of a request being unfulfilled",
            "broader": ("https://w3id.org/dpv#RequestStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#RequestedServiceProvision": {
            "label": "Requested Service Provision",
            "definition": "Purposes associated with delivering services as requested by user or consumer",
            "broader": ("https://w3id.org/dpv#ServiceProvision",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Required": {
            "label": "Required",
            "definition": "Indication of 'required' or 'necessary'",
            "broader": ("https://w3id.org/dpv#Necessity",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ResearchAndDevelopment": {
            "label": "Research and Development",
            "definition": "Purposes associated with conducting research and development for new methods, products, or services",
            "broader": ("https://w3id.org/dpv#Purpose",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ResidualRisk": {
            "label": "Residual Risk",
            "definition": "Risk remaining after treatment or mitigation",
            "broader": ("https://w3id.org/dpv#Risk",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Restrict": {
            "label": "Restrict",
            "definition": "to apply a restriction on the processing of specific records",
            "broader": ("https://w3id.org/dpv#Transform",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Retrieve": {
            "label": "Retrieve",
            "definition": "to retrieve data, often in an automated manner",
            "broader": ("https://w3id.org/dpv#Use",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ReuseCompatibility": {
            "label": "ReuseCompatibility",
            "definition": "Status indicating whether the specified context is compatible with another earlier context",
            "broader": ("https://w3id.org/dpv#Status",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ReversingProcessEffects": {
            "label": "Reversing Process Effects",
            "definition": "Involvement where entity can reverse effects of specified context",
            "broader": ("https://w3id.org/dpv#EntityPermissiveInvolvement",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ReversingProcessInput": {
            "label": "Reversing Process Input",
            "definition": "Involvement where entity can reverse input of specified context",
            "broader": ("https://w3id.org/dpv#EntityPermissiveInvolvement",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ReversingProcessOutput": {
            "label": "Reversing Process Output",
            "definition": "Involvement where entity can reverse output of specified context",
            "broader": ("https://w3id.org/dpv#EntityPermissiveInvolvement",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ReviewImpactAssessment": {
            "label": "Review Impact Assessment",
            "definition": "Procedures to review impact assessments in terms of continued validity, adequacy for intended purposes, and conformance of processes with findings",
            "broader": ("https://w3id.org/dpv#ImpactAssessment", "https://w3id.org/dpv#ReviewProcedure"),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ReviewProcedure": {
            "label": "Review Procedure",
            "definition": "A procedure or process that reviews the correctness and validity of other procedures and policies e.g. to ensure continued validity, adequacy for intended purposes, and conformance of processes with findings",
            "broader": ("https://w3id.org/dpv#GovernanceProcedures",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Right": {
            "label": "Right",
            "definition": "The right(s) applicable, provided, or expected",
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#RightExerciseActivity": {
            "label": "Right Exercise Activity",
            "definition": "An activity representing an exercising of an active right",
            "broader": ("https://w3id.org/dpv#OrganisationalMeasure",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#RightExerciseNotice": {
            "label": "Right Exercise Notice",
            "definition": "Information associated with exercising of an active right such as where and how to exercise the right, information required for it, or updates on an exercised rights request",
            "broader": ("https://w3id.org/dpv#RightNotice",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#RightExerciseRecord": {
            "label": "Right Exercise Record",
            "definition": "Record of a Right being exercised",
            "broader": ("https://w3id.org/dpv#RecordsOfActivities",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#RightFulfilmentNotice": {
            "label": "Right Fulfilment Notice",
            "definition": "Notice provided regarding fulfilment of a right",
            "broader": ("https://w3id.org/dpv#RightExerciseNotice",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#RightNonFulfilmentNotice": {
            "label": "Right Non-Fulfilment Notice",
            "definition": "Notice provided regarding non-fulfilment of a right",
            "broader": ("https://w3id.org/dpv#RightExerciseNotice",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#RightNotice": {
            "label": "Right Notice",
            "definition": "Information associated with rights, such as which rights exist, when and where they are applicable, and other relevant information",
            "broader": ("https://w3id.org/dpv#Notice",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#RightsFulfilment": {
            "label": "Rights Fulfilment",
            "definition": "Purposes associated with the fulfillment of rights specified in law",
            "broader": ("https://w3id.org/dpv#LegalObligation",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#RightsImpactAssessment": {
            "label": "Rights Impact Assessment",
            "definition": "Impact assessment which involves determining the impact on rights and freedoms",
            "broader": ("https://w3id.org/dpv#ImpactAssessment",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#RightsManagement": {
            "label": "Rights Management",
            "definition": "Methods associated with rights management where 'rights' refer to controlling who can do what with a resource",
            "broader": ("https://w3id.org/dpv#OrganisationalMeasure",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Risk": {
            "label": "Risk",
            "definition": "A risk or possibility or uncertainty of negative effects, impacts, or consequences",
            "broader": ("https://w3id.org/dpv#RiskConcept",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#RiskAssessment": {
            "label": "Risk Assessment",
            "definition": "Assessment involving identification, analysis, and evaluation of risk",
            "broader": ("https://w3id.org/dpv#Assessment",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#RiskConcept": {
            "label": "Risk Concept",
            "definition": "Parent concept for combining concepts associated with risk assessment such as actual and potential Risk, Risk Source, Consequences, and Impacts",
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#RiskLevel": {
            "label": "Risk Level",
            "definition": "The magnitude of a risk expressed as an indication to aid in its management",
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#RiskMitigationMeasure": {
            "label": "Risk Mitigation Measure",
            "definition": "Measures intended to mitigate, minimise, or prevent risk.",
            "broader": ("https://w3id.org/dpv#TechnicalOrganisationalMeasure",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Rule": {
            "label": "Rule",
            "definition": "A rule describing a process or control that directs or determines if and how an activity should be conducted",
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#RuleFulfilled": {
            "label": "Rule Fulfilled",
            "definition": "Status indicating a rule has been fulfilled, completed, or satisfied",
            "broader": ("https://w3id.org/dpv#RuleFulfilmentStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#RuleFulfilmentStatus": {
            "label": "Rule Fulfilment Status",
            "definition": "Status associated with a rule for indicating whether it is applicable, or has been utilised, and whether the requirements of the rule have been fulfilled or violated",
            "broader": ("https://w3id.org/dpv#Status",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#RuleUnfulfilled": {
            "label": "Rule Unfulfilled",
            "definition": "Status indicating a rule has not been fulfilled nor violated",
            "broader": ("https://w3id.org/dpv#RuleFulfilmentStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#RuleViolated": {
            "label": "Rule Violated",
            "definition": "Status indicating a rule has been violated, breached, broken, or infracted",
            "broader": ("https://w3id.org/dpv#RuleFulfilmentStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#SMEOrganisation": {
            "label": "SME Organisation",
            "definition": "An organisation that is characterised as a Small or Medium-sized Enterprise based on limited staff and revenue",
            "broader": ("https://w3id.org/dpv#LegalEntity",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Safeguard": {
            "label": "Safeguard",
            "definition": "A safeguard is a precautionary measure for the protection against or mitigation of negative effects",
            "broader": ("https://w3id.org/dpv#OrganisationalMeasure",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#SafeguardForDataTransfer": {
            "label": "Safeguard for Data Transfer",
            "definition": "Represents a safeguard used for data transfer. Can include technical or organisational measures.",
            "broader": ("https://w3id.org/dpv#Safeguard",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Scale": {
            "label": "Scale",
            "definition": "A measurement along some dimension",
            "broader": ("https://w3id.org/dpv#ProcessingContext",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ScientificResearch": {
            "label": "Scientific Research",
            "definition": "Purposes associated with scientific research",
            "broader": ("https://w3id.org/dpv#ResearchAndDevelopment",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Scope": {
            "label": "Scope",
            "definition": "Indication of the extent or range or boundaries associated with(in) a context",
            "broader": ("https://w3id.org/dpv#Context",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ScoringOfIndividuals": {
            "label": "Scoring of Individuals",
            "definition": "Processing that involves scoring of individuals",
            "broader": ("https://w3id.org/dpv#EvaluationScoring",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Screen": {
            "label": "Screen",
            "definition": "to remove data for some criteria",
            "broader": ("https://w3id.org/dpv#Transform",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Seal": {
            "label": "Seal",
            "definition": "A seal or a mark indicating proof of certification to some certification or standard",
            "broader": ("https://w3id.org/dpv#CertificationSeal",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#SearchFunctionalities": {
            "label": "Search Functionalities",
            "definition": "Purposes associated with providing searching, querying, or other forms of information retrieval related functionalities",
            "broader": ("https://w3id.org/dpv#ServiceProvision",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#SecondaryImportance": {
            "label": "Secondary Importance",
            "definition": "Indication of 'secondary' or 'minor' or 'auxiliary' importance",
            "broader": ("https://w3id.org/dpv#Importance",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#SecondaryUse": {
            "label": "Secondary Use",
            "definition": "Status indicating incompatibility based on the use not being compatible with an earlier context",
            "broader": ("https://w3id.org/dpv#ReuseCompatibility",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#SecretSharingSchemes": {
            "label": "Secret Sharing Schemes",
            "definition": "Use of secret sharing schemes where the secret can only be reconstructed through combination of sufficient number of individuals",
            "broader": ("https://w3id.org/dpv#CryptographicMethods",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Sector": {
            "label": "Sector",
            "definition": "Sector describes the area of application or domain that indicates or restricts scope for interpretation and application of purpose e.g. Agriculture, Banking",
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#SecureMultiPartyComputation": {
            "label": "Secure Multi-Party Computation",
            "definition": "Use of cryptographic methods for entities to jointly compute functions without revealing inputs",
            "broader": ("https://w3id.org/dpv#CryptographicMethods",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#SecureProcessingEnvironment": {
            "label": "Secure Processing Environment",
            "definition": "A physical or virtual environment supported by organisational means that integrates security and compliance requirements and allows supervising data processing actions",
            "broader": ("https://w3id.org/dpv#SecurityProcedure",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#SecurityAssessment": {
            "label": "Security Assessment",
            "definition": "Assessment of security intended to identify gaps, vulnerabilities, risks, and effectiveness of controls",
            "broader": ("https://w3id.org/dpv#RiskAssessment",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#SecurityAudit": {
            "label": "Security Audit",
            "definition": "An audit that systematically examines the existence and use of security risks and measures within information systems, networks, and security policies to identify vulnerabilities, risks, and gaps",
            "broader": ("https://w3id.org/dpv#Audit",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#SecurityIncidentNotice": {
            "label": "Security Incident Notice",
            "definition": "A notice providing information about security incident(s)",
            "broader": ("https://w3id.org/dpv#Notice",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#SecurityIncidentNotification": {
            "label": "Security Incident Notification",
            "definition": "Notification of information about security incident(s)",
            "broader": ("https://w3id.org/dpv#Notification",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#SecurityIncidentRecord": {
            "label": "Security Incident Record",
            "definition": "Record of a security incident",
            "broader": ("https://w3id.org/dpv#RecordsOfActivities",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#SecurityKnowledgeTraining": {
            "label": "Security Knowledge Training",
            "definition": "Training intended to increase knowledge regarding security",
            "broader": ("https://w3id.org/dpv#StaffTraining",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#SecurityMethod": {
            "label": "Security Method",
            "definition": "Methods that relate to creating and providing security",
            "broader": ("https://w3id.org/dpv#TechnicalMeasure",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#SecurityProcedure": {
            "label": "Security Procedure",
            "definition": "Procedures associated with assessing, implementing, and evaluating security",
            "broader": ("https://w3id.org/dpv#OrganisationalMeasure",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#SecurityRoleProcedures": {
            "label": "Security Role Procedures",
            "definition": "Procedures related to security roles",
            "broader": ("https://w3id.org/dpv#SecurityProcedure",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#SellDataToThirdParties": {
            "label": "Sell Data to Third Parties",
            "definition": "Purposes associated with selling or sharing data or information to third parties",
            "broader": ("https://w3id.org/dpv#SellProducts",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#SellInsightsFromData": {
            "label": "Sell Insights from Data",
            "definition": "Purposes associated with selling or sharing insights obtained from analysis of data",
            "broader": ("https://w3id.org/dpv#SellProducts",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#SellProducts": {
            "label": "Sell Products",
            "definition": "Purposes associated with selling products or services",
            "broader": ("https://w3id.org/dpv#ServiceProvision",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#SellProductsToDataSubject": {
            "label": "Sell Products to Data Subject",
            "definition": "Purposes associated with selling products or services to the user, consumer, or data subjects",
            "broader": ("https://w3id.org/dpv#SellProducts",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#SemiPrivateSpace": {
            "label": "Semi Private Space",
            "definition": "A private space that acts as a shared space with other entities but which is still essentially private for the individuals e.g. a semi-private hospital room shared with another patient",
            "broader": ("https://w3id.org/dpv#PrivateSpace",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#SensitiveData": {
            "label": "Sensitive Data",
            "definition": "Data deemed sensitive",
            "broader": ("https://w3id.org/dpv#Data",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#SensitiveNonPersonalData": {
            "label": "Sensitive Non Personal Data",
            "definition": "Non-personal data deemed sensitive",
            "broader": ("https://w3id.org/dpv#SensitiveData",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#SensitivePersonalData": {
            "label": "Sensitive Personal Data",
            "definition": "Personal data that is considered 'sensitive' in terms of privacy and/or impact, and therefore requires additional considerations and/or protection",
            "broader": ("https://w3id.org/dpv#PersonalData", "https://w3id.org/dpv#SensitiveData"),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#SensitivityLevel": {
            "label": "Sensitivity Level",
            "definition": "Sensitivity' reflects the risk of impact if not secured or utilised with appropriate measures and controls e.g. for sensitive data",
            "broader": ("https://w3id.org/dpv#Severity",),
            "source_vocab": "DPV",
        },
        "https://w3id.org/dpv#Service": {
            "label": "Service",
            "definition": "A service is a process where one entity provides some benefit or assistance to another entity",
            "broader": ("https://w3id.org/dpv#Process",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ServiceAccessDetermination": {
            "label": "Service Access Determination",
            "definition": "Purposes associated with the determination of whether specific conditions or criteria are met for accessing, using, or gaining access to a service",
            "broader": ("https://w3id.org/dpv#ServiceManagement",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ServiceConsumer": {
            "label": "Service Consumer",
            "definition": "The entity that consumes or receives the service",
            "broader": ("https://w3id.org/dpv#LegalEntity",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ServiceLevelAgreement": {
            "label": "Service Level Agreement (SLA)",
            "definition": "A contract regarding the provision of a service which outlines the acceptable metrics and performance of the service for the consumer",
            "broader": ("https://w3id.org/dpv#ContractByDomain",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ServiceManagement": {
            "label": "Service Management",
            "definition": "Purposes associated with the management of services or products",
            "broader": ("https://w3id.org/dpv#Purpose",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ServiceMonitoring": {
            "label": "Service Monitoring",
            "definition": "Purposes associated with the monitoring of services or products to understand their performance and utilisation with a view to inform their management",
            "broader": ("https://w3id.org/dpv#ServiceManagement",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ServiceOptimisation": {
            "label": "Service Optimisation",
            "definition": "Purposes associated with optimisation of services or activities",
            "broader": ("https://w3id.org/dpv#ServiceManagement",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ServicePersonalisation": {
            "label": "Service Personalisation",
            "definition": "Purposes associated with providing personalisation within services or product or activities",
            "broader": ("https://w3id.org/dpv#Personalisation", "https://w3id.org/dpv#ServiceManagement"),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ServiceProvider": {
            "label": "Service Provider",
            "definition": "The entity that provides a service",
            "broader": ("https://w3id.org/dpv#LegalEntity",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ServiceProvision": {
            "label": "Service Provision",
            "definition": "Purposes associated with providing service or product or activities",
            "broader": ("https://w3id.org/dpv#ServiceManagement",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ServiceRegistration": {
            "label": "Service Registration",
            "definition": "Purposes associated with registering users and collecting information required for providing a service",
            "broader": ("https://w3id.org/dpv#ServiceManagement",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ServiceUsageAnalytics": {
            "label": "Service Usage Analytics",
            "definition": "Purposes associated with conducting analysis and reporting related to usage of services or products",
            "broader": ("https://w3id.org/dpv#ServiceMonitoring",),
            "source_vocab": "2026-02-08",
        },
        "https://w3id.org/dpv#Severity": {
            "label": "Severity",
            "definition": "The magnitude of being unwanted or having negative effects such as harmful impacts",
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Share": {
            "label": "Share",
            "definition": "to give data (or a portion of it) to others",
            "broader": ("https://w3id.org/dpv#Disclose",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#SingleSignOn": {
            "label": "Single Sign On",
            "definition": "Use of credentials or processes that enable using one set of credentials to authenticate multiple contexts.",
            "broader": ("https://w3id.org/dpv#AuthenticationProtocols",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#SingularDataVolume": {
            "label": "Singular Data Volume",
            "definition": "Data volume that is considered singular i.e. a specific instance or single item",
            "broader": ("https://w3id.org/dpv#DataVolume",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#SingularFrequency": {
            "label": "Singular Frequency",
            "definition": "Frequency where occurrences are singular i.e. they take place only once",
            "broader": ("https://w3id.org/dpv#Frequency",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#SingularScaleOfDataSubjects": {
            "label": "Singular Scale Of Data Subjects",
            "definition": "Scale of data subjects considered singular i.e. a specific data subject",
            "broader": ("https://w3id.org/dpv#DataSubjectScale",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#SmallDataVolume": {
            "label": "Small Data Volume",
            "definition": "Data volume that is considered small or limited within the context",
            "broader": ("https://w3id.org/dpv#DataVolume",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#SmallScaleOfDataSubjects": {
            "label": "Small Scale Of Data Subjects",
            "definition": "Scale of data subjects considered small or limited within the context",
            "broader": ("https://w3id.org/dpv#DataSubjectScale",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#SmallScaleProcessing": {
            "label": "Small Scale Processing",
            "definition": "Processing that takes place at small scales (as specified by some criteria)",
            "broader": ("https://w3id.org/dpv#ProcessingScale",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#SocialMediaMarketing": {
            "label": "Social Media Marketing",
            "definition": "Purposes associated with conducting marketing through social media",
            "broader": ("https://w3id.org/dpv#Marketing",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#SpecialCategoryPersonalData": {
            "label": "Special Category Personal Data",
            "definition": "Sensitive Personal Data whose use requires specific additional legal permission or justification",
            "broader": ("https://w3id.org/dpv#SensitivePersonalData",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#SporadicDataVolume": {
            "label": "Sporadic Data Volume",
            "definition": "Data volume that is considered sporadic or sparse within the context",
            "broader": ("https://w3id.org/dpv#DataVolume",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#SporadicFrequency": {
            "label": "Sporadic Frequency",
            "definition": "Frequency where occurrences are sporadic or infrequent or sparse",
            "broader": ("https://w3id.org/dpv#Frequency",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#SporadicScaleOfDataSubjects": {
            "label": "Sporadic Scale Of Data Subjects",
            "definition": "Scale of data subjects considered sporadic or sparse within the context",
            "broader": ("https://w3id.org/dpv#DataSubjectScale",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#StaffTraining": {
            "label": "Staff Training",
            "definition": "Practices and policies regarding training of staff members",
            "broader": ("https://w3id.org/dpv#OrganisationalMeasure",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Standard": {
            "label": "Standard",
            "definition": "A set of requirements or norms that are agreed upon i.e. they are considered a 'standard'",
            "broader": ("https://w3id.org/dpv#GuidelinesPrinciple",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#StandardFormContract": {
            "label": "Standard Form Contract",
            "definition": "A contract where the terms and conditions are determined by one or more of the parties, and the other parties have negligible or no ability to negotiate the terms and conditions",
            "broader": ("https://w3id.org/dpv#ContractByNegotiationType",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#StandardsConformance": {
            "label": "Standards Conformance",
            "definition": "Purposes associated with activities undertaken to ensure or achieve conformance with standards",
            "broader": ("https://w3id.org/dpv#GovernanceProcedures",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#StartupOrganisation": {
            "label": "Startup Organisation",
            "definition": "An organisation that is newly established and is nascent in terms of available resources",
            "broader": ("https://w3id.org/dpv#LegalEntity",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#StatisticalConfidentialityAgreement": {
            "label": "Statistical Confidentiality Agreement",
            "definition": "An agreement outlining conditions, criteria, obligations, responsibilities, and specifics for classification and management of 'confidential data' based on a statistical framework",
            "broader": ("https://w3id.org/dpv#LegalAgreement",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#StatisticallyConfidentialData": {
            "label": "Statistically Confidential Data",
            "definition": "Data protected through Statistical Confidentiality regulations and agreements",
            "broader": ("https://w3id.org/dpv#ConfidentialData",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Status": {
            "label": "Status",
            "definition": "The status or state of something",
            "broader": ("https://w3id.org/dpv#Context",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#StorageCondition": {
            "label": "Storage Condition",
            "definition": "Conditions required or followed regarding storage of data",
            "broader": ("https://w3id.org/dpv#ProcessingCondition",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#StorageDeletion": {
            "label": "Storage Deletion",
            "definition": "Deletion or Erasure of data including any deletion guarantees",
            "broader": ("https://w3id.org/dpv#StorageCondition",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#StorageDuration": {
            "label": "Storage Duration",
            "definition": "Duration or temporal limitation on storage of data",
            "broader": ("https://w3id.org/dpv#ProcessingDuration", "https://w3id.org/dpv#StorageCondition"),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#StorageLocation": {
            "label": "Storage Location",
            "definition": "Location or geospatial scope where the data is stored",
            "broader": ("https://w3id.org/dpv#ProcessingLocation", "https://w3id.org/dpv#StorageCondition"),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#StorageRestoration": {
            "label": "Storage Restoration",
            "definition": "Regularity and temporal span of data restoration/backup mechanisms that guarantee that data is preserved",
            "broader": ("https://w3id.org/dpv#StorageCondition",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Store": {
            "label": "Store",
            "definition": "to keep data for future use",
            "broader": ("https://w3id.org/dpv#Processing",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Structure": {
            "label": "Structure",
            "definition": "to arrange data according to a structure",
            "broader": ("https://w3id.org/dpv#Organise",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Student": {
            "label": "Student",
            "definition": "Humans that are students",
            "broader": ("https://w3id.org/dpv#HumanSubject",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#SubProcessorAgreement": {
            "label": "Sub-Processor Agreement",
            "definition": "An agreement outlining conditions, criteria, obligations, responsibilities, and specifics for carrying out processing of data between a Data Processor and a Data (Sub-)Processor",
            "broader": ("https://w3id.org/dpv#DataProcessingAgreement",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Subscriber": {
            "label": "Subscriber",
            "definition": "Humans that subscribe to service(s)",
            "broader": ("https://w3id.org/dpv#HumanSubject",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#SubsidiaryLegalEntity": {
            "label": "Subsidiary Legal Entity",
            "definition": "A legal entity that operates as a subsidiary of another legal entity",
            "broader": ("https://w3id.org/dpv#Organisation",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#SupportContractNegotiation": {
            "label": "Support Contract Negotiation",
            "definition": "Supporting entities, including individuals, with negotiating a contract and its terms and conditions",
            "broader": ("https://w3id.org/dpv#SupportEntityDecisionMaking",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#SupportEntityDecisionMaking": {
            "label": "Support Entity Decision Making",
            "definition": "Supporting entities, including individuals, in making decisions",
            "broader": ("https://w3id.org/dpv#OrganisationalMeasure",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#SupportExchangeOfViews": {
            "label": "Support Exchange of Views",
            "definition": "Supporting individuals and entities in exchanging views e.g. regarding data processing purposes for their best interests",
            "broader": ("https://w3id.org/dpv#SupportEntityDecisionMaking",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#SupportInformedConsentDecision": {
            "label": "Support Informed Consent Decision",
            "definition": "Supporting individuals with making a decision regarding their informed consent",
            "broader": ("https://w3id.org/dpv#SupportEntityDecisionMaking",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#SupraNationalAuthority": {
            "label": "Supranational Authority",
            "definition": "An authority tasked with overseeing legal compliance for a supra-national union e.g. EU",
            "broader": ("https://w3id.org/dpv#Authority",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#SupraNationalUnion": {
            "label": "Supranational Union",
            "definition": "A political union of two or more countries with an establishment of common authority",
            "broader": ("https://w3id.org/dpv#Jurisdiction",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#SymmetricCryptography": {
            "label": "Symmetric Cryptography",
            "definition": "Use of cryptography where the same keys are utilised for encryption and decryption of information",
            "broader": ("https://w3id.org/dpv#CryptographicMethods",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#SymmetricEncryption": {
            "label": "Symmetric Encryption",
            "definition": "Use of symmetric cryptography to encrypt data",
            "broader": ("https://w3id.org/dpv#Encryption",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#SyntheticData": {
            "label": "Synthetic Data",
            "definition": "Synthetic data refers to artificially created data such that it is intended to resemble real data (personal or non-personal), but does not refer to any specific identified or identifiable individual, or to the real measure of an observable parameter in the case of non-personal data",
            "broader": ("https://w3id.org/dpv#GeneratedData",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#SystematicMonitoring": {
            "label": "Systematic Monitoring",
            "definition": "Processing that involves systematic monitoring of individuals",
            "broader": ("https://w3id.org/dpv#ProcessingContext",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#TargetedAdvertising": {
            "label": "Targeted Advertising",
            "definition": "Purposes associated with creating and providing personalised advertisement where the personalisation is targeted to a specific individual or group of individuals",
            "broader": ("https://w3id.org/dpv#PersonalisedAdvertising",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#TechnicalMeasure": {
            "label": "Technical Measure",
            "definition": "Technical measures used to safeguard and ensure good practices in connection with data and technologies",
            "broader": ("https://w3id.org/dpv#TechnicalOrganisationalMeasure",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#TechnicalOrganisationalMeasure": {
            "label": "Technical and Organisational Measure",
            "definition": "Technical and Organisational measures used to safeguard and ensure good practices in connection with data and technologies",
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#TechnicalServiceProvision": {
            "label": "Technical Service Provision",
            "definition": "Purposes associated with managing and providing technical processes and functions necessary for delivering services",
            "broader": ("https://w3id.org/dpv#ServiceProvision",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#TechnicalStandard": {
            "label": "Technical Standard",
            "definition": "A technical standard is a standard that establishes norms or requirements regarding technology or technical processes",
            "broader": ("https://w3id.org/dpv#Standard",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Technology": {
            "label": "Technology",
            "definition": "The technology, technological implementation, or any techniques, skills, methods, and processes used or applied",
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#TemporalDuration": {
            "label": "Temporal Duration",
            "definition": "Duration that has a fixed temporal duration e.g. 6 months",
            "broader": ("https://w3id.org/dpv#Duration",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#TerminateContract": {
            "label": "Terminate Contract",
            "definition": "Control for terminating a contract",
            "broader": ("https://w3id.org/dpv#ContractControl",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#TermsOfService": {
            "label": "Terms of Service",
            "definition": "Contractual clauses outlining the terms and conditions regarding the provision of a service, typically between a service provider and a service consumer, also know as 'Terms of Use' and 'Terms and Conditions' and commonly abbreviated as TOS, ToS, ToU, or T&C",
            "broader": ("https://w3id.org/dpv#ContractualClause",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ThirdCountry": {
            "label": "Third Country",
            "definition": "Represents a country outside applicable or compatible jurisdiction as outlined in law",
            "broader": ("https://w3id.org/dpv#Country",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ThirdParty": {
            "label": "Third Party",
            "definition": "A ‘third party’ means any natural or legal person other than - the entities directly involved or operating under those directly involved in a process",
            "broader": ("https://w3id.org/dpv#LegalEntity",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ThirdPartyAgreement": {
            "label": "Third-Party Agreement",
            "definition": "An agreement outlining conditions, criteria, obligations, responsibilities, and specifics for carrying out processing of data between a Data Controller or Processor and a Third Party",
            "broader": ("https://w3id.org/dpv#ThirdPartyContract",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ThirdPartyContract": {
            "label": "Third Party Contract",
            "definition": "Creation, completion, fulfilment, or performance of a contract, with the Data Controller and Third Party as parties, and involving specified processing of data or technologies. NOTE: This concept is being deprecated - use dpv:ThirdPartyAgreement which has a more explicit definition of the entitie...",
            "broader": ("https://w3id.org/dpv#DataProcessingAgreement",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ThirdPartyDataSource": {
            "label": "Third Party as Data Source",
            "definition": "Data Sourced from a Third Party, e.g. when data is collected from an entity that is neither the Controller nor the Data Subject",
            "broader": ("https://w3id.org/dpv#DataSource",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ThirdPartySecurityProcedures": {
            "label": "Third Party Security Procedures",
            "definition": "Procedures related to security associated with Third Parties",
            "broader": ("https://w3id.org/dpv#SecurityProcedure",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Tourist": {
            "label": "Tourist",
            "definition": "Humans that are tourists i.e. not citizens and not immigrants",
            "broader": ("https://w3id.org/dpv#HumanSubject",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Tracking": {
            "label": "Tracking",
            "definition": "to use data to track a specific factor (e.g. a human or their activities) across multiple distinct contexts",
            "broader": ("https://w3id.org/dpv#Use",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#TrackingByFirstParty": {
            "label": "Tracking by First Party",
            "definition": "to perform tracking where the performing entity is a first party within the context",
            "broader": ("https://w3id.org/dpv#Tracking",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#TrackingByThirdParty": {
            "label": "Tracking by Third Party",
            "definition": "to perform tracking where the performing entity is a third party within the context",
            "broader": ("https://w3id.org/dpv#Tracking",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Transfer": {
            "label": "Transfer",
            "definition": "to move data from one place to another",
            "broader": ("https://w3id.org/dpv#Processing",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Transform": {
            "label": "Transform",
            "definition": "to change the form or nature of data",
            "broader": ("https://w3id.org/dpv#Processing",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Transmit": {
            "label": "Transmit",
            "definition": "to send out data",
            "broader": ("https://w3id.org/dpv#Disclose",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#TrustedComputing": {
            "label": "Trusted Computing",
            "definition": "Use of cryptographic methods to restrict access and execution to trusted parties and code",
            "broader": ("https://w3id.org/dpv#CryptographicMethods",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#TrustedExecutionEnvironment": {
            "label": "Trusted Execution Environment",
            "definition": "Use of cryptographic methods to restrict access and execution to trusted parties and code within a dedicated execution environment",
            "broader": ("https://w3id.org/dpv#CryptographicMethods",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#UnacceptableRule": {
            "label": "Unacceptable Rule",
            "definition": "A rule that is unacceptable where it is not desirable if it occurs",
            "broader": ("https://w3id.org/dpv#Rule",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#UncategorisedData": {
            "label": "Uncategorised Data",
            "definition": "Data whose categorisation is not known e.g. whether it is personal or non-personal data",
            "broader": ("https://w3id.org/dpv#Data",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Unexpected": {
            "label": "Unexpected",
            "definition": "Status indicating the specified context was unexpected i.e. not expected",
            "broader": ("https://w3id.org/dpv#ExpectationStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#UninformedConsent": {
            "label": "Uninformed Consent",
            "definition": "Consent that is uninformed i.e. without requirement to provide sufficient information to make a consenting decision",
            "broader": ("https://w3id.org/dpv#Consent",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Unintended": {
            "label": "Unintended",
            "definition": "Status indicating the specified context was unintended i.e. not intended",
            "broader": ("https://w3id.org/dpv#IntentionStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#UnknownApplicability": {
            "label": "Unknown Applicability",
            "definition": "Concept indicating information or context availability is unknown i.e. it is not known if the information exists or is applicable and therefore statements about its availability cannot be made (yet)",
            "broader": ("https://w3id.org/dpv#Applicability",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Unlawful": {
            "label": "Unlawful",
            "definition": "State of being unlawful or legally non-compliant",
            "broader": ("https://w3id.org/dpv#Lawfulness",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#UnstructuredData": {
            "label": "Unstructured Data",
            "definition": "Data that is without a predefined data model or is not organised in a pre-defined manner",
            "broader": ("https://w3id.org/dpv#Data",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#UntilEventDuration": {
            "label": "Until Event Duration",
            "definition": "Duration that takes place until a specific event occurs e.g. Account Closure",
            "broader": ("https://w3id.org/dpv#Duration",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#UntilTimeDuration": {
            "label": "Until Time Duration",
            "definition": "Duration that has a fixed end date e.g. 2022-12-31",
            "broader": ("https://w3id.org/dpv#Duration",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#UnverifiedData": {
            "label": "Unverified Data",
            "definition": "Data that has not been verified in terms of accuracy, inconsistency, or quality",
            "broader": ("https://w3id.org/dpv#Data",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#UsageControl": {
            "label": "Usage Control",
            "definition": "Management of usage, which is intended to be broader than access control and may cover trust, digital rights, or other relevant controls",
            "broader": ("https://w3id.org/dpv#AccessControlMethod",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Use": {
            "label": "Use",
            "definition": "to use data",
            "broader": ("https://w3id.org/dpv#Processing",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#UseSyntheticData": {
            "label": "Use of Synthetic Data",
            "definition": "Use of synthetic data to preserve privacy, security, or other effects and side-effects",
            "broader": ("https://w3id.org/dpv#SecurityMethod",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#User": {
            "label": "User",
            "definition": "Humans that use service(s)",
            "broader": ("https://w3id.org/dpv#HumanSubject",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#UserInterfacePersonalisation": {
            "label": "User Interface Personalisation",
            "definition": "Purposes associated with personalisation of interfaces presented to the user",
            "broader": ("https://w3id.org/dpv#ServicePersonalisation",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#VariableLocation": {
            "label": "Variable Location",
            "definition": "Location that is known but is variable e.g. somewhere within a given area",
            "broader": ("https://w3id.org/dpv#LocationFixture",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#VendorManagement": {
            "label": "Vendor Management",
            "definition": "Purposes associated with manage orders, payment, evaluation, and prospecting related to vendors",
            "broader": ("https://w3id.org/dpv#Purpose",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#VendorPayment": {
            "label": "Vendor Payment",
            "definition": "Purposes associated with managing payment of vendors",
            "broader": ("https://w3id.org/dpv#VendorManagement",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#VendorRecordsManagement": {
            "label": "Vendor Records Management",
            "definition": "Purposes associated with managing records and orders related to vendors",
            "broader": ("https://w3id.org/dpv#VendorManagement",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#VendorSelectionAssessment": {
            "label": "Vendor Selection Assessment",
            "definition": "Purposes associated with managing selection, assessment, and evaluation related to vendors",
            "broader": ("https://w3id.org/dpv#VendorManagement",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Verification": {
            "label": "Verification",
            "definition": "Purposes association with verification e.g. information, identity, integrity",
            "broader": ("https://w3id.org/dpv#EnforceSecurity",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#VerifiedData": {
            "label": "Verified Data",
            "definition": "Data that has been verified in terms of accuracy, consistency, or quality",
            "broader": ("https://w3id.org/dpv#Data",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#VirtualisationSecurity": {
            "label": "Virtualisation Security",
            "definition": "Security implemented at or through virtualised environments",
            "broader": ("https://w3id.org/dpv#SecurityMethod",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#Visitor": {
            "label": "Visitor",
            "definition": "Humans that are temporary visitors",
            "broader": ("https://w3id.org/dpv#HumanSubject",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#VitalInterest": {
            "label": "Vital Interest",
            "definition": "Activities are necessary or required to protect vital interests of a data subject or other natural person",
            "broader": ("https://w3id.org/dpv#LegalBasis",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#VitalInterestCompleted": {
            "label": "Vital Interest Completed",
            "definition": "Status where the vital interest activity has been completed",
            "broader": ("https://w3id.org/dpv#VitalInterestStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#VitalInterestObjected": {
            "label": "Vital Interest Objected",
            "definition": "Status where the vital interest activity was objected to by the Data Subject or another relevant entity",
            "broader": ("https://w3id.org/dpv#VitalInterestStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#VitalInterestOfDataSubject": {
            "label": "Vital Interest of Data Subject",
            "definition": "Activities are necessary or required to protect vital interests of a data subject",
            "broader": ("https://w3id.org/dpv#VitalInterestOfNaturalPerson",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#VitalInterestOfNaturalPerson": {
            "label": "Vital Interest of Natural Person",
            "definition": "Activities are necessary or required to protect vital interests of a natural person",
            "broader": ("https://w3id.org/dpv#VitalInterest",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#VitalInterestOngoing": {
            "label": "Vital Interest Ongoing",
            "definition": "Status where the vital interest activity is ongoing",
            "broader": ("https://w3id.org/dpv#VitalInterestStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#VitalInterestPending": {
            "label": "Vital Interest Pending",
            "definition": "Status where the vital interest activity has not started",
            "broader": ("https://w3id.org/dpv#VitalInterestStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#VitalInterestStatus": {
            "label": "Vital Interest Status",
            "definition": "Status associated with use of Vital Interest as a legal basis",
            "broader": ("https://w3id.org/dpv#Status",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#VulnerabilityTestingMethods": {
            "label": "Vulnerability Testing Methods",
            "definition": "Methods that assess or discover vulnerabilities in a system",
            "broader": ("https://w3id.org/dpv#SecurityMethod",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#VulnerableDataSubject": {
            "label": "Vulnerable Data Subject",
            "definition": "Humans which should be considered 'vulnerable' and therefore would require additional measures and safeguards",
            "broader": ("https://w3id.org/dpv#VulnerableHuman",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#VulnerableHuman": {
            "label": "Vulnerable Human",
            "definition": "Human(s) which should be considered 'vulnerable' within the context",
            "broader": ("https://w3id.org/dpv#HumanSubject",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#WebBrowserSecurity": {
            "label": "WebBrowser Security",
            "definition": "Security implemented at or over web browsers",
            "broader": ("https://w3id.org/dpv#SecurityMethod",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#WebSecurityProtocols": {
            "label": "Web Security Protocols",
            "definition": "Security implemented at or over web-based protocols",
            "broader": ("https://w3id.org/dpv#SecurityMethod",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#WirelessSecurityProtocols": {
            "label": "Wireless Security Protocols",
            "definition": "Security implemented at or over wireless communication protocols",
            "broader": ("https://w3id.org/dpv#SecurityMethod",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#WithdrawConsent": {
            "label": "Withdraw Consent",
            "definition": "Control for withdrawing consent",
            "broader": ("https://w3id.org/dpv#ConsentControl", "https://w3id.org/dpv#WithdrawingFromProcess"),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#WithdrawingFromProcess": {
            "label": "Withdrawing from Process",
            "definition": "Involvement where entity can withdraw a previously given assent from specified context",
            "broader": ("https://w3id.org/dpv#EntityPermissiveInvolvement",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#WithinDevice": {
            "label": "Within Device (deprecated)",
            "definition": "Location is local and entirely within a device, such as a smartphone",
            "broader": ("https://w3id.org/dpv#LocalLocation",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#WithinPhysicalEnvironment": {
            "label": "Within Physical Environment",
            "definition": "Location is local and entirely within a physical environment, such as a room",
            "broader": ("https://w3id.org/dpv#Location",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#WithinVirtualEnvironment": {
            "label": "Within Virtual Environment",
            "definition": "Location is local and entirely within a virtual environment, such as a software system",
            "broader": ("https://w3id.org/dpv#Location",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#ZeroKnowledgeAuthentication": {
            "label": "Zero Knowledge Authentication",
            "definition": "Authentication using Zero-Knowledge proofs",
            "broader": ("https://w3id.org/dpv#AuthenticationProtocols", "https://w3id.org/dpv#CryptographicMethods"),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasActiveEntity": {
            "label": "has active entity",
            "definition": "indicates the entity is actively involved in specified context",
            "broader": ("https://w3id.org/dpv#hasEntity",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasActivityStatus": {
            "label": "has activity status",
            "definition": "Indicates the status of activity of specified concept",
            "broader": ("https://w3id.org/dpv#hasStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasAddress": {
            "label": "has address",
            "definition": "Specifies address of a legal entity such as street address or pin code",
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasAlgorithmicLogic": {
            "label": "has algorithmic logic",
            "definition": "Indicates the logic used in processing such as for automated decision making",
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasApplicability": {
            "label": "has applicability",
            "definition": "Indicates situations where the context is not applicable, information is not available, or this is unknown. An appropriate instance of dpv:Applicability should be used with this relation to express the situation",
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasApplicableLaw": {
            "label": "has applicable law",
            "definition": "Indicates applicability of a Law",
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasAssessment": {
            "label": "has assessment",
            "definition": "Indicates a relevant assessment associated with the specific context",
            "broader": ("https://w3id.org/dpv#hasOrganisationalMeasure",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasAuditStatus": {
            "label": "has audit status",
            "definition": "Indicates the status of audit associated with specified concept",
            "broader": ("https://w3id.org/dpv#hasStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasAuthority": {
            "label": "has authority",
            "definition": "Indicates applicability of authority for a jurisdiction",
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasAutomationLevel": {
            "label": "has automation level",
            "definition": "Indicates the level of automation involved in implementation of the specified context",
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasComplianceStatus": {
            "label": "has compliance status",
            "definition": "Indicates the status of compliance of specified concept",
            "broader": ("https://w3id.org/dpv#hasStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasConformanceStatus": {
            "label": "has conformance status",
            "definition": "Indicates the status of being conformant or non-conformant",
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasConsentControl": {
            "label": "has consent control",
            "definition": "Specific a control associated with consent",
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasConsentStatus": {
            "label": "has consent status",
            "definition": "Specifies the state or status of consent",
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasConsequence": {
            "label": "has consequence",
            "definition": "Indicates consequence(s) possible or arising from specified concept",
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasConsequenceOn": {
            "label": "has consequence on",
            "definition": "Indicates the thing (e.g. plan, process, or entity) affected by a consequence",
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasContact": {
            "label": "has contact",
            "definition": "Specifies contact details of a legal entity such as phone or email",
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasContext": {
            "label": "has context",
            "definition": "Indicates a purpose is restricted to the specified context(s)",
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasContractControl": {
            "label": "has contract control",
            "definition": "Indicates the contract to be used with a contract",
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasContractStatus": {
            "label": "has contract status",
            "definition": "Indicates the status of the contract",
            "broader": ("https://w3id.org/dpv#hasStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasContractualClause": {
            "label": "has contractual clause",
            "definition": "Indicates the association or involvement of specified contractual clause",
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasContractualFulfilmentStatus": {
            "label": "has contractual fulfilment status",
            "definition": "Indicates the fulfilment status of a contract or a contractual clause",
            "broader": ("https://w3id.org/dpv#hasContractStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasCountry": {
            "label": "has country",
            "definition": "Indicates applicability of specified country",
            "broader": ("https://w3id.org/dpv#hasLocation",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasData": {
            "label": "has data",
            "definition": "Indicates associated with Data (may or may not be personal)",
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasDataController": {
            "label": "has data controller",
            "definition": "Indicates association with Data Controller",
            "broader": ("https://w3id.org/dpv#hasEntity",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasDataExporter": {
            "label": "has data exporter",
            "definition": "Indicates inclusion or applicability of a LegalEntity in the role of Data Exporter",
            "broader": ("https://w3id.org/dpv#hasEntity",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasDataImporter": {
            "label": "has data importer",
            "definition": "Indicates inclusion or applicability of a LegalEntity in the role of Data Importer",
            "broader": ("https://w3id.org/dpv#hasRecipient",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasDataProcessor": {
            "label": "has data processor",
            "definition": "Indicates inclusion or applicability of a Data Processor",
            "broader": ("https://w3id.org/dpv#hasRecipient",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasDataProtectionOfficer": {
            "label": "has data protection officer",
            "definition": "Specifies an associated data protection officer",
            "broader": ("https://w3id.org/dpv#hasRepresentative",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasDataSource": {
            "label": "has data source",
            "definition": "Indicates the source or origin of data being processed",
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasDataSubject": {
            "label": "has data subject",
            "definition": "Indicates association with Data Subject",
            "broader": ("https://w3id.org/dpv#hasHumanSubject",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasDataSubjectScale": {
            "label": "has data subject scale",
            "definition": "Indicates the scale of data subjects",
            "broader": ("https://w3id.org/dpv#hasScale",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasDataVolume": {
            "label": "has data volume",
            "definition": "Indicates the volume of data",
            "broader": ("https://w3id.org/dpv#hasScale",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasDeterrence": {
            "label": "has deterrence",
            "definition": "Specifies applicability or inclusion of a deterrence rule within specified context",
            "broader": ("https://w3id.org/dpv#hasRule",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasDuration": {
            "label": "has duration",
            "definition": "Indicates information about duration",
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasEntity": {
            "label": "has entity",
            "definition": "Indicates inclusion or applicability of an entity to some concept",
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasEntityControl": {
            "label": "has entity control",
            "definition": "Indicates a control or measure provided for an entity to perform the specified action",
            "broader": ("https://w3id.org/dpv#hasTechnicalOrganisationalMeasure",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasEntityInvolvement": {
            "label": "has entity involvement",
            "definition": "Indicates involvement of an entity in specified context",
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasExpectation": {
            "label": "has expectation",
            "definition": "Indicates whether the specified context was expected or unexpected",
            "broader": ("https://w3id.org/dpv#hasStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasFee": {
            "label": "has fee",
            "definition": "Indicates whether a fee is required for the specified context",
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasFrequency": {
            "label": "has frequency",
            "definition": "Indicates the frequency with which something takes place",
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasFulfilmentStatus": {
            "label": "has fulfilment status",
            "definition": "Specifies the fulfillment status associated with a rule",
            "broader": ("https://w3id.org/dpv#hasStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasGeographicCoverage": {
            "label": "has geographic coverage",
            "definition": "Indicates the geographic coverage (of specified context)",
            "broader": ("https://w3id.org/dpv#hasScale",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasHumanInvolvement": {
            "label": "has human involvement",
            "definition": "Indicates Involvement of humans in processing such as within automated decision making process",
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasHumanSubject": {
            "label": "has human subject",
            "definition": "Indicates association with Human Subject",
            "broader": ("https://w3id.org/dpv#hasEntity",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasIdentifier": {
            "label": "has identifier",
            "definition": "Indicates an identifier associated for identification or reference",
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasImpact": {
            "label": "has impact",
            "definition": "Indicates impact(s) possible or arising as consequences from specified concept",
            "broader": ("https://w3id.org/dpv#hasConsequence",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasImpactAssessment": {
            "label": "has impact assessment",
            "definition": "Indicates an impact assessment associated with the specific context",
            "broader": ("https://w3id.org/dpv#hasAssessment",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasImpactOn": {
            "label": "has impact on",
            "definition": "Indicates the thing (e.g. plan, process, or entity) affected by an impact",
            "broader": ("https://w3id.org/dpv#hasConsequenceOn",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasImportance": {
            "label": "has importance",
            "definition": "Indicates the importance for specified context or criteria",
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasIndicationMethod": {
            "label": "has indication method",
            "definition": "Specifies the method by which an entity has indicated the specific context",
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasInformedStatus": {
            "label": "has informed status",
            "definition": "Indicates whether an entity was informed or uninformed",
            "broader": ("https://w3id.org/dpv#hasStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasIntention": {
            "label": "has intention",
            "definition": "Indicates whether the specified context was intended or unintended",
            "broader": ("https://w3id.org/dpv#hasStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasInverseJurisdiction": {
            "label": "has inverse jurisdiction",
            "definition": "Indicates the inverse jurisdiction for a given jurisdiction",
            "broader": ("https://w3id.org/dpv#hasLocation",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasInvolvement": {
            "label": "has involvement",
            "definition": "Indicates the involvement status for the specified context",
            "broader": ("https://w3id.org/dpv#hasStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasJointDataControllers": {
            "label": "has joint data controllers",
            "definition": "Indicates inclusion or applicability of a Joint Data Controller",
            "broader": ("https://w3id.org/dpv#hasDataController",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasJurisdiction": {
            "label": "has jurisdiction",
            "definition": "Indicates applicability of specified jurisdiction",
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasJustification": {
            "label": "has justification",
            "definition": "Indicates a justification for specified concept or context",
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasLawfulness": {
            "label": "has lawfulness",
            "definition": "Indicates the status of being lawful or legally compliant",
            "broader": ("https://w3id.org/dpv#hasComplianceStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasLegalBasis": {
            "label": "has legal basis",
            "definition": "Indicates use or applicability of a Legal Basis",
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasLegalMeasure": {
            "label": "has legal measure",
            "definition": "Indicates use or applicability of Legal measure",
            "broader": ("https://w3id.org/dpv#hasOrganisationalMeasure",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasLikelihood": {
            "label": "has likelihood",
            "definition": "Indicates the likelihood associated with a concept",
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasLocation": {
            "label": "has location",
            "definition": "Indicates information about location",
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasName": {
            "label": "has name",
            "definition": "Specifies name of a legal entity",
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasNecessity": {
            "label": "has necessity",
            "definition": "Indicates the necessity for specified context or criteria",
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasNonInvolvedEntity": {
            "label": "has non-involved entity",
            "definition": "indicates the entity is not involved in specified context",
            "broader": ("https://w3id.org/dpv#hasEntity",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasNonPersonalDataProcess": {
            "label": "has non-personal data process",
            "definition": "Indicates association with a Non-Personal Data Process",
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasNotice": {
            "label": "has notice",
            "definition": "Indicates the use or applicability of a Notice for the specified context",
            "broader": ("https://w3id.org/dpv#hasOrganisationalMeasure",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasNoticeIcon": {
            "label": "has notice icon",
            "definition": "Indicates the concept can be represented graphically using the specified icon",
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasNoticeLayer": {
            "label": "has notice layer",
            "definition": "Indicates the use of a notice layer within a notice or to associate a layer with another layer",
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasNoticeStatus": {
            "label": "has notice status",
            "definition": "Indicates the status of the associated notice",
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasNotificationStatus": {
            "label": "has notification status",
            "definition": "Indicates the status associated with a notice",
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasObligation": {
            "label": "has obligation",
            "definition": "Specifies applicability or inclusion of an obligation rule within specified context",
            "broader": ("https://w3id.org/dpv#hasRule",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasOrganisationalMeasure": {
            "label": "has organisational measure",
            "definition": "Indicates use or applicability of Organisational measure",
            "broader": ("https://w3id.org/dpv#hasTechnicalOrganisationalMeasure",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasOrganisationalUnit": {
            "label": "has organisational unit",
            "definition": "Indicates the specified entity is a unit of the organisation",
            "broader": ("https://w3id.org/dpv#hasEntity",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasOutcome": {
            "label": "has outcome",
            "definition": "Indicates an outcome of specified concept or context",
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasParty": {
            "label": "has party",
            "definition": "Indicates a legal entity involved as a party in a contract",
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasPassiveEntity": {
            "label": "has passive entity",
            "definition": "indicates the entity is passively involved in specified context",
            "broader": ("https://w3id.org/dpv#hasEntity",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasPermission": {
            "label": "has permission",
            "definition": "Specifies applicability or inclusion of a permission rule within specified context",
            "broader": ("https://w3id.org/dpv#hasRule",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasPersonalData": {
            "label": "has personal data",
            "definition": "Indicates association with Personal Data",
            "broader": ("https://w3id.org/dpv#hasData",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasPersonalDataHandling": {
            "label": "has personal data handling",
            "definition": "Indicates association with Personal Data Handling",
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasPersonalDataProcess": {
            "label": "has personal data process",
            "definition": "Indicates association with a Personal Data Process",
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasPhysicalMeasure": {
            "label": "has physical measure",
            "definition": "Indicates use or applicability of Physical measure",
            "broader": ("https://w3id.org/dpv#hasTechnicalOrganisationalMeasure",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasPolicy": {
            "label": "has policy",
            "definition": "Indicates policy applicable or used",
            "broader": ("https://w3id.org/dpv#hasTechnicalOrganisationalMeasure",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasProcess": {
            "label": "has process",
            "definition": "Indicates association with a Process",
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasProcessing": {
            "label": "has processing",
            "definition": "Indicates association with Processing",
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasProcessingCondition": {
            "label": "has processing condition",
            "definition": "Indicates information about processing condition",
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasProcessingScale": {
            "label": "has processing scale",
            "definition": "Indicates the scale of processing operations",
            "broader": ("https://w3id.org/dpv#hasScale",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasProhibition": {
            "label": "has prohibition",
            "definition": "Specifies applicability or inclusion of a prohibition rule within specified context",
            "broader": ("https://w3id.org/dpv#hasRule",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasPurpose": {
            "label": "has purpose",
            "definition": "Indicates association with Purpose",
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasRecipient": {
            "label": "has recipient",
            "definition": "Indicates Recipient of Data",
            "broader": ("https://w3id.org/dpv#hasEntity",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasRecipientDataController": {
            "label": "has recipient data controller",
            "definition": "Indicates inclusion or applicability of a Data Controller as a Recipient of personal data",
            "broader": ("https://w3id.org/dpv#hasRecipient",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasRecipientThirdParty": {
            "label": "has recipient third party",
            "definition": "Indicates inclusion or applicability of a Third Party as a Recipient of personal data",
            "broader": ("https://w3id.org/dpv#hasRecipient",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasRecommendation": {
            "label": "has recommendation",
            "definition": "Specifies applicability or inclusion of a recommendation rule within specified context",
            "broader": ("https://w3id.org/dpv#hasRule",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasRecordOfActivity": {
            "label": "has record of activity",
            "definition": "Indicates a relevant record of activity",
            "broader": ("https://w3id.org/dpv#hasOrganisationalMeasure",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasRelationWithDataSubject": {
            "label": "has relation with data subject",
            "definition": "Indicates the relation between specified Entity and Data Subject",
            "broader": ("https://w3id.org/dpv#hasEntity",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasRepresentative": {
            "label": "has representative",
            "definition": "Specifies representative of the legal entity",
            "broader": ("https://w3id.org/dpv#hasEntity",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasRequestStatus": {
            "label": "has request status",
            "definition": "Indicates the status associated with a request",
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasResidualRisk": {
            "label": "has residual risk",
            "definition": "Indicates the associated risk is the remaining or residual risk from applying mitigation measures or treatments to this risk",
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasResponsibleEntity": {
            "label": "has responsible entity",
            "definition": "Specifies the indicated entity is responsible within some context",
            "broader": ("https://w3id.org/dpv#hasEntity",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasReuseCompatibility": {
            "label": "has reuse compatibility",
            "definition": "Indicates the reuse compatibility for the specified context",
            "broader": ("https://w3id.org/dpv#hasStatus",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasRight": {
            "label": "has right",
            "definition": "Indicates use or applicability of Right",
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasRisk": {
            "label": "has risk",
            "definition": "Indicates applicability of Risk for this concept",
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasRiskAssessment": {
            "label": "has risk assessment",
            "definition": "Indicates an associated risk assessment",
            "broader": ("https://w3id.org/dpv#hasAssessment",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasRiskLevel": {
            "label": "has risk level",
            "definition": "Indicates the associated risk level associated with a risk",
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasRule": {
            "label": "has rule",
            "definition": "Specifies applicability or inclusion of a rule within specified context",
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasScale": {
            "label": "has scale",
            "definition": "Indicates the scale of specified concept",
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasScope": {
            "label": "has scope",
            "definition": "Indicates the scope of specified concept or context",
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasSector": {
            "label": "has sector",
            "definition": "Indicates the purpose is associated with activities in the indicated (Economic) Sector(s)",
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasSensitivityLevel": {
            "label": "has sensitivity level",
            "definition": "Indicates the associated level of sensitivity",
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasService": {
            "label": "has service",
            "definition": "Indicates associated with the specified service",
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasServiceConsumer": {
            "label": "has service consumer",
            "definition": "Indicates the entity that consumes or receives the associated service",
            "broader": ("https://w3id.org/dpv#hasEntity",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasServiceProvider": {
            "label": "has service provider",
            "definition": "Indicates the entity that provides the associated service",
            "broader": ("https://w3id.org/dpv#hasEntity",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasSeverity": {
            "label": "has severity",
            "definition": "Indicates the severity associated with a concept",
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasStatus": {
            "label": "has status",
            "definition": "Indicates the status of specified concept",
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasStorageCondition": {
            "label": "has storage condition",
            "definition": "Indicates information about storage condition",
            "broader": ("https://w3id.org/dpv#hasProcessingCondition",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasSubsidiary": {
            "label": "has subsidiary",
            "definition": "Indicates this entity has the specified entity as its subsidiary",
            "broader": ("https://w3id.org/dpv#hasEntity",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasTechnicalMeasure": {
            "label": "has technical measure",
            "definition": "Indicates use or applicability of Technical measure",
            "broader": ("https://w3id.org/dpv#hasTechnicalOrganisationalMeasure",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasTechnicalOrganisationalMeasure": {
            "label": "has technical and organisational measure",
            "definition": "Indicates use or applicability of Technical or Organisational measure",
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasThirdCountry": {
            "label": "has third country",
            "definition": "Indicates applicability or relevance of a 'third country'",
            "broader": ("https://w3id.org/dpv#hasCountry",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasThirdParty": {
            "label": "has third party",
            "definition": "Indicates association with Third Party",
            "broader": ("https://w3id.org/dpv#hasEntity",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasUncategorisedData": {
            "label": "has uncategorised data",
            "definition": "Indicates association with the specified uncategorised data",
            "broader": ("https://w3id.org/dpv#hasData",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#hasUnstructuredData": {
            "label": "has unstructured data",
            "definition": "Indicates association with the specified unstructured data",
            "broader": ("https://w3id.org/dpv#hasData",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#isAfter": {
            "label": "is after",
            "definition": "Indicates the specified concepts is 'after' this concept in some context",
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#isApplicableFor": {
            "label": "is applicable for",
            "definition": "Indicates the concept or information is applicable for specified context",
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#isAuthorityFor": {
            "label": "is authority for",
            "definition": "Indicates area, scope, or applicability of an Authority",
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#isBefore": {
            "label": "is before",
            "definition": "Indicates the specified concepts is 'before' this concept in some context",
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#isDeterminedByEntity": {
            "label": "is determined by entity",
            "definition": "Indicates the context is determined by the specified entity",
            "broader": ("https://w3id.org/dpv#hasEntity",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#isDuring": {
            "label": "is during",
            "definition": "Indicates the specified concepts occur 'during' this concept in some context",
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#isExercisedAt": {
            "label": "is exercised at",
            "definition": "Indicates context or information about exercising a right",
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#isImplementedByEntity": {
            "label": "is implemented by entity",
            "definition": "Indicates implementation details such as entities or agents",
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#isImplementedUsingTechnology": {
            "label": "is implemented using technology",
            "definition": "Indicates implementation details such as technologies or processes",
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#isIndicatedAtTime": {
            "label": "is indicated at time",
            "definition": "Specifies the temporal information for when the entity has indicated the specific context",
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#isIndicatedBy": {
            "label": "is indicated by",
            "definition": "Specifies entity who indicates the specific context",
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#isMitigatedByMeasure": {
            "label": "is mitigated by measure",
            "definition": "Indicate a risk is mitigated by specified measure",
            "broader": ("https://w3id.org/dpv#hasTechnicalOrganisationalMeasure",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#isNotApplicableFor": {
            "label": "is not applicable for",
            "definition": "Indicates the concept or information is not applicable for specified context",
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#isOrganisationalUnitOf": {
            "label": "is organisational unit of",
            "definition": "Indicates this entity is an organisational unit of the specified entity",
            "broader": ("https://w3id.org/dpv#hasEntity",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#isOutsideOfLocation": {
            "label": "is outside of location",
            "definition": "Indicates the interpretation where the location being referenced is outside of the indicated concept",
            "broader": ("https://w3id.org/dpv#hasLocation",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#isPolicyFor": {
            "label": "is policy for",
            "definition": "Indicates the context or application of policy",
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#isRepresentativeFor": {
            "label": "is representative for",
            "definition": "Indicates the entity is a representative for specified entity",
            "broader": ("https://w3id.org/dpv#hasEntity",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#isResidualRiskOf": {
            "label": "is residual risk of",
            "definition": "Indicates this risk is the remaining or residual risk from applying mitigation measures or treatments to specified risk",
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#isSubsidiaryOf": {
            "label": "is subsidiary of",
            "definition": "Indicates this entity is the subsidiary of the specified entity",
            "broader": ("https://w3id.org/dpv#hasEntity",),
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#mitigatesRisk": {
            "label": "mitigates risk",
            "definition": "Indicates risks mitigated by this concept",
            "source_vocab": "dpv",
        },
        "https://w3id.org/dpv#supportsComplianceWith": {
            "label": "supports Compliance With",
            "definition": "Indicate the measure is required for meeting specified requirement or satisfying specified condition/constraint",
            "source_vocab": "dpv",
        },
    }
)

__all__ = [
    "DPIA",
    "EULA",
    "FRIA",
    "NDA",
    "PIA",
    "ROPA",
    "AIGovernance",
    "AILiteracy",
    "AINotice",
    "AcademicResearch",
    "AcademicScientificOrganisation",
    "AcceptContract",
    "AcceptableRule",
    "AcceptableUsePolicy",
    "Access",
    "AccessControlMethod",
    "AccountManagement",
    "Acquire",
    "ActiveRight",
    "ActivelyInvolved",
    "ActivityCompleted",
    "ActivityHalted",
    "ActivityMonitoring",
    "ActivityNotCompleted",
    "ActivityOngoing",
    "ActivityPlanned",
    "ActivityProposed",
    "ActivityStatus",
    "Adapt",
    "Adult",
    "Advertising",
    "AgeVerification",
    "Agent",
    "Aggregate",
    "AlgorithmicLogic",
    "Align",
    "Alter",
    "AmbulanceProvider",
    "Analyse",
    "Anonymisation",
    "Anonymise",
    "AnonymisedData",
    "Applicability",
    "Applicant",
    "ApprovalProcedure",
    "Assess",
    "Assessment",
    "AssetManagementProcedures",
    "AssistiveAutomation",
    "AsylumSeeker",
    "AsymmetricCryptography",
    "AsymmetricEncryption",
    "Audit",
    "AuditApproved",
    "AuditConditionallyApproved",
    "AuditNotRequired",
    "AuditRejected",
    "AuditRequested",
    "AuditRequired",
    "AuditStatus",
    "AuthenticationProtocols",
    "Authentication_ABC",
    "Authentication_PABC",
    "AuthorisationProcedure",
    "AuthorisationProtocols",
    "Authority",
    "AuthorityInformed",
    "AuthorityUninformed",
    "AutomatedDecisionMaking",
    "AutomatedScoringOfIndividuals",
    "AutomationLevel",
    "Autonomous",
    "B2B2CContract",
    "B2BContract",
    "B2CContract",
    "BackgroundChecks",
    "BiometricAuthentication",
    "C2BContract",
    "C2CContract",
    "CannotChallengeProcess",
    "CannotChallengeProcessInput",
    "CannotChallengeProcessOutput",
    "CannotCorrectProcess",
    "CannotCorrectProcessInput",
    "CannotCorrectProcessOutput",
    "CannotObjectToProcess",
    "CannotOptInToProcess",
    "CannotOptOutFromProcess",
    "CannotReverseProcessEffects",
    "CannotReverseProcessInput",
    "CannotReverseProcessOutput",
    "CannotWithdrawFromProcess",
    "Certification",
    "CertificationSeal",
    "ChallengingProcess",
    "ChallengingProcessInput",
    "ChallengingProcessOutput",
    "CharityOrganisation",
    "Child",
    "Citizen",
    "City",
    "Client",
    "Clinic",
    "CloudLocation",
    "CodeOfConduct",
    "Collect",
    "CollectedData",
    "CollectedPersonalData",
    "CombatClimateChange",
    "Combine",
    "CommercialPurpose",
    "CommercialResearch",
    "CommerciallyConfidentialData",
    "CommunicationForCustomerCare",
    "CommunicationManagement",
    "CompatibilityUnknown",
    "ComplianceAssessment",
    "ComplianceIndeterminate",
    "ComplianceMonitoring",
    "ComplianceStatus",
    "ComplianceUnknown",
    "ComplianceViolation",
    "Compliant",
    "ConditionalAutomation",
    "ConfidentialData",
    "ConfidentialityAgreement",
    "ConformanceAssessment",
    "ConformanceStatus",
    "Conformant",
    "Consent",
    "ConsentControl",
    "ConsentExpired",
    "ConsentGiven",
    "ConsentInvalidated",
    "ConsentManagement",
    "ConsentNotice",
    "ConsentReceipt",
    "ConsentRecord",
    "ConsentRefused",
    "ConsentRequestDeferred",
    "ConsentRequested",
    "ConsentRevoked",
    "ConsentStatus",
    "ConsentStatusInvalidForProcessing",
    "ConsentStatusValidForProcessing",
    "ConsentUnknown",
    "ConsentWithdrawn",
    "Consequence",
    "ConsequenceAsSideEffect",
    "ConsequenceOfFailure",
    "ConsequenceOfSuccess",
    "Consult",
    "Consultation",
    "ConsultationWithAuthority",
    "ConsultationWithDPO",
    "ConsultationWithDataSubject",
    "ConsultationWithDataSubjectRepresentative",
    "Consumer",
    "ConsumerStandardFormContract",
    "Context",
    "ContextuallyAnonymisedData",
    "ContinuousFrequency",
    "Contract",
    "ContractActivationStatus",
    "ContractActive",
    "ContractAmended",
    "ContractAmendmentClause",
    "ContractApproved",
    "ContractBeingPerformed",
    "ContractBreached",
    "ContractByDomain",
    "ContractByEntityType",
    "ContractByNegotiationType",
    "ContractConfidentialityClause",
    "ContractControl",
    "ContractDefinitions",
    "ContractDisputeResolutionClause",
    "ContractDisputed",
    "ContractDrafted",
    "ContractExecutionStatus",
    "ContractExpired",
    "ContractExtended",
    "ContractFulfilled",
    "ContractFulfilmentStatus",
    "ContractFullyExecuted",
    "ContractFullySigned",
    "ContractInactive",
    "ContractJurisdictionClause",
    "ContractNegotiated",
    "ContractNotFulfilled",
    "ContractOffered",
    "ContractPartiallyFulfilled",
    "ContractPartiallySigned",
    "ContractPerformance",
    "ContractPerformanceStatus",
    "ContractPreamble",
    "ContractPreparationStatus",
    "ContractRejected",
    "ContractRenewed",
    "ContractSignedByParty",
    "ContractStatus",
    "ContractTemporarilySuspended",
    "ContractTerminated",
    "ContractTerminationClause",
    "ContractTerminationStatus",
    "ContractUnderNegotiation",
    "ContractUnderReview",
    "ContractViolated",
    "ContractualClause",
    "ContractualClauseFulfilled",
    "ContractualClauseFulfilmentStatus",
    "ContractualClauseNotFulfilled",
    "ContractualClausePartiallyFulfilled",
    "ContractualClauseViolated",
    "ContractualTerms",
    "ControllerDataSubjectAgreement",
    "ControllerInformed",
    "ControllerProcessorAgreement",
    "ControllerUninformed",
    "Copy",
    "CorrectingProcess",
    "CorrectingProcessInput",
    "CorrectingProcessOutput",
    "CounterMoneyLaundering",
    "Counterterrorism",
    "Country",
    "CredentialManagement",
    "CrossBorderTransfer",
    "CryptographicAuthentication",
    "CryptographicKeyManagement",
    "CryptographicMethods",
    "Customer",
    "CustomerCare",
    "CustomerClaimsManagement",
    "CustomerManagement",
    "CustomerOrderManagement",
    "CustomerRelationshipManagement",
    "CustomerSolvencyMonitoring",
    "CybersecurityAssessment",
    "CybersecurityTraining",
    "DashboardNotice",
    "Data",
    "DataAltruism",
    "DataAvailabilityAssessment",
    "DataBackupProtocols",
    "DataBreachImpactAssessment",
    "DataBreachNotice",
    "DataBreachNotification",
    "DataBreachRecord",
    "DataController",
    "DataControllerContract",
    "DataControllerDataSource",
    "DataDeletionPolicy",
    "DataErasurePolicy",
    "DataExporter",
    "DataGovernance",
    "DataHandlingClause",
    "DataImporter",
    "DataInteroperabilityAssessment",
    "DataInteroperabilityImprovement",
    "DataInteroperabilityManagement",
    "DataInventoryManagement",
    "DataJurisdictionPolicy",
    "DataLiteracy",
    "DataProcessingAgreement",
    "DataProcessingPolicy",
    "DataProcessingRecord",
    "DataProcessor",
    "DataProcessorContract",
    "DataProtectionAuthority",
    "DataProtectionOfficer",
    "DataProtectionTraining",
    "DataPublishedByDataSubject",
    "DataQualityAssessment",
    "DataQualityImprovement",
    "DataQualityManagement",
    "DataRedaction",
    "DataRestorationPolicy",
    "DataReusePolicy",
    "DataSanitisationTechnique",
    "DataSecurityManagement",
    "DataSource",
    "DataStoragePolicy",
    "DataSubProcessor",
    "DataSubject",
    "DataSubjectContract",
    "DataSubjectDataSource",
    "DataSubjectInformed",
    "DataSubjectRight",
    "DataSubjectRightsManagement",
    "DataSubjectScale",
    "DataSubjectUninformed",
    "DataSuitabilityAssessment",
    "DataTransferImpactAssessment",
    "DataTransferLegalBasis",
    "DataTransferNotice",
    "DataTransferRecord",
    "DataVolume",
    "DecentralisedLocations",
    "DecisionMaking",
    "Deidentification",
    "Delete",
    "DeliveryOfGoods",
    "Derive",
    "DerivedData",
    "DerivedPersonalData",
    "DesignStandard",
    "Destruct",
    "DeterministicPseudonymisation",
    "Deterrence",
    "DeterrenceFollowed",
    "DeterrenceNotFollowed",
    "DeviceNotice",
    "DifferentialPrivacy",
    "DigitalLiteracy",
    "DigitalRightsManagement",
    "DigitalSignatures",
    "DirectMarketing",
    "DisasterRecoveryProcedures",
    "Disclose",
    "DiscloseByTransmission",
    "Display",
    "DisputeManagement",
    "Disseminate",
    "DistributedSystemSecurity",
    "DistributionAgreement",
    "DocumentRandomisedPseudonymisation",
    "DocumentSecurity",
    "Download",
    "Duration",
    "EconomicUnion",
    "EducationalOrganisation",
    "EducationalTraining",
    "EffectivenessDeterminationProcedures",
    "ElderlyDataSubject",
    "ElderlyHuman",
    "EmergencyHealthcareProvider",
    "EmergencyServiceProvider",
    "Employee",
    "EmploymentContract",
    "Encryption",
    "EncryptionAtRest",
    "EncryptionInTransfer",
    "EncryptionInUse",
    "EndToEndEncryption",
    "EndlessDuration",
    "EnforceAccessControl",
    "EnforceSecurity",
    "EnterIntoContract",
    "Entity",
    "EntityActiveInvolvement",
    "EntityInformed",
    "EntityInformedStatus",
    "EntityIntendedInvolvement",
    "EntityInvolved",
    "EntityInvolvement",
    "EntityInvolvementStatus",
    "EntityNonInvolvement",
    "EntityNonPermissiveInvolvement",
    "EntityNotInvolved",
    "EntityPassiveInvolvement",
    "EntityPermissiveInvolvement",
    "EntityUninformed",
    "EntityUnintendedInvolvement",
    "EnvironmentalProtection",
    "Erase",
    "EstablishContractualAgreement",
    "EvaluationOfIndividuals",
    "EvaluationScoring",
    "ExpectationStatus",
    "Expected",
    "ExplicitlyExpressedConsent",
    "Export",
    "ExpressedConsent",
    "FailSafeProtocols",
    "FederatedLocations",
    "FeeNotRequired",
    "FeeRequired",
    "FeeRequirement",
    "FileSystemSecurity",
    "Filter",
    "FireDepartment",
    "FixedLocation",
    "FixedMultipleLocations",
    "FixedOccurrencesDuration",
    "FixedSingularLocation",
    "ForProfitOrganisation",
    "Format",
    "FraudPreventionAndDetection",
    "Frequency",
    "FulfilmentOfContractualObligation",
    "FulfilmentOfObligation",
    "FullAutomation",
    "FullyRandomisedPseudonymisation",
    "G2BContract",
    "G2CContract",
    "G2GContract",
    "Generate",
    "GeneratedData",
    "GeneratedPersonalData",
    "GeographicCoverage",
    "GlobalScale",
    "GovernanceProcedures",
    "GovernmentalOrganisation",
    "GraphicalNotice",
    "GuardianOfDataSubject",
    "GuardianOfHuman",
    "Guideline",
    "GuidelinesPrinciple",
    "HardwareSecurityProtocols",
    "HashFunctions",
    "HashMessageAuthenticationCode",
    "HealthcareOrganisation",
    "HighAutomation",
    "HomomorphicEncryption",
    "Hospital",
    "HugeDataVolume",
    "HugeScaleOfDataSubjects",
    "HumanInvolved",
    "HumanInvolvement",
    "HumanInvolvementForControl",
    "HumanInvolvementForDecision",
    "HumanInvolvementForInput",
    "HumanInvolvementForIntervention",
    "HumanInvolvementForOversight",
    "HumanInvolvementForVerification",
    "HumanNotInvolved",
    "HumanOversight",
    "HumanResourceManagement",
    "HumanSubject",
    "HybridPublicPrivateSpace",
    "IPRManagement",
    "IdentifyingPersonalData",
    "IdentityAuthentication",
    "IdentityManagementMethod",
    "IdentityVerification",
    "Immigrant",
    "Impact",
    "ImpactAssessment",
    "ImpliedConsent",
    "Importance",
    "ImproveExistingProductsAndServices",
    "ImproveHealthcare",
    "ImproveInternalCRMProcesses",
    "ImprovePublicServices",
    "ImproveTransportMobility",
    "IncidentManagementProcedures",
    "IncidentReportingCommunication",
    "IncorrectData",
    "IncreaseServiceRobustness",
    "IndeterminateDuration",
    "IndustryConsortium",
    "Infer",
    "InferredData",
    "InferredPersonalData",
    "InformationAudit",
    "InformationFlowControl",
    "InformationSecurityPolicy",
    "InformedConsent",
    "InnovativeUseOfExistingTechnology",
    "InnovativeUseOfNewTechnologies",
    "InnovativeUseOfTechnology",
    "IntellectualPropertyData",
    "Intended",
    "IntentionStatus",
    "InternalResourceOptimisation",
    "InternationalOrganisation",
    "IntrusionDetectionSystem",
    "InverseJurisdiction",
    "InvolvementStatus",
    "JITNotice",
    "JobApplicant",
    "JointDataControllers",
    "JointDataControllersAgreement",
    "JudicialOrganisation",
    "Jurisdiction",
    "Justification",
    "LargeDataVolume",
    "LargeScaleOfDataSubjects",
    "LargeScaleProcessing",
    "Law",
    "LawEnforcementOrganisation",
    "Lawful",
    "Lawfulness",
    "LawfulnessUnknown",
    "LayeredNotice",
    "LegalAgent",
    "LegalAgreement",
    "LegalBasis",
    "LegalCompliance",
    "LegalComplianceAssessment",
    "LegalComplianceAudit",
    "LegalEntity",
    "LegalMeasure",
    "LegalObligation",
    "LegalObligationCompleted",
    "LegalObligationOngoing",
    "LegalObligationPending",
    "LegalObligationStatus",
    "LegitimateInterest",
    "LegitimateInterestAssessment",
    "LegitimateInterestInformed",
    "LegitimateInterestNotObjected",
    "LegitimateInterestObjected",
    "LegitimateInterestOfController",
    "LegitimateInterestOfDataSubject",
    "LegitimateInterestOfThirdParty",
    "LegitimateInterestStatus",
    "LegitimateInterestUninformed",
    "LicenseAgreement",
    "Likelihood",
    "LocalEnvironmentScale",
    "LocalLocation",
    "LocalityScale",
    "Location",
    "LocationFixture",
    "LocationLocality",
    "LoggingPolicy",
    "MaintainFraudDatabase",
    "MakeAvailable",
    "ManageConsent",
    "ManagementStandard",
    "Marketing",
    "Match",
    "MediumDataVolume",
    "MediumScaleOfDataSubjects",
    "MediumScaleProcessing",
    "Member",
    "MemberPartnerManagement",
    "MentallyVulnerableDataSubject",
    "MentallyVulnerableHuman",
    "MessageAuthenticationCodes",
    "MetadataManagement",
    "MisusePreventionAndDetection",
    "MobilePlatformSecurity",
    "Modify",
    "Monitor",
    "MonitoringPolicy",
    "MonotonicCounterPseudonymisation",
    "Move",
    "MultiFactorAuthentication",
    "MultiNationalScale",
    "NationalAuthority",
    "NationalScale",
    "NaturalPerson",
    "NearlyGlobalScale",
    "Necessity",
    "NegotiateContract",
    "NegotiatedContract",
    "NetworkProxyRouting",
    "NetworkSecurityProtocols",
    "NonCitizen",
    "NonCommercialPurpose",
    "NonCommercialResearch",
    "NonCompliant",
    "NonConformant",
    "NonGovernmentalOrganisation",
    "NonPersonalData",
    "NonPersonalDataProcess",
    "NonProfitOrganisation",
    "NonPublicDataSource",
    "NotApplicable",
    "NotAutomated",
    "NotAvailable",
    "NotInvolved",
    "NotRequired",
    "Notice",
    "NoticeCommunicated",
    "NoticeGenerated",
    "NoticeIcon",
    "NoticeLatest",
    "NoticeLayer",
    "NoticeStale",
    "NoticeStatus",
    "NoticeUnused",
    "NoticeUpdated",
    "NoticeUsed",
    "Notification",
    "NotificationCompleted",
    "NotificationFailed",
    "NotificationNotNeeded",
    "NotificationOngoing",
    "NotificationPlanned",
    "NotificationStatus",
    "ObjectingToProcess",
    "Obligation",
    "ObligationFulfilled",
    "ObligationUnfulfilled",
    "ObligationViolated",
    "Observe",
    "ObservedData",
    "ObservedPersonalData",
    "Obtain",
    "ObtainConsent",
    "OfferContract",
    "OfficialAuthorityExerciseCompleted",
    "OfficialAuthorityExerciseOngoing",
    "OfficialAuthorityExercisePending",
    "OfficialAuthorityExerciseStatus",
    "OfficialAuthorityOfController",
    "OftenFrequency",
    "OperatingSystemSecurity",
    "OptimisationForConsumer",
    "OptimisationForController",
    "OptimiseUserInterface",
    "OptingInToProcess",
    "OptingOutFromProcess",
    "Optional",
    "OralNotice",
    "Organisation",
    "OrganisationComplianceManagement",
    "OrganisationGovernance",
    "OrganisationRiskManagement",
    "OrganisationalMeasure",
    "OrganisationalUnit",
    "Organise",
    "ParentLegalEntity",
    "ParentOfDataSubject",
    "ParentOfHuman",
    "PartialAutomation",
    "PartiallyCompliant",
    "Participant",
    "PassiveRight",
    "PassivelyInvolved",
    "PasswordAuthentication",
    "Patient",
    "PaymentManagement",
    "PenetrationTestingMethods",
    "Permission",
    "PermissionManagement",
    "PermissionNotUtilised",
    "PermissionUtilised",
    "PersonalData",
    "PersonalDataAudit",
    "PersonalDataHandling",
    "PersonalDataProcess",
    "PersonalSpace",
    "Personalisation",
    "PersonalisedAdvertising",
    "PersonalisedBenefits",
    "PersonnelBehaviourMonitoring",
    "PersonnelHiring",
    "PersonnelManagement",
    "PersonnelMonitoring",
    "PersonnelOffboarding",
    "PersonnelOnboarding",
    "PersonnelPayment",
    "PersonnelPerformanceEvaluation",
    "PersonnelPerformanceManagement",
    "PersonnelPerformanceMonitoring",
    "PersonnelPerformancePrediction",
    "PersonnelPromotionManagement",
    "PersonnelTerminationManagement",
    "PersonnelWorkloadManagement",
    "PhysicalAccessControlMethod",
    "PhysicalAuthentication",
    "PhysicalAuthorisation",
    "PhysicalDeviceSecurity",
    "PhysicalInterceptionProtection",
    "PhysicalInterruptionProtection",
    "PhysicalMeasure",
    "PhysicalNetworkSecurity",
    "PhysicalSecureStorage",
    "PhysicalSupplySecurity",
    "PhysicalSurveillance",
    "Policy",
    "PoliticalCampaign",
    "PostQuantumCryptography",
    "PostedNotice",
    "PrimaryImportance",
    "PrimaryUse",
    "Principle",
    "PrintedNotice",
    "PrivacyByDefault",
    "PrivacyByDesign",
    "PrivacyNotice",
    "PrivacyPreservingProtocol",
    "PrivateCommunalSpace",
    "PrivateInformationRetrieval",
    "PrivateLocation",
    "PrivateSectorBody",
    "PrivateSpace",
    "PrivatelyOperatedPublicSpace",
    "PrivatelyOwnedPublicSpace",
    "PrivatelyOwnedSpace",
    "Process",
    "Processing",
    "ProcessingCondition",
    "ProcessingContext",
    "ProcessingDuration",
    "ProcessingLocation",
    "ProcessingScale",
    "ProfessionalConfidentialData",
    "ProfessionalTraining",
    "Profiling",
    "Prohibition",
    "ProhibitionUnviolated",
    "ProhibitionViolated",
    "ProtectionOfIPR",
    "ProtectionOfNationalSecurity",
    "ProtectionOfPublicSecurity",
    "ProvideConsent",
    "ProvideEventRecommendations",
    "ProvideOfficialStatistics",
    "ProvidePersonalisedRecommendations",
    "ProvideProductRecommendations",
    "ProvidedData",
    "ProvidedPersonalData",
    "ProviderStandardFormContract",
    "Pseudonymisation",
    "Pseudonymise",
    "PseudonymisedData",
    "PublicBenefit",
    "PublicDataSource",
    "PublicInterest",
    "PublicInterestCompleted",
    "PublicInterestObjected",
    "PublicInterestOngoing",
    "PublicInterestPending",
    "PublicInterestStatus",
    "PublicLocation",
    "PublicPolicyMaking",
    "PublicRegisterOfEntities",
    "PublicRelations",
    "PublicSectorBody",
    "PublicSpace",
    "PubliclyAccessibleSpace",
    "PubliclyOwnedSpace",
    "Purpose",
    "QuantumCryptography",
    "Query",
    "RNGPseudonymisation",
    "RandomLocation",
    "ReaffirmConsent",
    "RecertificationPolicy",
    "Recipient",
    "RecipientInformed",
    "RecipientUninformed",
    "Recommendation",
    "RecommendationFollowed",
    "RecommendationNotFollowed",
    "Record",
    "RecordManagement",
    "RecordsOfActivities",
    "RecruitmentAdvertising",
    "RecruitmentApplicantBackgroundCheck",
    "RecruitmentApplicantCriminalBackgroundCheck",
    "RecruitmentApplicantInformationAuthentication",
    "RecruitmentApplicantSelection",
    "RecruitmentApplicationAnalysis",
    "RecruitmentApplicationManagement",
    "RecruitmentApplicationScreening",
    "RecruitmentInterviewAnalysis",
    "RecruitmentInterviewAssessment",
    "RecruitmentInterviewManagement",
    "RecruitmentInterviewScheduling",
    "RecruitmentManagement",
    "RecruitmentTargetedAdvertising",
    "Reformat",
    "RefuseConsent",
    "RefuseContract",
    "Region",
    "RegionalAuthority",
    "RegionalScale",
    "RegulatorySandbox",
    "ReligiousAssociations",
    "RemoteLocation",
    "Remove",
    "RenewedConsentGiven",
    "RepairImpairments",
    "Representative",
    "RequestAccepted",
    "RequestAcknowledged",
    "RequestActionDelayed",
    "RequestFulfilled",
    "RequestInitiated",
    "RequestRejected",
    "RequestRequiredActionPerformed",
    "RequestRequiresAction",
    "RequestStatus",
    "RequestStatusQuery",
    "RequestUnfulfilled",
    "RequestedServiceProvision",
    "Required",
    "ResearchAndDevelopment",
    "ResidualRisk",
    "Restrict",
    "Retrieve",
    "ReuseCompatibility",
    "ReversingProcessEffects",
    "ReversingProcessInput",
    "ReversingProcessOutput",
    "ReviewImpactAssessment",
    "ReviewProcedure",
    "Right",
    "RightExerciseActivity",
    "RightExerciseNotice",
    "RightExerciseRecord",
    "RightFulfilmentNotice",
    "RightNonFulfilmentNotice",
    "RightNotice",
    "RightsFulfilment",
    "RightsImpactAssessment",
    "RightsManagement",
    "Risk",
    "RiskAssessment",
    "RiskConcept",
    "RiskLevel",
    "RiskMitigationMeasure",
    "Rule",
    "RuleFulfilled",
    "RuleFulfilmentStatus",
    "RuleUnfulfilled",
    "RuleViolated",
    "SMEOrganisation",
    "Safeguard",
    "SafeguardForDataTransfer",
    "Scale",
    "ScientificResearch",
    "Scope",
    "ScoringOfIndividuals",
    "Screen",
    "Seal",
    "SearchFunctionalities",
    "SecondaryImportance",
    "SecondaryUse",
    "SecretSharingSchemes",
    "Sector",
    "SecureMultiPartyComputation",
    "SecureProcessingEnvironment",
    "SecurityAssessment",
    "SecurityAudit",
    "SecurityIncidentNotice",
    "SecurityIncidentNotification",
    "SecurityIncidentRecord",
    "SecurityKnowledgeTraining",
    "SecurityMethod",
    "SecurityProcedure",
    "SecurityRoleProcedures",
    "SellDataToThirdParties",
    "SellInsightsFromData",
    "SellProducts",
    "SellProductsToDataSubject",
    "SemiPrivateSpace",
    "SensitiveData",
    "SensitiveNonPersonalData",
    "SensitivePersonalData",
    "SensitivityLevel",
    "Service",
    "ServiceAccessDetermination",
    "ServiceConsumer",
    "ServiceLevelAgreement",
    "ServiceManagement",
    "ServiceMonitoring",
    "ServiceOptimisation",
    "ServicePersonalisation",
    "ServiceProvider",
    "ServiceProvision",
    "ServiceRegistration",
    "ServiceUsageAnalytics",
    "Severity",
    "Share",
    "SingleSignOn",
    "SingularDataVolume",
    "SingularFrequency",
    "SingularScaleOfDataSubjects",
    "SmallDataVolume",
    "SmallScaleOfDataSubjects",
    "SmallScaleProcessing",
    "SocialMediaMarketing",
    "SpecialCategoryPersonalData",
    "SporadicDataVolume",
    "SporadicFrequency",
    "SporadicScaleOfDataSubjects",
    "StaffTraining",
    "Standard",
    "StandardFormContract",
    "StandardsConformance",
    "StartupOrganisation",
    "StatisticalConfidentialityAgreement",
    "StatisticallyConfidentialData",
    "Status",
    "StorageCondition",
    "StorageDeletion",
    "StorageDuration",
    "StorageLocation",
    "StorageRestoration",
    "Store",
    "Structure",
    "Student",
    "SubProcessorAgreement",
    "Subscriber",
    "SubsidiaryLegalEntity",
    "SupportContractNegotiation",
    "SupportEntityDecisionMaking",
    "SupportExchangeOfViews",
    "SupportInformedConsentDecision",
    "SupraNationalAuthority",
    "SupraNationalUnion",
    "SymmetricCryptography",
    "SymmetricEncryption",
    "SyntheticData",
    "SystematicMonitoring",
    "TargetedAdvertising",
    "TechnicalMeasure",
    "TechnicalOrganisationalMeasure",
    "TechnicalServiceProvision",
    "TechnicalStandard",
    "Technology",
    "TemporalDuration",
    "TerminateContract",
    "TermsOfService",
    "ThirdCountry",
    "ThirdParty",
    "ThirdPartyAgreement",
    "ThirdPartyContract",
    "ThirdPartyDataSource",
    "ThirdPartySecurityProcedures",
    "Tourist",
    "Tracking",
    "TrackingByFirstParty",
    "TrackingByThirdParty",
    "Transfer",
    "Transform",
    "Transmit",
    "TrustedComputing",
    "TrustedExecutionEnvironment",
    "UnacceptableRule",
    "UncategorisedData",
    "Unexpected",
    "UninformedConsent",
    "Unintended",
    "UnknownApplicability",
    "Unlawful",
    "UnstructuredData",
    "UntilEventDuration",
    "UntilTimeDuration",
    "UnverifiedData",
    "UsageControl",
    "Use",
    "UseSyntheticData",
    "User",
    "UserInterfacePersonalisation",
    "VariableLocation",
    "VendorManagement",
    "VendorPayment",
    "VendorRecordsManagement",
    "VendorSelectionAssessment",
    "Verification",
    "VerifiedData",
    "VirtualisationSecurity",
    "Visitor",
    "VitalInterest",
    "VitalInterestCompleted",
    "VitalInterestObjected",
    "VitalInterestOfDataSubject",
    "VitalInterestOfNaturalPerson",
    "VitalInterestOngoing",
    "VitalInterestPending",
    "VitalInterestStatus",
    "VulnerabilityTestingMethods",
    "VulnerableDataSubject",
    "VulnerableHuman",
    "WebBrowserSecurity",
    "WebSecurityProtocols",
    "WirelessSecurityProtocols",
    "WithdrawConsent",
    "WithdrawingFromProcess",
    "WithinDevice",
    "WithinPhysicalEnvironment",
    "WithinVirtualEnvironment",
    "ZeroKnowledgeAuthentication",
    "hasActiveEntity",
    "hasActivityStatus",
    "hasAddress",
    "hasAlgorithmicLogic",
    "hasApplicability",
    "hasApplicableLaw",
    "hasAssessment",
    "hasAuditStatus",
    "hasAuthority",
    "hasAutomationLevel",
    "hasComplianceStatus",
    "hasConformanceStatus",
    "hasConsentControl",
    "hasConsentStatus",
    "hasConsequence",
    "hasConsequenceOn",
    "hasContact",
    "hasContext",
    "hasContractControl",
    "hasContractStatus",
    "hasContractualClause",
    "hasContractualFulfilmentStatus",
    "hasCountry",
    "hasData",
    "hasDataController",
    "hasDataExporter",
    "hasDataImporter",
    "hasDataProcessor",
    "hasDataProtectionOfficer",
    "hasDataSource",
    "hasDataSubject",
    "hasDataSubjectScale",
    "hasDataVolume",
    "hasDeterrence",
    "hasDuration",
    "hasEntity",
    "hasEntityControl",
    "hasEntityInvolvement",
    "hasExpectation",
    "hasFee",
    "hasFrequency",
    "hasFulfilmentStatus",
    "hasGeographicCoverage",
    "hasHumanInvolvement",
    "hasHumanSubject",
    "hasIdentifier",
    "hasImpact",
    "hasImpactAssessment",
    "hasImpactOn",
    "hasImportance",
    "hasIndicationMethod",
    "hasInformedStatus",
    "hasIntention",
    "hasInverseJurisdiction",
    "hasInvolvement",
    "hasJointDataControllers",
    "hasJurisdiction",
    "hasJustification",
    "hasLawfulness",
    "hasLegalBasis",
    "hasLegalMeasure",
    "hasLikelihood",
    "hasLocation",
    "hasName",
    "hasNecessity",
    "hasNonInvolvedEntity",
    "hasNonPersonalDataProcess",
    "hasNotice",
    "hasNoticeIcon",
    "hasNoticeLayer",
    "hasNoticeStatus",
    "hasNotificationStatus",
    "hasObligation",
    "hasOrganisationalMeasure",
    "hasOrganisationalUnit",
    "hasOutcome",
    "hasParty",
    "hasPassiveEntity",
    "hasPermission",
    "hasPersonalData",
    "hasPersonalDataHandling",
    "hasPersonalDataProcess",
    "hasPhysicalMeasure",
    "hasPolicy",
    "hasProcess",
    "hasProcessing",
    "hasProcessingCondition",
    "hasProcessingScale",
    "hasProhibition",
    "hasPurpose",
    "hasRecipient",
    "hasRecipientDataController",
    "hasRecipientThirdParty",
    "hasRecommendation",
    "hasRecordOfActivity",
    "hasRelationWithDataSubject",
    "hasRepresentative",
    "hasRequestStatus",
    "hasResidualRisk",
    "hasResponsibleEntity",
    "hasReuseCompatibility",
    "hasRight",
    "hasRisk",
    "hasRiskAssessment",
    "hasRiskLevel",
    "hasRule",
    "hasScale",
    "hasScope",
    "hasSector",
    "hasSensitivityLevel",
    "hasService",
    "hasServiceConsumer",
    "hasServiceProvider",
    "hasSeverity",
    "hasStatus",
    "hasStorageCondition",
    "hasSubsidiary",
    "hasTechnicalMeasure",
    "hasTechnicalOrganisationalMeasure",
    "hasThirdCountry",
    "hasThirdParty",
    "hasUncategorisedData",
    "hasUnstructuredData",
    "isAfter",
    "isApplicableFor",
    "isAuthorityFor",
    "isBefore",
    "isDeterminedByEntity",
    "isDuring",
    "isExercisedAt",
    "isImplementedByEntity",
    "isImplementedUsingTechnology",
    "isIndicatedAtTime",
    "isIndicatedBy",
    "isMitigatedByMeasure",
    "isNotApplicableFor",
    "isOrganisationalUnitOf",
    "isOutsideOfLocation",
    "isPolicyFor",
    "isRepresentativeFor",
    "isResidualRiskOf",
    "isSubsidiaryOf",
    "mitigatesRisk",
    "supportsComplianceWith",
]
