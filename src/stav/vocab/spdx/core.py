# SPDX-FileCopyrightText: 2026-present Arthit Suriyawongkul
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0
#
# AUTO-GENERATED — do not edit manually.
# Source: SPDX 3.0.1 Core profile
# Generated: 2026-04-30T08:53:34Z
# Regenerate: python -m stav.codegen.generate tools/recipes/spdx_core.json

"""Vocabulary from SPDX 3.0.1 Core profile.

84 term constants (accessible as ``module.TermName``); grouped enums: :class:`AnnotationType`, :class:`ExternalIdentifierType`, :class:`ExternalRefType`, :class:`HashAlgorithm`, :class:`LifecycleScopeType`, :class:`PresenceType`, :class:`ProfileIdentifierType`, :class:`RelationshipCompleteness`, :class:`RelationshipType`, :class:`SupportType`."""

from __future__ import annotations

from stav._registry import _register
from stav.term import _StavVocabEnum

__stav_namespace__ = "vocab.spdx.core"

# ── Individual term constants ─────────────────────────────────────────────────────
# Plain string IRIs — use directly with MLflow, Pitloom, SBOM serialisers.
# Metadata (label, definition, broader) via: stav.label(NaturalPerson) etc.
Agent = 'https://spdx.org/rdf/3.0.1/terms/Core/Agent'
algorithm = 'https://spdx.org/rdf/3.0.1/terms/Core/algorithm'
Annotation = 'https://spdx.org/rdf/3.0.1/terms/Core/Annotation'
annotationType = 'https://spdx.org/rdf/3.0.1/terms/Core/annotationType'
Artifact = 'https://spdx.org/rdf/3.0.1/terms/Core/Artifact'
beginIntegerRange = 'https://spdx.org/rdf/3.0.1/terms/Core/beginIntegerRange'
Bom = 'https://spdx.org/rdf/3.0.1/terms/Core/Bom'
builtTime = 'https://spdx.org/rdf/3.0.1/terms/Core/builtTime'
Bundle = 'https://spdx.org/rdf/3.0.1/terms/Core/Bundle'
comment = 'https://spdx.org/rdf/3.0.1/terms/Core/comment'
completeness = 'https://spdx.org/rdf/3.0.1/terms/Core/completeness'
contentType = 'https://spdx.org/rdf/3.0.1/terms/Core/contentType'
context = 'https://spdx.org/rdf/3.0.1/terms/Core/context'
created = 'https://spdx.org/rdf/3.0.1/terms/Core/created'
createdBy = 'https://spdx.org/rdf/3.0.1/terms/Core/createdBy'
createdUsing = 'https://spdx.org/rdf/3.0.1/terms/Core/createdUsing'
CreationInfo = 'https://spdx.org/rdf/3.0.1/terms/Core/CreationInfo'
creationInfo = 'https://spdx.org/rdf/3.0.1/terms/Core/creationInfo'
dataLicense = 'https://spdx.org/rdf/3.0.1/terms/Core/dataLicense'
definingArtifact = 'https://spdx.org/rdf/3.0.1/terms/Core/definingArtifact'
description = 'https://spdx.org/rdf/3.0.1/terms/Core/description'
DictionaryEntry = 'https://spdx.org/rdf/3.0.1/terms/Core/DictionaryEntry'
Element = 'https://spdx.org/rdf/3.0.1/terms/Core/Element'
element = 'https://spdx.org/rdf/3.0.1/terms/Core/element'
ElementCollection = 'https://spdx.org/rdf/3.0.1/terms/Core/ElementCollection'
endIntegerRange = 'https://spdx.org/rdf/3.0.1/terms/Core/endIntegerRange'
endTime = 'https://spdx.org/rdf/3.0.1/terms/Core/endTime'
extension = 'https://spdx.org/rdf/3.0.1/terms/Core/extension'
ExternalIdentifier = 'https://spdx.org/rdf/3.0.1/terms/Core/ExternalIdentifier'
externalIdentifier = 'https://spdx.org/rdf/3.0.1/terms/Core/externalIdentifier'
externalIdentifierType = 'https://spdx.org/rdf/3.0.1/terms/Core/externalIdentifierType'
ExternalMap = 'https://spdx.org/rdf/3.0.1/terms/Core/ExternalMap'
ExternalRef = 'https://spdx.org/rdf/3.0.1/terms/Core/ExternalRef'
externalRef = 'https://spdx.org/rdf/3.0.1/terms/Core/externalRef'
externalRefType = 'https://spdx.org/rdf/3.0.1/terms/Core/externalRefType'
externalSpdxId = 'https://spdx.org/rdf/3.0.1/terms/Core/externalSpdxId'
from_ = 'https://spdx.org/rdf/3.0.1/terms/Core/from'
Hash = 'https://spdx.org/rdf/3.0.1/terms/Core/Hash'
hashValue = 'https://spdx.org/rdf/3.0.1/terms/Core/hashValue'
identifier = 'https://spdx.org/rdf/3.0.1/terms/Core/identifier'
identifierLocator = 'https://spdx.org/rdf/3.0.1/terms/Core/identifierLocator'
import_ = 'https://spdx.org/rdf/3.0.1/terms/Core/import'
IndividualElement = 'https://spdx.org/rdf/3.0.1/terms/Core/IndividualElement'
IntegrityMethod = 'https://spdx.org/rdf/3.0.1/terms/Core/IntegrityMethod'
issuingAuthority = 'https://spdx.org/rdf/3.0.1/terms/Core/issuingAuthority'
key = 'https://spdx.org/rdf/3.0.1/terms/Core/key'
LifecycleScopedRelationship = 'https://spdx.org/rdf/3.0.1/terms/Core/LifecycleScopedRelationship'
locationHint = 'https://spdx.org/rdf/3.0.1/terms/Core/locationHint'
locator = 'https://spdx.org/rdf/3.0.1/terms/Core/locator'
name = 'https://spdx.org/rdf/3.0.1/terms/Core/name'
namespace = 'https://spdx.org/rdf/3.0.1/terms/Core/namespace'
namespaceMap = 'https://spdx.org/rdf/3.0.1/terms/Core/namespaceMap'
NamespaceMap = 'https://spdx.org/rdf/3.0.1/terms/Core/NamespaceMap'
NoAssertionElement = 'https://spdx.org/rdf/3.0.1/terms/Core/NoAssertionElement'
NoneElement = 'https://spdx.org/rdf/3.0.1/terms/Core/NoneElement'
Organization = 'https://spdx.org/rdf/3.0.1/terms/Core/Organization'
originatedBy = 'https://spdx.org/rdf/3.0.1/terms/Core/originatedBy'
PackageVerificationCode = 'https://spdx.org/rdf/3.0.1/terms/Core/PackageVerificationCode'
packageVerificationCodeExcludedFile = 'https://spdx.org/rdf/3.0.1/terms/Core/packageVerificationCodeExcludedFile'
Person = 'https://spdx.org/rdf/3.0.1/terms/Core/Person'
PositiveIntegerRange = 'https://spdx.org/rdf/3.0.1/terms/Core/PositiveIntegerRange'
prefix = 'https://spdx.org/rdf/3.0.1/terms/Core/prefix'
profileConformance = 'https://spdx.org/rdf/3.0.1/terms/Core/profileConformance'
Relationship = 'https://spdx.org/rdf/3.0.1/terms/Core/Relationship'
relationshipType = 'https://spdx.org/rdf/3.0.1/terms/Core/relationshipType'
releaseTime = 'https://spdx.org/rdf/3.0.1/terms/Core/releaseTime'
rootElement = 'https://spdx.org/rdf/3.0.1/terms/Core/rootElement'
scope = 'https://spdx.org/rdf/3.0.1/terms/Core/scope'
SoftwareAgent = 'https://spdx.org/rdf/3.0.1/terms/Core/SoftwareAgent'
SpdxDocument = 'https://spdx.org/rdf/3.0.1/terms/Core/SpdxDocument'
SpdxOrganization = 'https://spdx.org/rdf/3.0.1/terms/Core/SpdxOrganization'
specVersion = 'https://spdx.org/rdf/3.0.1/terms/Core/specVersion'
standardName = 'https://spdx.org/rdf/3.0.1/terms/Core/standardName'
startTime = 'https://spdx.org/rdf/3.0.1/terms/Core/startTime'
statement = 'https://spdx.org/rdf/3.0.1/terms/Core/statement'
subject = 'https://spdx.org/rdf/3.0.1/terms/Core/subject'
summary = 'https://spdx.org/rdf/3.0.1/terms/Core/summary'
suppliedBy = 'https://spdx.org/rdf/3.0.1/terms/Core/suppliedBy'
supportLevel = 'https://spdx.org/rdf/3.0.1/terms/Core/supportLevel'
to = 'https://spdx.org/rdf/3.0.1/terms/Core/to'
Tool = 'https://spdx.org/rdf/3.0.1/terms/Core/Tool'
validUntilTime = 'https://spdx.org/rdf/3.0.1/terms/Core/validUntilTime'
value = 'https://spdx.org/rdf/3.0.1/terms/Core/value'
verifiedUsing = 'https://spdx.org/rdf/3.0.1/terms/Core/verifiedUsing'

