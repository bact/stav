# SPDX-FileCopyrightText: 2026-present Arthit Suriyawongkul
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0
#
# AUTO-GENERATED — do not edit manually.
# Source: SPDX 3.0.1 Dataset profile
# Generated: 2026-04-30T08:42:28Z
# Regenerate: python -m stav.codegen.generate tools/recipes/spdx_dataset.json

"""Vocabulary from SPDX 3.0.1 Dataset profile.

14 term constants (accessible as ``module.TermName``); grouped enums: :class:`DatasetType`, :class:`ConfidentialityLevelType`, :class:`DatasetAvailabilityType`."""

from __future__ import annotations

from stav._registry import _register
from stav.term import _StavVocabEnum

__stav_namespace__ = "vocab.spdx.dataset"

# ── Individual term constants ─────────────────────────────────────────────────────
# Plain string IRIs — use directly with MLflow, Pitloom, SBOM serialisers.
# Metadata (label, definition, broader) via: stav.label(NaturalPerson) etc.
anonymizationMethodUsed = "https://spdx.org/rdf/3.0.1/terms/Dataset/anonymizationMethodUsed"
confidentialityLevel = "https://spdx.org/rdf/3.0.1/terms/Dataset/confidentialityLevel"
dataCollectionProcess = "https://spdx.org/rdf/3.0.1/terms/Dataset/dataCollectionProcess"
dataPreprocessing = "https://spdx.org/rdf/3.0.1/terms/Dataset/dataPreprocessing"
datasetAvailability = "https://spdx.org/rdf/3.0.1/terms/Dataset/datasetAvailability"
datasetNoise = "https://spdx.org/rdf/3.0.1/terms/Dataset/datasetNoise"
DatasetPackage = "https://spdx.org/rdf/3.0.1/terms/Dataset/DatasetPackage"
datasetSize = "https://spdx.org/rdf/3.0.1/terms/Dataset/datasetSize"
datasetType = "https://spdx.org/rdf/3.0.1/terms/Dataset/datasetType"
datasetUpdateMechanism = "https://spdx.org/rdf/3.0.1/terms/Dataset/datasetUpdateMechanism"
hasSensitivePersonalInformation = "https://spdx.org/rdf/3.0.1/terms/Dataset/hasSensitivePersonalInformation"
intendedUse = "https://spdx.org/rdf/3.0.1/terms/Dataset/intendedUse"
knownBias = "https://spdx.org/rdf/3.0.1/terms/Dataset/knownBias"
sensor = "https://spdx.org/rdf/3.0.1/terms/Dataset/sensor"


class DatasetType(_StavVocabEnum):
    """Dataset content types from SPDX 3.0.1 Dataset profile (dataset_datasetType field)."""

    audio = "https://spdx.org/rdf/3.0.1/terms/Dataset/DatasetType/audio"
    categorical = "https://spdx.org/rdf/3.0.1/terms/Dataset/DatasetType/categorical"
    graph = "https://spdx.org/rdf/3.0.1/terms/Dataset/DatasetType/graph"
    image = "https://spdx.org/rdf/3.0.1/terms/Dataset/DatasetType/image"
    noAssertion = "https://spdx.org/rdf/3.0.1/terms/Dataset/DatasetType/noAssertion"
    numeric = "https://spdx.org/rdf/3.0.1/terms/Dataset/DatasetType/numeric"
    other = "https://spdx.org/rdf/3.0.1/terms/Dataset/DatasetType/other"
    sensor = "https://spdx.org/rdf/3.0.1/terms/Dataset/DatasetType/sensor"
    structured = "https://spdx.org/rdf/3.0.1/terms/Dataset/DatasetType/structured"
    syntactic = "https://spdx.org/rdf/3.0.1/terms/Dataset/DatasetType/syntactic"
    text = "https://spdx.org/rdf/3.0.1/terms/Dataset/DatasetType/text"
    timeseries = "https://spdx.org/rdf/3.0.1/terms/Dataset/DatasetType/timeseries"
    timestamp = "https://spdx.org/rdf/3.0.1/terms/Dataset/DatasetType/timestamp"
    video = "https://spdx.org/rdf/3.0.1/terms/Dataset/DatasetType/video"


