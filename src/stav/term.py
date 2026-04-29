# SPDX-FileCopyrightText: 2026-present Arthit Suriyawongkul
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""Vocabulary enum base class for STAV generated vocab modules."""

from __future__ import annotations

from enum import Enum


class _StavVocabEnum(str, Enum):
    """Base for STAV vocabulary enums.

    Values are plain IRI strings pointing to the source standard.  As a
    ``str`` subclass each member IS a string — use it anywhere a plain string
    is accepted (MLflow tags, Pitloom setter arguments, f-strings, SBOM
    serialisation, equality checks).

    To access ontology metadata for an enum member, use the registry
    utility functions::

        from stav import label, definition, broader, validate
        from stav.vocab.dpv import ai

        label(ai.AITechnique.SupervisedLearning)
        # "Supervised Learning"

        validate(ai.AITechnique.SupervisedLearning, "some value")
        # True
    """

    def __str__(self) -> str:
        return self.value

    def __format__(self, fmt: str) -> str:
        return format(self.value, fmt) if fmt else self.value

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}.{self.name}"