class AnnotationType(_StavVocabEnum):
    """Annotation types from SPDX 3.0.1 Core profile."""
    other = 'https://spdx.org/rdf/3.0.1/terms/Core/AnnotationType/other'
    review = 'https://spdx.org/rdf/3.0.1/terms/Core/AnnotationType/review'

class ExternalIdentifierType(_StavVocabEnum):
    """External identifier types from SPDX 3.0.1 Core profile."""
    cpe22 = 'https://spdx.org/rdf/3.0.1/terms/Core/ExternalIdentifierType/cpe22'
    cpe23 = 'https://spdx.org/rdf/3.0.1/terms/Core/ExternalIdentifierType/cpe23'
    cve = 'https://spdx.org/rdf/3.0.1/terms/Core/ExternalIdentifierType/cve'
    email = 'https://spdx.org/rdf/3.0.1/terms/Core/ExternalIdentifierType/email'
    gitoid = 'https://spdx.org/rdf/3.0.1/terms/Core/ExternalIdentifierType/gitoid'
    other = 'https://spdx.org/rdf/3.0.1/terms/Core/ExternalIdentifierType/other'
    packageUrl = 'https://spdx.org/rdf/3.0.1/terms/Core/ExternalIdentifierType/packageUrl'
    securityOther = 'https://spdx.org/rdf/3.0.1/terms/Core/ExternalIdentifierType/securityOther'
    swhid = 'https://spdx.org/rdf/3.0.1/terms/Core/ExternalIdentifierType/swhid'
    swid = 'https://spdx.org/rdf/3.0.1/terms/Core/ExternalIdentifierType/swid'
    urlScheme = 'https://spdx.org/rdf/3.0.1/terms/Core/ExternalIdentifierType/urlScheme'

class ExternalRefType(_StavVocabEnum):
    """External reference types from SPDX 3.0.1 Core profile."""
    altDownloadLocation = 'https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/altDownloadLocation'
    altWebPage = 'https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/altWebPage'
    binaryArtifact = 'https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/binaryArtifact'
    bower = 'https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/bower'
    buildMeta = 'https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/buildMeta'
    buildSystem = 'https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/buildSystem'
    certificationReport = 'https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/certificationReport'
    chat = 'https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/chat'
    componentAnalysisReport = 'https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/componentAnalysisReport'
    cwe = 'https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/cwe'
    documentation = 'https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/documentation'
    dynamicAnalysisReport = 'https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/dynamicAnalysisReport'
    eolNotice = 'https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/eolNotice'
    exportControlAssessment = 'https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/exportControlAssessment'
    funding = 'https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/funding'
    issueTracker = 'https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/issueTracker'
    license = 'https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/license'
    mailingList = 'https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/mailingList'
    mavenCentral = 'https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/mavenCentral'
    metrics = 'https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/metrics'
    npm = 'https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/npm'
    nuget = 'https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/nuget'
    other = 'https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/other'
    privacyAssessment = 'https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/privacyAssessment'
    productMetadata = 'https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/productMetadata'
    purchaseOrder = 'https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/purchaseOrder'
    qualityAssessmentReport = 'https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/qualityAssessmentReport'
    releaseHistory = 'https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/releaseHistory'
    releaseNotes = 'https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/releaseNotes'
    riskAssessment = 'https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/riskAssessment'
    runtimeAnalysisReport = 'https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/runtimeAnalysisReport'
    secureSoftwareAttestation = 'https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/secureSoftwareAttestation'
    securityAdversaryModel = 'https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/securityAdversaryModel'
    securityAdvisory = 'https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/securityAdvisory'
    securityFix = 'https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/securityFix'
    securityOther = 'https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/securityOther'
    securityPenTestReport = 'https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/securityPenTestReport'
    securityPolicy = 'https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/securityPolicy'
    securityThreatModel = 'https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/securityThreatModel'
    socialMedia = 'https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/socialMedia'
    sourceArtifact = 'https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/sourceArtifact'
    staticAnalysisReport = 'https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/staticAnalysisReport'
    support = 'https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/support'
    vcs = 'https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/vcs'
    vulnerabilityDisclosureReport = 'https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/vulnerabilityDisclosureReport'
    vulnerabilityExploitabilityAssessment = 'https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/vulnerabilityExploitabilityAssessment'

class HashAlgorithm(_StavVocabEnum):
    """Hash / digest algorithm identifiers from SPDX 3.0.1 Core profile."""
    adler32 = 'https://spdx.org/rdf/3.0.1/terms/Core/HashAlgorithm/adler32'
    blake2b256 = 'https://spdx.org/rdf/3.0.1/terms/Core/HashAlgorithm/blake2b256'
    blake2b384 = 'https://spdx.org/rdf/3.0.1/terms/Core/HashAlgorithm/blake2b384'
    blake2b512 = 'https://spdx.org/rdf/3.0.1/terms/Core/HashAlgorithm/blake2b512'
    blake3 = 'https://spdx.org/rdf/3.0.1/terms/Core/HashAlgorithm/blake3'
    crystalsDilithium = 'https://spdx.org/rdf/3.0.1/terms/Core/HashAlgorithm/crystalsDilithium'
    crystalsKyber = 'https://spdx.org/rdf/3.0.1/terms/Core/HashAlgorithm/crystalsKyber'
    falcon = 'https://spdx.org/rdf/3.0.1/terms/Core/HashAlgorithm/falcon'
    md2 = 'https://spdx.org/rdf/3.0.1/terms/Core/HashAlgorithm/md2'
    md4 = 'https://spdx.org/rdf/3.0.1/terms/Core/HashAlgorithm/md4'
    md5 = 'https://spdx.org/rdf/3.0.1/terms/Core/HashAlgorithm/md5'
    md6 = 'https://spdx.org/rdf/3.0.1/terms/Core/HashAlgorithm/md6'
    other = 'https://spdx.org/rdf/3.0.1/terms/Core/HashAlgorithm/other'
    sha1 = 'https://spdx.org/rdf/3.0.1/terms/Core/HashAlgorithm/sha1'
    sha224 = 'https://spdx.org/rdf/3.0.1/terms/Core/HashAlgorithm/sha224'
    sha256 = 'https://spdx.org/rdf/3.0.1/terms/Core/HashAlgorithm/sha256'
    sha384 = 'https://spdx.org/rdf/3.0.1/terms/Core/HashAlgorithm/sha384'
    sha3_224 = 'https://spdx.org/rdf/3.0.1/terms/Core/HashAlgorithm/sha3_224'
    sha3_256 = 'https://spdx.org/rdf/3.0.1/terms/Core/HashAlgorithm/sha3_256'
    sha3_384 = 'https://spdx.org/rdf/3.0.1/terms/Core/HashAlgorithm/sha3_384'
    sha3_512 = 'https://spdx.org/rdf/3.0.1/terms/Core/HashAlgorithm/sha3_512'
    sha512 = 'https://spdx.org/rdf/3.0.1/terms/Core/HashAlgorithm/sha512'