class ConfidentialityLevelType(_StavVocabEnum):
    """Dataset confidentiality levels from SPDX 3.0.1 Dataset profile (traffic-light protocol)."""

    amber = "https://spdx.org/rdf/3.0.1/terms/Dataset/ConfidentialityLevelType/amber"
    clear = "https://spdx.org/rdf/3.0.1/terms/Dataset/ConfidentialityLevelType/clear"
    green = "https://spdx.org/rdf/3.0.1/terms/Dataset/ConfidentialityLevelType/green"
    red = "https://spdx.org/rdf/3.0.1/terms/Dataset/ConfidentialityLevelType/red"


class DatasetAvailabilityType(_StavVocabEnum):
    """Dataset availability / access methods from SPDX 3.0.1 Dataset profile."""

    clickthrough = "https://spdx.org/rdf/3.0.1/terms/Dataset/DatasetAvailabilityType/clickthrough"
    directDownload = "https://spdx.org/rdf/3.0.1/terms/Dataset/DatasetAvailabilityType/directDownload"
    query = "https://spdx.org/rdf/3.0.1/terms/Dataset/DatasetAvailabilityType/query"
    registration = "https://spdx.org/rdf/3.0.1/terms/Dataset/DatasetAvailabilityType/registration"
    scrapingScript = "https://spdx.org/rdf/3.0.1/terms/Dataset/DatasetAvailabilityType/scrapingScript"


