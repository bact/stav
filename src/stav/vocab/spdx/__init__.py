# SPDX-FileCopyrightText: 2026-present Arthit Suriyawongkul
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""STAV vocabulary namespace: vocab.spdx (SPDX 3.0 profiles).

Submodules map to SPDX AI and Dataset profiles::

    from stav.vocab import spdx
    spdx.dataset.DatasetType.text
    spdx.ai.SafetyRiskLevel.High
"""

from __future__ import annotations

__stav_namespace__ = "vocab.spdx"


def __getattr__(name: str):
    import importlib

    _submodules = {"ai", "dataset"}
    if name in _submodules:
        mod = importlib.import_module(f"{__name__}.{name}")
        globals()[name] = mod
        return mod
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