class LifecycleScopeType(_StavVocabEnum):
    """Lifecycle scope types from SPDX 3.0.1 Core profile."""
    build = 'https://spdx.org/rdf/3.0.1/terms/Core/LifecycleScopeType/build'
    design = 'https://spdx.org/rdf/3.0.1/terms/Core/LifecycleScopeType/design'
    development = 'https://spdx.org/rdf/3.0.1/terms/Core/LifecycleScopeType/development'
    other = 'https://spdx.org/rdf/3.0.1/terms/Core/LifecycleScopeType/other'
    runtime = 'https://spdx.org/rdf/3.0.1/terms/Core/LifecycleScopeType/runtime'
    test = 'https://spdx.org/rdf/3.0.1/terms/Core/LifecycleScopeType/test'

class PresenceType(_StavVocabEnum):
    """Presence / assertion types (yes / no / noAssertion) from SPDX 3.0.1 Core profile."""
    no = 'https://spdx.org/rdf/3.0.1/terms/Core/PresenceType/no'
    noAssertion = 'https://spdx.org/rdf/3.0.1/terms/Core/PresenceType/noAssertion'
    yes = 'https://spdx.org/rdf/3.0.1/terms/Core/PresenceType/yes'

class ProfileIdentifierType(_StavVocabEnum):
    """SPDX profile identifiers from SPDX 3.0.1 Core profile."""
    ai = 'https://spdx.org/rdf/3.0.1/terms/Core/ProfileIdentifierType/ai'
    build = 'https://spdx.org/rdf/3.0.1/terms/Core/ProfileIdentifierType/build'
    core = 'https://spdx.org/rdf/3.0.1/terms/Core/ProfileIdentifierType/core'
    dataset = 'https://spdx.org/rdf/3.0.1/terms/Core/ProfileIdentifierType/dataset'
    expandedLicensing = 'https://spdx.org/rdf/3.0.1/terms/Core/ProfileIdentifierType/expandedLicensing'
    extension = 'https://spdx.org/rdf/3.0.1/terms/Core/ProfileIdentifierType/extension'
    lite = 'https://spdx.org/rdf/3.0.1/terms/Core/ProfileIdentifierType/lite'
    security = 'https://spdx.org/rdf/3.0.1/terms/Core/ProfileIdentifierType/security'
    simpleLicensing = 'https://spdx.org/rdf/3.0.1/terms/Core/ProfileIdentifierType/simpleLicensing'
    software = 'https://spdx.org/rdf/3.0.1/terms/Core/ProfileIdentifierType/software'

class RelationshipCompleteness(_StavVocabEnum):
    """Relationship completeness values from SPDX 3.0.1 Core profile."""
    complete = 'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipCompleteness/complete'
    incomplete = 'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipCompleteness/incomplete'
    noAssertion = 'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipCompleteness/noAssertion'

class RelationshipType(_StavVocabEnum):
    """Relationship types between SPDX elements from SPDX 3.0.1 Core profile."""
    affects = 'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/affects'
    amendedBy = 'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/amendedBy'
    ancestorOf = 'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/ancestorOf'
    availableFrom = 'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/availableFrom'
    configures = 'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/configures'
    contains = 'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/contains'
    coordinatedBy = 'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/coordinatedBy'
    copiedTo = 'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/copiedTo'
    delegatedTo = 'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/delegatedTo'
    dependsOn = 'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/dependsOn'
    descendantOf = 'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/descendantOf'
    describes = 'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/describes'
    doesNotAffect = 'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/doesNotAffect'
    expandsTo = 'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/expandsTo'
    exploitCreatedBy = 'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/exploitCreatedBy'
    fixedBy = 'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/fixedBy'
    fixedIn = 'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/fixedIn'
    foundBy = 'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/foundBy'
    generates = 'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/generates'
    hasAddedFile = 'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/hasAddedFile'
    hasAssessmentFor = 'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/hasAssessmentFor'
    hasAssociatedVulnerability = 'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/hasAssociatedVulnerability'
    hasConcludedLicense = 'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/hasConcludedLicense'
    hasDataFile = 'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/hasDataFile'
    hasDeclaredLicense = 'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/hasDeclaredLicense'
    hasDeletedFile = 'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/hasDeletedFile'
    hasDependencyManifest = 'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/hasDependencyManifest'
    hasDistributionArtifact = 'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/hasDistributionArtifact'
    hasDocumentation = 'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/hasDocumentation'
    hasDynamicLink = 'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/hasDynamicLink'
    hasEvidence = 'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/hasEvidence'
    hasExample = 'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/hasExample'
    hasHost = 'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/hasHost'
    hasInput = 'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/hasInput'
    hasMetadata = 'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/hasMetadata'
    hasOptionalComponent = 'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/hasOptionalComponent'
    hasOptionalDependency = 'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/hasOptionalDependency'
    hasOutput = 'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/hasOutput'
    hasPrerequisite = 'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/hasPrerequisite'
    hasProvidedDependency = 'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/hasProvidedDependency'
    hasRequirement = 'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/hasRequirement'
    hasSpecification = 'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/hasSpecification'
    hasStaticLink = 'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/hasStaticLink'
    hasTest = 'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/hasTest'
    hasTestCase = 'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/hasTestCase'
    hasVariant = 'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/hasVariant'
    invokedBy = 'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/invokedBy'
    modifiedBy = 'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/modifiedBy'
    other = 'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/other'
    packagedBy = 'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/packagedBy'
    patchedBy = 'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/patchedBy'
    publishedBy = 'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/publishedBy'
    reportedBy = 'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/reportedBy'
    republishedBy = 'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/republishedBy'
    serializedInArtifact = 'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/serializedInArtifact'
    testedOn = 'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/testedOn'
    trainedOn = 'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/trainedOn'
    underInvestigationFor = 'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/underInvestigationFor'
    usesTool = 'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/usesTool'

class SupportType(_StavVocabEnum):
    """Support level types from SPDX 3.0.1 Core profile."""
    deployed = 'https://spdx.org/rdf/3.0.1/terms/Core/SupportType/deployed'
    development = 'https://spdx.org/rdf/3.0.1/terms/Core/SupportType/development'
    endOfSupport = 'https://spdx.org/rdf/3.0.1/terms/Core/SupportType/endOfSupport'
    limitedSupport = 'https://spdx.org/rdf/3.0.1/terms/Core/SupportType/limitedSupport'
    noAssertion = 'https://spdx.org/rdf/3.0.1/terms/Core/SupportType/noAssertion'
    noSupport = 'https://spdx.org/rdf/3.0.1/terms/Core/SupportType/noSupport'
    support = 'https://spdx.org/rdf/3.0.1/terms/Core/SupportType/support'

