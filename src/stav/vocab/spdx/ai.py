# SPDX-FileCopyrightText: 2026-present Arthit Suriyawongkul
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0
#
# AUTO-GENERATED — do not edit manually.
# Source: SPDX 3.0.1 AI profile
# Generated: 2026-04-30T08:42:26Z
# Regenerate: python -m stav.codegen.generate tools/recipes/spdx_ai.json

"""Vocabulary from SPDX 3.0.1 AI profile.

23 term constants (accessible as ``module.TermName``); grouped enums: :class:`SafetyRiskAssessmentType`, :class:`EnergyUnitType`."""

from __future__ import annotations

from stav._registry import _register
from stav.term import _StavVocabEnum

__stav_namespace__ = "vocab.spdx.ai"

# ── Individual term constants ─────────────────────────────────────────────────────
# Plain string IRIs — use directly with MLflow, Pitloom, SBOM serialisers.
# Metadata (label, definition, broader) via: stav.label(NaturalPerson) etc.
AIPackage = "https://spdx.org/rdf/3.0.1/terms/AI/AIPackage"
autonomyType = "https://spdx.org/rdf/3.0.1/terms/AI/autonomyType"
domain = "https://spdx.org/rdf/3.0.1/terms/AI/domain"
EnergyConsumption = "https://spdx.org/rdf/3.0.1/terms/AI/EnergyConsumption"
energyConsumption = "https://spdx.org/rdf/3.0.1/terms/AI/energyConsumption"
EnergyConsumptionDescription = "https://spdx.org/rdf/3.0.1/terms/AI/EnergyConsumptionDescription"
energyQuantity = "https://spdx.org/rdf/3.0.1/terms/AI/energyQuantity"
energyUnit = "https://spdx.org/rdf/3.0.1/terms/AI/energyUnit"
finetuningEnergyConsumption = "https://spdx.org/rdf/3.0.1/terms/AI/finetuningEnergyConsumption"
hyperparameter = "https://spdx.org/rdf/3.0.1/terms/AI/hyperparameter"
inferenceEnergyConsumption = "https://spdx.org/rdf/3.0.1/terms/AI/inferenceEnergyConsumption"
informationAboutApplication = "https://spdx.org/rdf/3.0.1/terms/AI/informationAboutApplication"
informationAboutTraining = "https://spdx.org/rdf/3.0.1/terms/AI/informationAboutTraining"
limitation = "https://spdx.org/rdf/3.0.1/terms/AI/limitation"
metric = "https://spdx.org/rdf/3.0.1/terms/AI/metric"
metricDecisionThreshold = "https://spdx.org/rdf/3.0.1/terms/AI/metricDecisionThreshold"
modelDataPreprocessing = "https://spdx.org/rdf/3.0.1/terms/AI/modelDataPreprocessing"
modelExplainability = "https://spdx.org/rdf/3.0.1/terms/AI/modelExplainability"
safetyRiskAssessment = "https://spdx.org/rdf/3.0.1/terms/AI/safetyRiskAssessment"
standardCompliance = "https://spdx.org/rdf/3.0.1/terms/AI/standardCompliance"
trainingEnergyConsumption = "https://spdx.org/rdf/3.0.1/terms/AI/trainingEnergyConsumption"
typeOfModel = "https://spdx.org/rdf/3.0.1/terms/AI/typeOfModel"
useSensitivePersonalInformation = "https://spdx.org/rdf/3.0.1/terms/AI/useSensitivePersonalInformation"


class SafetyRiskAssessmentType(_StavVocabEnum):
    """
    AI safety risk assessment levels from SPDX 3.0.1 AI profile (ai_safetyRiskAssessment
    field).
    """

    high = "https://spdx.org/rdf/3.0.1/terms/AI/SafetyRiskAssessmentType/high"
    low = "https://spdx.org/rdf/3.0.1/terms/AI/SafetyRiskAssessmentType/low"
    medium = "https://spdx.org/rdf/3.0.1/terms/AI/SafetyRiskAssessmentType/medium"
    serious = "https://spdx.org/rdf/3.0.1/terms/AI/SafetyRiskAssessmentType/serious"


class EnergyUnitType(_StavVocabEnum):
    """Energy measurement units from SPDX 3.0.1 AI profile (ai_energyUnit field)."""

    kilowattHour = "https://spdx.org/rdf/3.0.1/terms/AI/EnergyUnitType/kilowattHour"
    megajoule = "https://spdx.org/rdf/3.0.1/terms/AI/EnergyUnitType/megajoule"
    other = "https://spdx.org/rdf/3.0.1/terms/AI/EnergyUnitType/other"


