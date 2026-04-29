# SPDX-FileCopyrightText: 2026-present Arthit Suriyawongkul
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""STAV vocabulary namespace: vocab.dpv (W3C Data Privacy Vocabulary).

DPV core term constants are available directly on this module::

    from stav.vocab import dpv
    dpv.NaturalPerson       # "https://w3id.org/dpv#NaturalPerson"
    dpv.DataController      # "https://w3id.org/dpv#DataController"

The ``ai`` submodule contains the DPV AI Extension::

    dpv.ai.AITechnique.SupervisedLearning
    dpv.ai.ComputerVision
"""

from __future__ import annotations

__stav_namespace__ = "vocab.dpv"

try:
    from stav.vocab.dpv._core import *  # noqa: F403
except ImportError:
    pass  # _core.py not generated yet


def __getattr__(name: str):
    import importlib

    _submodules = {"ai"}
    if name in _submodules:
        mod = importlib.import_module(f"{__name__}.{name}")
        globals()[name] = mod
        return mod
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