# ── Metadata registry ──────────────────────────────────────────────────────────────
# Populated at import time so stav.label() / .definition() / .broader() work.
_register({
    'https://spdx.org/rdf/3.0.1/terms/Core/Agent': {"label": 'Agent', "definition": 'Agent represents anything with the potential to act on a system.', "broader": ('https://spdx.org/rdf/3.0.1/terms/Core/Element',), "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/Annotation': {"label": 'Annotation', "definition": 'An assertion made in relation to one or more elements.', "broader": ('https://spdx.org/rdf/3.0.1/terms/Core/Element',), "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/AnnotationType/other': {"label": 'other', "definition": 'Used to store extra information about an Element which is not part of a review (e.g. extra information provided during the creation of the Element).', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/AnnotationType/review': {"label": 'review', "definition": 'Used when someone reviews the Element.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/Artifact': {"label": 'Artifact', "definition": 'A distinct article or unit within the digital domain.', "broader": ('https://spdx.org/rdf/3.0.1/terms/Core/Element',), "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/Bom': {"label": 'Bom', "definition": 'A container for a grouping of SPDX-3.0 content characterizing details (provenence, composition, licensing, etc.) about a product.', "broader": ('https://spdx.org/rdf/3.0.1/terms/Core/Bundle',), "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/Bundle': {"label": 'Bundle', "definition": 'A collection of Elements that have a shared context.', "broader": ('https://spdx.org/rdf/3.0.1/terms/Core/ElementCollection',), "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/CreationInfo': {"label": 'CreationInfo', "definition": 'Provides information about the creation of the Element.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/DictionaryEntry': {"label": 'DictionaryEntry', "definition": 'A key with an associated value.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/Element': {"label": 'Element', "definition": 'Base domain class from which all other SPDX-3.0 domain classes derive.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/ElementCollection': {"label": 'ElementCollection', "definition": 'A collection of Elements, not necessarily with unifying context.', "broader": ('https://spdx.org/rdf/3.0.1/terms/Core/Element',), "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/ExternalIdentifier': {"label": 'ExternalIdentifier', "definition": 'A reference to a resource identifier defined outside the scope of SPDX-3.0 content that uniquely identifies an Element.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/ExternalIdentifierType/cpe22': {"label": 'cpe22', "definition": '[Common Platform Enumeration Specification 2.2](https://cpe.mitre.org/files/cpe-specification_2.2.pdf)', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/ExternalIdentifierType/cpe23': {"label": 'cpe23', "definition": '[Common Platform Enumeration: Naming Specification Version 2.3](https://csrc.nist.gov/publications/detail/nistir/7695/final)', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/ExternalIdentifierType/cve': {"label": 'cve', "definition": 'Common Vulnerabilities and Exposures identifiers, an identifier for a specific software flaw defined within the official CVE Dictionary and that conforms to the [CVE specification](https://csrc.nist.gov/glossary/term/cve_id).', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/ExternalIdentifierType/email': {"label": 'email', "definition": 'Email address, as defined in [RFC 3696](https://datatracker.ietf.org/doc/rfc3986/) Section 3.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/ExternalIdentifierType/gitoid': {"label": 'gitoid', "definition": '[Gitoid](https://www.iana.org/assignments/uri-schemes/prov/gitoid), stands for [Git Object ID](https://git-scm.com/book/en/v2/Git-Internals-Git-Objects). A gitoid of type blob is a unique hash of a binary artifact. A gitoid may represent either an [Artifact Identifier](https://github.com/omnibor/...', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/ExternalIdentifierType/other': {"label": 'other', "definition": 'Used when the type does not match any of the other options.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/ExternalIdentifierType/packageUrl': {"label": 'packageUrl', "definition": 'Package URL, as defined in the corresponding [Annex](../../../annexes/pkg-url-specification.md) of this specification.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/ExternalIdentifierType/securityOther': {"label": 'securityOther', "definition": 'Used when there is a security related identifier of unspecified type.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/ExternalIdentifierType/swhid': {"label": 'swhid', "definition": 'SoftWare Hash IDentifier, a persistent intrinsic identifier for digital artifacts, such as files, trees (also known as directories or folders), commits, and other objects typically found in version control systems. The format of the identifiers is defined in the [SWHID specification](https://www....', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/ExternalIdentifierType/swid': {"label": 'swid', "definition": 'Concise Software Identification (CoSWID) tag, as defined in [RFC 9393](https://datatracker.ietf.org/doc/rfc9393/) Section 2.3.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/ExternalIdentifierType/urlScheme': {"label": 'urlScheme', "definition": '[Uniform Resource Identifier (URI) Schemes](https://www.iana.org/assignments/uri-schemes/uri-schemes.xhtml). The scheme used in order to locate a resource.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/ExternalMap': {"label": 'ExternalMap', "definition": 'A map of Element identifiers that are used within an SpdxDocument but defined external to that SpdxDocument.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/ExternalRef': {"label": 'ExternalRef', "definition": 'A reference to a resource outside the scope of SPDX-3.0 content related to an Element.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/altDownloadLocation': {"label": 'altDownloadLocation', "definition": 'A reference to an alternative download location.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/altWebPage': {"label": 'altWebPage', "definition": 'A reference to an alternative web page.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/binaryArtifact': {"label": 'binaryArtifact', "definition": 'A reference to binary artifacts related to a package.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/bower': {"label": 'bower', "definition": 'A reference to a Bower package. The package locator format, looks like `package#version`, is defined in the "install" section of [Bower API documentation](https://bower.io/docs/api/#install).', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/buildMeta': {"label": 'buildMeta', "definition": 'A reference build metadata related to a published package.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/buildSystem': {"label": 'buildSystem', "definition": 'A reference build system used to create or publish the package.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/certificationReport': {"label": 'certificationReport', "definition": 'A reference to a certification report for a package from an accredited/independent body.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/chat': {"label": 'chat', "definition": 'A reference to the instant messaging system used by the maintainer for a package.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/componentAnalysisReport': {"label": 'componentAnalysisReport', "definition": 'A reference to a Software Composition Analysis (SCA) report.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/cwe': {"label": 'cwe', "definition": '[Common Weakness Enumeration](https://csrc.nist.gov/glossary/term/common_weakness_enumeration). A reference to a source of software flaw defined within the official [CWE List](https://cwe.mitre.org/data/) that conforms to the [CWE specification](https://cwe.mitre.org/).', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/documentation': {"label": 'documentation', "definition": 'A reference to the documentation for a package.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/dynamicAnalysisReport': {"label": 'dynamicAnalysisReport', "definition": 'A reference to a dynamic analysis report for a package.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/eolNotice': {"label": 'eolNotice', "definition": 'A reference to the End Of Sale (EOS) and/or End Of Life (EOL) information related to a package.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/exportControlAssessment': {"label": 'exportControlAssessment', "definition": 'A reference to a export control assessment for a package.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/funding': {"label": 'funding', "definition": 'A reference to funding information related to a package.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/issueTracker': {"label": 'issueTracker', "definition": 'A reference to the issue tracker for a package.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/license': {"label": 'license', "definition": 'A reference to additional license information related to an artifact.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/mailingList': {"label": 'mailingList', "definition": 'A reference to the mailing list used by the maintainer for a package.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/mavenCentral': {"label": 'mavenCentral', "definition": 'A reference to a Maven repository artifact. The artifact locator format is defined in the [Maven documentation](https://maven.apache.org/guides/mini/guide-naming-conventions.html) and looks like `groupId:artifactId[:version]`.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/metrics': {"label": 'metrics', "definition": 'A reference to metrics related to package such as OpenSSF scorecards.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/npm': {"label": 'npm', "definition": 'A reference to an npm package. The package locator format is defined in the [npm documentation](https://docs.npmjs.com/cli/v10/configuring-npm/package-json) and looks like `package@version`.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/nuget': {"label": 'nuget', "definition": 'A reference to a NuGet package. The package locator format is defined in the [NuGet documentation](https://docs.nuget.org) and looks like `package/version`.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/other': {"label": 'other', "definition": 'Used when the type does not match any of the other options.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/privacyAssessment': {"label": 'privacyAssessment', "definition": 'A reference to a privacy assessment for a package.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/productMetadata': {"label": 'productMetadata', "definition": "A reference to additional product metadata such as reference within organization's product catalog.", "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/purchaseOrder': {"label": 'purchaseOrder', "definition": 'A reference to a purchase order for a package.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/qualityAssessmentReport': {"label": 'qualityAssessmentReport', "definition": 'A reference to a quality assessment for a package.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/releaseHistory': {"label": 'releaseHistory', "definition": 'A reference to a published list of releases for a package.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/releaseNotes': {"label": 'releaseNotes', "definition": 'A reference to the release notes for a package.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/riskAssessment': {"label": 'riskAssessment', "definition": 'A reference to a risk assessment for a package.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/runtimeAnalysisReport': {"label": 'runtimeAnalysisReport', "definition": 'A reference to a runtime analysis report for a package.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/secureSoftwareAttestation': {"label": 'secureSoftwareAttestation', "definition": 'A reference to information assuring that the software is developed using security practices as defined by [NIST SP 800-218 Secure Software Development Framework (SSDF) Version 1.1](https://csrc.nist.gov/pubs/sp/800/218/final) or [CISA Secure Software Development Attestation Form](https://www.cisa...', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/securityAdversaryModel': {"label": 'securityAdversaryModel', "definition": 'A reference to the security adversary model for a package.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/securityAdvisory': {"label": 'securityAdvisory', "definition": 'A reference to a published security advisory (where advisory as defined per [ISO 29147:2018](https://www.iso.org/standard/72311.html)) that may affect one or more elements, e.g., vendor advisories or specific NVD entries.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/securityFix': {"label": 'securityFix', "definition": 'A reference to the patch or source code that fixes a vulnerability.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/securityOther': {"label": 'securityOther', "definition": 'A reference to related security information of unspecified type.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/securityPenTestReport': {"label": 'securityPenTestReport', "definition": 'A reference to a [penetration test](https://en.wikipedia.org/wiki/Penetration_test) report for a package.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/securityPolicy': {"label": 'securityPolicy', "definition": 'A reference to instructions for reporting newly discovered security vulnerabilities for a package.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/securityThreatModel': {"label": 'securityThreatModel', "definition": 'A reference the [security threat model](https://en.wikipedia.org/wiki/Threat_model) for a package.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/socialMedia': {"label": 'socialMedia', "definition": 'A reference to a social media channel for a package.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/sourceArtifact': {"label": 'sourceArtifact', "definition": 'A reference to an artifact containing the sources for a package.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/staticAnalysisReport': {"label": 'staticAnalysisReport', "definition": 'A reference to a static analysis report for a package.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/support': {"label": 'support', "definition": 'A reference to the software support channel or other support information for a package.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/vcs': {"label": 'vcs', "definition": 'A reference to a version control system related to a software artifact.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/vulnerabilityDisclosureReport': {"label": 'vulnerabilityDisclosureReport', "definition": "A reference to a Vulnerability Disclosure Report (VDR) which provides the software supplier's analysis and findings describing the impact (or lack of impact) that reported vulnerabilities have on packages or products in the supplier's SBOM as defined in [NIST SP 800-161 Cybersecurity Supply Chain...", "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/ExternalRefType/vulnerabilityExploitabilityAssessment': {"label": 'vulnerabilityExploitabilityAssessment', "definition": 'A reference to a Vulnerability Exploitability eXchange (VEX) statement which provides information on whether a product is impacted by a specific vulnerability in an included package and, if affected, whether there are actions recommended to remediate. See also [NTIA VEX one-page summary](https://...', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/Hash': {"label": 'Hash', "definition": 'A mathematically calculated representation of a grouping of data.', "broader": ('https://spdx.org/rdf/3.0.1/terms/Core/IntegrityMethod',), "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/HashAlgorithm/adler32': {"label": 'adler32', "definition": 'Adler-32 checksum is part of the widely used zlib compression library as defined in [RFC 1950](https://datatracker.ietf.org/doc/rfc1950/) Section 2.3.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/HashAlgorithm/blake2b256': {"label": 'blake2b256', "definition": 'BLAKE2b algorithm with a digest size of 256, as defined in [RFC 7693](https://datatracker.ietf.org/doc/rfc7693/) Section 4.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/HashAlgorithm/blake2b384': {"label": 'blake2b384', "definition": 'BLAKE2b algorithm with a digest size of 384, as defined in [RFC 7693](https://datatracker.ietf.org/doc/rfc7693/) Section 4.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/HashAlgorithm/blake2b512': {"label": 'blake2b512', "definition": 'BLAKE2b algorithm with a digest size of 512, as defined in [RFC 7693](https://datatracker.ietf.org/doc/rfc7693/) Section 4.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/HashAlgorithm/blake3': {"label": 'blake3', "definition": '[BLAKE3](https://github.com/BLAKE3-team/BLAKE3-specs/blob/master/blake3.pdf)', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/HashAlgorithm/crystalsDilithium': {"label": 'crystalsDilithium', "definition": '[Dilithium](https://pq-crystals.org/dilithium/)', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/HashAlgorithm/crystalsKyber': {"label": 'crystalsKyber', "definition": '[Kyber](https://pq-crystals.org/kyber/)', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/HashAlgorithm/falcon': {"label": 'falcon', "definition": '[FALCON](https://falcon-sign.info/falcon.pdf)', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/HashAlgorithm/md2': {"label": 'md2', "definition": 'MD2 message-digest algorithm, as defined in [RFC 1319](https://datatracker.ietf.org/doc/rfc1319/).', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/HashAlgorithm/md4': {"label": 'md4', "definition": 'MD4 message-digest algorithm, as defined in [RFC 1186](https://datatracker.ietf.org/doc/rfc1186/).', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/HashAlgorithm/md5': {"label": 'md5', "definition": 'MD5 message-digest algorithm, as defined in [RFC 1321](https://datatracker.ietf.org/doc/rfc1321/).', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/HashAlgorithm/md6': {"label": 'md6', "definition": '[MD6 hash function](https://people.csail.mit.edu/rivest/pubs/RABCx08.pdf)', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/HashAlgorithm/other': {"label": 'other', "definition": 'any hashing algorithm that does not exist in this list of entries', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/HashAlgorithm/sha1': {"label": 'sha1', "definition": 'SHA-1, a secure hashing algorithm, as defined in [RFC 3174](https://datatracker.ietf.org/doc/rfc3174/).', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/HashAlgorithm/sha224': {"label": 'sha224', "definition": 'SHA-2 with a digest length of 224, as defined in [RFC 3874](https://datatracker.ietf.org/doc/rfc3874/).', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/HashAlgorithm/sha256': {"label": 'sha256', "definition": 'SHA-2 with a digest length of 256, as defined in [RFC 6234](https://datatracker.ietf.org/doc/rfc6234/).', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/HashAlgorithm/sha384': {"label": 'sha384', "definition": 'SHA-2 with a digest length of 384, as defined in [RFC 6234](https://datatracker.ietf.org/doc/rfc6234/).', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/HashAlgorithm/sha3_224': {"label": 'sha3_224', "definition": 'SHA-3 with a digest length of 224, as defined in [FIPS 202](https://csrc.nist.gov/pubs/fips/202/final).', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/HashAlgorithm/sha3_256': {"label": 'sha3_256', "definition": 'SHA-3 with a digest length of 256, as defined in [FIPS 202](https://csrc.nist.gov/pubs/fips/202/final).', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/HashAlgorithm/sha3_384': {"label": 'sha3_384', "definition": 'SHA-3 with a digest length of 384, as defined in [FIPS 202](https://csrc.nist.gov/pubs/fips/202/final).', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/HashAlgorithm/sha3_512': {"label": 'sha3_512', "definition": 'SHA-3 with a digest length of 512, as defined in [FIPS 202](https://csrc.nist.gov/pubs/fips/202/final).', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/HashAlgorithm/sha512': {"label": 'sha512', "definition": 'SHA-2 with a digest length of 512, as defined in [RFC 6234](https://datatracker.ietf.org/doc/rfc6234/).', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/IndividualElement': {"label": 'IndividualElement', "definition": 'A concrete subclass of Element used by Individuals in the Core profile.', "broader": ('https://spdx.org/rdf/3.0.1/terms/Core/Element',), "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/IntegrityMethod': {"label": 'IntegrityMethod', "definition": 'Provides an independently reproducible mechanism that permits verification of a specific Element.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/LifecycleScopeType/build': {"label": 'build', "definition": "A relationship has specific context implications during an element's build phase, during development.", "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/LifecycleScopeType/design': {"label": 'design', "definition": "A relationship has specific context implications during an element's design.", "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/LifecycleScopeType/development': {"label": 'development', "definition": 'A relationship has specific context implications during development phase of an element.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/LifecycleScopeType/other': {"label": 'other', "definition": 'A relationship has other specific context information necessary to capture that the above set of enumerations does not handle.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/LifecycleScopeType/runtime': {"label": 'runtime', "definition": 'A relationship has specific context implications during the execution phase of an element.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/LifecycleScopeType/test': {"label": 'test', "definition": "A relationship has specific context implications during an element's testing phase, during development.", "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/LifecycleScopedRelationship': {"label": 'LifecycleScopedRelationship', "definition": 'Provide context for a relationship that occurs in the lifecycle.', "broader": ('https://spdx.org/rdf/3.0.1/terms/Core/Relationship',), "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/NamespaceMap': {"label": 'NamespaceMap', "definition": 'A mapping between prefixes and namespace partial URIs.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/NoAssertionElement': {"label": 'NoAssertionElement', "definition": 'An Individual Value for Element representing a set of Elements of unknown identify or cardinality (number).', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/NoneElement': {"label": 'NoneElement', "definition": 'An Individual Value for Element representing a set of Elements with cardinality (number/count) of zero.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/Organization': {"label": 'Organization', "definition": 'A group of people who work together in an organized way for a shared purpose.', "broader": ('https://spdx.org/rdf/3.0.1/terms/Core/Agent',), "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/PackageVerificationCode': {"label": 'PackageVerificationCode', "definition": 'An SPDX version 2.X compatible verification method for software packages.', "broader": ('https://spdx.org/rdf/3.0.1/terms/Core/IntegrityMethod',), "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/Person': {"label": 'Person', "definition": 'An individual human being.', "broader": ('https://spdx.org/rdf/3.0.1/terms/Core/Agent',), "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/PositiveIntegerRange': {"label": 'PositiveIntegerRange', "definition": 'A tuple of two positive integers that define a range.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/PresenceType/no': {"label": 'no', "definition": 'Indicates absence of the field.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/PresenceType/noAssertion': {"label": 'noAssertion', "definition": 'Makes no assertion about the field.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/PresenceType/yes': {"label": 'yes', "definition": 'Indicates presence of the field.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/ProfileIdentifierType/ai': {"label": 'ai', "definition": 'the element follows the AI profile specification', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/ProfileIdentifierType/build': {"label": 'build', "definition": 'the element follows the Build profile specification', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/ProfileIdentifierType/core': {"label": 'core', "definition": 'the element follows the Core profile specification', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/ProfileIdentifierType/dataset': {"label": 'dataset', "definition": 'the element follows the Dataset profile specification', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/ProfileIdentifierType/expandedLicensing': {"label": 'expandedLicensing', "definition": 'the element follows the ExpandedLicensing profile specification', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/ProfileIdentifierType/extension': {"label": 'extension', "definition": 'the element follows the Extension profile specification', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/ProfileIdentifierType/lite': {"label": 'lite', "definition": 'the element follows the Lite profile specification', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/ProfileIdentifierType/security': {"label": 'security', "definition": 'the element follows the Security profile specification', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/ProfileIdentifierType/simpleLicensing': {"label": 'simpleLicensing', "definition": 'the element follows the SimpleLicensing profile specification', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/ProfileIdentifierType/software': {"label": 'software', "definition": 'the element follows the Software profile specification', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/Relationship': {"label": 'Relationship', "definition": 'Describes a relationship between one or more elements.', "broader": ('https://spdx.org/rdf/3.0.1/terms/Core/Element',), "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipCompleteness/complete': {"label": 'complete', "definition": 'The relationship is known to be exhaustive.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipCompleteness/incomplete': {"label": 'incomplete', "definition": 'The relationship is known not to be exhaustive.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipCompleteness/noAssertion': {"label": 'noAssertion', "definition": 'No assertion can be made about the completeness of the relationship.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/affects': {"label": 'affects', "definition": 'The `from` Vulnerability affects each `to` Element. The use of the `affects` type is constrained to `VexAffectedVulnAssessmentRelationship` classed relationships.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/amendedBy': {"label": 'amendedBy', "definition": 'The `from` Element is amended by each `to` Element.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/ancestorOf': {"label": 'ancestorOf', "definition": 'The `from` Element is an ancestor of each `to` Element.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/availableFrom': {"label": 'availableFrom', "definition": 'The `from` Element is available from the additional supplier described by each `to` Element.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/configures': {"label": 'configures', "definition": 'The `from` Element is a configuration applied to each `to` Element, during a LifecycleScopeType period.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/contains': {"label": 'contains', "definition": 'The `from` Element contains each `to` Element.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/coordinatedBy': {"label": 'coordinatedBy', "definition": 'The `from` Vulnerability is coordinatedBy the `to` Agent(s) (vendor, researcher, or consumer agent).', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/copiedTo': {"label": 'copiedTo', "definition": 'The `from` Element has been copied to each `to` Element.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/delegatedTo': {"label": 'delegatedTo', "definition": 'The `from` Agent is delegating an action to the Agent of the `to` Relationship (which must be of type invokedBy), during a LifecycleScopeType (e.g. the `to` invokedBy Relationship is being done on behalf of `from`).', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/dependsOn': {"label": 'dependsOn', "definition": 'The `from` Element depends on each `to` Element, during a LifecycleScopeType period.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/descendantOf': {"label": 'descendantOf', "definition": 'The `from` Element is a descendant of each `to` Element.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/describes': {"label": 'describes', "definition": 'The `from` Element describes each `to` Element. To denote the root(s) of a tree of elements in a collection, the rootElement property should be used.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/doesNotAffect': {"label": 'doesNotAffect', "definition": 'The `from` Vulnerability has no impact on each `to` Element. The use of the `doesNotAffect` is constrained to `VexNotAffectedVulnAssessmentRelationship` classed relationships.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/expandsTo': {"label": 'expandsTo', "definition": 'The `from` archive expands out as an artifact described by each `to` Element.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/exploitCreatedBy': {"label": 'exploitCreatedBy', "definition": 'The `from` Vulnerability has had an exploit created against it by each `to` Agent.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/fixedBy': {"label": 'fixedBy', "definition": 'Designates a `from` Vulnerability has been fixed by the `to` Agent(s).', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/fixedIn': {"label": 'fixedIn', "definition": 'A `from` Vulnerability has been fixed in each `to` Element. The use of the `fixedIn` type is constrained to `VexFixedVulnAssessmentRelationship` classed relationships.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/foundBy': {"label": 'foundBy', "definition": 'Designates a `from` Vulnerability was originally discovered by the `to` Agent(s).', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/generates': {"label": 'generates', "definition": 'The `from` Element generates each `to` Element.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/hasAddedFile': {"label": 'hasAddedFile', "definition": 'Every `to` Element is a file added to the `from` Element (`from` hasAddedFile `to`).', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/hasAssessmentFor': {"label": 'hasAssessmentFor', "definition": 'Relates a `from` Vulnerability and each `to` Element with a security assessment. To be used with `VulnAssessmentRelationship` types.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/hasAssociatedVulnerability': {"label": 'hasAssociatedVulnerability', "definition": 'Used to associate a `from` Artifact with each `to` Vulnerability.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/hasConcludedLicense': {"label": 'hasConcludedLicense', "definition": 'The `from` SoftwareArtifact is concluded by the SPDX data creator to be governed by each `to` license.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/hasDataFile': {"label": 'hasDataFile', "definition": "The `from` Element treats each `to` Element as a data file. A data file is an artifact that stores data required or optional for the `from` Element's functionality. A data file can be a database file, an index file, a log file, an AI model file, a calibration data file, a temporary file, a backup...", "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/hasDeclaredLicense': {"label": 'hasDeclaredLicense', "definition": 'The `from` SoftwareArtifact was discovered to actually contain each `to` license, for example as detected by use of automated tooling.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/hasDeletedFile': {"label": 'hasDeletedFile', "definition": 'Every `to` Element is a file deleted from the `from` Element (`from` hasDeletedFile `to`).', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/hasDependencyManifest': {"label": 'hasDependencyManifest', "definition": 'The `from` Element has manifest files that contain dependency information in each `to` Element.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/hasDistributionArtifact': {"label": 'hasDistributionArtifact', "definition": 'The `from` Element is distributed as an artifact in each `to` Element (e.g. an RPM or archive file).', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/hasDocumentation': {"label": 'hasDocumentation', "definition": 'The `from` Element is documented by each `to` Element.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/hasDynamicLink': {"label": 'hasDynamicLink', "definition": 'The `from` Element dynamically links in each `to` Element, during a LifecycleScopeType period.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/hasEvidence': {"label": 'hasEvidence', "definition": 'Every `to` Element is considered as evidence for the `from` Element (`from` hasEvidence `to`).', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/hasExample': {"label": 'hasExample', "definition": 'Every `to` Element is an example for the `from` Element (`from` hasExample `to`).', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/hasHost': {"label": 'hasHost', "definition": 'The `from` Build was run on the `to` Element during a LifecycleScopeType period (e.g. the host that the build runs on).', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/hasInput': {"label": 'hasInput', "definition": 'The `from` Build has each `to` Element as an input, during a LifecycleScopeType period.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/hasMetadata': {"label": 'hasMetadata', "definition": 'Every `to` Element is metadata about the `from` Element (`from` hasMetadata `to`).', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/hasOptionalComponent': {"label": 'hasOptionalComponent', "definition": 'Every `to` Element is an optional component of the `from` Element (`from` hasOptionalComponent `to`).', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/hasOptionalDependency': {"label": 'hasOptionalDependency', "definition": 'The `from` Element optionally depends on each `to` Element, during a LifecycleScopeType period.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/hasOutput': {"label": 'hasOutput', "definition": 'The `from` Build element generates each `to` Element as an output, during a LifecycleScopeType period.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/hasPrerequisite': {"label": 'hasPrerequisite', "definition": 'The `from` Element has a prerequisite on each `to` Element, during a LifecycleScopeType period.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/hasProvidedDependency': {"label": 'hasProvidedDependency', "definition": 'The `from` Element has a dependency on each `to` Element, dependency is not in the distributed artifact, but assumed to be provided, during a LifecycleScopeType period.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/hasRequirement': {"label": 'hasRequirement', "definition": 'The `from` Element has a requirement on each `to` Element, during a LifecycleScopeType period.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/hasSpecification': {"label": 'hasSpecification', "definition": 'Every `to` Element is a specification for the `from` Element (`from` hasSpecification `to`), during a LifecycleScopeType period.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/hasStaticLink': {"label": 'hasStaticLink', "definition": 'The `from` Element statically links in each `to` Element, during a LifecycleScopeType period.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/hasTest': {"label": 'hasTest', "definition": 'Every `to` Element is a test artifact for the `from` Element (`from` hasTest `to`), during a LifecycleScopeType period.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/hasTestCase': {"label": 'hasTestCase', "definition": 'Every `to` Element is a test case for the `from` Element (`from` hasTestCase `to`).', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/hasVariant': {"label": 'hasVariant', "definition": 'Every `to` Element is a variant the `from` Element (`from` hasVariant `to`).', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/invokedBy': {"label": 'invokedBy', "definition": 'The `from` Element was invoked by the `to` Agent, during a LifecycleScopeType period (for example, a Build element that describes a build step).', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/modifiedBy': {"label": 'modifiedBy', "definition": 'The `from` Element is modified by each `to` Element.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/other': {"label": 'other', "definition": 'Every `to` Element is related to the `from` Element where the relationship type is not described by any of the SPDX relationship types (this relationship is directionless).', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/packagedBy': {"label": 'packagedBy', "definition": 'Every `to` Element is a packaged instance of the `from` Element (`from` packagedBy `to`).', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/patchedBy': {"label": 'patchedBy', "definition": 'Every `to` Element is a patch for the `from` Element (`from` patchedBy `to`).', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/publishedBy': {"label": 'publishedBy', "definition": 'Designates a `from` Vulnerability was made available for public use or reference by each `to` Agent.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/reportedBy': {"label": 'reportedBy', "definition": 'Designates a `from` Vulnerability was first reported to a project, vendor, or tracking database for formal identification by each `to` Agent.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/republishedBy': {"label": 'republishedBy', "definition": "Designates a `from` Vulnerability's details were tracked, aggregated, and/or enriched to improve context (i.e. NVD) by each `to` Agent.", "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/serializedInArtifact': {"label": 'serializedInArtifact', "definition": 'The `from` SpdxDocument can be found in a serialized form in each `to` Artifact.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/testedOn': {"label": 'testedOn', "definition": 'The `from` Element has been tested on the `to` Element(s).', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/trainedOn': {"label": 'trainedOn', "definition": 'The `from` Element has been trained on the `to` Element(s).', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/underInvestigationFor': {"label": 'underInvestigationFor', "definition": 'The `from` Vulnerability impact is being investigated for each `to` Element. The use of the `underInvestigationFor` type is constrained to `VexUnderInvestigationVulnAssessmentRelationship` classed relationships.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/usesTool': {"label": 'usesTool', "definition": 'The `from` Element uses each `to` Element as a tool, during a LifecycleScopeType period.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/SoftwareAgent': {"label": 'SoftwareAgent', "definition": 'A software agent.', "broader": ('https://spdx.org/rdf/3.0.1/terms/Core/Agent',), "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/SpdxDocument': {"label": 'SpdxDocument', "definition": 'A collection of SPDX Elements that could potentially be serialized.', "broader": ('https://spdx.org/rdf/3.0.1/terms/Core/ElementCollection',), "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/SpdxOrganization': {"label": 'SpdxOrganization', "definition": 'An Organization representing the SPDX Project.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/SupportType/deployed': {"label": 'deployed', "definition": 'in addition to being supported by the supplier, the software is known to have been deployed and is in use.  For a software as a service provider, this implies the software is now available as a service.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/SupportType/development': {"label": 'development', "definition": 'the artifact is in active development and is not considered ready for formal support from the supplier.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/SupportType/endOfSupport': {"label": 'endOfSupport', "definition": 'there is a defined end of support for the artifact from the supplier.  This may also be referred to as end of life. There is a validUntilDate that can be used to signal when support ends for the artifact.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/SupportType/limitedSupport': {"label": 'limitedSupport', "definition": 'the artifact has been released, and there is limited support available from the supplier. There is a validUntilDate that can provide additional information about the duration of support.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/SupportType/noAssertion': {"label": 'noAssertion', "definition": 'no assertion about the type of support is made.   This is considered the default if no other support type is used.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/SupportType/noSupport': {"label": 'noSupport', "definition": 'there is no support for the artifact from the supplier, consumer assumes any support obligations.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/SupportType/support': {"label": 'support', "definition": 'the artifact has been released, and is supported from the supplier.   There is a validUntilDate that can provide additional information about the duration of support.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/Tool': {"label": 'Tool', "definition": 'An element of hardware and/or software utilized to carry out a particular function.', "broader": ('https://spdx.org/rdf/3.0.1/terms/Core/Element',), "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/algorithm': {"label": 'algorithm', "definition": 'Specifies the algorithm used for calculating the hash value.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/annotationType': {"label": 'annotationType', "definition": 'Describes the type of annotation.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/beginIntegerRange': {"label": 'beginIntegerRange', "definition": 'Defines the beginning of a range.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/builtTime': {"label": 'builtTime', "definition": 'Specifies the time an artifact was built.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/comment': {"label": 'comment', "definition": 'Provide consumers with comments by the creator of the Element about the Element.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/completeness': {"label": 'completeness', "definition": 'Provides information about the completeness of relationships.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/contentType': {"label": 'contentType', "definition": 'Provides information about the content type of an Element or a Property.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/context': {"label": 'context', "definition": 'Gives information about the circumstances or unifying properties that Elements of the bundle have been assembled under.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/created': {"label": 'created', "definition": 'Identifies when the Element was originally created.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/createdBy': {"label": 'createdBy', "definition": 'Identifies who or what created the Element.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/createdUsing': {"label": 'createdUsing', "definition": 'Identifies the tooling that was used during the creation of the Element.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/creationInfo': {"label": 'creationInfo', "definition": 'Provides information about the creation of the Element.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/dataLicense': {"label": 'dataLicense', "definition": 'Provides the license under which the SPDX documentation of the Element can be used.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/definingArtifact': {"label": 'definingArtifact', "definition": 'Artifact representing a serialization instance of SPDX data containing the definition of a particular Element.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/description': {"label": 'description', "definition": 'Provides a detailed description of the Element.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/element': {"label": 'element', "definition": 'Refers to one or more Elements that are part of an ElementCollection.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/endIntegerRange': {"label": 'endIntegerRange', "definition": 'Defines the end of a range.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/endTime': {"label": 'endTime', "definition": 'Specifies the time from which an element is no longer applicable / valid.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/extension': {"label": 'extension', "definition": 'Specifies an Extension characterization of some aspect of an Element.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/externalIdentifier': {"label": 'externalIdentifier', "definition": 'Provides a reference to a resource outside the scope of SPDX-3.0 content that uniquely identifies an Element.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/externalIdentifierType': {"label": 'externalIdentifierType', "definition": 'Specifies the type of the external identifier.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/externalRef': {"label": 'externalRef', "definition": 'Points to a resource outside the scope of the SPDX-3.0 content that provides additional characteristics of an Element.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/externalRefType': {"label": 'externalRefType', "definition": 'Specifies the type of the external reference.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/externalSpdxId': {"label": 'externalSpdxId', "definition": 'Identifies an external Element used within an SpdxDocument but defined external to that SpdxDocument.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/from': {"label": 'from', "definition": 'References the Element on the left-hand side of a relationship.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/hashValue': {"label": 'hashValue', "definition": 'The result of applying a hash algorithm to an Element.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/identifier': {"label": 'identifier', "definition": 'Uniquely identifies an external element.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/identifierLocator': {"label": 'identifierLocator', "definition": 'Provides the location for more information regarding an external identifier.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/import': {"label": 'import', "definition": 'Provides an ExternalMap of Element identifiers.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/issuingAuthority': {"label": 'issuingAuthority', "definition": 'An entity that is authorized to issue identification credentials.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/key': {"label": 'key', "definition": 'A key used in a generic key-value pair.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/locationHint': {"label": 'locationHint', "definition": 'Provides an indication of where to retrieve an external Element.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/locator': {"label": 'locator', "definition": 'Provides the location of an external reference.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/name': {"label": 'name', "definition": 'Identifies the name of an Element as designated by the creator.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/namespace': {"label": 'namespace', "definition": 'Provides an unambiguous mechanism for conveying a URI fragment portion of an Element ID.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/namespaceMap': {"label": 'namespaceMap', "definition": 'Provides a NamespaceMap of prefixes and associated namespace partial URIs applicable to an SpdxDocument and independent of any specific serialization format or instance.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/originatedBy': {"label": 'originatedBy', "definition": 'Identifies from where or whom the Element originally came.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/packageVerificationCodeExcludedFile': {"label": 'packageVerificationCodeExcludedFile', "definition": 'The relative file name of a file to be excluded from the `PackageVerificationCode`.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/prefix': {"label": 'prefix', "definition": 'A substitute for a URI.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/profileConformance': {"label": 'profileConformance', "definition": 'Describes one a profile which the creator of this ElementCollection intends to conform to.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/relationshipType': {"label": 'relationshipType', "definition": 'Information about the relationship between two Elements.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/releaseTime': {"label": 'releaseTime', "definition": 'Specifies the time an artifact was released.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/rootElement': {"label": 'rootElement', "definition": 'This property is used to denote the root Element(s) of a tree of elements contained in a BOM.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/scope': {"label": 'scope', "definition": 'Capture the scope of information about a specific relationship between elements.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/specVersion': {"label": 'specVersion', "definition": 'Provides a reference number that can be used to understand how to parse and interpret an Element.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/standardName': {"label": 'standardName', "definition": 'The name of a relevant standard that may apply to an artifact.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/startTime': {"label": 'startTime', "definition": 'Specifies the time from which an element is applicable / valid.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/statement': {"label": 'statement', "definition": 'Commentary on an assertion that an annotator has made.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/subject': {"label": 'subject', "definition": 'An Element an annotator has made an assertion about.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/summary': {"label": 'summary', "definition": 'A short description of an Element.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/suppliedBy': {"label": 'suppliedBy', "definition": 'Identifies who or what supplied the artifact or VulnAssessmentRelationship referenced by the Element.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/supportLevel': {"label": 'supportLevel', "definition": 'Specifies the level of support associated with an artifact.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/to': {"label": 'to', "definition": 'References an Element on the right-hand side of a relationship.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/validUntilTime': {"label": 'validUntilTime', "definition": 'Specifies until when the artifact can be used before its usage needs to be reassessed.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/value': {"label": 'value', "definition": 'A value used in a generic key-value pair.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Core/verifiedUsing': {"label": 'verifiedUsing', "definition": 'Provides an IntegrityMethod with which the integrity of an Element can be asserted.', "source_vocab": 'SPDX-3.0.1'},
})

__all__ = ["Agent", "algorithm", "Annotation", "annotationType", "Artifact", "beginIntegerRange", "Bom", "builtTime", "Bundle", "comment", "completeness", "contentType", "context", "created", "createdBy", "createdUsing", "CreationInfo", "creationInfo", "dataLicense", "definingArtifact", "description", "DictionaryEntry", "Element", "element", "ElementCollection", "endIntegerRange", "endTime", "extension", "ExternalIdentifier", "externalIdentifier", "externalIdentifierType", "ExternalMap", "ExternalRef", "externalRef", "externalRefType", "externalSpdxId", "from_", "Hash", "hashValue", "identifier", "identifierLocator", "import_", "IndividualElement", "IntegrityMethod", "issuingAuthority", "key", "LifecycleScopedRelationship", "locationHint", "locator", "name", "namespace", "namespaceMap", "NamespaceMap", "NoAssertionElement", "NoneElement", "Organization", "originatedBy", "PackageVerificationCode", "packageVerificationCodeExcludedFile", "Person", "PositiveIntegerRange", "prefix", "profileConformance", "Relationship", "relationshipType", "releaseTime", "rootElement", "scope", "SoftwareAgent", "SpdxDocument", "SpdxOrganization", "specVersion", "standardName", "startTime", "statement", "subject", "summary", "suppliedBy", "supportLevel", "to", "Tool", "validUntilTime", "value", "verifiedUsing", "AnnotationType", "ExternalIdentifierType", "ExternalRefType", "HashAlgorithm", "LifecycleScopeType", "PresenceType", "ProfileIdentifierType", "RelationshipCompleteness", "RelationshipType", "SupportType"]
