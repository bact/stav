# SPDX-FileCopyrightText: 2026-present Arthit Suriyawongkul
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""STAV vocabulary namespace: vocab.eu (European Union legislation).

Submodules map to specific EU instruments::

    from stav.vocab import eu
    eu.aia.AIProvider              # EU AI Act (AIA) term
    eu.aia.AIRole.AIDeployer       # enum member
"""

from __future__ import annotations

__stav_namespace__ = "vocab.eu"


def __getattr__(name: str):
    import importlib

    _submodules = {"aia", "cra"}
    if name in _submodules:
        mod = importlib.import_module(f"{__name__}.{name}")
        globals()[name] = mod
        return mod
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