# ── Metadata registry ──────────────────────────────────────────────────────────────
# Populated at import time so stav.label() / .definition() / .broader() work.
_register(
    {
        "https://spdx.org/rdf/3.0.1/terms/AI/AIPackage": {
            "label": "AIPackage",
            "definition": "Specifies an AI package and its associated information.",
            "broader": ("https://spdx.org/rdf/3.0.1/terms/Software/Package",),
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/AI/EnergyConsumption": {
            "label": "EnergyConsumption",
            "definition": "A class for describing the energy consumption incurred by an AI model in different stages of its lifecycle.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/AI/EnergyConsumptionDescription": {
            "label": "EnergyConsumptionDescription",
            "definition": "The class that helps note down the quantity of energy consumption and the unit used for measurement.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/AI/EnergyUnitType/kilowattHour": {
            "label": "kilowattHour",
            "definition": "Kilowatt-hour.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/AI/EnergyUnitType/megajoule": {
            "label": "megajoule",
            "definition": "Megajoule.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/AI/EnergyUnitType/other": {
            "label": "other",
            "definition": "Any other units of energy measurement.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/AI/SafetyRiskAssessmentType/high": {
            "label": "high",
            "definition": "The second-highest level of risk posed by an AI system.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/AI/SafetyRiskAssessmentType/low": {
            "label": "low",
            "definition": "Low/no risk is posed by an AI system.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/AI/SafetyRiskAssessmentType/medium": {
            "label": "medium",
            "definition": "The third-highest level of risk posed by an AI system.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/AI/SafetyRiskAssessmentType/serious": {
            "label": "serious",
            "definition": "The highest level of risk posed by an AI system.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/AI/autonomyType": {
            "label": "autonomyType",
            "definition": "Indicates whether the system can perform a decision or action without human involvement or guidance.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/AI/domain": {
            "label": "domain",
            "definition": "Captures the domain in which the AI package can be used.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/AI/energyConsumption": {
            "label": "energyConsumption",
            "definition": "Indicates the amount of energy consumption incurred by an AI model.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/AI/energyQuantity": {
            "label": "energyQuantity",
            "definition": "Represents the energy quantity.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/AI/energyUnit": {
            "label": "energyUnit",
            "definition": "Specifies the unit in which energy is measured.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/AI/finetuningEnergyConsumption": {
            "label": "finetuningEnergyConsumption",
            "definition": "Specifies the amount of energy consumed when finetuning the AI model that is being used in the AI system.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/AI/hyperparameter": {
            "label": "hyperparameter",
            "definition": "Records a hyperparameter used to build the AI model contained in the AI package.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/AI/inferenceEnergyConsumption": {
            "label": "inferenceEnergyConsumption",
            "definition": "Specifies the amount of energy consumed during inference time by an AI model that is being used in the AI system.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/AI/informationAboutApplication": {
            "label": "informationAboutApplication",
            "definition": "Provides relevant information about the AI software, not including the model description.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/AI/informationAboutTraining": {
            "label": "informationAboutTraining",
            "definition": "Describes relevant information about different steps of the training process.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/AI/limitation": {
            "label": "limitation",
            "definition": "Captures a limitation of the AI software.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/AI/metric": {
            "label": "metric",
            "definition": "Records the measurement of prediction quality of the AI model.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/AI/metricDecisionThreshold": {
            "label": "metricDecisionThreshold",
            "definition": "Captures the threshold that was used for computation of a metric described in the metric field.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/AI/modelDataPreprocessing": {
            "label": "modelDataPreprocessing",
            "definition": "Describes all the preprocessing steps applied to the training data before the model training.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/AI/modelExplainability": {
            "label": "modelExplainability",
            "definition": "Describes methods that can be used to explain the results from the AI model.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/AI/safetyRiskAssessment": {
            "label": "safetyRiskAssessment",
            "definition": "Records the results of general safety risk assessment of the AI system.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/AI/standardCompliance": {
            "label": "standardCompliance",
            "definition": "Captures a standard that is being complied with.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/AI/trainingEnergyConsumption": {
            "label": "trainingEnergyConsumption",
            "definition": "Specifies the amount of energy consumed when training the AI model that is being used in the AI system.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/AI/typeOfModel": {
            "label": "typeOfModel",
            "definition": "Records the type of the model used in the AI software.",
            "source_vocab": "SPDX-3.0.1",
        },
        "https://spdx.org/rdf/3.0.1/terms/AI/useSensitivePersonalInformation": {
            "label": "useSensitivePersonalInformation",
            "definition": "Records if sensitive personal information is used during model training or could be used during the inference.",
            "source_vocab": "SPDX-3.0.1",
        },
    }
)

__all__ = [
    "AIPackage",
    "EnergyConsumption",
    "EnergyConsumptionDescription",
    "EnergyUnitType",
    "SafetyRiskAssessmentType",
    "autonomyType",
    "domain",
    "energyConsumption",
    "energyQuantity",
    "energyUnit",
    "finetuningEnergyConsumption",
    "hyperparameter",
    "inferenceEnergyConsumption",
    "informationAboutApplication",
    "informationAboutTraining",
    "limitation",
    "metric",
    "metricDecisionThreshold",
    "modelDataPreprocessing",
    "modelExplainability",
    "safetyRiskAssessment",
    "standardCompliance",
    "trainingEnergyConsumption",
    "typeOfModel",
    "useSensitivePersonalInformation",
]
