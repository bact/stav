# SPDX-FileCopyrightText: 2023 Arthit Suriyawongkul <suriyawa@tcd.ie>
# SPDX-License-Identifier: Apache-2.0

__stav_namespace__ = ""

from stav.eu.aia import LogRecord, TechnicalDocumentation

# Obligations
INFORMATION_CREATION_OBLIGATION = "InformationCreationObligation"
INFORMATION_SUBMISSION_OBLIGATION = "InformationSubmissionObligation"
QUALITY_MANAGEMENT_SYSTEM_DOCUMENTATION_OBLIGATION = "QualityManagementSystemDocumentationObligation"
REGISTERATION_OBLIGATION = "RegisterationObligation"
TECHNICAL_DOCUMENTATION_OBLIGATION = "TechnicalDocumentationObligation"

# System information
INSTRUCTIONS_FOR_USE = "InstructionsForUse"
INSTRUCTIONS_INSTALLATION = "InstallationInstructions"
INTENDED_PURPOSES = "IntendedPurposes"
SYSTEM_GENERAL_DESCRIPTION = "SystemGeneralDescription"

# Stakeholders
AI_PROVIDER = "AIProvider"
AI_DEPLOYER = "AIDeployer"
MARKET_SURVEILLENCE_AUTHORITY = "MarketSurveillenceAuthority"

# Documentation
PREVIOUSLY_EXISTING_PROCESS_DOCUMENTATION = "PreviouslyExistingProcessDocumentation"
PREVIOUSLY_EXISTING_PROCESS_EVALUATION_DOCUMENTATION = "PreviouslyExistingProcessEvaluationDocumentation"
PREVIOUSLY_EXISTING_PROCESS_KNOWN_NEGATIVE_IMPACT_INFORMATION = (
    "PreviouslyExistingProcessKnownNegativeImpactInformation"
)
INTENDED_BENEFITS_OVER_PREVIOUSLY_EXISTING_PROCESS = "IntendedBenefitsOverPreviouslyExistingProcess"
CURRENT_AND_POTENTIAL_FUTURE_IMPACTS = "CurrentAndPotentialFutureImpacts"
TECHNICAL_DOCUMENTATION = "TechnicalDocumentation"
PRIVACY_RISKS_AND_PRIVACY_MEASURES_EVALUATION_DOCUMENTATION = "PrivacyRisksAndPrivacyMeasuresEvaluationDocumentation"
SYSTEM_EVALUATION_DOCUMENTATION = "SystemEvaluationDocumentation"
CONSUMER_RIGHTS_EVALUATION_INFORMATION = "ConsumerRightsEvaluationInformation"
IMPACT_ASSESSMENT_DOCUMENTATION = "ImpactAssessmentDocumentation"
BASELINE_PROCESS_DESCRIPTION = "BaselineProcessDescription"
DATA_MINIMIZATION_PRACTICES = "DataMinimizationPractices"

# Actions / Verbs
MAKING_AVAILABLE_ON_THE_MARKET = "MakingAvailableOnTheMarket"
PLACING_ON_THE_MARKET = "PlacingOnTheMarket"
PUTTING_INTO_SERVICE = "PuttingIntoService"

# Measures
INFORMATION_SECURITY_MEASURES = "InformationSecurityMeasures"

# Metrics
METRICS_ACCURACY = "MetricsAccuracy"
METRICS_PRECISION = "MetricsPrecision"
METRICS_RECALL = "MetricsRecall"
METRICS_F1 = "MetricsF1"
METRICS_R2 = "MetricsR2"
METRICS_RMSE = "MetricsRMSE"
METRICS_MAE = "MetricsMAE"
METRICS_ENERGY = "MetricsEnergy"

LOG = "Log"
DATASET_SIZE = "DatasetSize"

