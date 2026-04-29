# SPDX-FileCopyrightText: 2026-present Arthit Suriyawongkul
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0
#
# AUTO-GENERATED — do not edit manually.
# Source: SPDX 3.0.1 Dataset profile
# Generated: 2026-04-29T22:30:23Z
# Regenerate: python -m stav.codegen.generate tools/recipes/spdx_dataset.json

"""Vocabulary from SPDX 3.0.1 Dataset profile.

349 term constants (accessible as ``module.TermName``); grouped enums: :class:`DatasetType`, :class:`ConfidentialityLevel`."""

from __future__ import annotations

from stav._registry import _register
from stav.term import _StavVocabEnum

__stav_namespace__ = "vocab.spdx.dataset"

# ── Individual term constants ─────────────────────────────────────────────────────
# Plain string IRIs — use directly with MLflow, Pitloom, SBOM serialisers.
# Metadata (label, definition, broader) via: stav.label(NaturalPerson) etc.
act = "https://spdx.org/rdf/3.0.1/terms/Security/SsvcDecisionType/act"
adler32 = "https://spdx.org/rdf/3.0.1/terms/Core/HashAlgorithm/adler32"
affects = "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/affects"
Agent = "https://spdx.org/rdf/3.0.1/terms/Core/Agent"
ai = "https://spdx.org/rdf/3.0.1/terms/Core/ProfileIdentifierType/ai"
AIPackage = "https://spdx.org/rdf/3.0.1/terms/AI/AIPackage"
altDownloadLocation = "https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/altDownloadLocation"
altWebPage = "https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/altWebPage"
amber = "https://spdx.org/rdf/3.0.1/terms/Dataset/ConfidentialityLevelType/amber"
amendedBy = "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/amendedBy"
analyzed = "https://spdx.org/rdf/3.0.1/terms/Software/SbomType/analyzed"
ancestorOf = "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/ancestorOf"
Annotation = "https://spdx.org/rdf/3.0.1/terms/Core/Annotation"
AnnotationType = "https://spdx.org/rdf/3.0.1/terms/Core/AnnotationType"
AnyLicenseInfo = "https://spdx.org/rdf/3.0.1/terms/SimpleLicensing/AnyLicenseInfo"
application = "https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/application"
archive = "https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/archive"
Artifact = "https://spdx.org/rdf/3.0.1/terms/Core/Artifact"
attend = "https://spdx.org/rdf/3.0.1/terms/Security/SsvcDecisionType/attend"
audio = "https://spdx.org/rdf/3.0.1/terms/Dataset/DatasetType/audio"
availableFrom = "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/availableFrom"
binaryArtifact = "https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/binaryArtifact"
blake2b256 = "https://spdx.org/rdf/3.0.1/terms/Core/HashAlgorithm/blake2b256"
blake2b384 = "https://spdx.org/rdf/3.0.1/terms/Core/HashAlgorithm/blake2b384"
blake2b512 = "https://spdx.org/rdf/3.0.1/terms/Core/HashAlgorithm/blake2b512"
blake3 = "https://spdx.org/rdf/3.0.1/terms/Core/HashAlgorithm/blake3"
Bom = "https://spdx.org/rdf/3.0.1/terms/Core/Bom"
bom = "https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/bom"
bower = "https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/bower"
Build = "https://spdx.org/rdf/3.0.1/terms/Build/Build"
build = "https://spdx.org/rdf/3.0.1/terms/Software/SbomType/build"
build_1 = "https://spdx.org/rdf/3.0.1/terms/Core/ProfileIdentifierType/build"
build_2 = "https://spdx.org/rdf/3.0.1/terms/Core/LifecycleScopeType/build"
buildMeta = "https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/buildMeta"
buildSystem = "https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/buildSystem"
Bundle = "https://spdx.org/rdf/3.0.1/terms/Core/Bundle"
categorical = "https://spdx.org/rdf/3.0.1/terms/Dataset/DatasetType/categorical"
CdxPropertiesExtension = "https://spdx.org/rdf/3.0.1/terms/Extension/CdxPropertiesExtension"
CdxPropertyEntry = "https://spdx.org/rdf/3.0.1/terms/Extension/CdxPropertyEntry"
certificationReport = "https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/certificationReport"
chat = "https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/chat"
clear = "https://spdx.org/rdf/3.0.1/terms/Dataset/ConfidentialityLevelType/clear"
clickthrough = "https://spdx.org/rdf/3.0.1/terms/Dataset/DatasetAvailabilityType/clickthrough"
complete = "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipCompleteness/complete"
componentAnalysisReport = "https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/componentAnalysisReport"
componentNotPresent = "https://spdx.org/rdf/3.0.1/terms/Security/VexJustificationType/componentNotPresent"
ConfidentialityLevelType = "https://spdx.org/rdf/3.0.1/terms/Dataset/ConfidentialityLevelType"
configuration = "https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/configuration"
configures = "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/configures"
ConjunctiveLicenseSet = "https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/ConjunctiveLicenseSet"
container = "https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/container"
contains = "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/contains"
ContentIdentifier = "https://spdx.org/rdf/3.0.1/terms/Software/ContentIdentifier"
ContentIdentifierType = "https://spdx.org/rdf/3.0.1/terms/Software/ContentIdentifierType"
coordinatedBy = "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/coordinatedBy"
copiedTo = "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/copiedTo"
core = "https://spdx.org/rdf/3.0.1/terms/Core/ProfileIdentifierType/core"
cpe22 = "https://spdx.org/rdf/3.0.1/terms/Core/ExternalIdentifierType/cpe22"
cpe23 = "https://spdx.org/rdf/3.0.1/terms/Core/ExternalIdentifierType/cpe23"
CreationInfo = "https://spdx.org/rdf/3.0.1/terms/Core/CreationInfo"
critical = "https://spdx.org/rdf/3.0.1/terms/Security/CvssSeverityType/critical"
crystalsDilithium = "https://spdx.org/rdf/3.0.1/terms/Core/HashAlgorithm/crystalsDilithium"
crystalsKyber = "https://spdx.org/rdf/3.0.1/terms/Core/HashAlgorithm/crystalsKyber"
CustomLicense = "https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/CustomLicense"
CustomLicenseAddition = "https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/CustomLicenseAddition"
cve = "https://spdx.org/rdf/3.0.1/terms/Core/ExternalIdentifierType/cve"
CvssSeverityType = "https://spdx.org/rdf/3.0.1/terms/Security/CvssSeverityType"
CvssV2VulnAssessmentRelationship = "https://spdx.org/rdf/3.0.1/terms/Security/CvssV2VulnAssessmentRelationship"
CvssV3VulnAssessmentRelationship = "https://spdx.org/rdf/3.0.1/terms/Security/CvssV3VulnAssessmentRelationship"
CvssV4VulnAssessmentRelationship = "https://spdx.org/rdf/3.0.1/terms/Security/CvssV4VulnAssessmentRelationship"
cwe = "https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/cwe"
data = "https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/data"
dataset = "https://spdx.org/rdf/3.0.1/terms/Core/ProfileIdentifierType/dataset"
DatasetAvailabilityType = "https://spdx.org/rdf/3.0.1/terms/Dataset/DatasetAvailabilityType"
DatasetPackage = "https://spdx.org/rdf/3.0.1/terms/Dataset/DatasetPackage"
DatasetType = "https://spdx.org/rdf/3.0.1/terms/Dataset/DatasetType"
delegatedTo = "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/delegatedTo"
dependsOn = "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/dependsOn"
deployed = "https://spdx.org/rdf/3.0.1/terms/Software/SbomType/deployed"
deployed_1 = "https://spdx.org/rdf/3.0.1/terms/Core/SupportType/deployed"
descendantOf = "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/descendantOf"
describes = "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/describes"
design = "https://spdx.org/rdf/3.0.1/terms/Core/LifecycleScopeType/design"
design_1 = "https://spdx.org/rdf/3.0.1/terms/Software/SbomType/design"
development = "https://spdx.org/rdf/3.0.1/terms/Core/LifecycleScopeType/development"
development_1 = "https://spdx.org/rdf/3.0.1/terms/Core/SupportType/development"
device = "https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/device"
deviceDriver = "https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/deviceDriver"
DictionaryEntry = "https://spdx.org/rdf/3.0.1/terms/Core/DictionaryEntry"
directDownload = "https://spdx.org/rdf/3.0.1/terms/Dataset/DatasetAvailabilityType/directDownload"
directory = "https://spdx.org/rdf/3.0.1/terms/Software/FileKindType/directory"
DisjunctiveLicenseSet = "https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/DisjunctiveLicenseSet"
diskImage = "https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/diskImage"
documentation = "https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/documentation"
documentation_1 = "https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/documentation"
doesNotAffect = "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/doesNotAffect"
dynamicAnalysisReport = "https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/dynamicAnalysisReport"
Element = "https://spdx.org/rdf/3.0.1/terms/Core/Element"
ElementCollection = "https://spdx.org/rdf/3.0.1/terms/Core/ElementCollection"
email = "https://spdx.org/rdf/3.0.1/terms/Core/ExternalIdentifierType/email"
endOfSupport = "https://spdx.org/rdf/3.0.1/terms/Core/SupportType/endOfSupport"
EnergyConsumption = "https://spdx.org/rdf/3.0.1/terms/AI/EnergyConsumption"
EnergyConsumptionDescription = "https://spdx.org/rdf/3.0.1/terms/AI/EnergyConsumptionDescription"
EnergyUnitType = "https://spdx.org/rdf/3.0.1/terms/AI/EnergyUnitType"
eolNotice = "https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/eolNotice"
EpssVulnAssessmentRelationship = "https://spdx.org/rdf/3.0.1/terms/Security/EpssVulnAssessmentRelationship"
evidence = "https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/evidence"
executable = "https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/executable"
expandedLicensing = "https://spdx.org/rdf/3.0.1/terms/Core/ProfileIdentifierType/expandedLicensing"
expandsTo = "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/expandsTo"
ExploitCatalogType = "https://spdx.org/rdf/3.0.1/terms/Security/ExploitCatalogType"
ExploitCatalogVulnAssessmentRelationship = (
    "https://spdx.org/rdf/3.0.1/terms/Security/ExploitCatalogVulnAssessmentRelationship"
)
exploitCreatedBy = "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/exploitCreatedBy"
exportControlAssessment = "https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/exportControlAssessment"
ExtendableLicense = "https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/ExtendableLicense"
extension = "https://spdx.org/rdf/3.0.1/terms/Core/ProfileIdentifierType/extension"
Extension = "https://spdx.org/rdf/3.0.1/terms/Extension/Extension"
ExternalIdentifier = "https://spdx.org/rdf/3.0.1/terms/Core/ExternalIdentifier"
ExternalIdentifierType = "https://spdx.org/rdf/3.0.1/terms/Core/ExternalIdentifierType"
ExternalMap = "https://spdx.org/rdf/3.0.1/terms/Core/ExternalMap"
ExternalRef = "https://spdx.org/rdf/3.0.1/terms/Core/ExternalRef"
ExternalRefType = "https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType"
falcon = "https://spdx.org/rdf/3.0.1/terms/Core/HashAlgorithm/falcon"
file = "https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/file"
File = "https://spdx.org/rdf/3.0.1/terms/Software/File"
file_1 = "https://spdx.org/rdf/3.0.1/terms/Software/FileKindType/file"
FileKindType = "https://spdx.org/rdf/3.0.1/terms/Software/FileKindType"
filesystemImage = "https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/filesystemImage"
firmware = "https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/firmware"
fixedBy = "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/fixedBy"
fixedIn = "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/fixedIn"
foundBy = "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/foundBy"
framework = "https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/framework"
funding = "https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/funding"
generates = "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/generates"
gitoid = "https://spdx.org/rdf/3.0.1/terms/Core/ExternalIdentifierType/gitoid"
gitoid_1 = "https://spdx.org/rdf/3.0.1/terms/Software/ContentIdentifierType/gitoid"
graph = "https://spdx.org/rdf/3.0.1/terms/Dataset/DatasetType/graph"
green = "https://spdx.org/rdf/3.0.1/terms/Dataset/ConfidentialityLevelType/green"
hasAddedFile = "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/hasAddedFile"
hasAssessmentFor = "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/hasAssessmentFor"
hasAssociatedVulnerability = "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/hasAssociatedVulnerability"
hasConcludedLicense = "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/hasConcludedLicense"
hasDataFile = "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/hasDataFile"
hasDeclaredLicense = "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/hasDeclaredLicense"
hasDeletedFile = "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/hasDeletedFile"
hasDependencyManifest = "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/hasDependencyManifest"
hasDistributionArtifact = "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/hasDistributionArtifact"
hasDocumentation = "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/hasDocumentation"
hasDynamicLink = "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/hasDynamicLink"
hasEvidence = "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/hasEvidence"
hasExample = "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/hasExample"
Hash = "https://spdx.org/rdf/3.0.1/terms/Core/Hash"
HashAlgorithm = "https://spdx.org/rdf/3.0.1/terms/Core/HashAlgorithm"
hasHost = "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/hasHost"
hasInput = "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/hasInput"
hasMetadata = "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/hasMetadata"
hasOptionalComponent = "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/hasOptionalComponent"
hasOptionalDependency = "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/hasOptionalDependency"
hasOutput = "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/hasOutput"
hasPrerequisite = "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/hasPrerequisite"
hasProvidedDependency = "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/hasProvidedDependency"
hasRequirement = "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/hasRequirement"
hasSpecification = "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/hasSpecification"
hasStaticLink = "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/hasStaticLink"
hasTest = "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/hasTest"
hasTestCase = "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/hasTestCase"
hasVariant = "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/hasVariant"
high = "https://spdx.org/rdf/3.0.1/terms/Security/CvssSeverityType/high"
high_1 = "https://spdx.org/rdf/3.0.1/terms/AI/SafetyRiskAssessmentType/high"
image = "https://spdx.org/rdf/3.0.1/terms/Dataset/DatasetType/image"
incomplete = "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipCompleteness/incomplete"
IndividualElement = "https://spdx.org/rdf/3.0.1/terms/Core/IndividualElement"
IndividualLicensingInfo = "https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/IndividualLicensingInfo"
inlineMitigationsAlreadyExist = (
    "https://spdx.org/rdf/3.0.1/terms/Security/VexJustificationType/inlineMitigationsAlreadyExist"
)
install = "https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/install"
IntegrityMethod = "https://spdx.org/rdf/3.0.1/terms/Core/IntegrityMethod"
invokedBy = "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/invokedBy"
issueTracker = "https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/issueTracker"
kev = "https://spdx.org/rdf/3.0.1/terms/Security/ExploitCatalogType/kev"
kilowattHour = "https://spdx.org/rdf/3.0.1/terms/AI/EnergyUnitType/kilowattHour"
library = "https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/library"
License = "https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/License"
license = "https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/license"
LicenseAddition = "https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/LicenseAddition"
LicenseExpression = "https://spdx.org/rdf/3.0.1/terms/SimpleLicensing/LicenseExpression"
LifecycleScopedRelationship = "https://spdx.org/rdf/3.0.1/terms/Core/LifecycleScopedRelationship"
LifecycleScopeType = "https://spdx.org/rdf/3.0.1/terms/Core/LifecycleScopeType"
limitedSupport = "https://spdx.org/rdf/3.0.1/terms/Core/SupportType/limitedSupport"
ListedLicense = "https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/ListedLicense"
ListedLicenseException = "https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/ListedLicenseException"
lite = "https://spdx.org/rdf/3.0.1/terms/Core/ProfileIdentifierType/lite"
low = "https://spdx.org/rdf/3.0.1/terms/AI/SafetyRiskAssessmentType/low"
low_1 = "https://spdx.org/rdf/3.0.1/terms/Security/CvssSeverityType/low"
mailingList = "https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/mailingList"
manifest = "https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/manifest"
mavenCentral = "https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/mavenCentral"
md2 = "https://spdx.org/rdf/3.0.1/terms/Core/HashAlgorithm/md2"
md4 = "https://spdx.org/rdf/3.0.1/terms/Core/HashAlgorithm/md4"
md5 = "https://spdx.org/rdf/3.0.1/terms/Core/HashAlgorithm/md5"
md6 = "https://spdx.org/rdf/3.0.1/terms/Core/HashAlgorithm/md6"
medium = "https://spdx.org/rdf/3.0.1/terms/Security/CvssSeverityType/medium"
medium_1 = "https://spdx.org/rdf/3.0.1/terms/AI/SafetyRiskAssessmentType/medium"
megajoule = "https://spdx.org/rdf/3.0.1/terms/AI/EnergyUnitType/megajoule"
metrics = "https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/metrics"
model = "https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/model"
modifiedBy = "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/modifiedBy"
module = "https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/module"
NamespaceMap = "https://spdx.org/rdf/3.0.1/terms/Core/NamespaceMap"
no = "https://spdx.org/rdf/3.0.1/terms/Core/PresenceType/no"
noAssertion = "https://spdx.org/rdf/3.0.1/terms/Core/PresenceType/noAssertion"
noAssertion_1 = "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipCompleteness/noAssertion"
noAssertion_2 = "https://spdx.org/rdf/3.0.1/terms/Dataset/DatasetType/noAssertion"
noAssertion_3 = "https://spdx.org/rdf/3.0.1/terms/Core/SupportType/noAssertion"
NoAssertionElement = "https://spdx.org/rdf/3.0.1/terms/Core/NoAssertionElement"
NoAssertionLicense = "https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/NoAssertionLicense"
none = "https://spdx.org/rdf/3.0.1/terms/Security/CvssSeverityType/none"
NoneElement = "https://spdx.org/rdf/3.0.1/terms/Core/NoneElement"
NoneLicense = "https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/NoneLicense"
noSupport = "https://spdx.org/rdf/3.0.1/terms/Core/SupportType/noSupport"
npm = "https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/npm"
nuget = "https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/nuget"
numeric = "https://spdx.org/rdf/3.0.1/terms/Dataset/DatasetType/numeric"
operatingSystem = "https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/operatingSystem"
Organization = "https://spdx.org/rdf/3.0.1/terms/Core/Organization"
OrLaterOperator = "https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/OrLaterOperator"
other = "https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/other"
other_1 = "https://spdx.org/rdf/3.0.1/terms/Core/LifecycleScopeType/other"
other_2 = "https://spdx.org/rdf/3.0.1/terms/Core/AnnotationType/other"
other_3 = "https://spdx.org/rdf/3.0.1/terms/Core/ExternalIdentifierType/other"
other_4 = "https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/other"
other_5 = "https://spdx.org/rdf/3.0.1/terms/Security/ExploitCatalogType/other"
other_6 = "https://spdx.org/rdf/3.0.1/terms/Core/HashAlgorithm/other"
other_7 = "https://spdx.org/rdf/3.0.1/terms/Dataset/DatasetType/other"
other_8 = "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/other"
other_9 = "https://spdx.org/rdf/3.0.1/terms/AI/EnergyUnitType/other"
Package = "https://spdx.org/rdf/3.0.1/terms/Software/Package"
packagedBy = "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/packagedBy"
packageUrl = "https://spdx.org/rdf/3.0.1/terms/Core/ExternalIdentifierType/packageUrl"
PackageVerificationCode = "https://spdx.org/rdf/3.0.1/terms/Core/PackageVerificationCode"
patch = "https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/patch"
patchedBy = "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/patchedBy"
Person = "https://spdx.org/rdf/3.0.1/terms/Core/Person"
platform = "https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/platform"
PositiveIntegerRange = "https://spdx.org/rdf/3.0.1/terms/Core/PositiveIntegerRange"
PresenceType = "https://spdx.org/rdf/3.0.1/terms/Core/PresenceType"
privacyAssessment = "https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/privacyAssessment"
productMetadata = "https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/productMetadata"
ProfileIdentifierType = "https://spdx.org/rdf/3.0.1/terms/Core/ProfileIdentifierType"
publishedBy = "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/publishedBy"
purchaseOrder = "https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/purchaseOrder"
qualityAssessmentReport = "https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/qualityAssessmentReport"
query = "https://spdx.org/rdf/3.0.1/terms/Dataset/DatasetAvailabilityType/query"
red = "https://spdx.org/rdf/3.0.1/terms/Dataset/ConfidentialityLevelType/red"
registration = "https://spdx.org/rdf/3.0.1/terms/Dataset/DatasetAvailabilityType/registration"
Relationship = "https://spdx.org/rdf/3.0.1/terms/Core/Relationship"
RelationshipCompleteness = "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipCompleteness"
RelationshipType = "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType"
releaseHistory = "https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/releaseHistory"
releaseNotes = "https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/releaseNotes"
reportedBy = "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/reportedBy"
republishedBy = "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/republishedBy"
requirement = "https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/requirement"
review = "https://spdx.org/rdf/3.0.1/terms/Core/AnnotationType/review"
riskAssessment = "https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/riskAssessment"
runtime = "https://spdx.org/rdf/3.0.1/terms/Software/SbomType/runtime"
runtime_1 = "https://spdx.org/rdf/3.0.1/terms/Core/LifecycleScopeType/runtime"
runtimeAnalysisReport = "https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/runtimeAnalysisReport"
SafetyRiskAssessmentType = "https://spdx.org/rdf/3.0.1/terms/AI/SafetyRiskAssessmentType"
Sbom = "https://spdx.org/rdf/3.0.1/terms/Software/Sbom"
SbomType = "https://spdx.org/rdf/3.0.1/terms/Software/SbomType"
scrapingScript = "https://spdx.org/rdf/3.0.1/terms/Dataset/DatasetAvailabilityType/scrapingScript"
secureSoftwareAttestation = "https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/secureSoftwareAttestation"
security = "https://spdx.org/rdf/3.0.1/terms/Core/ProfileIdentifierType/security"
securityAdversaryModel = "https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/securityAdversaryModel"
securityAdvisory = "https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/securityAdvisory"
securityFix = "https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/securityFix"
securityOther = "https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/securityOther"
securityOther_1 = "https://spdx.org/rdf/3.0.1/terms/Core/ExternalIdentifierType/securityOther"
securityPenTestReport = "https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/securityPenTestReport"
securityPolicy = "https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/securityPolicy"
securityThreatModel = "https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/securityThreatModel"
sensor = "https://spdx.org/rdf/3.0.1/terms/Dataset/DatasetType/sensor"
serializedInArtifact = "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/serializedInArtifact"
serious = "https://spdx.org/rdf/3.0.1/terms/AI/SafetyRiskAssessmentType/serious"
sha1 = "https://spdx.org/rdf/3.0.1/terms/Core/HashAlgorithm/sha1"
sha224 = "https://spdx.org/rdf/3.0.1/terms/Core/HashAlgorithm/sha224"
sha256 = "https://spdx.org/rdf/3.0.1/terms/Core/HashAlgorithm/sha256"
sha384 = "https://spdx.org/rdf/3.0.1/terms/Core/HashAlgorithm/sha384"
sha3_224 = "https://spdx.org/rdf/3.0.1/terms/Core/HashAlgorithm/sha3_224"
sha3_256 = "https://spdx.org/rdf/3.0.1/terms/Core/HashAlgorithm/sha3_256"
sha3_384 = "https://spdx.org/rdf/3.0.1/terms/Core/HashAlgorithm/sha3_384"
sha3_512 = "https://spdx.org/rdf/3.0.1/terms/Core/HashAlgorithm/sha3_512"
sha512 = "https://spdx.org/rdf/3.0.1/terms/Core/HashAlgorithm/sha512"
simpleLicensing = "https://spdx.org/rdf/3.0.1/terms/Core/ProfileIdentifierType/simpleLicensing"
SimpleLicensingText = "https://spdx.org/rdf/3.0.1/terms/SimpleLicensing/SimpleLicensingText"
Snippet = "https://spdx.org/rdf/3.0.1/terms/Software/Snippet"
socialMedia = "https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/socialMedia"
software = "https://spdx.org/rdf/3.0.1/terms/Core/ProfileIdentifierType/software"
SoftwareAgent = "https://spdx.org/rdf/3.0.1/terms/Core/SoftwareAgent"
SoftwareArtifact = "https://spdx.org/rdf/3.0.1/terms/Software/SoftwareArtifact"
SoftwarePurpose = "https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose"
source = "https://spdx.org/rdf/3.0.1/terms/Software/SbomType/source"
source_1 = "https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/source"
sourceArtifact = "https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/sourceArtifact"
SpdxDocument = "https://spdx.org/rdf/3.0.1/terms/Core/SpdxDocument"
SpdxOrganization = "https://spdx.org/rdf/3.0.1/terms/Core/SpdxOrganization"
specification = "https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/specification"
SsvcDecisionType = "https://spdx.org/rdf/3.0.1/terms/Security/SsvcDecisionType"
SsvcVulnAssessmentRelationship = "https://spdx.org/rdf/3.0.1/terms/Security/SsvcVulnAssessmentRelationship"
staticAnalysisReport = "https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/staticAnalysisReport"
structured = "https://spdx.org/rdf/3.0.1/terms/Dataset/DatasetType/structured"
support = "https://spdx.org/rdf/3.0.1/terms/Core/SupportType/support"
support_1 = "https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/support"
SupportType = "https://spdx.org/rdf/3.0.1/terms/Core/SupportType"
swhid = "https://spdx.org/rdf/3.0.1/terms/Core/ExternalIdentifierType/swhid"
swhid_1 = "https://spdx.org/rdf/3.0.1/terms/Software/ContentIdentifierType/swhid"
swid = "https://spdx.org/rdf/3.0.1/terms/Core/ExternalIdentifierType/swid"
syntactic = "https://spdx.org/rdf/3.0.1/terms/Dataset/DatasetType/syntactic"
test = "https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/test"
test_1 = "https://spdx.org/rdf/3.0.1/terms/Core/LifecycleScopeType/test"
testedOn = "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/testedOn"
text = "https://spdx.org/rdf/3.0.1/terms/Dataset/DatasetType/text"
timeseries = "https://spdx.org/rdf/3.0.1/terms/Dataset/DatasetType/timeseries"
timestamp = "https://spdx.org/rdf/3.0.1/terms/Dataset/DatasetType/timestamp"
Tool = "https://spdx.org/rdf/3.0.1/terms/Core/Tool"
track = "https://spdx.org/rdf/3.0.1/terms/Security/SsvcDecisionType/track"
trackStar = "https://spdx.org/rdf/3.0.1/terms/Security/SsvcDecisionType/trackStar"
trainedOn = "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/trainedOn"
underInvestigationFor = "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/underInvestigationFor"
urlScheme = "https://spdx.org/rdf/3.0.1/terms/Core/ExternalIdentifierType/urlScheme"
usesTool = "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/usesTool"
vcs = "https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/vcs"
VexAffectedVulnAssessmentRelationship = (
    "https://spdx.org/rdf/3.0.1/terms/Security/VexAffectedVulnAssessmentRelationship"
)
VexFixedVulnAssessmentRelationship = "https://spdx.org/rdf/3.0.1/terms/Security/VexFixedVulnAssessmentRelationship"
VexJustificationType = "https://spdx.org/rdf/3.0.1/terms/Security/VexJustificationType"
VexNotAffectedVulnAssessmentRelationship = (
    "https://spdx.org/rdf/3.0.1/terms/Security/VexNotAffectedVulnAssessmentRelationship"
)
VexUnderInvestigationVulnAssessmentRelationship = (
    "https://spdx.org/rdf/3.0.1/terms/Security/VexUnderInvestigationVulnAssessmentRelationship"
)
VexVulnAssessmentRelationship = "https://spdx.org/rdf/3.0.1/terms/Security/VexVulnAssessmentRelationship"
video = "https://spdx.org/rdf/3.0.1/terms/Dataset/DatasetType/video"
VulnAssessmentRelationship = "https://spdx.org/rdf/3.0.1/terms/Security/VulnAssessmentRelationship"
Vulnerability = "https://spdx.org/rdf/3.0.1/terms/Security/Vulnerability"
vulnerabilityDisclosureReport = "https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/vulnerabilityDisclosureReport"
vulnerabilityExploitabilityAssessment = (
    "https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/vulnerabilityExploitabilityAssessment"
)
vulnerableCodeCannotBeControlledByAdversary = (
    "https://spdx.org/rdf/3.0.1/terms/Security/VexJustificationType/vulnerableCodeCannotBeControlledByAdversary"
)
vulnerableCodeNotInExecutePath = (
    "https://spdx.org/rdf/3.0.1/terms/Security/VexJustificationType/vulnerableCodeNotInExecutePath"
)
vulnerableCodeNotPresent = "https://spdx.org/rdf/3.0.1/terms/Security/VexJustificationType/vulnerableCodeNotPresent"
WithAdditionOperator = "https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/WithAdditionOperator"
yes = "https://spdx.org/rdf/3.0.1/terms/Core/PresenceType/yes"


