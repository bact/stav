# SPDX-FileCopyrightText: 2026-present Arthit Suriyawongkul
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0
#
# AUTO-GENERATED — do not edit manually.
# Source: SPDX 3.0.1 Software profile
# Generated: 2026-04-30T08:53:34Z
# Regenerate: python -m stav.codegen.generate tools/recipes/spdx_software.json

"""Vocabulary from SPDX 3.0.1 Software profile.

23 term constants (accessible as ``module.TermName``); grouped enums: :class:`ContentIdentifierType`, :class:`FileKindType`, :class:`SbomType`, :class:`SoftwarePurpose`."""

from __future__ import annotations

from stav._registry import _register
from stav.term import _StavVocabEnum

__stav_namespace__ = "vocab.spdx.software"

# ── Individual term constants ─────────────────────────────────────────────────────
# Plain string IRIs — use directly with MLflow, Pitloom, SBOM serialisers.
# Metadata (label, definition, broader) via: stav.label(NaturalPerson) etc.
additionalPurpose = 'https://spdx.org/rdf/3.0.1/terms/Software/additionalPurpose'
attributionText = 'https://spdx.org/rdf/3.0.1/terms/Software/attributionText'
byteRange = 'https://spdx.org/rdf/3.0.1/terms/Software/byteRange'
ContentIdentifier = 'https://spdx.org/rdf/3.0.1/terms/Software/ContentIdentifier'
contentIdentifier = 'https://spdx.org/rdf/3.0.1/terms/Software/contentIdentifier'
contentIdentifierType = 'https://spdx.org/rdf/3.0.1/terms/Software/contentIdentifierType'
contentIdentifierValue = 'https://spdx.org/rdf/3.0.1/terms/Software/contentIdentifierValue'
copyrightText = 'https://spdx.org/rdf/3.0.1/terms/Software/copyrightText'
downloadLocation = 'https://spdx.org/rdf/3.0.1/terms/Software/downloadLocation'
File = 'https://spdx.org/rdf/3.0.1/terms/Software/File'
fileKind = 'https://spdx.org/rdf/3.0.1/terms/Software/fileKind'
homePage = 'https://spdx.org/rdf/3.0.1/terms/Software/homePage'
lineRange = 'https://spdx.org/rdf/3.0.1/terms/Software/lineRange'
Package = 'https://spdx.org/rdf/3.0.1/terms/Software/Package'
packageUrl = 'https://spdx.org/rdf/3.0.1/terms/Software/packageUrl'
packageVersion = 'https://spdx.org/rdf/3.0.1/terms/Software/packageVersion'
primaryPurpose = 'https://spdx.org/rdf/3.0.1/terms/Software/primaryPurpose'
Sbom = 'https://spdx.org/rdf/3.0.1/terms/Software/Sbom'
sbomType = 'https://spdx.org/rdf/3.0.1/terms/Software/sbomType'
Snippet = 'https://spdx.org/rdf/3.0.1/terms/Software/Snippet'
snippetFromFile = 'https://spdx.org/rdf/3.0.1/terms/Software/snippetFromFile'
SoftwareArtifact = 'https://spdx.org/rdf/3.0.1/terms/Software/SoftwareArtifact'
sourceInfo = 'https://spdx.org/rdf/3.0.1/terms/Software/sourceInfo'

class ContentIdentifierType(_StavVocabEnum):
    """Content identifier types from SPDX 3.0.1 Software profile."""
    gitoid = 'https://spdx.org/rdf/3.0.1/terms/Software/ContentIdentifierType/gitoid'
    swhid = 'https://spdx.org/rdf/3.0.1/terms/Software/ContentIdentifierType/swhid'

class FileKindType(_StavVocabEnum):
    """File kind types from SPDX 3.0.1 Software profile."""
    directory = 'https://spdx.org/rdf/3.0.1/terms/Software/FileKindType/directory'
    file = 'https://spdx.org/rdf/3.0.1/terms/Software/FileKindType/file'

class SbomType(_StavVocabEnum):
    """SBOM type classifications from SPDX 3.0.1 Software profile."""
    analyzed = 'https://spdx.org/rdf/3.0.1/terms/Software/SbomType/analyzed'
    build = 'https://spdx.org/rdf/3.0.1/terms/Software/SbomType/build'
    deployed = 'https://spdx.org/rdf/3.0.1/terms/Software/SbomType/deployed'
    design = 'https://spdx.org/rdf/3.0.1/terms/Software/SbomType/design'
    runtime = 'https://spdx.org/rdf/3.0.1/terms/Software/SbomType/runtime'
    source = 'https://spdx.org/rdf/3.0.1/terms/Software/SbomType/source'