# ── Metadata registry ──────────────────────────────────────────────────────────────
# Populated at import time so stav.label() / .definition() / .broader() work.
_register(
    {
        "https://spdx.org/rdf/3.0.1/terms/Dataset/ConfidentialityLevelType/amber": {
            "label": "amber",
            "definition": "Data points in the dataset can be shared only with specific organizations and their clients on a need to know basis.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Dataset/ConfidentialityLevelType/clear": {
            "label": "clear",
            "definition": "Dataset may be distributed freely, without restriction.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Dataset/ConfidentialityLevelType/green": {
            "label": "green",
            "definition": "Dataset can be shared within a community of peers and partners.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Dataset/ConfidentialityLevelType/red": {
            "label": "red",
            "definition": "Data points in the dataset are highly confidential and can only be shared with named recipients.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Dataset/DatasetAvailabilityType/clickthrough": {
            "label": "clickthrough",
            "definition": "the dataset is not publicly available and can only be accessed after affirmatively accepting terms on a clickthrough webpage.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Dataset/DatasetAvailabilityType/directDownload": {
            "label": "directDownload",
            "definition": "the dataset is publicly available and can be downloaded directly.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Dataset/DatasetAvailabilityType/query": {
            "label": "query",
            "definition": "the dataset is publicly available, but not all at once, and can only be accessed through queries which return parts of the dataset.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Dataset/DatasetAvailabilityType/registration": {
            "label": "registration",
            "definition": "the dataset is not publicly available and an email registration is required before accessing the dataset, although without an affirmative acceptance of terms.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Dataset/DatasetAvailabilityType/scrapingScript": {
            "label": "scrapingScript",
            "definition": "the dataset provider is not making available the underlying data and the dataset must be reassembled, typically using the provided script for scraping the data.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Dataset/DatasetPackage": {
            "label": "DatasetPackage",
            "definition": "Specifies a data package and its associated information.",
            "broader": ("https://spdx.org/rdf/3.0.1/terms/Software/Package",),
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Dataset/DatasetType/audio": {
            "label": "audio",
            "definition": "data is audio based, such as a collection of music from the 80s.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Dataset/DatasetType/categorical": {
            "label": "categorical",
            "definition": "data that is classified into a discrete number of categories, such as the eye color of a population of people.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Dataset/DatasetType/graph": {
            "label": "graph",
            "definition": "data is in the form of a graph where entries are somehow related to each other through edges, such a social network of friends.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Dataset/DatasetType/image": {
            "label": "image",
            "definition": "data is a collection of images such as pictures of animals.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Dataset/DatasetType/noAssertion": {
            "label": "noAssertion",
            "definition": "data type is not known.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Dataset/DatasetType/numeric": {
            "label": "numeric",
            "definition": "data consists only of numeric entries.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Dataset/DatasetType/other": {
            "label": "other",
            "definition": "data is of a type not included in this list.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Dataset/DatasetType/sensor": {
            "label": "sensor",
            "definition": "data is recorded from a physical sensor, such as a thermometer reading or biometric device.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Dataset/DatasetType/structured": {
            "label": "structured",
            "definition": "data is stored in tabular format or retrieved from a relational database.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Dataset/DatasetType/syntactic": {
            "label": "syntactic",
            "definition": "data describes the syntax or semantics of a language or text, such as a parse tree used for natural language processing.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Dataset/DatasetType/text": {
            "label": "text",
            "definition": "data consists of unstructured text, such as a book, Wikipedia article (without images), or transcript.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Dataset/DatasetType/timeseries": {
            "label": "timeseries",
            "definition": "data is recorded in an ordered sequence of timestamped entries, such as the price of a stock over the course of a day.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Dataset/DatasetType/timestamp": {
            "label": "timestamp",
            "definition": "data is recorded with a timestamp for each entry, but not necessarily ordered or at specific intervals, such as when a taxi ride starts and ends.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Dataset/DatasetType/video": {
            "label": "video",
            "definition": "data is video based, such as a collection of movie clips featuring Tom Hanks.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Dataset/anonymizationMethodUsed": {
            "label": "anonymizationMethodUsed",
            "definition": "Describes the anonymization methods used.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Dataset/confidentialityLevel": {
            "label": "confidentialityLevel",
            "definition": "Describes the confidentiality level of the data points contained in the dataset.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Dataset/dataCollectionProcess": {
            "label": "dataCollectionProcess",
            "definition": "Describes how the dataset was collected.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Dataset/dataPreprocessing": {
            "label": "dataPreprocessing",
            "definition": "Describes the preprocessing steps that were applied to the raw data to create the given dataset.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Dataset/datasetAvailability": {
            "label": "datasetAvailability",
            "definition": "The field describes the availability of a dataset.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Dataset/datasetNoise": {
            "label": "datasetNoise",
            "definition": "Describes potentially noisy elements of the dataset.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Dataset/datasetSize": {
            "label": "datasetSize",
            "definition": "Captures the size of the dataset.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Dataset/datasetType": {
            "label": "datasetType",
            "definition": "Describes the type of the given dataset.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Dataset/datasetUpdateMechanism": {
            "label": "datasetUpdateMechanism",
            "definition": "Describes a mechanism to update the dataset.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Dataset/hasSensitivePersonalInformation": {
            "label": "hasSensitivePersonalInformation",
            "definition": "Describes if any sensitive personal information is present in the dataset.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Dataset/intendedUse": {
            "label": "intendedUse",
            "definition": "Describes what the given dataset should be used for.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Dataset/knownBias": {
            "label": "knownBias",
            "definition": "Records the biases that the dataset is known to encompass.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/Dataset/sensor": {
            "label": "sensor",
            "definition": "Describes a sensor used for collecting the data.",
            "source_vocab": "SPDX-3.0.1",
        },
    }
)

__all__ = [
    "ConfidentialityLevelType",
    "DatasetAvailabilityType",
    "DatasetPackage",
    "DatasetType",
    "anonymizationMethodUsed",
    "confidentialityLevel",
    "dataCollectionProcess",
    "dataPreprocessing",
    "datasetAvailability",
    "datasetNoise",
    "datasetSize",
    "datasetType",
    "datasetUpdateMechanism",
    "hasSensitivePersonalInformation",
    "intendedUse",
    "knownBias",
    "sensor",
]
