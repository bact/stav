# SPDX-FileCopyrightText: 2026-present Arthit Suriyawongkul
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""STAV vocabulary root namespace.

All controlled vocabulary terms live under this namespace::

    from stav.vocab import dpv, eu, spdx
    from stav import label, validate

    dpv.NaturalPerson                       # "https://w3id.org/dpv#NaturalPerson"
    dpv.ai.AITechnique.SupervisedLearning   # IRI string, usable in MLflow / Pitloom

    label(dpv.NaturalPerson)               # "Natural Person"
    validate(dpv.NaturalPerson, "foo")     # True
"""

from __future__ import annotations

__stav_namespace__ = "vocab"


def __getattr__(name: str):
    import importlib

    _submodules = {"dpv", "eu", "spdx"}
    if name in _submodules:
        mod = importlib.import_module(f"{__name__}.{name}")
        globals()[name] = mod
        return mod
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