class SoftwarePurpose(_StavVocabEnum):
    """Software purpose / type classifications from SPDX 3.0.1 Software profile."""
    application = 'https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/application'
    archive = 'https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/archive'
    bom = 'https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/bom'
    configuration = 'https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/configuration'
    container = 'https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/container'
    data = 'https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/data'
    device = 'https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/device'
    deviceDriver = 'https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/deviceDriver'
    diskImage = 'https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/diskImage'
    documentation = 'https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/documentation'
    evidence = 'https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/evidence'
    executable = 'https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/executable'
    file = 'https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/file'
    filesystemImage = 'https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/filesystemImage'
    firmware = 'https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/firmware'
    framework = 'https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/framework'
    install = 'https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/install'
    library = 'https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/library'
    manifest = 'https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/manifest'
    model = 'https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/model'
    module = 'https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/module'
    operatingSystem = 'https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/operatingSystem'
    other = 'https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/other'
    patch = 'https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/patch'
    platform = 'https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/platform'
    requirement = 'https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/requirement'
    source = 'https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/source'
    specification = 'https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/specification'
    test = 'https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/test'

# ── Metadata registry ──────────────────────────────────────────────────────────────
# Populated at import time so stav.label() / .definition() / .broader() work.
_register({
    'https://spdx.org/rdf/3.0.1/terms/Software/ContentIdentifier': {"label": 'ContentIdentifier', "definition": 'A canonical, unique, immutable identifier', "broader": ('https://spdx.org/rdf/3.0.1/terms/Core/IntegrityMethod',), "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Software/ContentIdentifierType/gitoid': {"label": 'gitoid', "definition": '[Gitoid](https://www.iana.org/assignments/uri-schemes/prov/gitoid), stands for [Git Object ID](https://git-scm.com/book/en/v2/Git-Internals-Git-Objects). A gitoid of type blob is a unique hash of a binary artifact. A gitoid may represent either an [Artifact Identifier](https://github.com/omnibor/...', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Software/ContentIdentifierType/swhid': {"label": 'swhid', "definition": 'SoftWare Hash IDentifier, a persistent intrinsic identifier for digital artifacts, such as files, trees (also known as directories or folders), commits, and other objects typically found in version control systems. The format of the identifiers is defined in the [SWHID specification](https://www....', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Software/File': {"label": 'File', "definition": 'Refers to any object that stores content on a computer.', "broader": ('https://spdx.org/rdf/3.0.1/terms/Software/SoftwareArtifact',), "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Software/FileKindType/directory': {"label": 'directory', "definition": 'The file represents a directory and all content stored in that directory.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Software/FileKindType/file': {"label": 'file', "definition": 'The file represents a single file (default).', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Software/Package': {"label": 'Package', "definition": 'Refers to any unit of content that can be associated with a distribution of software.', "broader": ('https://spdx.org/rdf/3.0.1/terms/Software/SoftwareArtifact',), "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Software/Sbom': {"label": 'Sbom', "definition": 'A collection of SPDX Elements describing a single package.', "broader": ('https://spdx.org/rdf/3.0.1/terms/Core/Bom',), "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Software/SbomType/analyzed': {"label": 'analyzed', "definition": 'SBOM generated through analysis of artifacts (e.g., executables, packages, containers, and virtual machine images) after its build. Such analysis generally requires a variety of heuristics. In some contexts, this may also be referred to as a "3rd party" SBOM.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Software/SbomType/build': {"label": 'build', "definition": 'SBOM generated as part of the process of building the software to create a releasable artifact (e.g., executable or package) from data such as source files, dependencies, built components, build process ephemeral data, and other SBOMs.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Software/SbomType/deployed': {"label": 'deployed', "definition": 'SBOM provides an inventory of software that is present on a system. This may be an assembly of other SBOMs that combines analysis of configuration options, and examination of execution behavior in a (potentially simulated) deployment environment.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Software/SbomType/design': {"label": 'design', "definition": 'SBOM of intended, planned software project or product with included components (some of which may not yet exist) for a new software artifact.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Software/SbomType/runtime': {"label": 'runtime', "definition": 'SBOM generated through instrumenting the system running the software, to capture only components present in the system, as well as external call-outs or dynamically loaded components. In some contexts, this may also be referred to as an "Instrumented" or "Dynamic" SBOM.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Software/SbomType/source': {"label": 'source', "definition": 'SBOM created directly from the development environment, source files, and included dependencies used to build an product artifact.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Software/Snippet': {"label": 'Snippet', "definition": 'Describes a certain part of a file.', "broader": ('https://spdx.org/rdf/3.0.1/terms/Software/SoftwareArtifact',), "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Software/SoftwareArtifact': {"label": 'SoftwareArtifact', "definition": 'A distinct article or unit related to Software.', "broader": ('https://spdx.org/rdf/3.0.1/terms/Core/Artifact',), "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/application': {"label": 'application', "definition": 'The Element is a software application.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/archive': {"label": 'archive', "definition": 'The Element is an archived collection of one or more files (.tar, .zip, etc.).', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/bom': {"label": 'bom', "definition": 'The Element is a bill of materials.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/configuration': {"label": 'configuration', "definition": 'The Element is configuration data.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/container': {"label": 'container', "definition": 'The Element is a container image which can be used by a container runtime application.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/data': {"label": 'data', "definition": 'The Element is data.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/device': {"label": 'device', "definition": 'The Element refers to a chipset, processor, or electronic board.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/deviceDriver': {"label": 'deviceDriver', "definition": 'The Element represents software that controls hardware devices.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/diskImage': {"label": 'diskImage', "definition": 'The Element refers to a disk image that can be written to a disk, booted in a VM, etc. A disk image typically contains most or all of the components necessary to boot, such as bootloaders, kernels, firmware, userspace, etc.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/documentation': {"label": 'documentation', "definition": 'The Element is documentation.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/evidence': {"label": 'evidence', "definition": 'The Element is the evidence that a specification or requirement has been fulfilled.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/executable': {"label": 'executable', "definition": 'The Element is an Artifact that can be run on a computer.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/file': {"label": 'file', "definition": 'The Element is a single file which can be independently distributed (configuration file, statically linked binary, Kubernetes deployment, etc.).', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/filesystemImage': {"label": 'filesystemImage', "definition": 'The Element is a file system image that can be written to a disk (or virtual) partition.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/firmware': {"label": 'firmware', "definition": "The Element provides low level control over a device's hardware.", "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/framework': {"label": 'framework', "definition": 'The Element is a software framework.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/install': {"label": 'install', "definition": 'The Element is used to install software on disk.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/library': {"label": 'library', "definition": 'The Element is a software library.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/manifest': {"label": 'manifest', "definition": 'The Element is a software manifest.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/model': {"label": 'model', "definition": 'The Element is a machine learning or artificial intelligence model.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/module': {"label": 'module', "definition": 'The Element is a module of a piece of software.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/operatingSystem': {"label": 'operatingSystem', "definition": 'The Element is an operating system.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/other': {"label": 'other', "definition": "The Element doesn't fit into any of the other categories.", "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/patch': {"label": 'patch', "definition": 'The Element contains a set of changes to update, fix, or improve another Element.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/platform': {"label": 'platform', "definition": 'The Element represents a runtime environment.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/requirement': {"label": 'requirement', "definition": 'The Element provides a requirement needed as input for another Element.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/source': {"label": 'source', "definition": 'The Element is a single or a collection of source files.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/specification': {"label": 'specification', "definition": 'The Element is a plan, guideline or strategy how to create, perform or analyze an application.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/test': {"label": 'test', "definition": 'The Element is a test used to verify functionality on an software element.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Software/additionalPurpose': {"label": 'additionalPurpose', "definition": 'Provides additional purpose information of the software artifact.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Software/attributionText': {"label": 'attributionText', "definition": 'Provides a place for the SPDX data creator to record acknowledgement text for a software Package, File or Snippet.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Software/byteRange': {"label": 'byteRange', "definition": 'Defines the byte range in the original host file that the snippet information applies to.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Software/contentIdentifier': {"label": 'contentIdentifier', "definition": 'A canonical, unique, immutable identifier of the artifact content, that may be used for verifying its identity and/or integrity.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Software/contentIdentifierType': {"label": 'contentIdentifierType', "definition": 'Specifies the type of the content identifier.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Software/contentIdentifierValue': {"label": 'contentIdentifierValue', "definition": 'Specifies the value of the content identifier.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Software/copyrightText': {"label": 'copyrightText', "definition": 'Identifies the text of one or more copyright notices for a software Package, File or Snippet, if any.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Software/downloadLocation': {"label": 'downloadLocation', "definition": 'Identifies the download Uniform Resource Identifier for the package at the time that the document was created.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Software/fileKind': {"label": 'fileKind', "definition": 'Describes if a given file is a directory or non-directory kind of file.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Software/homePage': {"label": 'homePage', "definition": "A place for the SPDX document creator to record a website that serves as the package's home page.", "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Software/lineRange': {"label": 'lineRange', "definition": 'Defines the line range in the original host file that the snippet information applies to.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Software/packageUrl': {"label": 'packageUrl', "definition": 'Provides a place for the SPDX data creator to record the package URL string (in accordance with the Package URL specification) for a software Package.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Software/packageVersion': {"label": 'packageVersion', "definition": 'Identify the version of a package.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Software/primaryPurpose': {"label": 'primaryPurpose', "definition": 'Provides information about the primary purpose of the software artifact.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Software/sbomType': {"label": 'sbomType', "definition": 'Provides information about the type of an SBOM.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Software/snippetFromFile': {"label": 'snippetFromFile', "definition": 'Defines the original host file that the snippet information applies to.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Software/sourceInfo': {"label": 'sourceInfo', "definition": 'Records any relevant background information or additional comments about the origin of the package.', "source_vocab": 'SPDX-3.0.1'},
})

__all__ = ["additionalPurpose", "attributionText", "byteRange", "ContentIdentifier", "contentIdentifier", "contentIdentifierType", "contentIdentifierValue", "copyrightText", "downloadLocation", "File", "fileKind", "homePage", "lineRange", "Package", "packageUrl", "packageVersion", "primaryPurpose", "Sbom", "sbomType", "Snippet", "snippetFromFile", "SoftwareArtifact", "sourceInfo", "ContentIdentifierType", "FileKindType", "SbomType", "SoftwarePurpose"]