class DatasetType(_StavVocabEnum):
    """
    Dataset content types from SPDX 3.0.1 Dataset profile. Use for the dataset_type argument
    in pitloom loom.add_dataset() and related calls — maps directly to the SPDX
    dataset_datasetType field.
    """

    audio = "https://spdx.org/rdf/3.0.1/terms/Dataset/DatasetType/audio"
    categorical = "https://spdx.org/rdf/3.0.1/terms/Dataset/DatasetType/categorical"
    graph = "https://spdx.org/rdf/3.0.1/terms/Dataset/DatasetType/graph"
    image = "https://spdx.org/rdf/3.0.1/terms/Dataset/DatasetType/image"
    noAssertion = "https://spdx.org/rdf/3.0.1/terms/Dataset/DatasetType/noAssertion"
    numeric = "https://spdx.org/rdf/3.0.1/terms/Dataset/DatasetType/numeric"
    other = "https://spdx.org/rdf/3.0.1/terms/Dataset/DatasetType/other"
    sensor = "https://spdx.org/rdf/3.0.1/terms/Dataset/DatasetType/sensor"
    structured = "https://spdx.org/rdf/3.0.1/terms/Dataset/DatasetType/structured"
    syntactic = "https://spdx.org/rdf/3.0.1/terms/Dataset/DatasetType/syntactic"
    text = "https://spdx.org/rdf/3.0.1/terms/Dataset/DatasetType/text"
    timeseries = "https://spdx.org/rdf/3.0.1/terms/Dataset/DatasetType/timeseries"
    timestamp = "https://spdx.org/rdf/3.0.1/terms/Dataset/DatasetType/timestamp"
    video = "https://spdx.org/rdf/3.0.1/terms/Dataset/DatasetType/video"


