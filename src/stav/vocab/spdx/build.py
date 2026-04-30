# SPDX-FileCopyrightText: 2026-present Arthit Suriyawongkul
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0
#
# AUTO-GENERATED — do not edit manually.
# Source: SPDX 3.0.1 Build profile
# Generated: 2026-04-30T08:53:34Z
# Regenerate: python -m stav.codegen.generate tools/recipes/spdx_build.json

"""Vocabulary from SPDX 3.0.1 Build profile.

10 term constants (accessible as ``module.TermName``)."""

from __future__ import annotations

from stav._registry import _register
from stav.term import _StavVocabEnum

__stav_namespace__ = "vocab.spdx.build"

# ── Individual term constants ─────────────────────────────────────────────────────
# Plain string IRIs — use directly with MLflow, Pitloom, SBOM serialisers.
# Metadata (label, definition, broader) via: stav.label(NaturalPerson) etc.
Build = 'https://spdx.org/rdf/3.0.1/terms/Build/Build'
buildEndTime = 'https://spdx.org/rdf/3.0.1/terms/Build/buildEndTime'
buildId = 'https://spdx.org/rdf/3.0.1/terms/Build/buildId'
buildStartTime = 'https://spdx.org/rdf/3.0.1/terms/Build/buildStartTime'
buildType = 'https://spdx.org/rdf/3.0.1/terms/Build/buildType'
configSourceDigest = 'https://spdx.org/rdf/3.0.1/terms/Build/configSourceDigest'
configSourceEntrypoint = 'https://spdx.org/rdf/3.0.1/terms/Build/configSourceEntrypoint'
configSourceUri = 'https://spdx.org/rdf/3.0.1/terms/Build/configSourceUri'
environment = 'https://spdx.org/rdf/3.0.1/terms/Build/environment'
parameter = 'https://spdx.org/rdf/3.0.1/terms/Build/parameter'

# ── Metadata registry ──────────────────────────────────────────────────────────────
# Populated at import time so stav.label() / .definition() / .broader() work.
_register({
    'https://spdx.org/rdf/3.0.1/terms/Build/Build': {"label": 'Build', "definition": 'Class that describes a build instance of software/artifacts.', "broader": ('https://spdx.org/rdf/3.0.1/terms/Core/Element',), "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Build/buildEndTime': {"label": 'buildEndTime', "definition": 'Property that describes the time at which a build stops.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Build/buildId': {"label": 'buildId', "definition": 'A buildId is a locally unique identifier used by a builder to identify a unique instance of a build produced by it.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Build/buildStartTime': {"label": 'buildStartTime', "definition": 'Property describing the start time of a build.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Build/buildType': {"label": 'buildType', "definition": 'A buildType is a hint that is used to indicate the toolchain, platform, or infrastructure that the build was invoked on.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Build/configSourceDigest': {"label": 'configSourceDigest', "definition": 'Property that describes the digest of the build configuration file used to invoke a build.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Build/configSourceEntrypoint': {"label": 'configSourceEntrypoint', "definition": 'Property describes the invocation entrypoint of a build.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Build/configSourceUri': {"label": 'configSourceUri', "definition": 'Property that describes the URI of the build configuration source file.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Build/environment': {"label": 'environment', "definition": 'Property describing the session in which a build is invoked.', "source_vocab": 'SPDX-3.0.1'},
    'https://spdx.org/rdf/3.0.1/terms/Build/parameter': {"label": 'parameter', "definition": 'Property describing a parameter used in an instance of a build.', "source_vocab": 'SPDX-3.0.1'},
})

__all__ = ["Build", "buildEndTime", "buildId", "buildStartTime", "buildType", "configSourceDigest", "configSourceEntrypoint", "configSourceUri", "environment", "parameter"]
