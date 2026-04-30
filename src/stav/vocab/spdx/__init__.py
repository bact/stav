# SPDX-FileCopyrightText: 2026-present Arthit Suriyawongkul
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""STAV vocabulary namespace: vocab.spdx (SPDX 3.0.1 profiles).

Each submodule maps to one SPDX profile::

    from stav.vocab import spdx

    spdx.core.RelationshipType.describes
    spdx.ai.AIPackage
    spdx.ai.SafetyRiskAssessmentType.medium
    spdx.dataset.DatasetType.text
    spdx.software.SoftwarePurpose.model
    spdx.security.CvssSeverityType.high
    spdx.build.Build
    spdx.expanded_licensing.License
    spdx.simple_licensing.LicenseExpression
    spdx.extension.Extension
"""

from __future__ import annotations

__stav_namespace__ = "vocab.spdx"

_SUBMODULES = {
    "ai",
    "build",
    "core",
    "dataset",
    "expanded_licensing",
    "extension",
    "security",
    "simple_licensing",
    "software",
}


def __getattr__(name: str):
    import importlib

    if name in _SUBMODULES:
        mod = importlib.import_module(f"{__name__}.{name}")
        globals()[name] = mod
        return mod
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