class ConfidentialityLevel(_StavVocabEnum):
    """
    Dataset confidentiality levels from SPDX 3.0.1 Dataset profile (traffic-light protocol).
    Use to annotate the sensitivity classification of a dataset.
    """

    amber = "https://spdx.org/rdf/3.0.1/terms/Dataset/ConfidentialityLevelType/amber"
    clear = "https://spdx.org/rdf/3.0.1/terms/Dataset/ConfidentialityLevelType/clear"
    green = "https://spdx.org/rdf/3.0.1/terms/Dataset/ConfidentialityLevelType/green"
    red = "https://spdx.org/rdf/3.0.1/terms/Dataset/ConfidentialityLevelType/red"


# ── Metadata registry ──────────────────────────────────────────────────────────────
# Populated at import time so stav.label() / .definition() / .broader() work.
_register(
    {
        "https://spdx.org/rdf/3.0.1/terms/AI/AIPackage": {
            "label": "AIPackage",
            "definition": "Specifies an AI package and its associated information.",
            "broader": ("https://spdx.org/rdf/3.0.1/terms/Software/Package",),
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/AI/EnergyConsumption": {
            "label": "EnergyConsumption",
            "definition": "A class for describing the energy consumption incurred by an AI model in different stages of its lifecycle.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/AI/EnergyConsumptionDescription": {
            "label": "EnergyConsumptionDescription",
            "definition": "The class that helps note down the quantity of energy consumption and the unit used for measurement.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/AI/EnergyUnitType": {
            "label": "EnergyUnitType",
            "definition": "Specifies the unit of energy consumption.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/AI/EnergyUnitType/kilowattHour": {
            "label": "kilowattHour",
            "definition": "Kilowatt-hour.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/AI/EnergyUnitType/megajoule": {
            "label": "megajoule",
            "definition": "Megajoule.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/AI/EnergyUnitType/other": {
            "label": "other",
            "definition": "Any other units of energy measurement.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/AI/SafetyRiskAssessmentType": {
            "label": "SafetyRiskAssessmentType",
            "definition": "Specifies the safety risk level.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/AI/SafetyRiskAssessmentType/high": {
            "label": "high",
            "definition": "The second-highest level of risk posed by an AI system.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/AI/SafetyRiskAssessmentType/low": {
            "label": "low",
            "definition": "Low/no risk is posed by an AI system.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/AI/SafetyRiskAssessmentType/medium": {
            "label": "medium",
            "definition": "The third-highest level of risk posed by an AI system.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/AI/SafetyRiskAssessmentType/serious": {
            "label": "serious",
            "definition": "The highest level of risk posed by an AI system.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Build/Build": {
            "label": "Build",
            "definition": "Class that describes a build instance of software/artifacts.",
            "broader": ("https://spdx.org/rdf/3.0.1/terms/Core/Element",),
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/Agent": {
            "label": "Agent",
            "definition": "Agent represents anything with the potential to act on a system.",
            "broader": ("https://spdx.org/rdf/3.0.1/terms/Core/Element",),
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/Annotation": {
            "label": "Annotation",
            "definition": "An assertion made in relation to one or more elements.",
            "broader": ("https://spdx.org/rdf/3.0.1/terms/Core/Element",),
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/AnnotationType": {
            "label": "AnnotationType",
            "definition": "Specifies the type of an annotation.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/AnnotationType/other": {
            "label": "other",
            "definition": "Used to store extra information about an Element which is not part of a review (e.g. extra information provided during the creation of the Element).",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/AnnotationType/review": {
            "label": "review",
            "definition": "Used when someone reviews the Element.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/Artifact": {
            "label": "Artifact",
            "definition": "A distinct article or unit within the digital domain.",
            "broader": ("https://spdx.org/rdf/3.0.1/terms/Core/Element",),
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/Bom": {
            "label": "Bom",
            "definition": "A container for a grouping of SPDX-3.0 content characterizing details (provenence, composition, licensing, etc.) about a product.",
            "broader": ("https://spdx.org/rdf/3.0.1/terms/Core/Bundle",),
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/Bundle": {
            "label": "Bundle",
            "definition": "A collection of Elements that have a shared context.",
            "broader": ("https://spdx.org/rdf/3.0.1/terms/Core/ElementCollection",),
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/CreationInfo": {
            "label": "CreationInfo",
            "definition": "Provides information about the creation of the Element.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/DictionaryEntry": {
            "label": "DictionaryEntry",
            "definition": "A key with an associated value.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/Element": {
            "label": "Element",
            "definition": "Base domain class from which all other SPDX-3.0 domain classes derive.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/ElementCollection": {
            "label": "ElementCollection",
            "definition": "A collection of Elements, not necessarily with unifying context.",
            "broader": ("https://spdx.org/rdf/3.0.1/terms/Core/Element",),
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/ExternalIdentifier": {
            "label": "ExternalIdentifier",
            "definition": "A reference to a resource identifier defined outside the scope of SPDX-3.0 content that uniquely identifies an Element.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/ExternalIdentifierType": {
            "label": "ExternalIdentifierType",
            "definition": "Specifies the type of an external identifier.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/ExternalIdentifierType/cpe22": {
            "label": "cpe22",
            "definition": "[Common Platform Enumeration Specification 2.2](https://cpe.mitre.org/files/cpe-specification_2.2.pdf)",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/ExternalIdentifierType/cpe23": {
            "label": "cpe23",
            "definition": "[Common Platform Enumeration: Naming Specification Version 2.3](https://csrc.nist.gov/publications/detail/nistir/7695/final)",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/ExternalIdentifierType/cve": {
            "label": "cve",
            "definition": "Common Vulnerabilities and Exposures identifiers, an identifier for a specific software flaw defined within the official CVE Dictionary and that conforms to the [CVE specification](https://csrc.nist.gov/glossary/term/cve_id).",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/ExternalIdentifierType/email": {
            "label": "email",
            "definition": "Email address, as defined in [RFC 3696](https://datatracker.ietf.org/doc/rfc3986/) Section 3.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/ExternalIdentifierType/gitoid": {
            "label": "gitoid",
            "definition": "[Gitoid](https://www.iana.org/assignments/uri-schemes/prov/gitoid), stands for [Git Object ID](https://git-scm.com/book/en/v2/Git-Internals-Git-Objects). A gitoid of type blob is a unique hash of a binary artifact. A gitoid may represent either an [Artifact Identifier](https://github.com/omnibor/...",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/ExternalIdentifierType/other": {
            "label": "other",
            "definition": "Used when the type does not match any of the other options.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/ExternalIdentifierType/packageUrl": {
            "label": "packageUrl",
            "definition": "Package URL, as defined in the corresponding [Annex](../../../annexes/pkg-url-specification.md) of this specification.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/ExternalIdentifierType/securityOther": {
            "label": "securityOther",
            "definition": "Used when there is a security related identifier of unspecified type.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/ExternalIdentifierType/swhid": {
            "label": "swhid",
            "definition": "SoftWare Hash IDentifier, a persistent intrinsic identifier for digital artifacts, such as files, trees (also known as directories or folders), commits, and other objects typically found in version control systems. The format of the identifiers is defined in the [SWHID specification](https://www....",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/ExternalIdentifierType/swid": {
            "label": "swid",
            "definition": "Concise Software Identification (CoSWID) tag, as defined in [RFC 9393](https://datatracker.ietf.org/doc/rfc9393/) Section 2.3.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/ExternalIdentifierType/urlScheme": {
            "label": "urlScheme",
            "definition": "[Uniform Resource Identifier (URI) Schemes](https://www.iana.org/assignments/uri-schemes/uri-schemes.xhtml). The scheme used in order to locate a resource.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/ExternalMap": {
            "label": "ExternalMap",
            "definition": "A map of Element identifiers that are used within an SpdxDocument but defined external to that SpdxDocument.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/ExternalRef": {
            "label": "ExternalRef",
            "definition": "A reference to a resource outside the scope of SPDX-3.0 content related to an Element.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType": {
            "label": "ExternalRefType",
            "definition": "Specifies the type of an external reference.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/altDownloadLocation": {
            "label": "altDownloadLocation",
            "definition": "A reference to an alternative download location.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/altWebPage": {
            "label": "altWebPage",
            "definition": "A reference to an alternative web page.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/binaryArtifact": {
            "label": "binaryArtifact",
            "definition": "A reference to binary artifacts related to a package.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/bower": {
            "label": "bower",
            "definition": 'A reference to a Bower package. The package locator format, looks like `package#version`, is defined in the "install" section of [Bower API documentation](https://bower.io/docs/api/#install).',
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/buildMeta": {
            "label": "buildMeta",
            "definition": "A reference build metadata related to a published package.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/buildSystem": {
            "label": "buildSystem",
            "definition": "A reference build system used to create or publish the package.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/certificationReport": {
            "label": "certificationReport",
            "definition": "A reference to a certification report for a package from an accredited/independent body.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/chat": {
            "label": "chat",
            "definition": "A reference to the instant messaging system used by the maintainer for a package.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/componentAnalysisReport": {
            "label": "componentAnalysisReport",
            "definition": "A reference to a Software Composition Analysis (SCA) report.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/cwe": {
            "label": "cwe",
            "definition": "[Common Weakness Enumeration](https://csrc.nist.gov/glossary/term/common_weakness_enumeration). A reference to a source of software flaw defined within the official [CWE List](https://cwe.mitre.org/data/) that conforms to the [CWE specification](https://cwe.mitre.org/).",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/documentation": {
            "label": "documentation",
            "definition": "A reference to the documentation for a package.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/dynamicAnalysisReport": {
            "label": "dynamicAnalysisReport",
            "definition": "A reference to a dynamic analysis report for a package.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/eolNotice": {
            "label": "eolNotice",
            "definition": "A reference to the End Of Sale (EOS) and/or End Of Life (EOL) information related to a package.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/exportControlAssessment": {
            "label": "exportControlAssessment",
            "definition": "A reference to a export control assessment for a package.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/funding": {
            "label": "funding",
            "definition": "A reference to funding information related to a package.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/issueTracker": {
            "label": "issueTracker",
            "definition": "A reference to the issue tracker for a package.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/license": {
            "label": "license",
            "definition": "A reference to additional license information related to an artifact.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/mailingList": {
            "label": "mailingList",
            "definition": "A reference to the mailing list used by the maintainer for a package.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/mavenCentral": {
            "label": "mavenCentral",
            "definition": "A reference to a Maven repository artifact. The artifact locator format is defined in the [Maven documentation](https://maven.apache.org/guides/mini/guide-naming-conventions.html) and looks like `groupId:artifactId[:version]`.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/metrics": {
            "label": "metrics",
            "definition": "A reference to metrics related to package such as OpenSSF scorecards.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/npm": {
            "label": "npm",
            "definition": "A reference to an npm package. The package locator format is defined in the [npm documentation](https://docs.npmjs.com/cli/v10/configuring-npm/package-json) and looks like `package@version`.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/nuget": {
            "label": "nuget",
            "definition": "A reference to a NuGet package. The package locator format is defined in the [NuGet documentation](https://docs.nuget.org) and looks like `package/version`.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/other": {
            "label": "other",
            "definition": "Used when the type does not match any of the other options.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/privacyAssessment": {
            "label": "privacyAssessment",
            "definition": "A reference to a privacy assessment for a package.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/productMetadata": {
            "label": "productMetadata",
            "definition": "A reference to additional product metadata such as reference within organization's product catalog.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/purchaseOrder": {
            "label": "purchaseOrder",
            "definition": "A reference to a purchase order for a package.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/qualityAssessmentReport": {
            "label": "qualityAssessmentReport",
            "definition": "A reference to a quality assessment for a package.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/releaseHistory": {
            "label": "releaseHistory",
            "definition": "A reference to a published list of releases for a package.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/releaseNotes": {
            "label": "releaseNotes",
            "definition": "A reference to the release notes for a package.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/riskAssessment": {
            "label": "riskAssessment",
            "definition": "A reference to a risk assessment for a package.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/runtimeAnalysisReport": {
            "label": "runtimeAnalysisReport",
            "definition": "A reference to a runtime analysis report for a package.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/secureSoftwareAttestation": {
            "label": "secureSoftwareAttestation",
            "definition": "A reference to information assuring that the software is developed using security practices as defined by [NIST SP 800-218 Secure Software Development Framework (SSDF) Version 1.1](https://csrc.nist.gov/pubs/sp/800/218/final) or [CISA Secure Software Development Attestation Form](https://www.cisa...",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/securityAdversaryModel": {
            "label": "securityAdversaryModel",
            "definition": "A reference to the security adversary model for a package.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/securityAdvisory": {
            "label": "securityAdvisory",
            "definition": "A reference to a published security advisory (where advisory as defined per [ISO 29147:2018](https://www.iso.org/standard/72311.html)) that may affect one or more elements, e.g., vendor advisories or specific NVD entries.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/securityFix": {
            "label": "securityFix",
            "definition": "A reference to the patch or source code that fixes a vulnerability.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/securityOther": {
            "label": "securityOther",
            "definition": "A reference to related security information of unspecified type.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/securityPenTestReport": {
            "label": "securityPenTestReport",
            "definition": "A reference to a [penetration test](https://en.wikipedia.org/wiki/Penetration_test) report for a package.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/securityPolicy": {
            "label": "securityPolicy",
            "definition": "A reference to instructions for reporting newly discovered security vulnerabilities for a package.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/securityThreatModel": {
            "label": "securityThreatModel",
            "definition": "A reference the [security threat model](https://en.wikipedia.org/wiki/Threat_model) for a package.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/socialMedia": {
            "label": "socialMedia",
            "definition": "A reference to a social media channel for a package.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/sourceArtifact": {
            "label": "sourceArtifact",
            "definition": "A reference to an artifact containing the sources for a package.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/staticAnalysisReport": {
            "label": "staticAnalysisReport",
            "definition": "A reference to a static analysis report for a package.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/support": {
            "label": "support",
            "definition": "A reference to the software support channel or other support information for a package.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/vcs": {
            "label": "vcs",
            "definition": "A reference to a version control system related to a software artifact.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/vulnerabilityDisclosureReport": {
            "label": "vulnerabilityDisclosureReport",
            "definition": "A reference to a Vulnerability Disclosure Report (VDR) which provides the software supplier's analysis and findings describing the impact (or lack of impact) that reported vulnerabilities have on packages or products in the supplier's SBOM as defined in [NIST SP 800-161 Cybersecurity Supply Chain...",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/vulnerabilityExploitabilityAssessment": {
            "label": "vulnerabilityExploitabilityAssessment",
            "definition": "A reference to a Vulnerability Exploitability eXchange (VEX) statement which provides information on whether a product is impacted by a specific vulnerability in an included package and, if affected, whether there are actions recommended to remediate. See also [NTIA VEX one-page summary](https://...",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/Hash": {
            "label": "Hash",
            "definition": "A mathematically calculated representation of a grouping of data.",
            "broader": ("https://spdx.org/rdf/3.0.1/terms/Core/IntegrityMethod",),
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/HashAlgorithm": {
            "label": "HashAlgorithm",
            "definition": "A mathematical algorithm that maps data of arbitrary size to a bit string.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/HashAlgorithm/adler32": {
            "label": "adler32",
            "definition": "Adler-32 checksum is part of the widely used zlib compression library as defined in [RFC 1950](https://datatracker.ietf.org/doc/rfc1950/) Section 2.3.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/HashAlgorithm/blake2b256": {
            "label": "blake2b256",
            "definition": "BLAKE2b algorithm with a digest size of 256, as defined in [RFC 7693](https://datatracker.ietf.org/doc/rfc7693/) Section 4.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/HashAlgorithm/blake2b384": {
            "label": "blake2b384",
            "definition": "BLAKE2b algorithm with a digest size of 384, as defined in [RFC 7693](https://datatracker.ietf.org/doc/rfc7693/) Section 4.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/HashAlgorithm/blake2b512": {
            "label": "blake2b512",
            "definition": "BLAKE2b algorithm with a digest size of 512, as defined in [RFC 7693](https://datatracker.ietf.org/doc/rfc7693/) Section 4.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/HashAlgorithm/blake3": {
            "label": "blake3",
            "definition": "[BLAKE3](https://github.com/BLAKE3-team/BLAKE3-specs/blob/master/blake3.pdf)",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/HashAlgorithm/crystalsDilithium": {
            "label": "crystalsDilithium",
            "definition": "[Dilithium](https://pq-crystals.org/dilithium/)",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/HashAlgorithm/crystalsKyber": {
            "label": "crystalsKyber",
            "definition": "[Kyber](https://pq-crystals.org/kyber/)",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/HashAlgorithm/falcon": {
            "label": "falcon",
            "definition": "[FALCON](https://falcon-sign.info/falcon.pdf)",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/HashAlgorithm/md2": {
            "label": "md2",
            "definition": "MD2 message-digest algorithm, as defined in [RFC 1319](https://datatracker.ietf.org/doc/rfc1319/).",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/HashAlgorithm/md4": {
            "label": "md4",
            "definition": "MD4 message-digest algorithm, as defined in [RFC 1186](https://datatracker.ietf.org/doc/rfc1186/).",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/HashAlgorithm/md5": {
            "label": "md5",
            "definition": "MD5 message-digest algorithm, as defined in [RFC 1321](https://datatracker.ietf.org/doc/rfc1321/).",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/HashAlgorithm/md6": {
            "label": "md6",
            "definition": "[MD6 hash function](https://people.csail.mit.edu/rivest/pubs/RABCx08.pdf)",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/HashAlgorithm/other": {
            "label": "other",
            "definition": "any hashing algorithm that does not exist in this list of entries",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/HashAlgorithm/sha1": {
            "label": "sha1",
            "definition": "SHA-1, a secure hashing algorithm, as defined in [RFC 3174](https://datatracker.ietf.org/doc/rfc3174/).",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/HashAlgorithm/sha224": {
            "label": "sha224",
            "definition": "SHA-2 with a digest length of 224, as defined in [RFC 3874](https://datatracker.ietf.org/doc/rfc3874/).",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/HashAlgorithm/sha256": {
            "label": "sha256",
            "definition": "SHA-2 with a digest length of 256, as defined in [RFC 6234](https://datatracker.ietf.org/doc/rfc6234/).",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/HashAlgorithm/sha384": {
            "label": "sha384",
            "definition": "SHA-2 with a digest length of 384, as defined in [RFC 6234](https://datatracker.ietf.org/doc/rfc6234/).",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/HashAlgorithm/sha3_224": {
            "label": "sha3_224",
            "definition": "SHA-3 with a digest length of 224, as defined in [FIPS 202](https://csrc.nist.gov/pubs/fips/202/final).",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/HashAlgorithm/sha3_256": {
            "label": "sha3_256",
            "definition": "SHA-3 with a digest length of 256, as defined in [FIPS 202](https://csrc.nist.gov/pubs/fips/202/final).",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/HashAlgorithm/sha3_384": {
            "label": "sha3_384",
            "definition": "SHA-3 with a digest length of 384, as defined in [FIPS 202](https://csrc.nist.gov/pubs/fips/202/final).",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/HashAlgorithm/sha3_512": {
            "label": "sha3_512",
            "definition": "SHA-3 with a digest length of 512, as defined in [FIPS 202](https://csrc.nist.gov/pubs/fips/202/final).",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/HashAlgorithm/sha512": {
            "label": "sha512",
            "definition": "SHA-2 with a digest length of 512, as defined in [RFC 6234](https://datatracker.ietf.org/doc/rfc6234/).",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/IndividualElement": {
            "label": "IndividualElement",
            "definition": "A concrete subclass of Element used by Individuals in the Core profile.",
            "broader": ("https://spdx.org/rdf/3.0.1/terms/Core/Element",),
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/IntegrityMethod": {
            "label": "IntegrityMethod",
            "definition": "Provides an independently reproducible mechanism that permits verification of a specific Element.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/LifecycleScopeType": {
            "label": "LifecycleScopeType",
            "definition": "Provide an enumerated set of lifecycle phases that can provide context to relationships.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/LifecycleScopeType/build": {
            "label": "build",
            "definition": "A relationship has specific context implications during an element's build phase, during development.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/LifecycleScopeType/design": {
            "label": "design",
            "definition": "A relationship has specific context implications during an element's design.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/LifecycleScopeType/development": {
            "label": "development",
            "definition": "A relationship has specific context implications during development phase of an element.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/LifecycleScopeType/other": {
            "label": "other",
            "definition": "A relationship has other specific context information necessary to capture that the above set of enumerations does not handle.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/LifecycleScopeType/runtime": {
            "label": "runtime",
            "definition": "A relationship has specific context implications during the execution phase of an element.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/LifecycleScopeType/test": {
            "label": "test",
            "definition": "A relationship has specific context implications during an element's testing phase, during development.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/LifecycleScopedRelationship": {
            "label": "LifecycleScopedRelationship",
            "definition": "Provide context for a relationship that occurs in the lifecycle.",
            "broader": ("https://spdx.org/rdf/3.0.1/terms/Core/Relationship",),
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/NamespaceMap": {
            "label": "NamespaceMap",
            "definition": "A mapping between prefixes and namespace partial URIs.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/NoAssertionElement": {
            "label": "NoAssertionElement",
            "definition": "An Individual Value for Element representing a set of Elements of unknown identify or cardinality (number).",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/NoneElement": {
            "label": "NoneElement",
            "definition": "An Individual Value for Element representing a set of Elements with cardinality (number/count) of zero.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/Organization": {
            "label": "Organization",
            "definition": "A group of people who work together in an organized way for a shared purpose.",
            "broader": ("https://spdx.org/rdf/3.0.1/terms/Core/Agent",),
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/PackageVerificationCode": {
            "label": "PackageVerificationCode",
            "definition": "An SPDX version 2.X compatible verification method for software packages.",
            "broader": ("https://spdx.org/rdf/3.0.1/terms/Core/IntegrityMethod",),
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/Person": {
            "label": "Person",
            "definition": "An individual human being.",
            "broader": ("https://spdx.org/rdf/3.0.1/terms/Core/Agent",),
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/PositiveIntegerRange": {
            "label": "PositiveIntegerRange",
            "definition": "A tuple of two positive integers that define a range.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/PresenceType": {
            "label": "PresenceType",
            "definition": "Categories of presence or absence.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/PresenceType/no": {
            "label": "no",
            "definition": "Indicates absence of the field.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/PresenceType/noAssertion": {
            "label": "noAssertion",
            "definition": "Makes no assertion about the field.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/PresenceType/yes": {
            "label": "yes",
            "definition": "Indicates presence of the field.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/ProfileIdentifierType": {
            "label": "ProfileIdentifierType",
            "definition": "Enumeration of the valid profiles.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/ProfileIdentifierType/ai": {
            "label": "ai",
            "definition": "the element follows the AI profile specification",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/ProfileIdentifierType/build": {
            "label": "build",
            "definition": "the element follows the Build profile specification",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/ProfileIdentifierType/core": {
            "label": "core",
            "definition": "the element follows the Core profile specification",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/ProfileIdentifierType/dataset": {
            "label": "dataset",
            "definition": "the element follows the Dataset profile specification",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/ProfileIdentifierType/expandedLicensing": {
            "label": "expandedLicensing",
            "definition": "the element follows the ExpandedLicensing profile specification",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/ProfileIdentifierType/extension": {
            "label": "extension",
            "definition": "the element follows the Extension profile specification",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/ProfileIdentifierType/lite": {
            "label": "lite",
            "definition": "the element follows the Lite profile specification",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/ProfileIdentifierType/security": {
            "label": "security",
            "definition": "the element follows the Security profile specification",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/ProfileIdentifierType/simpleLicensing": {
            "label": "simpleLicensing",
            "definition": "the element follows the SimpleLicensing profile specification",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/ProfileIdentifierType/software": {
            "label": "software",
            "definition": "the element follows the Software profile specification",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/Relationship": {
            "label": "Relationship",
            "definition": "Describes a relationship between one or more elements.",
            "broader": ("https://spdx.org/rdf/3.0.1/terms/Core/Element",),
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipCompleteness": {
            "label": "RelationshipCompleteness",
            "definition": "Indicates whether a relationship is known to be complete, incomplete, or if no assertion is made with respect to relationship completeness.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipCompleteness/complete": {
            "label": "complete",
            "definition": "The relationship is known to be exhaustive.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipCompleteness/incomplete": {
            "label": "incomplete",
            "definition": "The relationship is known not to be exhaustive.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipCompleteness/noAssertion": {
            "label": "noAssertion",
            "definition": "No assertion can be made about the completeness of the relationship.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType": {
            "label": "RelationshipType",
            "definition": "Information about the relationship between two Elements.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/affects": {
            "label": "affects",
            "definition": "The `from` Vulnerability affects each `to` Element. The use of the `affects` type is constrained to `VexAffectedVulnAssessmentRelationship` classed relationships.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/amendedBy": {
            "label": "amendedBy",
            "definition": "The `from` Element is amended by each `to` Element.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/ancestorOf": {
            "label": "ancestorOf",
            "definition": "The `from` Element is an ancestor of each `to` Element.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/availableFrom": {
            "label": "availableFrom",
            "definition": "The `from` Element is available from the additional supplier described by each `to` Element.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/configures": {
            "label": "configures",
            "definition": "The `from` Element is a configuration applied to each `to` Element, during a LifecycleScopeType period.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/contains": {
            "label": "contains",
            "definition": "The `from` Element contains each `to` Element.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/coordinatedBy": {
            "label": "coordinatedBy",
            "definition": "The `from` Vulnerability is coordinatedBy the `to` Agent(s) (vendor, researcher, or consumer agent).",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/copiedTo": {
            "label": "copiedTo",
            "definition": "The `from` Element has been copied to each `to` Element.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/delegatedTo": {
            "label": "delegatedTo",
            "definition": "The `from` Agent is delegating an action to the Agent of the `to` Relationship (which must be of type invokedBy), during a LifecycleScopeType (e.g. the `to` invokedBy Relationship is being done on behalf of `from`).",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/dependsOn": {
            "label": "dependsOn",
            "definition": "The `from` Element depends on each `to` Element, during a LifecycleScopeType period.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/descendantOf": {
            "label": "descendantOf",
            "definition": "The `from` Element is a descendant of each `to` Element.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/describes": {
            "label": "describes",
            "definition": "The `from` Element describes each `to` Element. To denote the root(s) of a tree of elements in a collection, the rootElement property should be used.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/doesNotAffect": {
            "label": "doesNotAffect",
            "definition": "The `from` Vulnerability has no impact on each `to` Element. The use of the `doesNotAffect` is constrained to `VexNotAffectedVulnAssessmentRelationship` classed relationships.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/expandsTo": {
            "label": "expandsTo",
            "definition": "The `from` archive expands out as an artifact described by each `to` Element.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/exploitCreatedBy": {
            "label": "exploitCreatedBy",
            "definition": "The `from` Vulnerability has had an exploit created against it by each `to` Agent.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/fixedBy": {
            "label": "fixedBy",
            "definition": "Designates a `from` Vulnerability has been fixed by the `to` Agent(s).",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/fixedIn": {
            "label": "fixedIn",
            "definition": "A `from` Vulnerability has been fixed in each `to` Element. The use of the `fixedIn` type is constrained to `VexFixedVulnAssessmentRelationship` classed relationships.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/foundBy": {
            "label": "foundBy",
            "definition": "Designates a `from` Vulnerability was originally discovered by the `to` Agent(s).",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/generates": {
            "label": "generates",
            "definition": "The `from` Element generates each `to` Element.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/hasAddedFile": {
            "label": "hasAddedFile",
            "definition": "Every `to` Element is a file added to the `from` Element (`from` hasAddedFile `to`).",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/hasAssessmentFor": {
            "label": "hasAssessmentFor",
            "definition": "Relates a `from` Vulnerability and each `to` Element with a security assessment. To be used with `VulnAssessmentRelationship` types.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/hasAssociatedVulnerability": {
            "label": "hasAssociatedVulnerability",
            "definition": "Used to associate a `from` Artifact with each `to` Vulnerability.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/hasConcludedLicense": {
            "label": "hasConcludedLicense",
            "definition": "The `from` SoftwareArtifact is concluded by the SPDX data creator to be governed by each `to` license.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/hasDataFile": {
            "label": "hasDataFile",
            "definition": "The `from` Element treats each `to` Element as a data file. A data file is an artifact that stores data required or optional for the `from` Element's functionality. A data file can be a database file, an index file, a log file, an AI model file, a calibration data file, a temporary file, a backup...",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/hasDeclaredLicense": {
            "label": "hasDeclaredLicense",
            "definition": "The `from` SoftwareArtifact was discovered to actually contain each `to` license, for example as detected by use of automated tooling.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/hasDeletedFile": {
            "label": "hasDeletedFile",
            "definition": "Every `to` Element is a file deleted from the `from` Element (`from` hasDeletedFile `to`).",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/hasDependencyManifest": {
            "label": "hasDependencyManifest",
            "definition": "The `from` Element has manifest files that contain dependency information in each `to` Element.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/hasDistributionArtifact": {
            "label": "hasDistributionArtifact",
            "definition": "The `from` Element is distributed as an artifact in each `to` Element (e.g. an RPM or archive file).",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/hasDocumentation": {
            "label": "hasDocumentation",
            "definition": "The `from` Element is documented by each `to` Element.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/hasDynamicLink": {
            "label": "hasDynamicLink",
            "definition": "The `from` Element dynamically links in each `to` Element, during a LifecycleScopeType period.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/hasEvidence": {
            "label": "hasEvidence",
            "definition": "Every `to` Element is considered as evidence for the `from` Element (`from` hasEvidence `to`).",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/hasExample": {
            "label": "hasExample",
            "definition": "Every `to` Element is an example for the `from` Element (`from` hasExample `to`).",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/hasHost": {
            "label": "hasHost",
            "definition": "The `from` Build was run on the `to` Element during a LifecycleScopeType period (e.g. the host that the build runs on).",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/hasInput": {
            "label": "hasInput",
            "definition": "The `from` Build has each `to` Element as an input, during a LifecycleScopeType period.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/hasMetadata": {
            "label": "hasMetadata",
            "definition": "Every `to` Element is metadata about the `from` Element (`from` hasMetadata `to`).",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/hasOptionalComponent": {
            "label": "hasOptionalComponent",
            "definition": "Every `to` Element is an optional component of the `from` Element (`from` hasOptionalComponent `to`).",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/hasOptionalDependency": {
            "label": "hasOptionalDependency",
            "definition": "The `from` Element optionally depends on each `to` Element, during a LifecycleScopeType period.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/hasOutput": {
            "label": "hasOutput",
            "definition": "The `from` Build element generates each `to` Element as an output, during a LifecycleScopeType period.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/hasPrerequisite": {
            "label": "hasPrerequisite",
            "definition": "The `from` Element has a prerequisite on each `to` Element, during a LifecycleScopeType period.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/hasProvidedDependency": {
            "label": "hasProvidedDependency",
            "definition": "The `from` Element has a dependency on each `to` Element, dependency is not in the distributed artifact, but assumed to be provided, during a LifecycleScopeType period.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/hasRequirement": {
            "label": "hasRequirement",
            "definition": "The `from` Element has a requirement on each `to` Element, during a LifecycleScopeType period.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/hasSpecification": {
            "label": "hasSpecification",
            "definition": "Every `to` Element is a specification for the `from` Element (`from` hasSpecification `to`), during a LifecycleScopeType period.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/hasStaticLink": {
            "label": "hasStaticLink",
            "definition": "The `from` Element statically links in each `to` Element, during a LifecycleScopeType period.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/hasTest": {
            "label": "hasTest",
            "definition": "Every `to` Element is a test artifact for the `from` Element (`from` hasTest `to`), during a LifecycleScopeType period.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/hasTestCase": {
            "label": "hasTestCase",
            "definition": "Every `to` Element is a test case for the `from` Element (`from` hasTestCase `to`).",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/hasVariant": {
            "label": "hasVariant",
            "definition": "Every `to` Element is a variant the `from` Element (`from` hasVariant `to`).",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/invokedBy": {
            "label": "invokedBy",
            "definition": "The `from` Element was invoked by the `to` Agent, during a LifecycleScopeType period (for example, a Build element that describes a build step).",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/modifiedBy": {
            "label": "modifiedBy",
            "definition": "The `from` Element is modified by each `to` Element.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/other": {
            "label": "other",
            "definition": "Every `to` Element is related to the `from` Element where the relationship type is not described by any of the SPDX relationship types (this relationship is directionless).",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/packagedBy": {
            "label": "packagedBy",
            "definition": "Every `to` Element is a packaged instance of the `from` Element (`from` packagedBy `to`).",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/patchedBy": {
            "label": "patchedBy",
            "definition": "Every `to` Element is a patch for the `from` Element (`from` patchedBy `to`).",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/publishedBy": {
            "label": "publishedBy",
            "definition": "Designates a `from` Vulnerability was made available for public use or reference by each `to` Agent.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/reportedBy": {
            "label": "reportedBy",
            "definition": "Designates a `from` Vulnerability was first reported to a project, vendor, or tracking database for formal identification by each `to` Agent.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/republishedBy": {
            "label": "republishedBy",
            "definition": "Designates a `from` Vulnerability's details were tracked, aggregated, and/or enriched to improve context (i.e. NVD) by each `to` Agent.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/serializedInArtifact": {
            "label": "serializedInArtifact",
            "definition": "The `from` SpdxDocument can be found in a serialized form in each `to` Artifact.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/testedOn": {
            "label": "testedOn",
            "definition": "The `from` Element has been tested on the `to` Element(s).",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/trainedOn": {
            "label": "trainedOn",
            "definition": "The `from` Element has been trained on the `to` Element(s).",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/underInvestigationFor": {
            "label": "underInvestigationFor",
            "definition": "The `from` Vulnerability impact is being investigated for each `to` Element. The use of the `underInvestigationFor` type is constrained to `VexUnderInvestigationVulnAssessmentRelationship` classed relationships.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/usesTool": {
            "label": "usesTool",
            "definition": "The `from` Element uses each `to` Element as a tool, during a LifecycleScopeType period.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/SoftwareAgent": {
            "label": "SoftwareAgent",
            "definition": "A software agent.",
            "broader": ("https://spdx.org/rdf/3.0.1/terms/Core/Agent",),
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/SpdxDocument": {
            "label": "SpdxDocument",
            "definition": "A collection of SPDX Elements that could potentially be serialized.",
            "broader": ("https://spdx.org/rdf/3.0.1/terms/Core/ElementCollection",),
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/SpdxOrganization": {
            "label": "SpdxOrganization",
            "definition": "An Organization representing the SPDX Project.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/SupportType": {
            "label": "SupportType",
            "definition": "Indicates the type of support that is associated with an artifact.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/SupportType/deployed": {
            "label": "deployed",
            "definition": "in addition to being supported by the supplier, the software is known to have been deployed and is in use.  For a software as a service provider, this implies the software is now available as a service.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/SupportType/development": {
            "label": "development",
            "definition": "the artifact is in active development and is not considered ready for formal support from the supplier.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/SupportType/endOfSupport": {
            "label": "endOfSupport",
            "definition": "there is a defined end of support for the artifact from the supplier.  This may also be referred to as end of life. There is a validUntilDate that can be used to signal when support ends for the artifact.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/SupportType/limitedSupport": {
            "label": "limitedSupport",
            "definition": "the artifact has been released, and there is limited support available from the supplier. There is a validUntilDate that can provide additional information about the duration of support.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/SupportType/noAssertion": {
            "label": "noAssertion",
            "definition": "no assertion about the type of support is made.   This is considered the default if no other support type is used.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/SupportType/noSupport": {
            "label": "noSupport",
            "definition": "there is no support for the artifact from the supplier, consumer assumes any support obligations.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/SupportType/support": {
            "label": "support",
            "definition": "the artifact has been released, and is supported from the supplier.   There is a validUntilDate that can provide additional information about the duration of support.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Core/Tool": {
            "label": "Tool",
            "definition": "An element of hardware and/or software utilized to carry out a particular function.",
            "broader": ("https://spdx.org/rdf/3.0.1/terms/Core/Element",),
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Dataset/ConfidentialityLevelType": {
            "label": "ConfidentialityLevelType",
            "definition": "Categories of confidentiality level.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Dataset/ConfidentialityLevelType/amber": {
            "label": "amber",
            "definition": "Data points in the dataset can be shared only with specific organizations and their clients on a need to know basis.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Dataset/ConfidentialityLevelType/clear": {
            "label": "clear",
            "definition": "Dataset may be distributed freely, without restriction.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Dataset/ConfidentialityLevelType/green": {
            "label": "green",
            "definition": "Dataset can be shared within a community of peers and partners.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Dataset/ConfidentialityLevelType/red": {
            "label": "red",
            "definition": "Data points in the dataset are highly confidential and can only be shared with named recipients.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Dataset/DatasetAvailabilityType": {
            "label": "DatasetAvailabilityType",
            "definition": "Availability of dataset.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Dataset/DatasetAvailabilityType/clickthrough": {
            "label": "clickthrough",
            "definition": "the dataset is not publicly available and can only be accessed after affirmatively accepting terms on a clickthrough webpage.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Dataset/DatasetAvailabilityType/directDownload": {
            "label": "directDownload",
            "definition": "the dataset is publicly available and can be downloaded directly.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Dataset/DatasetAvailabilityType/query": {
            "label": "query",
            "definition": "the dataset is publicly available, but not all at once, and can only be accessed through queries which return parts of the dataset.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Dataset/DatasetAvailabilityType/registration": {
            "label": "registration",
            "definition": "the dataset is not publicly available and an email registration is required before accessing the dataset, although without an affirmative acceptance of terms.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Dataset/DatasetAvailabilityType/scrapingScript": {
            "label": "scrapingScript",
            "definition": "the dataset provider is not making available the underlying data and the dataset must be reassembled, typically using the provided script for scraping the data.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Dataset/DatasetPackage": {
            "label": "DatasetPackage",
            "definition": "Specifies a data package and its associated information.",
            "broader": ("https://spdx.org/rdf/3.0.1/terms/Software/Package",),
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Dataset/DatasetType": {
            "label": "DatasetType",
            "definition": "Enumeration of dataset types.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Dataset/DatasetType/audio": {
            "label": "audio",
            "definition": "data is audio based, such as a collection of music from the 80s.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Dataset/DatasetType/categorical": {
            "label": "categorical",
            "definition": "data that is classified into a discrete number of categories, such as the eye color of a population of people.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Dataset/DatasetType/graph": {
            "label": "graph",
            "definition": "data is in the form of a graph where entries are somehow related to each other through edges, such a social network of friends.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Dataset/DatasetType/image": {
            "label": "image",
            "definition": "data is a collection of images such as pictures of animals.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Dataset/DatasetType/noAssertion": {
            "label": "noAssertion",
            "definition": "data type is not known.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Dataset/DatasetType/numeric": {
            "label": "numeric",
            "definition": "data consists only of numeric entries.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Dataset/DatasetType/other": {
            "label": "other",
            "definition": "data is of a type not included in this list.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Dataset/DatasetType/sensor": {
            "label": "sensor",
            "definition": "data is recorded from a physical sensor, such as a thermometer reading or biometric device.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Dataset/DatasetType/structured": {
            "label": "structured",
            "definition": "data is stored in tabular format or retrieved from a relational database.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Dataset/DatasetType/syntactic": {
            "label": "syntactic",
            "definition": "data describes the syntax or semantics of a language or text, such as a parse tree used for natural language processing.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Dataset/DatasetType/text": {
            "label": "text",
            "definition": "data consists of unstructured text, such as a book, Wikipedia article (without images), or transcript.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Dataset/DatasetType/timeseries": {
            "label": "timeseries",
            "definition": "data is recorded in an ordered sequence of timestamped entries, such as the price of a stock over the course of a day.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Dataset/DatasetType/timestamp": {
            "label": "timestamp",
            "definition": "data is recorded with a timestamp for each entry, but not necessarily ordered or at specific intervals, such as when a taxi ride starts and ends.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Dataset/DatasetType/video": {
            "label": "video",
            "definition": "data is video based, such as a collection of movie clips featuring Tom Hanks.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/ConjunctiveLicenseSet": {
            "label": "ConjunctiveLicenseSet",
            "definition": "Portion of an AnyLicenseInfo representing a set of licensing information where all elements apply.",
            "broader": ("https://spdx.org/rdf/3.0.1/terms/SimpleLicensing/AnyLicenseInfo",),
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/CustomLicense": {
            "label": "CustomLicense",
            "definition": "A license that is not listed on the SPDX License List.",
            "broader": ("https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/License",),
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/CustomLicenseAddition": {
            "label": "CustomLicenseAddition",
            "definition": "A license addition that is not listed on the SPDX Exceptions List.",
            "broader": ("https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/LicenseAddition",),
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/DisjunctiveLicenseSet": {
            "label": "DisjunctiveLicenseSet",
            "definition": "Portion of an AnyLicenseInfo representing a set of licensing information where only one of the elements applies.",
            "broader": ("https://spdx.org/rdf/3.0.1/terms/SimpleLicensing/AnyLicenseInfo",),
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/ExtendableLicense": {
            "label": "ExtendableLicense",
            "definition": "Abstract class representing a License or an OrLaterOperator.",
            "broader": ("https://spdx.org/rdf/3.0.1/terms/SimpleLicensing/AnyLicenseInfo",),
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/IndividualLicensingInfo": {
            "label": "IndividualLicensingInfo",
            "definition": "A concrete subclass of AnyLicenseInfo used by Individuals in the ExpandedLicensing profile.",
            "broader": ("https://spdx.org/rdf/3.0.1/terms/SimpleLicensing/AnyLicenseInfo",),
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/License": {
            "label": "License",
            "definition": "Abstract class for the portion of an AnyLicenseInfo representing a license.",
            "broader": ("https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/ExtendableLicense",),
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/LicenseAddition": {
            "label": "LicenseAddition",
            "definition": "Abstract class for additional text intended to be added to a License, but which is not itself a standalone License.",
            "broader": ("https://spdx.org/rdf/3.0.1/terms/Core/Element",),
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/ListedLicense": {
            "label": "ListedLicense",
            "definition": "A license that is listed on the SPDX License List.",
            "broader": ("https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/License",),
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/ListedLicenseException": {
            "label": "ListedLicenseException",
            "definition": "A license exception that is listed on the SPDX Exceptions list.",
            "broader": ("https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/LicenseAddition",),
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/NoAssertionLicense": {
            "label": "NoAssertionLicense",
            "definition": "An Individual Value for License when no assertion can be made about its actual value.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/NoneLicense": {
            "label": "NoneLicense",
            "definition": "An Individual Value for License where the SPDX data creator determines that no license is present.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/OrLaterOperator": {
            "label": "OrLaterOperator",
            "definition": "Portion of an AnyLicenseInfo representing this version, or any later version, of the indicated License.",
            "broader": ("https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/ExtendableLicense",),
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/WithAdditionOperator": {
            "label": "WithAdditionOperator",
            "definition": "Portion of an AnyLicenseInfo representing a License which has additional text applied to it.",
            "broader": ("https://spdx.org/rdf/3.0.1/terms/SimpleLicensing/AnyLicenseInfo",),
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Extension/CdxPropertiesExtension": {
            "label": "CdxPropertiesExtension",
            "definition": "A type of extension consisting of a list of name value pairs.",
            "broader": ("https://spdx.org/rdf/3.0.1/terms/Extension/Extension",),
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Extension/CdxPropertyEntry": {
            "label": "CdxPropertyEntry",
            "definition": "A property name with an associated value.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Extension/Extension": {
            "label": "Extension",
            "definition": "A characterization of some aspect of an Element that is associated with the Element in a generalized fashion.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Security/CvssSeverityType": {
            "label": "CvssSeverityType",
            "definition": "Specifies the CVSS base, temporal, threat, or environmental severity type.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Security/CvssSeverityType/critical": {
            "label": "critical",
            "definition": "When a CVSS score is between 9.0 - 10.0",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Security/CvssSeverityType/high": {
            "label": "high",
            "definition": "When a CVSS score is between 7.0 - 8.9",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Security/CvssSeverityType/low": {
            "label": "low",
            "definition": "When a CVSS score is between 0.1 - 3.9",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Security/CvssSeverityType/medium": {
            "label": "medium",
            "definition": "When a CVSS score is between 4.0 - 6.9",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Security/CvssSeverityType/none": {
            "label": "none",
            "definition": "When a CVSS score is 0.0",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Security/CvssV2VulnAssessmentRelationship": {
            "label": "CvssV2VulnAssessmentRelationship",
            "definition": "Provides a CVSS version 2.0 assessment for a vulnerability.",
            "broader": ("https://spdx.org/rdf/3.0.1/terms/Security/VulnAssessmentRelationship",),
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Security/CvssV3VulnAssessmentRelationship": {
            "label": "CvssV3VulnAssessmentRelationship",
            "definition": "Provides a CVSS version 3 assessment for a vulnerability.",
            "broader": ("https://spdx.org/rdf/3.0.1/terms/Security/VulnAssessmentRelationship",),
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Security/CvssV4VulnAssessmentRelationship": {
            "label": "CvssV4VulnAssessmentRelationship",
            "definition": "Provides a CVSS version 4 assessment for a vulnerability.",
            "broader": ("https://spdx.org/rdf/3.0.1/terms/Security/VulnAssessmentRelationship",),
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Security/EpssVulnAssessmentRelationship": {
            "label": "EpssVulnAssessmentRelationship",
            "definition": "Provides an EPSS assessment for a vulnerability.",
            "broader": ("https://spdx.org/rdf/3.0.1/terms/Security/VulnAssessmentRelationship",),
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Security/ExploitCatalogType": {
            "label": "ExploitCatalogType",
            "definition": "Specifies the exploit catalog type.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Security/ExploitCatalogType/kev": {
            "label": "kev",
            "definition": "CISA's Known Exploited Vulnerability (KEV) Catalog",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Security/ExploitCatalogType/other": {
            "label": "other",
            "definition": "Other exploit catalogs",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Security/ExploitCatalogVulnAssessmentRelationship": {
            "label": "ExploitCatalogVulnAssessmentRelationship",
            "definition": "Provides an exploit assessment of a vulnerability.",
            "broader": ("https://spdx.org/rdf/3.0.1/terms/Security/VulnAssessmentRelationship",),
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Security/SsvcDecisionType": {
            "label": "SsvcDecisionType",
            "definition": "Specifies the SSVC decision type.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Security/SsvcDecisionType/act": {
            "label": "act",
            "definition": "The vulnerability requires attention from the organization's internal, supervisory-level and leadership-level individuals. Necessary actions include requesting assistance or information about the vulnerability, as well as publishing a notification either internally and/or externally. Typically, i...",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Security/SsvcDecisionType/attend": {
            "label": "attend",
            "definition": "The vulnerability requires attention from the organization's internal, supervisory-level individuals. Necessary actions include requesting assistance or information about the vulnerability, and may involve publishing a notification either internally and/or externally. CISA recommends remediating ...",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Security/SsvcDecisionType/track": {
            "label": "track",
            "definition": "The vulnerability does not require action at this time. The organization would continue to track the vulnerability and reassess it if new information becomes available. CISA recommends remediating Track vulnerabilities within standard update timelines.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Security/SsvcDecisionType/trackStar": {
            "label": "trackStar",
            "definition": '("Track\\*" in the SSVC spec) The vulnerability contains specific characteristics that may require closer monitoring for changes. CISA recommends remediating Track\\* vulnerabilities within standard update timelines.',
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Security/SsvcVulnAssessmentRelationship": {
            "label": "SsvcVulnAssessmentRelationship",
            "definition": "Provides an SSVC assessment for a vulnerability.",
            "broader": ("https://spdx.org/rdf/3.0.1/terms/Security/VulnAssessmentRelationship",),
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Security/VexAffectedVulnAssessmentRelationship": {
            "label": "VexAffectedVulnAssessmentRelationship",
            "definition": "Connects a vulnerability and an element designating the element as a product affected by the vulnerability.",
            "broader": ("https://spdx.org/rdf/3.0.1/terms/Security/VexVulnAssessmentRelationship",),
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Security/VexFixedVulnAssessmentRelationship": {
            "label": "VexFixedVulnAssessmentRelationship",
            "definition": "Links a vulnerability and elements representing products (in the VEX sense) where a fix has been applied and are no longer affected.",
            "broader": ("https://spdx.org/rdf/3.0.1/terms/Security/VexVulnAssessmentRelationship",),
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Security/VexJustificationType": {
            "label": "VexJustificationType",
            "definition": "Specifies the VEX justification type.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Security/VexJustificationType/componentNotPresent": {
            "label": "componentNotPresent",
            "definition": "The software is not affected because the vulnerable component is not in the product.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Security/VexJustificationType/inlineMitigationsAlreadyExist": {
            "label": "inlineMitigationsAlreadyExist",
            "definition": "Built-in inline controls or mitigations prevent an adversary from leveraging the vulnerability.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Security/VexJustificationType/vulnerableCodeCannotBeControlledByAdversary": {
            "label": "vulnerableCodeCannotBeControlledByAdversary",
            "definition": "The vulnerable component is present, and the component contains the vulnerable code. However, vulnerable code is used in such a way that an attacker cannot mount any anticipated attack.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Security/VexJustificationType/vulnerableCodeNotInExecutePath": {
            "label": "vulnerableCodeNotInExecutePath",
            "definition": "The affected code is not reachable through the execution of the code, including non-anticipated states of the product.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Security/VexJustificationType/vulnerableCodeNotPresent": {
            "label": "vulnerableCodeNotPresent",
            "definition": "The product is not affected because the code underlying the vulnerability is not present in the product.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Security/VexNotAffectedVulnAssessmentRelationship": {
            "label": "VexNotAffectedVulnAssessmentRelationship",
            "definition": "Links a vulnerability and one or more elements designating the latter as products not affected by the vulnerability.",
            "broader": ("https://spdx.org/rdf/3.0.1/terms/Security/VexVulnAssessmentRelationship",),
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Security/VexUnderInvestigationVulnAssessmentRelationship": {
            "label": "VexUnderInvestigationVulnAssessmentRelationship",
            "definition": "Designates elements as products where the impact of a vulnerability is being investigated.",
            "broader": ("https://spdx.org/rdf/3.0.1/terms/Security/VexVulnAssessmentRelationship",),
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Security/VexVulnAssessmentRelationship": {
            "label": "VexVulnAssessmentRelationship",
            "definition": "Abstract ancestor class for all VEX relationships",
            "broader": ("https://spdx.org/rdf/3.0.1/terms/Security/VulnAssessmentRelationship",),
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Security/VulnAssessmentRelationship": {
            "label": "VulnAssessmentRelationship",
            "definition": "Abstract ancestor class for all vulnerability assessments",
            "broader": ("https://spdx.org/rdf/3.0.1/terms/Core/Relationship",),
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Security/Vulnerability": {
            "label": "Vulnerability",
            "definition": "Specifies a vulnerability and its associated information.",
            "broader": ("https://spdx.org/rdf/3.0.1/terms/Core/Artifact",),
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/SimpleLicensing/AnyLicenseInfo": {
            "label": "AnyLicenseInfo",
            "definition": "Abstract class representing a license combination consisting of one or more licenses.",
            "broader": ("https://spdx.org/rdf/3.0.1/terms/Core/Element",),
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/SimpleLicensing/LicenseExpression": {
            "label": "LicenseExpression",
            "definition": "An SPDX Element containing an SPDX license expression string.",
            "broader": ("https://spdx.org/rdf/3.0.1/terms/SimpleLicensing/AnyLicenseInfo",),
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/SimpleLicensing/SimpleLicensingText": {
            "label": "SimpleLicensingText",
            "definition": "A license or addition that is not listed on the SPDX License List.",
            "broader": ("https://spdx.org/rdf/3.0.1/terms/Core/Element",),
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Software/ContentIdentifier": {
            "label": "ContentIdentifier",
            "definition": "A canonical, unique, immutable identifier",
            "broader": ("https://spdx.org/rdf/3.0.1/terms/Core/IntegrityMethod",),
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Software/ContentIdentifierType": {
            "label": "ContentIdentifierType",
            "definition": "Specifies the type of a content identifier.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Software/ContentIdentifierType/gitoid": {
            "label": "gitoid",
            "definition": "[Gitoid](https://www.iana.org/assignments/uri-schemes/prov/gitoid), stands for [Git Object ID](https://git-scm.com/book/en/v2/Git-Internals-Git-Objects). A gitoid of type blob is a unique hash of a binary artifact. A gitoid may represent either an [Artifact Identifier](https://github.com/omnibor/...",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Software/ContentIdentifierType/swhid": {
            "label": "swhid",
            "definition": "SoftWare Hash IDentifier, a persistent intrinsic identifier for digital artifacts, such as files, trees (also known as directories or folders), commits, and other objects typically found in version control systems. The format of the identifiers is defined in the [SWHID specification](https://www....",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Software/File": {
            "label": "File",
            "definition": "Refers to any object that stores content on a computer.",
            "broader": ("https://spdx.org/rdf/3.0.1/terms/Software/SoftwareArtifact",),
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Software/FileKindType": {
            "label": "FileKindType",
            "definition": "Enumeration of the different kinds of SPDX file.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Software/FileKindType/directory": {
            "label": "directory",
            "definition": "The file represents a directory and all content stored in that directory.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Software/FileKindType/file": {
            "label": "file",
            "definition": "The file represents a single file (default).",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Software/Package": {
            "label": "Package",
            "definition": "Refers to any unit of content that can be associated with a distribution of software.",
            "broader": ("https://spdx.org/rdf/3.0.1/terms/Software/SoftwareArtifact",),
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Software/Sbom": {
            "label": "Sbom",
            "definition": "A collection of SPDX Elements describing a single package.",
            "broader": ("https://spdx.org/rdf/3.0.1/terms/Core/Bom",),
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Software/SbomType": {
            "label": "SbomType",
            "definition": "Provides a set of values to be used to describe the common types of SBOMs that tools may create.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Software/SbomType/analyzed": {
            "label": "analyzed",
            "definition": 'SBOM generated through analysis of artifacts (e.g., executables, packages, containers, and virtual machine images) after its build. Such analysis generally requires a variety of heuristics. In some contexts, this may also be referred to as a "3rd party" SBOM.',
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Software/SbomType/build": {
            "label": "build",
            "definition": "SBOM generated as part of the process of building the software to create a releasable artifact (e.g., executable or package) from data such as source files, dependencies, built components, build process ephemeral data, and other SBOMs.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Software/SbomType/deployed": {
            "label": "deployed",
            "definition": "SBOM provides an inventory of software that is present on a system. This may be an assembly of other SBOMs that combines analysis of configuration options, and examination of execution behavior in a (potentially simulated) deployment environment.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Software/SbomType/design": {
            "label": "design",
            "definition": "SBOM of intended, planned software project or product with included components (some of which may not yet exist) for a new software artifact.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Software/SbomType/runtime": {
            "label": "runtime",
            "definition": 'SBOM generated through instrumenting the system running the software, to capture only components present in the system, as well as external call-outs or dynamically loaded components. In some contexts, this may also be referred to as an "Instrumented" or "Dynamic" SBOM.',
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Software/SbomType/source": {
            "label": "source",
            "definition": "SBOM created directly from the development environment, source files, and included dependencies used to build an product artifact.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Software/Snippet": {
            "label": "Snippet",
            "definition": "Describes a certain part of a file.",
            "broader": ("https://spdx.org/rdf/3.0.1/terms/Software/SoftwareArtifact",),
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Software/SoftwareArtifact": {
            "label": "SoftwareArtifact",
            "definition": "A distinct article or unit related to Software.",
            "broader": ("https://spdx.org/rdf/3.0.1/terms/Core/Artifact",),
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose": {
            "label": "SoftwarePurpose",
            "definition": "Provides information about the primary purpose of an Element.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/application": {
            "label": "application",
            "definition": "The Element is a software application.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/archive": {
            "label": "archive",
            "definition": "The Element is an archived collection of one or more files (.tar, .zip, etc.).",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/bom": {
            "label": "bom",
            "definition": "The Element is a bill of materials.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/configuration": {
            "label": "configuration",
            "definition": "The Element is configuration data.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/container": {
            "label": "container",
            "definition": "The Element is a container image which can be used by a container runtime application.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/data": {
            "label": "data",
            "definition": "The Element is data.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/device": {
            "label": "device",
            "definition": "The Element refers to a chipset, processor, or electronic board.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/deviceDriver": {
            "label": "deviceDriver",
            "definition": "The Element represents software that controls hardware devices.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/diskImage": {
            "label": "diskImage",
            "definition": "The Element refers to a disk image that can be written to a disk, booted in a VM, etc. A disk image typically contains most or all of the components necessary to boot, such as bootloaders, kernels, firmware, userspace, etc.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/documentation": {
            "label": "documentation",
            "definition": "The Element is documentation.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/evidence": {
            "label": "evidence",
            "definition": "The Element is the evidence that a specification or requirement has been fulfilled.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/executable": {
            "label": "executable",
            "definition": "The Element is an Artifact that can be run on a computer.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/file": {
            "label": "file",
            "definition": "The Element is a single file which can be independently distributed (configuration file, statically linked binary, Kubernetes deployment, etc.).",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/filesystemImage": {
            "label": "filesystemImage",
            "definition": "The Element is a file system image that can be written to a disk (or virtual) partition.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/firmware": {
            "label": "firmware",
            "definition": "The Element provides low level control over a device's hardware.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/framework": {
            "label": "framework",
            "definition": "The Element is a software framework.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/install": {
            "label": "install",
            "definition": "The Element is used to install software on disk.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/library": {
            "label": "library",
            "definition": "The Element is a software library.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/manifest": {
            "label": "manifest",
            "definition": "The Element is a software manifest.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/model": {
            "label": "model",
            "definition": "The Element is a machine learning or artificial intelligence model.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/module": {
            "label": "module",
            "definition": "The Element is a module of a piece of software.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/operatingSystem": {
            "label": "operatingSystem",
            "definition": "The Element is an operating system.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/other": {
            "label": "other",
            "definition": "The Element doesn't fit into any of the other categories.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/patch": {
            "label": "patch",
            "definition": "The Element contains a set of changes to update, fix, or improve another Element.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/platform": {
            "label": "platform",
            "definition": "The Element represents a runtime environment.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/requirement": {
            "label": "requirement",
            "definition": "The Element provides a requirement needed as input for another Element.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/source": {
            "label": "source",
            "definition": "The Element is a single or a collection of source files.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/specification": {
            "label": "specification",
            "definition": "The Element is a plan, guideline or strategy how to create, perform or analyze an application.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/test": {
            "label": "test",
            "definition": "The Element is a test used to verify functionality on an software element.",
            "source_vocab": "SPDX-3.0.1",
        },
    }
)

__all__ = [
    "AIPackage",
    "Agent",
    "Annotation",
    "AnnotationType",
    "AnyLicenseInfo",
    "Artifact",
    "Bom",
    "Build",
    "Bundle",
    "CdxPropertiesExtension",
    "CdxPropertyEntry",
    "ConfidentialityLevel",
    "ConfidentialityLevelType",
    "ConjunctiveLicenseSet",
    "ContentIdentifier",
    "ContentIdentifierType",
    "CreationInfo",
    "CustomLicense",
    "CustomLicenseAddition",
    "CvssSeverityType",
    "CvssV2VulnAssessmentRelationship",
    "CvssV3VulnAssessmentRelationship",
    "CvssV4VulnAssessmentRelationship",
    "DatasetAvailabilityType",
    "DatasetPackage",
    "DatasetType",
    "DatasetType",
    "DictionaryEntry",
    "DisjunctiveLicenseSet",
    "Element",
    "ElementCollection",
    "EnergyConsumption",
    "EnergyConsumptionDescription",
    "EnergyUnitType",
    "EpssVulnAssessmentRelationship",
    "ExploitCatalogType",
    "ExploitCatalogVulnAssessmentRelationship",
    "ExtendableLicense",
    "Extension",
    "ExternalIdentifier",
    "ExternalIdentifierType",
    "ExternalMap",
    "ExternalRef",
    "ExternalRefType",
    "File",
    "FileKindType",
    "Hash",
    "HashAlgorithm",
    "IndividualElement",
    "IndividualLicensingInfo",
    "IntegrityMethod",
    "License",
    "LicenseAddition",
    "LicenseExpression",
    "LifecycleScopeType",
    "LifecycleScopedRelationship",
    "ListedLicense",
    "ListedLicenseException",
    "NamespaceMap",
    "NoAssertionElement",
    "NoAssertionLicense",
    "NoneElement",
    "NoneLicense",
    "OrLaterOperator",
    "Organization",
    "Package",
    "PackageVerificationCode",
    "Person",
    "PositiveIntegerRange",
    "PresenceType",
    "ProfileIdentifierType",
    "Relationship",
    "RelationshipCompleteness",
    "RelationshipType",
    "SafetyRiskAssessmentType",
    "Sbom",
    "SbomType",
    "SimpleLicensingText",
    "Snippet",
    "SoftwareAgent",
    "SoftwareArtifact",
    "SoftwarePurpose",
    "SpdxDocument",
    "SpdxOrganization",
    "SsvcDecisionType",
    "SsvcVulnAssessmentRelationship",
    "SupportType",
    "Tool",
    "VexAffectedVulnAssessmentRelationship",
    "VexFixedVulnAssessmentRelationship",
    "VexJustificationType",
    "VexNotAffectedVulnAssessmentRelationship",
    "VexUnderInvestigationVulnAssessmentRelationship",
    "VexVulnAssessmentRelationship",
    "VulnAssessmentRelationship",
    "Vulnerability",
    "WithAdditionOperator",
    "act",
    "adler32",
    "affects",
    "ai",
    "altDownloadLocation",
    "altWebPage",
    "amber",
    "amendedBy",
    "analyzed",
    "ancestorOf",
    "application",
    "archive",
    "attend",
    "audio",
    "availableFrom",
    "binaryArtifact",
    "blake2b256",
    "blake2b384",
    "blake2b512",
    "blake3",
    "bom",
    "bower",
    "build",
    "buildMeta",
    "buildSystem",
    "build_1",
    "build_2",
    "categorical",
    "certificationReport",
    "chat",
    "clear",
    "clickthrough",
    "complete",
    "componentAnalysisReport",
    "componentNotPresent",
    "configuration",
    "configures",
    "container",
    "contains",
    "coordinatedBy",
    "copiedTo",
    "core",
    "cpe22",
    "cpe23",
    "critical",
    "crystalsDilithium",
    "crystalsKyber",
    "cve",
    "cwe",
    "data",
    "dataset",
    "delegatedTo",
    "dependsOn",
    "deployed",
    "deployed_1",
    "descendantOf",
    "describes",
    "design",
    "design_1",
    "development",
    "development_1",
    "device",
    "deviceDriver",
    "directDownload",
    "directory",
    "diskImage",
    "documentation",
    "documentation_1",
    "doesNotAffect",
    "dynamicAnalysisReport",
    "email",
    "endOfSupport",
    "eolNotice",
    "evidence",
    "executable",
    "expandedLicensing",
    "expandsTo",
    "exploitCreatedBy",
    "exportControlAssessment",
    "extension",
    "falcon",
    "file",
    "file_1",
    "filesystemImage",
    "firmware",
    "fixedBy",
    "fixedIn",
    "foundBy",
    "framework",
    "funding",
    "generates",
    "gitoid",
    "gitoid_1",
    "graph",
    "green",
    "hasAddedFile",
    "hasAssessmentFor",
    "hasAssociatedVulnerability",
    "hasConcludedLicense",
    "hasDataFile",
    "hasDeclaredLicense",
    "hasDeletedFile",
    "hasDependencyManifest",
    "hasDistributionArtifact",
    "hasDocumentation",
    "hasDynamicLink",
    "hasEvidence",
    "hasExample",
    "hasHost",
    "hasInput",
    "hasMetadata",
    "hasOptionalComponent",
    "hasOptionalDependency",
    "hasOutput",
    "hasPrerequisite",
    "hasProvidedDependency",
    "hasRequirement",
    "hasSpecification",
    "hasStaticLink",
    "hasTest",
    "hasTestCase",
    "hasVariant",
    "high",
    "high_1",
    "image",
    "incomplete",
    "inlineMitigationsAlreadyExist",
    "install",
    "invokedBy",
    "issueTracker",
    "kev",
    "kilowattHour",
    "library",
    "license",
    "limitedSupport",
    "lite",
    "low",
    "low_1",
    "mailingList",
    "manifest",
    "mavenCentral",
    "md2",
    "md4",
    "md5",
    "md6",
    "medium",
    "medium_1",
    "megajoule",
    "metrics",
    "model",
    "modifiedBy",
    "module",
    "no",
    "noAssertion",
    "noAssertion_1",
    "noAssertion_2",
    "noAssertion_3",
    "noSupport",
    "none",
    "npm",
    "nuget",
    "numeric",
    "operatingSystem",
    "other",
    "other_1",
    "other_2",
    "other_3",
    "other_4",
    "other_5",
    "other_6",
    "other_7",
    "other_8",
    "other_9",
    "packageUrl",
    "packagedBy",
    "patch",
    "patchedBy",
    "platform",
    "privacyAssessment",
    "productMetadata",
    "publishedBy",
    "purchaseOrder",
    "qualityAssessmentReport",
    "query",
    "red",
    "registration",
    "releaseHistory",
    "releaseNotes",
    "reportedBy",
    "republishedBy",
    "requirement",
    "review",
    "riskAssessment",
    "runtime",
    "runtimeAnalysisReport",
    "runtime_1",
    "scrapingScript",
    "secureSoftwareAttestation",
    "security",
    "securityAdversaryModel",
    "securityAdvisory",
    "securityFix",
    "securityOther",
    "securityOther_1",
    "securityPenTestReport",
    "securityPolicy",
    "securityThreatModel",
    "sensor",
    "serializedInArtifact",
    "serious",
    "sha1",
    "sha3_224",
    "sha3_256",
    "sha3_384",
    "sha3_512",
    "sha224",
    "sha256",
    "sha384",
    "sha512",
    "simpleLicensing",
    "socialMedia",
    "software",
    "source",
    "sourceArtifact",
    "source_1",
    "specification",
    "staticAnalysisReport",
    "structured",
    "support",
    "support_1",
    "swhid",
    "swhid_1",
    "swid",
    "syntactic",
    "test",
    "test_1",
    "testedOn",
    "text",
    "timeseries",
    "timestamp",
    "track",
    "trackStar",
    "trainedOn",
    "underInvestigationFor",
    "urlScheme",
    "usesTool",
    "vcs",
    "video",
    "vulnerabilityDisclosureReport",
    "vulnerabilityExploitabilityAssessment",
    "vulnerableCodeCannotBeControlledByAdversary",
    "vulnerableCodeNotInExecutePath",
    "vulnerableCodeNotPresent",
    "yes",
]
