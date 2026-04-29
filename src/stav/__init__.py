# SPDX-FileCopyrightText: 2023-present Arthit Suriyawongkul
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""System Trustworthiness and Accountability Vocabulary (STAV).

Vocabulary terms live under :mod:`stav.vocab`::

    from stav.vocab import dpv, eu, spdx
    from stav import label, definition, broader, datatype, validate

    dpv.NaturalPerson                            # "https://w3id.org/dpv#NaturalPerson"
    dpv.ai.AITechnique.SupervisedLearning        # IRI string
    eu.aia.AIProvider                            # "https://w3id.org/stav#AIProvider"
    spdx.dataset.DatasetType.text                # enum member

    label(dpv.NaturalPerson)                     # "Natural Person"
    definition(dpv.NaturalPerson)                # "A human ..."
    broader(dpv.NaturalPerson)                   # ("https://w3id.org/dpv#Entity",)
    validate(dpv.NaturalPerson, "foo")           # True  (str expected for xsd:anyURI)
    validate(dpv.NaturalPerson, 5)               # False
"""

from stav._registry import broader, datatype, definition, label, source_vocab, validate

__all__ = [
    "broader",
    "datatype",
    "definition",
    "label",
    "source_vocab",
    "validate",
]