# SPDX AI Profile
AUTONOMY_TYPE = "AutonomyType"
DOMAIN = "Domain"
ENERGY_CONSUMPTION = "EnergyConsumption"
ENERGY_CONSUMPTION_FINE_TUNING = "FineTuningEnergyConsumption"
ENERGY_CONSUMPTION_INFERENCE = "InferenceEnergyConsumption"
ENERGY_CONSUMPTION_TRAINING = "TrainingEnergyConsumption"
ENERGY_UNIT = "EnergyUnit"
HYPERPARAMETER = "Hyperparameter"
INFO_APP = "InformationAboutApplication"
INFO_TRAINING = "InformationAboutTraining"
LIMITATION = "Limitation"
METRIC = "Metric"
METRIC_DECISION_THRESHOLD = "MetricDecisionThreshold"
MODEL_DATA_PROCESSING = "ModelDataPreprocessing"
MODEL_EXPLAINABILITY = "ModelExplainability"
SAFETY_RISK_ASSESSMENT = "SafetyRiskAssessment"
STANDARD_COMPLIANCE = "StandardCompliance"
MODEL_TYPE = "TypeOfModel"
USE_SENSITIVE_PERSONAL_INFO = "UseSensitivePersonalInformation"

__all__ = [
    "LogRecord",
    "TechnicalDocumentation",
    "AI_PROVIDER",
    "AI_DEPLOYER",
    "PREVIOUSLY_EXISTING_PROCESS_EVALUATION_DOCUMENTATION",
    "TECHNICAL_DOCUMENTATION_OBLIGATION",
    "BASELINE_PROCESS_DESCRIPTION",
    "INSTRUCTIONS_FOR_USE",
    "MAKING_AVAILABLE_ON_THE_MARKET",
    "MARKET_SURVEILLENCE_AUTHORITY",
    "SYSTEM_GENERAL_DESCRIPTION",
    "CURRENT_AND_POTENTIAL_FUTURE_IMPACTS",
    "TECHNICAL_DOCUMENTATION",
    "QUALITY_MANAGEMENT_SYSTEM_DOCUMENTATION_OBLIGATION",
    "PUTTING_INTO_SERVICE",
    "INTENDED_PURPOSES",
    "DATA_MINIMIZATION_PRACTICES",
    "PRIVACY_RISKS_AND_PRIVACY_MEASURES_EVALUATION_DOCUMENTATION",
    "PLACING_ON_THE_MARKET",
    "INSTALLATION_INSTRUCTIONS",
    "SYSTEM_EVALUATION_DOCUMENTATION",
    "PREVIOUSLY_EXISTING_PROCESS_KNOWN_NEGATIVE_IMPACT_INFORMATION",
    "PREVIOUSLY_EXISTING_PROCESS_DOCUMENTATION",
    "CONSUMER_RIGHTS_EVALUATION_INFORMATION",
    "INFORMATION_CREATION_OBLIGATION",
    "IMPACT_ASSESSMENT_DOCUMENTATION",
    "INTENDED_BENEFITS_OVER_PREVIOUSLY_EXISTING_PROCESS",
    "INFORMATION_SUBMISSION_OBLIGATION",
    "LOG",
    "INFORMATION_SECURITY_MEASURES",
    "REGISTERATION_OBLIGATION",
    "stav.eu.aia.TechnicalDocumentation",
    "stav.eu.aia.LogRecord",
    "METRICS_RECALL",
    "METRICS_PRECISION",
    "METRICS_F1",
    "METRICS_R2",
    "METRICS_RMSE",
    "METRICS_MAE",
    "METRICS_ENERGY",
    "METRICS_ACCURACY",
    "DATASET_SIZE",
    "AUTONOMY_TYPE",
    "DOMAIN",
    "ENERGY_CONSUMPTION",
    "ENERGY_CONSUMPTION_FINE_TUNING",
    "ENERGY_CONSUMPTION_INFERENCE",
    "ENERGY_CONSUMPTION_TRAINING",
    "ENERGY_UNIT",
    "HYPERPARAMETER",
    "INFO_APP",
    "INFO_TRAINING",
    "LIMITATION",
    "METRIC",
    "METRIC_DECISION_THRESHOLD",
    "MODEL_DATA_PROCESSING",
    "MODEL_EXPLAINABILITY",
    "SAFETY_RISK_ASSESSMENT",
    "STANDARD_COMPLIANCE",
    "MODEL_TYPE",
    "USE_SENSITIVE_PERSONAL_INFO",
]
