# SPDX-FileCopyrightText: 2026-present Arthit Suriyawongkul
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0
#
# AUTO-GENERATED — do not edit manually.
# Source: W3C Data Privacy Vocabulary (DPV) AI Extension v2.3
# Generated: 2026-04-29T22:30:22Z
# Regenerate: python -m stav.codegen.generate tools/recipes/dpv_ai.json

"""Vocabulary from W3C Data Privacy Vocabulary (DPV) AI Extension v2.3.

241 term constants (accessible as ``module.TermName``); grouped enums: :class:`AITechnique`, :class:`AICapability`, :class:`AILifecycleStage`, :class:`AISystemType`."""

from __future__ import annotations

from stav._registry import _register
from stav.term import _StavVocabEnum

__stav_namespace__ = "vocab.dpv.ai"

# ── Individual term constants ─────────────────────────────────────────────────────
# Plain string IRIs — use directly with MLflow, Pitloom, SBOM serialisers.
# Metadata (label, definition, broader) via: stav.label(NaturalPerson) etc.
ActionRecognition = "https://w3id.org/dpv/ai#ActionRecognition"  # Action Recognition
AdversarialAttack = "https://w3id.org/dpv/ai#AdversarialAttack"  # Adversarial Attack
AGI = "https://w3id.org/dpv/ai#AGI"  # Artificial General Intelligence (AGI)
AI = "https://w3id.org/dpv/ai#AI"  # Artificial Intelligence (AI)
AIAgent = "https://w3id.org/dpv/ai#AIAgent"  # AI Agent
AIBias = "https://w3id.org/dpv/ai#AIBias"  # AI Bias
AIProcess = "https://w3id.org/dpv/ai#AIProcess"  # AI Process
AISystem = "https://w3id.org/dpv/ai#AISystem"  # AI System
AISystemRisk = "https://w3id.org/dpv/ai#AISystemRisk"  # AI System Risk
AlgorithmSelectionBias = "https://w3id.org/dpv/ai#AlgorithmSelectionBias"  # Algorithm Selection Bias
AudioCapability = "https://w3id.org/dpv/ai#AudioCapability"  # Audio Capability
AudioGeneration = "https://w3id.org/dpv/ai#AudioGeneration"  # Audio Generation
AudioProcessing = "https://w3id.org/dpv/ai#AudioProcessing"  # Audio Processing
AutomaticSummarisation = "https://w3id.org/dpv/ai#AutomaticSummarisation"  # Automatic Summarisation
AutomationBias = "https://w3id.org/dpv/ai#AutomationBias"  # Automation Bias
BayesianEstimation = "https://w3id.org/dpv/ai#BayesianEstimation"  # Bayesian Estimation
BayesianNetwork = "https://w3id.org/dpv/ai#BayesianNetwork"  # Bayesian Network
BayesianOptimisation = "https://w3id.org/dpv/ai#BayesianOptimisation"  # Bayesian Optimisation
BehaviourAnalysis = "https://w3id.org/dpv/ai#BehaviourAnalysis"  # Behaviour Analysis
Benchmarking = "https://w3id.org/dpv/ai#Benchmarking"
BiasAssessment = "https://w3id.org/dpv/ai#BiasAssessment"  # Bias Assessment
BiasDetection = "https://w3id.org/dpv/ai#BiasDetection"  # Bias Detection
BiasMitigation = "https://w3id.org/dpv/ai#BiasMitigation"  # Bias Mitigation
BiasPrevention = "https://w3id.org/dpv/ai#BiasPrevention"  # Bias Prevention
BiometricCapability = "https://w3id.org/dpv/ai#BiometricCapability"  # Biometric Capability
BiometricCategorisation = "https://w3id.org/dpv/ai#BiometricCategorisation"  # Biometric Categorisation
BiometricEmotionRecognition = "https://w3id.org/dpv/ai#BiometricEmotionRecognition"  # Biometric Emotion Recognition
BiometricIdentification = "https://w3id.org/dpv/ai#BiometricIdentification"  # Biometric Identification
Capability = "https://w3id.org/dpv/ai#Capability"
ChatbotCapability = "https://w3id.org/dpv/ai#ChatbotCapability"  # Chatbot Capability
CognitiveComputing = "https://w3id.org/dpv/ai#CognitiveComputing"  # Cognitive Computing
ComputationalCreativity = "https://w3id.org/dpv/ai#ComputationalCreativity"  # Computational Creativity
ComputerVision = "https://w3id.org/dpv/ai#ComputerVision"  # Computer Vision
ContentBasedRetrieval = "https://w3id.org/dpv/ai#ContentBasedRetrieval"  # Content-based Retrieval
ContentGeneration = "https://w3id.org/dpv/ai#ContentGeneration"  # Content Generation
ContextAwareRetrieval = "https://w3id.org/dpv/ai#ContextAwareRetrieval"  # Context-aware Retrieval
ContinuousValidationStage = "https://w3id.org/dpv/ai#ContinuousValidationStage"  # Continuous Validation Stage
ConvolutionalNeuralNetwork = "https://w3id.org/dpv/ai#ConvolutionalNeuralNetwork"  # Convolutional Neural Network (CNN)
CyberphysicalSystem = "https://w3id.org/dpv/ai#CyberphysicalSystem"  # Cyber-physical System
Data = "https://w3id.org/dpv/ai#Data"  # AI Data
DataAggregation = "https://w3id.org/dpv/ai#DataAggregation"  # Data Aggregation
DataAggregationBias = "https://w3id.org/dpv/ai#DataAggregationBias"  # Data Aggregation Bias
DataAnnotation = "https://w3id.org/dpv/ai#DataAnnotation"  # Data Annotation
DataBias = "https://w3id.org/dpv/ai#DataBias"  # Data Bias
DataCleaning = "https://w3id.org/dpv/ai#DataCleaning"  # Data Cleaning
DataCollection = "https://w3id.org/dpv/ai#DataCollection"  # Data Collection
DataEnrichment = "https://w3id.org/dpv/ai#DataEnrichment"  # Data Enrichment
DataLabelling = "https://w3id.org/dpv/ai#DataLabelling"  # Data Labelling
DataLabellingProcessBias = "https://w3id.org/dpv/ai#DataLabellingProcessBias"  # Data Labelling Process Bias
DataOperation = "https://w3id.org/dpv/ai#DataOperation"
DataPoisoning = "https://w3id.org/dpv/ai#DataPoisoning"  # Data Poisoning
DataPreparation = "https://w3id.org/dpv/ai#DataPreparation"  # Data Preparation
DataRisk = "https://w3id.org/dpv/ai#DataRisk"  # Data Risk
DataUpdating = "https://w3id.org/dpv/ai#DataUpdating"  # Data Updating
DecisionTree = "https://w3id.org/dpv/ai#DecisionTree"  # Decision Tree
DecommissionStage = "https://w3id.org/dpv/ai#DecommissionStage"  # Decommission Stage
DeepLearning = "https://w3id.org/dpv/ai#DeepLearning"  # Deep Learning
DeploymentStage = "https://w3id.org/dpv/ai#DeploymentStage"  # Deployment Stage
DesignStage = "https://w3id.org/dpv/ai#DesignStage"  # Design Stage
DevelopmentStage = "https://w3id.org/dpv/ai#DevelopmentStage"  # Development Stage
DialogueManagement = "https://w3id.org/dpv/ai#DialogueManagement"  # Dialogue Management
DiscardStage = "https://w3id.org/dpv/ai#DiscardStage"  # Discard Stage
DistributedTrainingBias = "https://w3id.org/dpv/ai#DistributedTrainingBias"  # Distributed Training Bias
EdgeAI = "https://w3id.org/dpv/ai#EdgeAI"  # Edge AI
EmotionRecognition = "https://w3id.org/dpv/ai#EmotionRecognition"  # Emotion Recognition
EngineeringDecisionBias = "https://w3id.org/dpv/ai#EngineeringDecisionBias"  # Engineering Decision Bias
ExpertSystem = "https://w3id.org/dpv/ai#ExpertSystem"  # Expert System
ExplainabilityRisk = "https://w3id.org/dpv/ai#ExplainabilityRisk"  # Explainability Risk
FaceRecognition = "https://w3id.org/dpv/ai#FaceRecognition"  # Face Recognition
FeatureEngineeringBias = "https://w3id.org/dpv/ai#FeatureEngineeringBias"  # Feature Engineering Bias
FeedForwardNeuralNetwork = "https://w3id.org/dpv/ai#FeedForwardNeuralNetwork"  # Feed Forward Neural Network
FineTunedModel = "https://w3id.org/dpv/ai#FineTunedModel"  # Fine-tuned Model
FrugalAISystem = "https://w3id.org/dpv/ai#FrugalAISystem"  # Frugal AI System
FrugalMachineLearning = "https://w3id.org/dpv/ai#FrugalMachineLearning"  # Frugal Machine Learning
GenAI = "https://w3id.org/dpv/ai#GenAI"  # Generative AI
GeneticAlgorithm = "https://w3id.org/dpv/ai#GeneticAlgorithm"  # Genetic Algorithm
GestureRecognition = "https://w3id.org/dpv/ai#GestureRecognition"  # Gesture Recognition
GPAI = "https://w3id.org/dpv/ai#GPAI"  # General-Purpose AI System (GPAI)
GPAIModel = "https://w3id.org/dpv/ai#GPAIModel"  # General Purpose AI Model
hasAI = "https://w3id.org/dpv/ai#hasAI"  # has AI
hasAISystem = "https://w3id.org/dpv/ai#hasAISystem"  # has AI system
hasCapability = "https://w3id.org/dpv/ai#hasCapability"  # has capability
hasData = "https://w3id.org/dpv/ai#hasData"  # has data
hasGPAIModel = "https://w3id.org/dpv/ai#hasGPAIModel"  # has GPAI model
hasModel = "https://w3id.org/dpv/ai#hasModel"  # has model
hasTechnique = "https://w3id.org/dpv/ai#hasTechnique"  # has technique
hasTestingData = "https://w3id.org/dpv/ai#hasTestingData"  # has testing data
hasTrainingData = "https://w3id.org/dpv/ai#hasTrainingData"  # has training data
hasValidationData = "https://w3id.org/dpv/ai#hasValidationData"  # has validation data
HeuristicProgramming = "https://w3id.org/dpv/ai#HeuristicProgramming"  # Heuristic Programming
HumanIdentification = "https://w3id.org/dpv/ai#HumanIdentification"  # Human Identification
HumanOrientedCapability = "https://w3id.org/dpv/ai#HumanOrientedCapability"  # Human-Oriented Capability
HyperparameterTuningBias = "https://w3id.org/dpv/ai#HyperparameterTuningBias"  # Hyperparameter Tuning Bias
ImageClassification = "https://w3id.org/dpv/ai#ImageClassification"  # Image Classification
ImageGeneration = "https://w3id.org/dpv/ai#ImageGeneration"  # Image Generation
ImageRecognition = "https://w3id.org/dpv/ai#ImageRecognition"  # Image Recognition
InceptionStage = "https://w3id.org/dpv/ai#InceptionStage"  # Inception Stage
IncidentMonitoringStage = "https://w3id.org/dpv/ai#IncidentMonitoringStage"  # Incident Monitoring Stage
InductiveProgramming = "https://w3id.org/dpv/ai#InductiveProgramming"  # Inductive Programming
IndustrialRobot = "https://w3id.org/dpv/ai#IndustrialRobot"  # Industrial Robot
InformationRetrieval = "https://w3id.org/dpv/ai#InformationRetrieval"  # Information Retrieval (IR)
InformativenessBias = "https://w3id.org/dpv/ai#InformativenessBias"  # Informativeness Bias
InputDataBias = "https://w3id.org/dpv/ai#InputDataBias"  # Input Data Bias
InputDataInaccurate = "https://w3id.org/dpv/ai#InputDataInaccurate"  # Input Data Inaccurate
InputDataInappropriate = "https://w3id.org/dpv/ai#InputDataInappropriate"  # Input Data Inappropriate
InputDataIncomplete = "https://w3id.org/dpv/ai#InputDataIncomplete"  # Input Data Incomplete
InputDataInconsistent = "https://w3id.org/dpv/ai#InputDataInconsistent"  # Input Data Inconsistent
InputDataMisclassified = "https://w3id.org/dpv/ai#InputDataMisclassified"  # Input Data Misclassified
InputDataMisinterpretation = "https://w3id.org/dpv/ai#InputDataMisinterpretation"  # Input Data Misinterpretation
InputDataNoise = "https://w3id.org/dpv/ai#InputDataNoise"  # Input Data Noise
InputDataOutdated = "https://w3id.org/dpv/ai#InputDataOutdated"  # Input Data Outdated
InputDataRisk = "https://w3id.org/dpv/ai#InputDataRisk"  # Input Data Risk
InputDataSelectionError = "https://w3id.org/dpv/ai#InputDataSelectionError"  # Input Data Selection Error
InputDataSparse = "https://w3id.org/dpv/ai#InputDataSparse"  # Input Data Sparse
InputDataUnrepresentative = "https://w3id.org/dpv/ai#InputDataUnrepresentative"  # Input Data Unrepresentative
InputDataUnstructured = "https://w3id.org/dpv/ai#InputDataUnstructured"  # Input Data Unstructured
InputDataUnverified = "https://w3id.org/dpv/ai#InputDataUnverified"  # Input Data Unverified
IntelligentControlSystem = "https://w3id.org/dpv/ai#IntelligentControlSystem"  # Intelligent Control System
KnowledgeRepresentation = "https://w3id.org/dpv/ai#KnowledgeRepresentation"  # Knowledge Representation
KnowledgeTechnique = "https://w3id.org/dpv/ai#KnowledgeTechnique"  # Knowledge Technique
LanguageCapability = "https://w3id.org/dpv/ai#LanguageCapability"  # Language Capability
LieDetection = "https://w3id.org/dpv/ai#LieDetection"  # Lie Detection
LifecycleStage = "https://w3id.org/dpv/ai#LifecycleStage"  # Lifecycle Stage
LLM = "https://w3id.org/dpv/ai#LLM"  # Large Language Model (LLM)
LocalBiometricIdentification = "https://w3id.org/dpv/ai#LocalBiometricIdentification"  # Local Biometric Identification
LogicTechnique = "https://w3id.org/dpv/ai#LogicTechnique"  # Logic Technique
LongShortTermMemory = "https://w3id.org/dpv/ai#LongShortTermMemory"  # Long Short-Term Memory (LSTM)
MachineLearning = "https://w3id.org/dpv/ai#MachineLearning"  # Machine Learning
MachineLearningModel = "https://w3id.org/dpv/ai#MachineLearningModel"  # Machine Learning Model
MachineLearningPlatform = "https://w3id.org/dpv/ai#MachineLearningPlatform"  # Machine Learning Platform
MachineTranslation = "https://w3id.org/dpv/ai#MachineTranslation"  # Machine Translation
MissingFeaturesBias = "https://w3id.org/dpv/ai#MissingFeaturesBias"  # Missing Features Bias
Model = "https://w3id.org/dpv/ai#Model"
ModelBias = "https://w3id.org/dpv/ai#ModelBias"  # Model Bias
ModelEvasion = "https://w3id.org/dpv/ai#ModelEvasion"  # Model Evasion
ModelExpressivenessBias = "https://w3id.org/dpv/ai#ModelExpressivenessBias"  # Model Expressiveness Bias
ModelFineTuning = "https://w3id.org/dpv/ai#ModelFineTuning"  # Model Fine-Tuning
ModelInteractionBias = "https://w3id.org/dpv/ai#ModelInteractionBias"  # Model Interaction Bias
ModelInversion = "https://w3id.org/dpv/ai#ModelInversion"  # Model Inversion
ModelRisk = "https://w3id.org/dpv/ai#ModelRisk"  # Model Risk
ModelTraining = "https://w3id.org/dpv/ai#ModelTraining"  # Model Training
MotionAnalysis = "https://w3id.org/dpv/ai#MotionAnalysis"  # Motion Analysis
MultiModalRetrieval = "https://w3id.org/dpv/ai#MultiModalRetrieval"  # Multi-modal Retrieval
MusicInformationRetrieval = "https://w3id.org/dpv/ai#MusicInformationRetrieval"  # Music Information Retrieval (MIR)
NamedEntityRecognition = "https://w3id.org/dpv/ai#NamedEntityRecognition"  # Named Entity Recognition
NarrowAI = "https://w3id.org/dpv/ai#NarrowAI"  # Narrow AI
NaturalLanguageGeneration = "https://w3id.org/dpv/ai#NaturalLanguageGeneration"  # Natural Language Generation
NaturalLanguageProcessing = "https://w3id.org/dpv/ai#NaturalLanguageProcessing"  # Natural Language Processing
NeuralNetwork = "https://w3id.org/dpv/ai#NeuralNetwork"  # Neural Network
NonRepresentativeSamplingBias = (
    "https://w3id.org/dpv/ai#NonRepresentativeSamplingBias"  # Non-Representative Sampling Bias
)
ObjectDetection = "https://w3id.org/dpv/ai#ObjectDetection"  # Object Detection
ObjectRecognition = "https://w3id.org/dpv/ai#ObjectRecognition"  # Object Recognition
OperationStage = "https://w3id.org/dpv/ai#OperationStage"  # Operation Stage
OptimisationMethod = "https://w3id.org/dpv/ai#OptimisationMethod"  # Optimisation Method
PartOfSpeechTagging = "https://w3id.org/dpv/ai#PartOfSpeechTagging"  # Part Of Speech Tagging
PatternRecognition = "https://w3id.org/dpv/ai#PatternRecognition"  # Pattern Recognition
PerceptionBasedAI = "https://w3id.org/dpv/ai#PerceptionBasedAI"  # Perception-based AI
PersonalityTraitAnalysis = "https://w3id.org/dpv/ai#PersonalityTraitAnalysis"  # Personality Trait Analysis
PostTimeBiometricIdentification = (
    "https://w3id.org/dpv/ai#PostTimeBiometricIdentification"  # Post-Time Biometric Identification
)
Profiling = "https://w3id.org/dpv/ai#Profiling"
QuestionAnswering = "https://w3id.org/dpv/ai#QuestionAnswering"  # Question Answering
RealTimeBiometricIdentification = (
    "https://w3id.org/dpv/ai#RealTimeBiometricIdentification"  # Real-Time Biometric Identification
)
ReasoningSystem = "https://w3id.org/dpv/ai#ReasoningSystem"  # Reasoning System
ReasoningTechnique = "https://w3id.org/dpv/ai#ReasoningTechnique"  # Reasoning Technique
RecurrentNeuralNetwork = "https://w3id.org/dpv/ai#RecurrentNeuralNetwork"  # Recurrent Neural Network (RNN)
ReevaluationStage = "https://w3id.org/dpv/ai#ReevaluationStage"  # Reevaluation Stage
ReinforcementLearning = "https://w3id.org/dpv/ai#ReinforcementLearning"  # Reinforcement Learning
RelationshipExtraction = "https://w3id.org/dpv/ai#RelationshipExtraction"  # Relationship Extraction
RemoteBiometricIdentification = (
    "https://w3id.org/dpv/ai#RemoteBiometricIdentification"  # Remote Biometric Identification
)
RemoteSensing = "https://w3id.org/dpv/ai#RemoteSensing"  # Remote Sensing
RepairStage = "https://w3id.org/dpv/ai#RepairStage"  # Repair Stage
ReplaceStage = "https://w3id.org/dpv/ai#ReplaceStage"  # Replace Stage
RetirementStage = "https://w3id.org/dpv/ai#RetirementStage"  # Retirement Stage
RiskConcept = "https://w3id.org/dpv/ai#RiskConcept"
Robot = "https://w3id.org/dpv/ai#Robot"
RoboticProcessAutomation = "https://w3id.org/dpv/ai#RoboticProcessAutomation"  # Robotic Process Automation
Robotics = "https://w3id.org/dpv/ai#Robotics"
RuleBasedTechnique = "https://w3id.org/dpv/ai#RuleBasedTechnique"  # Rule Technique
SearchMethod = "https://w3id.org/dpv/ai#SearchMethod"  # Search Method
SecurityAttack = "https://w3id.org/dpv/ai#SecurityAttack"  # Security Attack
SelfSupervisedLearning = "https://w3id.org/dpv/ai#SelfSupervisedLearning"  # Self-Supervised Learning
SemiSupervisedLearning = "https://w3id.org/dpv/ai#SemiSupervisedLearning"  # Semi Supervised Learning
SentimentAnalysis = "https://w3id.org/dpv/ai#SentimentAnalysis"  # Sentiment Analysis
ServiceRobot = "https://w3id.org/dpv/ai#ServiceRobot"  # Service Robot
SocialRobot = "https://w3id.org/dpv/ai#SocialRobot"  # Social Robot
SoundSourceSeparation = "https://w3id.org/dpv/ai#SoundSourceSeparation"  # Sound Source Separation
SoundSynthesis = "https://w3id.org/dpv/ai#SoundSynthesis"  # Sound Synthesis
SpeakerRecognition = "https://w3id.org/dpv/ai#SpeakerRecognition"  # Speaker Recognition
SpeechRecognition = "https://w3id.org/dpv/ai#SpeechRecognition"  # Speech Recognition
SpeechSynthesis = "https://w3id.org/dpv/ai#SpeechSynthesis"  # Speech Synthesis
StatisticalTechnique = "https://w3id.org/dpv/ai#StatisticalTechnique"  # Statistical Technique
SupervisedLearning = "https://w3id.org/dpv/ai#SupervisedLearning"  # Supervised Learning
SupportVectorMachine = "https://w3id.org/dpv/ai#SupportVectorMachine"  # Support Vector Machine
SymbolicReasoning = "https://w3id.org/dpv/ai#SymbolicReasoning"  # Symbolic Reasoning
Technique = "https://w3id.org/dpv/ai#Technique"
TestingData = "https://w3id.org/dpv/ai#TestingData"  # Testing Data
TestingDataBias = "https://w3id.org/dpv/ai#TestingDataBias"  # Testing Data Bias
TestingDataInaccurate = "https://w3id.org/dpv/ai#TestingDataInaccurate"  # Testing Data Inaccurate
TestingDataInappropriate = "https://w3id.org/dpv/ai#TestingDataInappropriate"  # Testing Data Inappropriate
TestingDataIncomplete = "https://w3id.org/dpv/ai#TestingDataIncomplete"  # Testing Data Incomplete
TestingDataInconsistent = "https://w3id.org/dpv/ai#TestingDataInconsistent"  # Testing Data Inconsistent
TestingDataMisclassified = "https://w3id.org/dpv/ai#TestingDataMisclassified"  # Testing Data Misclassified
TestingDataMisinterpretation = "https://w3id.org/dpv/ai#TestingDataMisinterpretation"  # Testing Data Misinterpretation
TestingDataNoise = "https://w3id.org/dpv/ai#TestingDataNoise"  # Testing Data Noise
TestingDataOutdated = "https://w3id.org/dpv/ai#TestingDataOutdated"  # Testing Data Outdated
TestingDataRisk = "https://w3id.org/dpv/ai#TestingDataRisk"  # Testing Data Risk
TestingDataSelectionError = "https://w3id.org/dpv/ai#TestingDataSelectionError"  # Testing Data Selection Error
TestingDataSparse = "https://w3id.org/dpv/ai#TestingDataSparse"  # Testing Data Sparse
TestingDataUnrepresentative = "https://w3id.org/dpv/ai#TestingDataUnrepresentative"  # Testing Data Unrepresentative
TestingDataUnstructured = "https://w3id.org/dpv/ai#TestingDataUnstructured"  # Testing Data Unstructured
TestingDataUnverified = "https://w3id.org/dpv/ai#TestingDataUnverified"  # Testing Data Unverified
TextClassification = "https://w3id.org/dpv/ai#TextClassification"  # Text Classification
TextDataMining = "https://w3id.org/dpv/ai#TextDataMining"  # Text and Data Mining
TrainedModel = "https://w3id.org/dpv/ai#TrainedModel"  # Trained Model
TrainingData = "https://w3id.org/dpv/ai#TrainingData"  # Training Data
TrainingTechnique = "https://w3id.org/dpv/ai#TrainingTechnique"  # Training Technique
TransferLearning = "https://w3id.org/dpv/ai#TransferLearning"
TransparencyRisk = "https://w3id.org/dpv/ai#TransparencyRisk"  # Transparency Risk
UnsupervisedLearning = "https://w3id.org/dpv/ai#UnsupervisedLearning"  # Unsupervised Learning
UpdateStage = "https://w3id.org/dpv/ai#UpdateStage"  # Update Stage
UserRisk = "https://w3id.org/dpv/ai#UserRisk"  # User Risk
ValidationData = "https://w3id.org/dpv/ai#ValidationData"  # Validation Data
ValidationDataBias = "https://w3id.org/dpv/ai#ValidationDataBias"  # Validation Data Bias
ValidationDataInaccurate = "https://w3id.org/dpv/ai#ValidationDataInaccurate"  # Validation Data Inaccurate
ValidationDataInappropriate = "https://w3id.org/dpv/ai#ValidationDataInappropriate"  # Validation Data Inappropriate
ValidationDataIncomplete = "https://w3id.org/dpv/ai#ValidationDataIncomplete"  # Validation Data Incomplete
ValidationDataInconsistent = "https://w3id.org/dpv/ai#ValidationDataInconsistent"  # Validation Data Inconsistent
ValidationDataMisclassified = "https://w3id.org/dpv/ai#ValidationDataMisclassified"  # Validation Data Misclassified
ValidationDataMisinterpretation = (
    "https://w3id.org/dpv/ai#ValidationDataMisinterpretation"  # Validation Data Misinterpretation
)
ValidationDataNoise = "https://w3id.org/dpv/ai#ValidationDataNoise"  # Validation Data Noise
ValidationDataOutdated = "https://w3id.org/dpv/ai#ValidationDataOutdated"  # Validation Data Outdated
ValidationDataRisk = "https://w3id.org/dpv/ai#ValidationDataRisk"  # Validation Data Risk
ValidationDataSelectionError = "https://w3id.org/dpv/ai#ValidationDataSelectionError"  # Validation Data Selection Error
ValidationDataSparse = "https://w3id.org/dpv/ai#ValidationDataSparse"  # Validation Data Sparse
ValidationDataUnrepresentative = (
    "https://w3id.org/dpv/ai#ValidationDataUnrepresentative"  # Validation Data Unrepresentative
)
ValidationDataUnstructured = "https://w3id.org/dpv/ai#ValidationDataUnstructured"  # Validation Data Unstructured
ValidationDataUnverified = "https://w3id.org/dpv/ai#ValidationDataUnverified"  # Validation Data Unverified
ValidationStage = "https://w3id.org/dpv/ai#ValidationStage"  # Validation Stage
VerificationStage = "https://w3id.org/dpv/ai#VerificationStage"  # Verification Stage
VideoGeneration = "https://w3id.org/dpv/ai#VideoGeneration"  # Video Generation
VisualRecognition = "https://w3id.org/dpv/ai#VisualRecognition"  # Visual Recognition


class AITechnique(_StavVocabEnum):
    """
    AI technique types from the W3C Data Privacy Vocabulary (DPV) AI extension. Use for
    annotating the machine learning or AI technique used in a model — maps to the SPDX 3
    ai_typeOfModel field.
    """

    AudioProcessing = "https://w3id.org/dpv/ai#AudioProcessing"  # Audio Processing
    BayesianEstimation = "https://w3id.org/dpv/ai#BayesianEstimation"  # Bayesian Estimation
    BayesianNetwork = "https://w3id.org/dpv/ai#BayesianNetwork"  # Bayesian Network
    BayesianOptimisation = "https://w3id.org/dpv/ai#BayesianOptimisation"  # Bayesian Optimisation
    ConvolutionalNeuralNetwork = (
        "https://w3id.org/dpv/ai#ConvolutionalNeuralNetwork"  # Convolutional Neural Network (CNN)
    )
    DecisionTree = "https://w3id.org/dpv/ai#DecisionTree"  # Decision Tree
    DeepLearning = "https://w3id.org/dpv/ai#DeepLearning"  # Deep Learning
    FeedForwardNeuralNetwork = "https://w3id.org/dpv/ai#FeedForwardNeuralNetwork"  # Feed Forward Neural Network
    FrugalMachineLearning = "https://w3id.org/dpv/ai#FrugalMachineLearning"  # Frugal Machine Learning
    GeneticAlgorithm = "https://w3id.org/dpv/ai#GeneticAlgorithm"  # Genetic Algorithm
    HeuristicProgramming = "https://w3id.org/dpv/ai#HeuristicProgramming"  # Heuristic Programming
    InductiveProgramming = "https://w3id.org/dpv/ai#InductiveProgramming"  # Inductive Programming
    KnowledgeRepresentation = "https://w3id.org/dpv/ai#KnowledgeRepresentation"  # Knowledge Representation
    KnowledgeTechnique = "https://w3id.org/dpv/ai#KnowledgeTechnique"  # Knowledge Technique
    LogicTechnique = "https://w3id.org/dpv/ai#LogicTechnique"  # Logic Technique
    LongShortTermMemory = "https://w3id.org/dpv/ai#LongShortTermMemory"  # Long Short-Term Memory (LSTM)
    MachineLearning = "https://w3id.org/dpv/ai#MachineLearning"  # Machine Learning
    NeuralNetwork = "https://w3id.org/dpv/ai#NeuralNetwork"  # Neural Network
    OptimisationMethod = "https://w3id.org/dpv/ai#OptimisationMethod"  # Optimisation Method
    ReasoningTechnique = "https://w3id.org/dpv/ai#ReasoningTechnique"  # Reasoning Technique
    RecurrentNeuralNetwork = "https://w3id.org/dpv/ai#RecurrentNeuralNetwork"  # Recurrent Neural Network (RNN)
    ReinforcementLearning = "https://w3id.org/dpv/ai#ReinforcementLearning"  # Reinforcement Learning
    RuleBasedTechnique = "https://w3id.org/dpv/ai#RuleBasedTechnique"  # Rule Technique
    SearchMethod = "https://w3id.org/dpv/ai#SearchMethod"  # Search Method
    SelfSupervisedLearning = "https://w3id.org/dpv/ai#SelfSupervisedLearning"  # Self-Supervised Learning
    SemiSupervisedLearning = "https://w3id.org/dpv/ai#SemiSupervisedLearning"  # Semi Supervised Learning
    SpeakerRecognition = "https://w3id.org/dpv/ai#SpeakerRecognition"  # Speaker Recognition
    SpeechRecognition = "https://w3id.org/dpv/ai#SpeechRecognition"  # Speech Recognition
    StatisticalTechnique = "https://w3id.org/dpv/ai#StatisticalTechnique"  # Statistical Technique
    SupervisedLearning = "https://w3id.org/dpv/ai#SupervisedLearning"  # Supervised Learning
    SupportVectorMachine = "https://w3id.org/dpv/ai#SupportVectorMachine"  # Support Vector Machine
    SymbolicReasoning = "https://w3id.org/dpv/ai#SymbolicReasoning"  # Symbolic Reasoning
    Technique = "https://w3id.org/dpv/ai#Technique"
    TransferLearning = "https://w3id.org/dpv/ai#TransferLearning"
    UnsupervisedLearning = "https://w3id.org/dpv/ai#UnsupervisedLearning"  # Unsupervised Learning


class AICapability(_StavVocabEnum):
    """
    AI capability types from the W3C Data Privacy Vocabulary (DPV) AI extension. Use for
    annotating the capabilities or outputs of an AI system — maps to the SPDX 3 ai_domain
    field.
    """

    ActionRecognition = "https://w3id.org/dpv/ai#ActionRecognition"  # Action Recognition
    AudioCapability = "https://w3id.org/dpv/ai#AudioCapability"  # Audio Capability
    AudioGeneration = "https://w3id.org/dpv/ai#AudioGeneration"  # Audio Generation
    AutomaticSummarisation = "https://w3id.org/dpv/ai#AutomaticSummarisation"  # Automatic Summarisation
    BehaviourAnalysis = "https://w3id.org/dpv/ai#BehaviourAnalysis"  # Behaviour Analysis
    BiometricCapability = "https://w3id.org/dpv/ai#BiometricCapability"  # Biometric Capability
    BiometricCategorisation = "https://w3id.org/dpv/ai#BiometricCategorisation"  # Biometric Categorisation
    BiometricEmotionRecognition = "https://w3id.org/dpv/ai#BiometricEmotionRecognition"  # Biometric Emotion Recognition
    BiometricIdentification = "https://w3id.org/dpv/ai#BiometricIdentification"  # Biometric Identification
    Capability = "https://w3id.org/dpv/ai#Capability"
    ChatbotCapability = "https://w3id.org/dpv/ai#ChatbotCapability"  # Chatbot Capability
    ComputationalCreativity = "https://w3id.org/dpv/ai#ComputationalCreativity"  # Computational Creativity
    ComputerVision = "https://w3id.org/dpv/ai#ComputerVision"  # Computer Vision
    ContentBasedRetrieval = "https://w3id.org/dpv/ai#ContentBasedRetrieval"  # Content-based Retrieval
    ContentGeneration = "https://w3id.org/dpv/ai#ContentGeneration"  # Content Generation
    ContextAwareRetrieval = "https://w3id.org/dpv/ai#ContextAwareRetrieval"  # Context-aware Retrieval
    DialogueManagement = "https://w3id.org/dpv/ai#DialogueManagement"  # Dialogue Management
    EmotionRecognition = "https://w3id.org/dpv/ai#EmotionRecognition"  # Emotion Recognition
    FaceRecognition = "https://w3id.org/dpv/ai#FaceRecognition"  # Face Recognition
    GestureRecognition = "https://w3id.org/dpv/ai#GestureRecognition"  # Gesture Recognition
    HumanIdentification = "https://w3id.org/dpv/ai#HumanIdentification"  # Human Identification
    HumanOrientedCapability = "https://w3id.org/dpv/ai#HumanOrientedCapability"  # Human-Oriented Capability
    ImageClassification = "https://w3id.org/dpv/ai#ImageClassification"  # Image Classification
    ImageGeneration = "https://w3id.org/dpv/ai#ImageGeneration"  # Image Generation
    ImageRecognition = "https://w3id.org/dpv/ai#ImageRecognition"  # Image Recognition
    InformationRetrieval = "https://w3id.org/dpv/ai#InformationRetrieval"  # Information Retrieval (IR)
    LanguageCapability = "https://w3id.org/dpv/ai#LanguageCapability"  # Language Capability
    LieDetection = "https://w3id.org/dpv/ai#LieDetection"  # Lie Detection
    LocalBiometricIdentification = (
        "https://w3id.org/dpv/ai#LocalBiometricIdentification"  # Local Biometric Identification
    )
    MachineTranslation = "https://w3id.org/dpv/ai#MachineTranslation"  # Machine Translation
    MotionAnalysis = "https://w3id.org/dpv/ai#MotionAnalysis"  # Motion Analysis
    MultiModalRetrieval = "https://w3id.org/dpv/ai#MultiModalRetrieval"  # Multi-modal Retrieval
    MusicInformationRetrieval = "https://w3id.org/dpv/ai#MusicInformationRetrieval"  # Music Information Retrieval (MIR)
    NamedEntityRecognition = "https://w3id.org/dpv/ai#NamedEntityRecognition"  # Named Entity Recognition
    NaturalLanguageGeneration = "https://w3id.org/dpv/ai#NaturalLanguageGeneration"  # Natural Language Generation
    NaturalLanguageProcessing = "https://w3id.org/dpv/ai#NaturalLanguageProcessing"  # Natural Language Processing
    ObjectDetection = "https://w3id.org/dpv/ai#ObjectDetection"  # Object Detection
    ObjectRecognition = "https://w3id.org/dpv/ai#ObjectRecognition"  # Object Recognition
    PartOfSpeechTagging = "https://w3id.org/dpv/ai#PartOfSpeechTagging"  # Part Of Speech Tagging
    PatternRecognition = "https://w3id.org/dpv/ai#PatternRecognition"  # Pattern Recognition
    PerceptionBasedAI = "https://w3id.org/dpv/ai#PerceptionBasedAI"  # Perception-based AI
    PersonalityTraitAnalysis = "https://w3id.org/dpv/ai#PersonalityTraitAnalysis"  # Personality Trait Analysis
    PostTimeBiometricIdentification = (
        "https://w3id.org/dpv/ai#PostTimeBiometricIdentification"  # Post-Time Biometric Identification
    )
    Profiling = "https://w3id.org/dpv/ai#Profiling"
    QuestionAnswering = "https://w3id.org/dpv/ai#QuestionAnswering"  # Question Answering
    RealTimeBiometricIdentification = (
        "https://w3id.org/dpv/ai#RealTimeBiometricIdentification"  # Real-Time Biometric Identification
    )
    RelationshipExtraction = "https://w3id.org/dpv/ai#RelationshipExtraction"  # Relationship Extraction
    RemoteBiometricIdentification = (
        "https://w3id.org/dpv/ai#RemoteBiometricIdentification"  # Remote Biometric Identification
    )
    RemoteSensing = "https://w3id.org/dpv/ai#RemoteSensing"  # Remote Sensing
    SentimentAnalysis = "https://w3id.org/dpv/ai#SentimentAnalysis"  # Sentiment Analysis
    SoundSourceSeparation = "https://w3id.org/dpv/ai#SoundSourceSeparation"  # Sound Source Separation
    SoundSynthesis = "https://w3id.org/dpv/ai#SoundSynthesis"  # Sound Synthesis
    SpeakerRecognition = "https://w3id.org/dpv/ai#SpeakerRecognition"  # Speaker Recognition
    SpeechRecognition = "https://w3id.org/dpv/ai#SpeechRecognition"  # Speech Recognition
    SpeechSynthesis = "https://w3id.org/dpv/ai#SpeechSynthesis"  # Speech Synthesis
    TextClassification = "https://w3id.org/dpv/ai#TextClassification"  # Text Classification
    TextDataMining = "https://w3id.org/dpv/ai#TextDataMining"  # Text and Data Mining
    VideoGeneration = "https://w3id.org/dpv/ai#VideoGeneration"  # Video Generation
    VisualRecognition = "https://w3id.org/dpv/ai#VisualRecognition"  # Visual Recognition


class AILifecycleStage(_StavVocabEnum):
    """
    AI lifecycle stages from the W3C Data Privacy Vocabulary (DPV) AI extension. Use for
    annotating which stage of the AI development or operation pipeline a piece of code or
    data belongs to.
    """

    ContinuousValidationStage = "https://w3id.org/dpv/ai#ContinuousValidationStage"  # Continuous Validation Stage
    DecommissionStage = "https://w3id.org/dpv/ai#DecommissionStage"  # Decommission Stage
    DeploymentStage = "https://w3id.org/dpv/ai#DeploymentStage"  # Deployment Stage
    DesignStage = "https://w3id.org/dpv/ai#DesignStage"  # Design Stage
    DevelopmentStage = "https://w3id.org/dpv/ai#DevelopmentStage"  # Development Stage
    DiscardStage = "https://w3id.org/dpv/ai#DiscardStage"  # Discard Stage
    InceptionStage = "https://w3id.org/dpv/ai#InceptionStage"  # Inception Stage
    IncidentMonitoringStage = "https://w3id.org/dpv/ai#IncidentMonitoringStage"  # Incident Monitoring Stage
    LifecycleStage = "https://w3id.org/dpv/ai#LifecycleStage"  # Lifecycle Stage
    OperationStage = "https://w3id.org/dpv/ai#OperationStage"  # Operation Stage
    ReevaluationStage = "https://w3id.org/dpv/ai#ReevaluationStage"  # Reevaluation Stage
    RepairStage = "https://w3id.org/dpv/ai#RepairStage"  # Repair Stage
    ReplaceStage = "https://w3id.org/dpv/ai#ReplaceStage"  # Replace Stage
    RetirementStage = "https://w3id.org/dpv/ai#RetirementStage"  # Retirement Stage
    UpdateStage = "https://w3id.org/dpv/ai#UpdateStage"  # Update Stage
    ValidationStage = "https://w3id.org/dpv/ai#ValidationStage"  # Validation Stage
    VerificationStage = "https://w3id.org/dpv/ai#VerificationStage"  # Verification Stage


class AISystemType(_StavVocabEnum):
    """
    AI system classification types from the W3C Data Privacy Vocabulary (DPV) AI extension.
    Use for annotating the broad category or architecture of an AI system.
    """

    AGI = "https://w3id.org/dpv/ai#AGI"  # Artificial General Intelligence (AGI)
    AI = "https://w3id.org/dpv/ai#AI"  # Artificial Intelligence (AI)
    AIAgent = "https://w3id.org/dpv/ai#AIAgent"  # AI Agent
    AISystem = "https://w3id.org/dpv/ai#AISystem"  # AI System
    CyberphysicalSystem = "https://w3id.org/dpv/ai#CyberphysicalSystem"  # Cyber-physical System
    NarrowAI = "https://w3id.org/dpv/ai#NarrowAI"  # Narrow AI
    PerceptionBasedAI = "https://w3id.org/dpv/ai#PerceptionBasedAI"  # Perception-based AI
    ReasoningSystem = "https://w3id.org/dpv/ai#ReasoningSystem"  # Reasoning System
    Robot = "https://w3id.org/dpv/ai#Robot"
    RoboticProcessAutomation = "https://w3id.org/dpv/ai#RoboticProcessAutomation"  # Robotic Process Automation


# ── Metadata registry ──────────────────────────────────────────────────────────────
# Populated at import time so stav.label() / .definition() / .broader() work.
_register(
    {
        "https://w3id.org/dpv/ai#AGI": {
            "label": "Artificial General Intelligence (AGI)",
            "definition": "Type of AI system that addresses a broad range of tasks with a satisfactory level of performance",
            "broader": ("https://w3id.org/dpv/ai#AISystem",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#AI": {
            "label": "Artificial Intelligence (AI)",
            "definition": "A technical and scientific field devoted to the engineered system that generates outputs such as content, forecasts, recommendations or decisions for a given set of human-defined objectives",
            "broader": ("https://w3id.org/dpv#Technology",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#AIAgent": {
            "label": "AI Agent",
            "definition": "An AI Agent, also known as an 'intelligent agent', is a software agent that utilises AI technologies",
            "broader": ("https://w3id.org/dpv/ai#AI", "https://w3id.org/dpv/tech#SoftwareAgent"),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#AIBias": {
            "label": "AI Bias",
            "definition": "Bias associated with development, use, or other activities involving an AI technology or system",
            "broader": ("https://w3id.org/dpv/ai#RiskConcept", "https://w3id.org/dpv/risk#Bias"),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#AIProcess": {
            "label": "AI Process",
            "definition": "A process involving AI technologies",
            "broader": ("https://w3id.org/dpv#Process",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#AISystem": {
            "label": "AI System",
            "definition": "An engineered system that generates outputs such as content, forecasts, recommendations or decisions for a given set of human-defined objectives (ISO/IEC 22989:2022 definition); or A machine-based system that, for explicit or implicit objectives, infers, from the input it receives, how to generat...",
            "broader": ("https://w3id.org/dpv/ai#AI", "https://w3id.org/dpv/tech#System"),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#AISystemRisk": {
            "label": "AI System Risk",
            "definition": "Risks associated with AI Systems",
            "broader": ("https://w3id.org/dpv/ai#RiskConcept",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#ActionRecognition": {
            "label": "Action Recognition",
            "definition": "Capability to recognise actions",
            "broader": ("https://w3id.org/dpv/ai#BiometricCapability", "https://w3id.org/dpv/ai#ComputerVision"),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#AdversarialAttack": {
            "label": "Adversarial Attack",
            "definition": "Inputs designed to cause the model to make a mistake",
            "broader": ("https://w3id.org/dpv/ai#SecurityAttack",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#AlgorithmSelectionBias": {
            "label": "Algorithm Selection Bias",
            "definition": "Bias that occurs from the selection of machine learning algorithms built into the AI system which introduce unwanted bias in predictions made by the system because the type of algorithm used introduces a variation in the performance of the ML model",
            "broader": ("https://w3id.org/dpv/ai#EngineeringDecisionBias",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#AudioCapability": {
            "label": "Audio Capability",
            "definition": "Capabilities related to the processing and generation of audio",
            "broader": ("https://w3id.org/dpv/ai#Capability",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#AudioGeneration": {
            "label": "Audio Generation",
            "definition": "Capability to generate audio",
            "broader": ("https://w3id.org/dpv/ai#AudioCapability", "https://w3id.org/dpv/ai#ContentGeneration"),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#AudioProcessing": {
            "label": "Audio Processing",
            "definition": "Technique involving processing audio",
            "broader": ("https://w3id.org/dpv/ai#Technique",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#AutomaticSummarisation": {
            "label": "Automatic Summarisation",
            "definition": "Capability for shortening a portion of content such as text while retaining important semantic information",
            "broader": ("https://w3id.org/dpv/ai#InformationRetrieval", "https://w3id.org/dpv/ai#LanguageCapability"),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#AutomationBias": {
            "label": "Automation Bias",
            "definition": "Bias that occurs due to propensity for humans to favour suggestions from automated decision-making systems and to ignore contradictory information made without automation, even if it is correct",
            "broader": ("https://w3id.org/dpv/ai#AIBias", "https://w3id.org/dpv/risk#CognitiveBias"),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#BayesianEstimation": {
            "label": "Bayesian Estimation",
            "definition": "Refers to Bayesian estimation approach",
            "broader": ("https://w3id.org/dpv/ai#StatisticalTechnique",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#BayesianNetwork": {
            "label": "Bayesian Network",
            "definition": "Probabilistic technique that uses Bayesian inference for probability computations using a directed acyclic graph",
            "broader": ("https://w3id.org/dpv/ai#StatisticalTechnique",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#BayesianOptimisation": {
            "label": "Bayesian Optimisation",
            "definition": "Refers to Bayesian optimisation technique",
            "broader": ("https://w3id.org/dpv/ai#StatisticalTechnique",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#BehaviourAnalysis": {
            "label": "Behaviour Analysis",
            "definition": "Capability of a system in analysing people's behaviour",
            "broader": ("https://w3id.org/dpv/ai#HumanOrientedCapability",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#Benchmarking": {
            "label": "Benchmarking",
            "definition": "Measure where performance and outputs are compared to best practices, gold standards, or other forms of desired quality",
            "broader": ("https://w3id.org/dpv#DataQualityAssessment",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#BiasAssessment": {
            "label": "Bias Assessment",
            "definition": "Examination of a data set, model, or AI system for bias",
            "broader": ("https://w3id.org/dpv#DataQualityAssessment",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#BiasDetection": {
            "label": "Bias Detection",
            "definition": "Indicates measures to detect bias",
            "broader": ("https://w3id.org/dpv/ai#BiasAssessment",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#BiasMitigation": {
            "label": "Bias Mitigation",
            "definition": "Indicates measures to mitigate bias",
            "broader": ("https://w3id.org/dpv/ai#BiasAssessment",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#BiasPrevention": {
            "label": "Bias Prevention",
            "definition": "Indicates measures to prevent bias",
            "broader": ("https://w3id.org/dpv/ai#BiasAssessment",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#BiometricCapability": {
            "label": "Biometric Capability",
            "definition": "Capability involving processing of biometric data or related to biometrics",
            "broader": ("https://w3id.org/dpv/ai#HumanOrientedCapability",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#BiometricCategorisation": {
            "label": "Biometric Categorisation",
            "definition": "Capability involving assigning natural persons to specific categories based on their biometric data",
            "broader": ("https://w3id.org/dpv/ai#BiometricCapability",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#BiometricEmotionRecognition": {
            "label": "Biometric Emotion Recognition",
            "definition": "Capability for recognising emotions based on biometrics information",
            "broader": ("https://w3id.org/dpv/ai#EmotionRecognition",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#BiometricIdentification": {
            "label": "Biometric Identification",
            "definition": "Capability involving automated recognition of physical, physiological and behavioural human features such as the face, eye movement, body shape, voice, prosody, gait, posture, heart rate, blood pressure, odour, keystrokes characteristics, for the purpose of establishing an individual’s identity b...",
            "broader": ("https://w3id.org/dpv/ai#BiometricCapability", "https://w3id.org/dpv/ai#HumanIdentification"),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#Capability": {
            "label": "Capability",
            "definition": "Capability or use of AI to achieve a technical goal or objective",
            "broader": ("https://w3id.org/dpv/ai#AI",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#ChatbotCapability": {
            "label": "Chatbot Capability",
            "definition": "Capability to simulate human-like conversation with a user through messaging platforms, websites, mobile apps, or telephone systems, often employing natural language processing and machine learning to engage in conversation mimicking human interaction",
            "broader": ("https://w3id.org/dpv/ai#NaturalLanguageProcessing",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#CognitiveComputing": {
            "label": "Cognitive Computing",
            "definition": "Category of AI systems that enables people and machines to interact more naturally",
            "broader": ("https://w3id.org/dpv/ai#AISystem",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#ComputationalCreativity": {
            "label": "Computational Creativity",
            "definition": "computer systems that emulate human creative processes and produce artistic, design output that simulates innovation and originality",
            "broader": ("https://w3id.org/dpv/ai#HumanOrientedCapability",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#ComputerVision": {
            "label": "Computer Vision",
            "definition": "Capability of a functional unit to acquire, process and interpret data representing images or video",
            "broader": ("https://w3id.org/dpv/ai#Capability",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#ContentBasedRetrieval": {
            "label": "Content-based Retrieval",
            "definition": "Capability for retrieval of information using the actual content to identify, select, filter, and provide results",
            "broader": ("https://w3id.org/dpv/ai#InformationRetrieval",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#ContentGeneration": {
            "label": "Content Generation",
            "definition": "Capability to generate new content that is distinct from merely deriving or transforming existing content",
            "broader": ("https://w3id.org/dpv/ai#Capability",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#ContextAwareRetrieval": {
            "label": "Context-aware Retrieval",
            "definition": "Capability for retrieval of information that takes into account the user's context such as e.g., location, time, device, or activity to provide more relevant results",
            "broader": ("https://w3id.org/dpv/ai#InformationRetrieval",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#ContinuousValidationStage": {
            "label": "Continuous Validation Stage",
            "definition": "The stage in the lifecycle where there is continuous learning within the AI system by incremental training on an ongoing basis while the system is running in production",
            "broader": ("https://w3id.org/dpv/ai#LifecycleStage",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#ConvolutionalNeuralNetwork": {
            "label": "Convolutional Neural Network (CNN)",
            "definition": "Feed forward neural network using convolution in at least one of its layers",
            "broader": ("https://w3id.org/dpv/ai#NeuralNetwork",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#CyberphysicalSystem": {
            "label": "Cyber-physical System",
            "definition": "Engineered system built from, and depending upon, the seamless integration of computation and physical components",
            "broader": ("https://w3id.org/dpv/ai#AISystem",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#Data": {
            "label": "AI Data",
            "definition": "Data involved in the development and use of an AI system or model",
            "broader": ("https://w3id.org/dpv#Data", "https://w3id.org/dpv/tech#InputOutput"),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#DataAggregation": {
            "label": "Data Aggregation",
            "definition": "Processing operation where data is aggregated, e.g. by combining multiple records into one",
            "broader": ("https://w3id.org/dpv#Transform", "https://w3id.org/dpv/ai#DataPreparation"),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#DataAggregationBias": {
            "label": "Data Aggregation Bias",
            "definition": "Bias that occurs from aggregating data covering different groups of objects that might have different statistical distributions which introduce bias into the data used to train AI systems",
            "broader": ("https://w3id.org/dpv/ai#DataBias",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#DataAnnotation": {
            "label": "Data Annotation",
            "definition": "Processing operation where data is annoated, e.g. by adding additional metadata or context to make it useful",
            "broader": ("https://w3id.org/dpv#Obtain", "https://w3id.org/dpv/ai#DataPreparation"),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#DataBias": {
            "label": "Data Bias",
            "definition": "Bias that occurs due to unaddressed data properties that lead to AI systems that perform better or worse for different groups",
            "broader": ("https://w3id.org/dpv/ai#AIBias",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#DataCleaning": {
            "label": "Data Cleaning",
            "definition": "Processing operation where data is cleaned, e.g. by detecting and removing errors or unwanted records",
            "broader": ("https://w3id.org/dpv#Transform", "https://w3id.org/dpv/ai#DataPreparation"),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#DataCollection": {
            "label": "Data Collection",
            "definition": "Processing operation where data is collected, e.g. in a raw or unrefined form",
            "broader": ("https://w3id.org/dpv#Collect", "https://w3id.org/dpv/ai#DataOperation"),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#DataEnrichment": {
            "label": "Data Enrichment",
            "definition": "Processing operation where data is enriced, e.g. by adding additional data that increases its value or usefulness",
            "broader": ("https://w3id.org/dpv#Obtain", "https://w3id.org/dpv/ai#DataPreparation"),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#DataLabelling": {
            "label": "Data Labelling",
            "definition": "Processing operation where data annotation is carried out through labelling, e.g. by assigning tags or categories",
            "broader": ("https://w3id.org/dpv#Obtain", "https://w3id.org/dpv/ai#DataAnnotation"),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#DataLabellingProcessBias": {
            "label": "Data Labelling Process Bias",
            "definition": "Bias that occurs due to the labelling process itself introducing societal or cognitive biases",
            "broader": ("https://w3id.org/dpv/ai#DataBias",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#DataOperation": {
            "label": "DataOperation",
            "definition": "Processing of data for the development or use of AI models",
            "broader": ("https://w3id.org/dpv#Processing",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#DataPoisoning": {
            "label": "Data Poisoning",
            "definition": "Attack trying to manipulate the training dataset",
            "broader": ("https://w3id.org/dpv/ai#SecurityAttack",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#DataPreparation": {
            "label": "Data Preparation",
            "definition": "Processing operation where data is prepared, e.g. organising and transforming it to make it ready for use",
            "broader": (
                "https://w3id.org/dpv#Organise",
                "https://w3id.org/dpv#Transform",
                "https://w3id.org/dpv/ai#DataOperation",
            ),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#DataRisk": {
            "label": "Data Risk",
            "definition": "Risk associated with data used or produced or otherwise involved in the context of AI",
            "broader": ("https://w3id.org/dpv/ai#RiskConcept",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#DataUpdating": {
            "label": "Data Updating",
            "definition": "Processing operation where data is updated, e.g. by adding the latest records",
            "broader": ("https://w3id.org/dpv#Obtain", "https://w3id.org/dpv/ai#DataPreparation"),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#DecisionTree": {
            "label": "Decision Tree",
            "definition": "Technique for which inference is encoded as paths from the root to a leaf node in a tree structure",
            "broader": ("https://w3id.org/dpv/ai#MachineLearning",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#DecommissionStage": {
            "label": "Decommission Stage",
            "definition": "The stage in the lifecycle where the AI system is being decommissioned as part of retirement",
            "broader": ("https://w3id.org/dpv/ai#RetirementStage",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#DeepLearning": {
            "label": "Deep Learning",
            "definition": "Approach to creating rich hierarchical representations through the training of neural networks with many hidden layers",
            "broader": ("https://w3id.org/dpv/ai#MachineLearning",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#DeploymentStage": {
            "label": "Deployment Stage",
            "definition": "The stage in the lifecycle where the AI system is installed, released or configured for deployment and operation in a target environment",
            "broader": ("https://w3id.org/dpv/ai#LifecycleStage",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#DesignStage": {
            "label": "Design Stage",
            "definition": "The stage in the lifecycle where designs are created for the AI system",
            "broader": ("https://w3id.org/dpv/ai#LifecycleStage",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#DevelopmentStage": {
            "label": "Development Stage",
            "definition": "The stage in the lifecycle where the development and creation of the system occurs, signalling upon completion that it is ready for verification and validation",
            "broader": ("https://w3id.org/dpv/ai#LifecycleStage",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#DialogueManagement": {
            "label": "Dialogue Management",
            "definition": "Capability for shortening a portion of content such as text while retaining important semantic information",
            "broader": ("https://w3id.org/dpv/ai#LanguageCapability",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#DiscardStage": {
            "label": "Discard Stage",
            "definition": "The stage in the lifecycle where the AI system is being discarded as part of retirement",
            "broader": ("https://w3id.org/dpv/ai#RetirementStage",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#DistributedTrainingBias": {
            "label": "Distributed Training Bias",
            "definition": "Bias that occurs due to distributed machine having different sources of data that do not have the same distribution of feature space",
            "broader": ("https://w3id.org/dpv/ai#DataBias",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#EdgeAI": {
            "label": "Edge AI",
            "definition": "The deployment and execution of AI and ML models on Edge devices, including smartphones, IoT sensors, industrial controllers, and other resource-constrained devices located at the Edge of the network and closer to the data sources",
            "broader": ("https://w3id.org/dpv/ai#AISystem",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#EmotionRecognition": {
            "label": "Emotion Recognition",
            "definition": "Capability for identifying and categorising emotions expressed in a piece of text, speech, video or image or combination thereof",
            "broader": ("https://w3id.org/dpv/ai#HumanOrientedCapability",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#EngineeringDecisionBias": {
            "label": "Engineering Decision Bias",
            "definition": "Bias that occurs due to machine learning model architectures - encompassing all model specifications, parameters and manually designed features",
            "broader": ("https://w3id.org/dpv/ai#AIBias",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#ExpertSystem": {
            "label": "Expert System",
            "definition": "AI system that accumulates, combines and encapsulates knowledge provided by a human expert or experts in a specific domain to infer solutions to problems (ISO/IEC 22989:2022 definition); Artificial intelligence system emulating human expert decision-making abilities, addressing complex problems t...",
            "broader": ("https://w3id.org/dpv/ai#AISystem",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#ExplainabilityRisk": {
            "label": "Explainability Risk",
            "definition": "Risk that an AI's decisions or behaviors cannot be adequately understood, interpreted, or justified by relevant stakeholders.",
            "broader": ("https://w3id.org/dpv#RiskConcept",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#FaceRecognition": {
            "label": "Face Recognition",
            "definition": "Capability involving automatic pattern recognition for comparing stored images of human faces with the image of an actual face, indicating any matching, if it exists, and any data, if they exist, identifying the person to whom the face belongs",
            "broader": ("https://w3id.org/dpv/ai#BiometricCapability", "https://w3id.org/dpv/ai#ComputerVision"),
            "source_vocab": "such purposes are defined separately within the main DPV",
        },
        "https://w3id.org/dpv/ai#FeatureEngineeringBias": {
            "label": "Feature Engineering Bias",
            "definition": "Bias that occurs from steps such as encoding, data type conversion, dimensionality reduction and feature selection which are subject to choices made by the AI developer and introduce bias in the ML model",
            "broader": ("https://w3id.org/dpv/ai#EngineeringDecisionBias",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#FeedForwardNeuralNetwork": {
            "label": "Feed Forward Neural Network",
            "definition": "Neural network where information is fed from the input layer to the output layer in one direction only",
            "broader": ("https://w3id.org/dpv/ai#NeuralNetwork",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#FineTunedModel": {
            "label": "Fine-tuned Model",
            "definition": "Model resulting from fine-tuning of a pre-trained model",
            "broader": ("https://w3id.org/dpv/ai#TrainedModel",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#FrugalAISystem": {
            "label": "Frugal AI System",
            "definition": "AI systems intended to be more efficient, cost-effective, and accessible while maintaining or even improving their performance",
            "broader": ("https://w3id.org/dpv/ai#AISystem",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#FrugalMachineLearning": {
            "label": "Frugal Machine Learning",
            "definition": "Machine learning techniques that aim to make models more efficient, cost-effective, and accessible while maintaining or even improving their performance",
            "broader": ("https://w3id.org/dpv/ai#MachineLearning",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#GPAI": {
            "label": "General-Purpose AI System (GPAI)",
            "definition": "Artificial intelligence system based on a general-purpose model and capable of serving a variety of purposes, either in direct use or integrated with other AI systems",
            "broader": ("https://w3id.org/dpv/ai#AISystem",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#GPAIModel": {
            "label": "General Purpose AI Model",
            "definition": "A model that displays generality in terms of capabilities and potential applications",
            "broader": ("https://w3id.org/dpv/ai#Model",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#GenAI": {
            "label": "Generative AI",
            "definition": "Use of artificial intelligence models that can learn from and mimic large amounts of data to create content such as text, images, music, videos, code, and more, based on inputs or prompts",
            "broader": ("https://w3id.org/dpv/ai#AI",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#GeneticAlgorithm": {
            "label": "Genetic Algorithm",
            "definition": "Algorithm which simulates natural selection by creating and evolving a population of individuals (solutions) for optimization problems",
            "broader": ("https://w3id.org/dpv/ai#MachineLearning",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#GestureRecognition": {
            "label": "Gesture Recognition",
            "definition": "Capability for recognising human gestures",
            "broader": ("https://w3id.org/dpv/ai#BiometricCapability", "https://w3id.org/dpv/ai#ComputerVision"),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#HeuristicProgramming": {
            "label": "Heuristic Programming",
            "definition": "Programming approach designed to tackle problems for which there lacks a systematic or optimized approach, frequently used in expert systems",
            "broader": ("https://w3id.org/dpv/ai#RuleBasedTechnique",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#HumanIdentification": {
            "label": "Human Identification",
            "definition": "Capability of a system that identifies a human whether at an individual or group level",
            "broader": ("https://w3id.org/dpv/ai#HumanOrientedCapability",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#HumanOrientedCapability": {
            "label": "Human-Oriented Capability",
            "definition": "Capabilities that are inherently about humans or oriented towards human characteristics and activities",
            "broader": ("https://w3id.org/dpv/ai#Capability",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#HyperparameterTuningBias": {
            "label": "Hyperparameter Tuning Bias",
            "definition": "Bias that occurs from hyperparameters defining how the model is structured and which cannot be directly trained from the data like model parameters, where hyperparameters affect the model functioning and accuracy of the model",
            "broader": ("https://w3id.org/dpv/ai#EngineeringDecisionBias",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#ImageClassification": {
            "label": "Image Classification",
            "definition": "Capability of categorising and labelling groups of pixels or vectors within an image based on particular rules, involving the assignment of images to predefined classes or categories",
            "broader": ("https://w3id.org/dpv/ai#ComputerVision",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#ImageGeneration": {
            "label": "Image Generation",
            "definition": "Capability to generate image",
            "broader": ("https://w3id.org/dpv/ai#ContentGeneration",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#ImageRecognition": {
            "label": "Image Recognition",
            "definition": "Capability for image classification process that classifies object(s), pattern(s) or concept(s) in an image",
            "broader": ("https://w3id.org/dpv/ai#ComputerVision",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#InceptionStage": {
            "label": "Inception Stage",
            "definition": "The stage in the lifecycle where inception regarding AI occurs and one or more stakeholders decide to turn an idea into a tangible system",
            "broader": ("https://w3id.org/dpv/ai#LifecycleStage",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#IncidentMonitoringStage": {
            "label": "Incident Monitoring Stage",
            "definition": "The stage in the lifecycle where an AI system is actively being monitored for incidents",
            "broader": ("https://w3id.org/dpv/ai#OperationStage",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#InductiveProgramming": {
            "label": "Inductive Programming",
            "definition": "An algorithm or program featuring recursive calls or repetition control structures",
            "broader": ("https://w3id.org/dpv/ai#KnowledgeTechnique",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#IndustrialRobot": {
            "label": "Industrial Robot",
            "definition": "A robot or robotic system for use in industrial automation applications",
            "broader": ("https://w3id.org/dpv/ai#Robot",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#InformationRetrieval": {
            "label": "Information Retrieval (IR)",
            "definition": "Capability for retrieving relevant documents or parts of documents from a dataset, typically based on keyword or natural language queries",
            "broader": ("https://w3id.org/dpv/ai#Capability",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#InformativenessBias": {
            "label": "Informativeness Bias",
            "definition": "Bias that occurs or some groups, the mapping between inputs present in the data and outputs are more difficult to learn and where a model that only has one feature set available, can be biased against the group whose relationships are difficult to learn from available data",
            "broader": ("https://w3id.org/dpv/ai#EngineeringDecisionBias",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#InputDataBias": {
            "label": "Input Data Bias",
            "definition": "Concept representing input data containing or potentially containing bias",
            "broader": ("https://w3id.org/dpv/ai#InputDataRisk",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#InputDataInaccurate": {
            "label": "Input Data Inaccurate",
            "definition": "Concept representing input data being inaccurate",
            "broader": ("https://w3id.org/dpv/ai#InputDataRisk",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#InputDataInappropriate": {
            "label": "Input Data Inappropriate",
            "definition": "Concept representing input data being inappropriate",
            "broader": ("https://w3id.org/dpv/ai#InputDataRisk",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#InputDataIncomplete": {
            "label": "Input Data Incomplete",
            "definition": "Concept representing input data being incomplete",
            "broader": ("https://w3id.org/dpv/ai#InputDataRisk",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#InputDataInconsistent": {
            "label": "Input Data Inconsistent",
            "definition": "Concept representing input data being inconsistent",
            "broader": ("https://w3id.org/dpv/ai#InputDataRisk",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#InputDataMisclassified": {
            "label": "Input Data Misclassified",
            "definition": "Concept representing input data being misclassified",
            "broader": ("https://w3id.org/dpv/ai#InputDataRisk",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#InputDataMisinterpretation": {
            "label": "Input Data Misinterpretation",
            "definition": "Concept representing input data being misinterpreted",
            "broader": ("https://w3id.org/dpv/ai#InputDataRisk",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#InputDataNoise": {
            "label": "Input Data Noise",
            "definition": "Concept representing input data being noisy",
            "broader": ("https://w3id.org/dpv/ai#InputDataRisk",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#InputDataOutdated": {
            "label": "Input Data Outdated",
            "definition": "Concept representing input data being outdated",
            "broader": ("https://w3id.org/dpv/ai#InputDataRisk",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#InputDataRisk": {
            "label": "Input Data Risk",
            "definition": "Risks and risk concepts related to input data",
            "broader": ("https://w3id.org/dpv/ai#DataRisk",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#InputDataSelectionError": {
            "label": "Input Data Selection Error",
            "definition": "Concept representing an error in input data selection",
            "broader": ("https://w3id.org/dpv/ai#InputDataRisk",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#InputDataSparse": {
            "label": "Input Data Sparse",
            "definition": "Concept representing input data being sparse",
            "broader": ("https://w3id.org/dpv/ai#InputDataRisk",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#InputDataUnrepresentative": {
            "label": "Input Data Unrepresentative",
            "definition": "Concept representing input data being unrepresentative",
            "broader": ("https://w3id.org/dpv/ai#InputDataRisk",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#InputDataUnstructured": {
            "label": "Input Data Unstructured",
            "definition": "Concept representing input data being unstructured",
            "broader": ("https://w3id.org/dpv/ai#InputDataRisk",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#InputDataUnverified": {
            "label": "Input Data Unverified",
            "definition": "Concept representing input data being unverified",
            "broader": ("https://w3id.org/dpv/ai#InputDataRisk",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#IntelligentControlSystem": {
            "label": "Intelligent Control System",
            "definition": "Category of AI systems which implement intelligent control principles for real-world applications by using AI capabilities and techniques",
            "broader": ("https://w3id.org/dpv/ai#AISystem",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#KnowledgeRepresentation": {
            "label": "Knowledge Representation",
            "definition": "Encoding knowledge in a formal language or in a form that can be used for computer-based problem solving",
            "broader": ("https://w3id.org/dpv/ai#KnowledgeTechnique",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#KnowledgeTechnique": {
            "label": "Knowledge Technique",
            "definition": "Techniques based on the use of knowledge bases",
            "broader": ("https://w3id.org/dpv/ai#Technique",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#LLM": {
            "label": "Large Language Model (LLM)",
            "definition": "Deep learning model that uses artificial neural networks trained on vast amounts of data to understand and generate natural language and other types of content to perform a wide range of tasks",
            "broader": ("https://w3id.org/dpv/ai#Model",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#LanguageCapability": {
            "label": "Language Capability",
            "definition": "Capabilities related to languages",
            "broader": ("https://w3id.org/dpv/ai#Capability",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#LieDetection": {
            "label": "Lie Detection",
            "definition": "Capability to detect lies in the context of human speech, behaviour, information, or activities",
            "broader": ("https://w3id.org/dpv/ai#HumanOrientedCapability",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#LifecycleStage": {
            "label": "Lifecycle Stage",
            "definition": "A stage in the lifecycle of AI",
            "broader": ("https://w3id.org/dpv/tech#LifecycleStage",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#LocalBiometricIdentification": {
            "label": "Local Biometric Identification",
            "definition": "Capability involving biometric identification carried out locally",
            "broader": ("https://w3id.org/dpv/ai#BiometricIdentification",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#LogicTechnique": {
            "label": "Logic Technique",
            "definition": "Refers to logic based techniques",
            "broader": ("https://w3id.org/dpv/ai#Technique",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#LongShortTermMemory": {
            "label": "Long Short-Term Memory (LSTM)",
            "definition": "Type of recurrent neural network that processes sequential data with a satisfactory performance for both long and short span dependencies",
            "broader": ("https://w3id.org/dpv/ai#NeuralNetwork",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#MachineLearning": {
            "label": "Machine Learning",
            "definition": "Process of optimising model parameters through computational techniques, such that the model's behaviour reflects the data or experience",
            "broader": ("https://w3id.org/dpv/ai#Technique",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#MachineLearningModel": {
            "label": "Machine Learning Model",
            "definition": "Mathematical construct that generates an inference or prediction based on input data or information",
            "broader": ("https://w3id.org/dpv/ai#Model",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#MachineLearningPlatform": {
            "label": "Machine Learning Platform",
            "definition": "Technology platform for developing, deploying, and managing machine learning models and resources",
            "broader": ("https://w3id.org/dpv/tech#Platform",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#MachineTranslation": {
            "label": "Machine Translation",
            "definition": "Capability for automated translation of text or speech from one natural language to another using a computer system",
            "broader": ("https://w3id.org/dpv/ai#LanguageCapability",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#MissingFeaturesBias": {
            "label": "Missing Features Bias",
            "definition": "Bias that occurs when features are missing from individual training samples",
            "broader": ("https://w3id.org/dpv/ai#DataBias",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#Model": {
            "label": "Model",
            "definition": "Physical, mathematical or otherwise logical representation of a system, entity, phenomenon, process or data involving the use of AI techniques",
            "broader": ("https://w3id.org/dpv/ai#AI", "https://w3id.org/dpv/tech#Model"),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#ModelBias": {
            "label": "Model Bias",
            "definition": "Bias that occurs when ML uses functions like a maximum likelihood estimator to determine parameters, and there is data skew or under-representation present in the data, where the maximum likelihood estimation tends to amplify any underlying bias in the distribution",
            "broader": ("https://w3id.org/dpv/ai#EngineeringDecisionBias",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#ModelEvasion": {
            "label": "Model Evasion",
            "definition": "An input, which seems normal for a human but is wrongly classified by ML models",
            "broader": ("https://w3id.org/dpv/ai#SecurityAttack",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#ModelExpressivenessBias": {
            "label": "Model Expressiveness Bias",
            "definition": "Bias that occurs from the number and nature of parameters in a model as well as the neural network topology which affect the expressiveness of the model and any feature that affects model expressiveness differently across groups",
            "broader": ("https://w3id.org/dpv/ai#ModelInteractionBias",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#ModelFineTuning": {
            "label": "Model Fine-Tuning",
            "definition": "Process where a pre-trained model is further refined through the use of a smaller training dataset",
            "broader": ("https://w3id.org/dpv#Transform", "https://w3id.org/dpv/ai#ModelTraining"),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#ModelInteractionBias": {
            "label": "Model Interaction Bias",
            "definition": "Bias that occurs from the structure of a model to create biased predictions",
            "broader": ("https://w3id.org/dpv/ai#EngineeringDecisionBias",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#ModelInversion": {
            "label": "Model Inversion",
            "definition": "A type of attack to AI models, in which the access to a model is abused to infer information about the training data",
            "broader": ("https://w3id.org/dpv/ai#SecurityAttack",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#ModelRisk": {
            "label": "Model Risk",
            "definition": "Risks associated with AI Models",
            "broader": ("https://w3id.org/dpv/ai#RiskConcept",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#ModelTraining": {
            "label": "Model Training",
            "definition": "Process to determine or to improve the parameters of a machine learning model based on a machine learning technique by using training data",
            "broader": ("https://w3id.org/dpv#Transform",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#MotionAnalysis": {
            "label": "Motion Analysis",
            "definition": "Capability of deriving meaningful information about motion from visual data, including tracking objects across frames, analysing trajectories, estimating velocity and acceleration, and interpreting the meaning of motion patterns",
            "broader": ("https://w3id.org/dpv/ai#ComputerVision",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#MultiModalRetrieval": {
            "label": "Multi-modal Retrieval",
            "definition": "Capability for retrieval of information using multiple modalities such as text, images, audio, and video and supporting cross-modal queries such as taking text as input to search images",
            "broader": ("https://w3id.org/dpv/ai#InformationRetrieval",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#MusicInformationRetrieval": {
            "label": "Music Information Retrieval (MIR)",
            "definition": "Capability for retrieving, analysing, and categorising music-related information such as audio files, melodies, or lyrics using audio features, metadata, and user queries",
            "broader": ("https://w3id.org/dpv/ai#InformationRetrieval",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#NamedEntityRecognition": {
            "label": "Named Entity Recognition",
            "definition": "Capability for recognising and labelling the denotational names of entities and their categories for sequences of words in a stream of text or speech",
            "broader": ("https://w3id.org/dpv/ai#LanguageCapability",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#NarrowAI": {
            "label": "Narrow AI",
            "definition": "Type of AI system that is focused on defined tasks to address a specific problem i.e. it addresses a narrow scope of tasks and problems",
            "broader": ("https://w3id.org/dpv/ai#AISystem",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#NaturalLanguageGeneration": {
            "label": "Natural Language Generation",
            "definition": "Converting data carrying semantics into natural language",
            "broader": ("https://w3id.org/dpv/ai#LanguageCapability",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#NaturalLanguageProcessing": {
            "label": "Natural Language Processing",
            "definition": "Capability enabling computers to understand and communicate with human language",
            "broader": ("https://w3id.org/dpv/ai#LanguageCapability",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#NeuralNetwork": {
            "label": "Neural Network",
            "definition": "Network of one or more layers of neurons connected by weighted links with adjustable weights, which takes input data and produces an output",
            "broader": ("https://w3id.org/dpv/ai#MachineLearning",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#NonRepresentativeSamplingBias": {
            "label": "Non-Representative Sampling Bias",
            "definition": "Bias that occurs if a dataset is not representative of the intended deployment environment, where the model learns biases based on the ways in which the data is non-representative",
            "broader": ("https://w3id.org/dpv/ai#DataBias",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#ObjectDetection": {
            "label": "Object Detection",
            "definition": "computer vision technology that detects instances of semantic objects in digital images and videos, covering domains like face detection and pedestrian detection, with applications spanning image retrieval and video surveillance",
            "broader": ("https://w3id.org/dpv/ai#ComputerVision",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#ObjectRecognition": {
            "label": "Object Recognition",
            "definition": "Capability to recognise objects",
            "broader": ("https://w3id.org/dpv/ai#ComputerVision",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#OperationStage": {
            "label": "Operation Stage",
            "definition": "The stage in the lifecycle where an AI system is running and generally available for operations",
            "broader": ("https://w3id.org/dpv/ai#LifecycleStage",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#OptimisationMethod": {
            "label": "Optimisation Method",
            "definition": "Refers to optimisation Method",
            "broader": ("https://w3id.org/dpv/ai#StatisticalTechnique",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#PartOfSpeechTagging": {
            "label": "Part Of Speech Tagging",
            "definition": "Capability for assigning a category (e.g. verb, noun, adjective) to a word based on its grammatical properties",
            "broader": ("https://w3id.org/dpv/ai#LanguageCapability",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#PatternRecognition": {
            "label": "Pattern Recognition",
            "definition": "Capability for automated identification of patterns and regularities in data, utilising algorithms to detect patterns or regularities for categorising data into distinct groups, encompassing diverse applications such as image analysis, speech processing, and biometric authentication",
            "broader": ("https://w3id.org/dpv/ai#ComputerVision",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#PerceptionBasedAI": {
            "label": "Perception-based AI",
            "definition": "Capability of using agents to interpret and understand information from their environment through sensory inputs",
            "broader": ("https://w3id.org/dpv/ai#ComputerVision",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#PersonalityTraitAnalysis": {
            "label": "Personality Trait Analysis",
            "definition": "Capability for determining and analysing people's personality traits",
            "broader": ("https://w3id.org/dpv/ai#HumanOrientedCapability",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#PostTimeBiometricIdentification": {
            "label": "Post-Time Biometric Identification",
            "definition": "Capability involving biometric identification carried out later or not in real-time or non-instantaneously",
            "broader": ("https://w3id.org/dpv/ai#BiometricIdentification",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#Profiling": {
            "label": "Profiling",
            "definition": "Capability where AI is used to construct a profile of an individual (human) or a group of individuals",
            "broader": ("https://w3id.org/dpv#Profiling", "https://w3id.org/dpv/ai#HumanOrientedCapability"),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#QuestionAnswering": {
            "label": "Question Answering",
            "definition": "Capability for determining the most appropriate answer to a question provided in natural language",
            "broader": ("https://w3id.org/dpv/ai#LanguageCapability",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#RealTimeBiometricIdentification": {
            "label": "Real-Time Biometric Identification",
            "definition": "Capability involving biometric identification carried out in real-time or instantaneously",
            "broader": ("https://w3id.org/dpv/ai#BiometricIdentification",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#ReasoningSystem": {
            "label": "Reasoning System",
            "definition": "Artificial intelligence systems that uses available information to generate predictions, make inferences and draw conclusions, involving the representation of data in machine-processable form and application of logic to arrive at decisions",
            "broader": ("https://w3id.org/dpv/ai#AISystem",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#ReasoningTechnique": {
            "label": "Reasoning Technique",
            "definition": "Refers to reasoning techniques",
            "broader": ("https://w3id.org/dpv/ai#Technique",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#RecurrentNeuralNetwork": {
            "label": "Recurrent Neural Network (RNN)",
            "definition": "Neural network in which outputs from both the previous layer and the previous processing step are fed into the current layer",
            "broader": ("https://w3id.org/dpv/ai#NeuralNetwork",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#ReevaluationStage": {
            "label": "Reevaluation Stage",
            "definition": "The stage in the lifecycle where the AI system is reevaluated after the operation and monitoring stage based on the operations of the AI system",
            "broader": ("https://w3id.org/dpv/ai#LifecycleStage",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#ReinforcementLearning": {
            "label": "Reinforcement Learning",
            "definition": "Learning of an optimal sequence of actions to maximise a reward through interaction with an environment",
            "broader": ("https://w3id.org/dpv/ai#MachineLearning",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#RelationshipExtraction": {
            "label": "Relationship Extraction",
            "definition": "Capability for identifying relationships among entities mentioned in a text",
            "broader": ("https://w3id.org/dpv/ai#LanguageCapability",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#RemoteBiometricIdentification": {
            "label": "Remote Biometric Identification",
            "definition": "Capability involving biometric identification carried out remotely",
            "broader": ("https://w3id.org/dpv/ai#BiometricIdentification",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#RemoteSensing": {
            "label": "Remote Sensing",
            "definition": "Capability for acquisition of information about an object or phenomenon without physical contact, typically using aerial sensor technologies",
            "broader": ("https://w3id.org/dpv/ai#PerceptionBasedAI",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#RepairStage": {
            "label": "Repair Stage",
            "definition": "The stage in the lifecycle where an AI system is being repaired due to suspected or occurred incidents",
            "broader": ("https://w3id.org/dpv/ai#OperationStage",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#ReplaceStage": {
            "label": "Replace Stage",
            "definition": "The stage in the lifecycle where the AI system is being replaced as part of retirement",
            "broader": ("https://w3id.org/dpv/ai#RetirementStage",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#RetirementStage": {
            "label": "Retirement Stage",
            "definition": "The stage in the lifecycle where the AI system is retired and becomes obsolete",
            "broader": ("https://w3id.org/dpv/ai#LifecycleStage",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#RiskConcept": {
            "label": "RiskConcept",
            "definition": "Risk concepts such as risk sources, risks, consequences, and impacts associated specifically with development, use, or operation of AI",
            "broader": ("https://w3id.org/dpv#RiskConcept",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#Robot": {
            "label": "Robot",
            "definition": "An automation system with actuators that performs intended tasks in the physical world, by means of sensing its environment and a software control system",
            "broader": ("https://w3id.org/dpv/ai#AISystem",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#RoboticProcessAutomation": {
            "label": "Robotic Process Automation",
            "definition": "Technology focused on automation of repetitive, routine, rule-based human tasks",
            "broader": ("https://w3id.org/dpv/ai#AISystem",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#Robotics": {
            "label": "Robotics",
            "definition": "The science of designing, engineering and using robots, i.e. machines controlled by computers which perform jobs automatically",
            "broader": ("https://w3id.org/dpv/ai#AISystem",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#RuleBasedTechnique": {
            "label": "Rule Technique",
            "definition": "Artificial intelligence approach governed by human-defined rules that explicitly dictate behaviour, relying on logical statements (rules) to determine actions in specific situations",
            "broader": ("https://w3id.org/dpv/ai#KnowledgeTechnique",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#SearchMethod": {
            "label": "Search Method",
            "definition": "Refers to statistical-based search Methods",
            "broader": ("https://w3id.org/dpv/ai#StatisticalTechnique",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#SecurityAttack": {
            "label": "Security Attack",
            "definition": "Risks or issues associated with security attacks related to AI technologies, models, and systems",
            "broader": ("https://w3id.org/dpv/ai#RiskConcept",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#SelfSupervisedLearning": {
            "label": "Self-Supervised Learning",
            "definition": "Machine learning approach that uses unsupervised learning for tasks that typically require supervision, generating implicit labels from unstructured data, where models are trained on a task using the data itself to provide supervisory signals, often used in neural networks to exploit inherent str...",
            "broader": ("https://w3id.org/dpv/ai#MachineLearning",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#SemiSupervisedLearning": {
            "label": "Semi Supervised Learning",
            "definition": "Machine learning that makes use of both labelled and unlabelled data during training",
            "broader": ("https://w3id.org/dpv/ai#MachineLearning",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#SentimentAnalysis": {
            "label": "Sentiment Analysis",
            "definition": "Capability for computationally identifying and categorising opinions expressed in a piece of text, speech or image, to determine a range of feeling such as from positive to negative",
            "broader": (
                "https://w3id.org/dpv/ai#HumanOrientedCapability",
                "https://w3id.org/dpv/ai#LanguageCapability",
            ),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#ServiceRobot": {
            "label": "Service Robot",
            "definition": "A robot or robotic system in personal use or professional use that performs useful tasks for humans or equipment",
            "broader": ("https://w3id.org/dpv/ai#Robot",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#SocialRobot": {
            "label": "Social Robot",
            "definition": "A robot or robotic system with social interaction functions",
            "broader": ("https://w3id.org/dpv/ai#Robot",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#SoundSourceSeparation": {
            "label": "Sound Source Separation",
            "definition": "Capability for extracting individual sound from audio recordings",
            "broader": ("https://w3id.org/dpv/ai#AudioCapability",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#SoundSynthesis": {
            "label": "Sound Synthesis",
            "definition": "Capability for generation of artificial sound",
            "broader": ("https://w3id.org/dpv/ai#AudioCapability", "https://w3id.org/dpv/ai#ContentGeneration"),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#SpeakerRecognition": {
            "label": "Speaker Recognition",
            "definition": "Capability of recognising speaker(s) in audio recordings",
            "broader": ("https://w3id.org/dpv/ai#AudioProcessing", "https://w3id.org/dpv/ai#HumanOrientedCapability"),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#SpeechRecognition": {
            "label": "Speech Recognition",
            "definition": "Capability of converting a speech signal to a representation of the content of the speech",
            "broader": ("https://w3id.org/dpv/ai#AudioProcessing", "https://w3id.org/dpv/ai#HumanOrientedCapability"),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#SpeechSynthesis": {
            "label": "Speech Synthesis",
            "definition": "Capability for generation of artificial speech",
            "broader": ("https://w3id.org/dpv/ai#AudioCapability", "https://w3id.org/dpv/ai#ContentGeneration"),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#StatisticalTechnique": {
            "label": "Statistical Technique",
            "definition": "Refers to techniques that are based on statistics",
            "broader": ("https://w3id.org/dpv/ai#Technique",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#SupervisedLearning": {
            "label": "Supervised Learning",
            "definition": "Machine learning that makes only use of labelled data during training",
            "broader": ("https://w3id.org/dpv/ai#MachineLearning",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#SupportVectorMachine": {
            "label": "Support Vector Machine",
            "definition": "A machine learning algorithm that finds decision boundaries with maximal margins",
            "broader": ("https://w3id.org/dpv/ai#MachineLearning",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#SymbolicReasoning": {
            "label": "Symbolic Reasoning",
            "definition": "Reasoning based on the knowledge encoded in a formal language",
            "broader": ("https://w3id.org/dpv/ai#KnowledgeTechnique",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#Technique": {
            "label": "Technique",
            "definition": "The underlying technological algorithm, method, or process that forms the technique for using or applying AI",
            "broader": ("https://w3id.org/dpv/ai#AI",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#TestingData": {
            "label": "Testing Data",
            "definition": "Data involved in the testing of an AI system or model",
            "broader": ("https://w3id.org/dpv/ai#Data",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#TestingDataBias": {
            "label": "Testing Data Bias",
            "definition": "Concept representing testing data containing or potentially containing bias",
            "broader": ("https://w3id.org/dpv/ai#TestingDataRisk",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#TestingDataInaccurate": {
            "label": "Testing Data Inaccurate",
            "definition": "Concept representing testing data being inaccurate",
            "broader": ("https://w3id.org/dpv/ai#TestingDataRisk",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#TestingDataInappropriate": {
            "label": "Testing Data Inappropriate",
            "definition": "Concept representing testing data being inappropriate",
            "broader": ("https://w3id.org/dpv/ai#TestingDataRisk",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#TestingDataIncomplete": {
            "label": "Testing Data Incomplete",
            "definition": "Concept representing testing data being incomplete",
            "broader": ("https://w3id.org/dpv/ai#TestingDataRisk",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#TestingDataInconsistent": {
            "label": "Testing Data Inconsistent",
            "definition": "Concept representing testing data being inconsistent",
            "broader": ("https://w3id.org/dpv/ai#TestingDataRisk",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#TestingDataMisclassified": {
            "label": "Testing Data Misclassified",
            "definition": "Concept representing testing data being misclassified",
            "broader": ("https://w3id.org/dpv/ai#TestingDataRisk",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#TestingDataMisinterpretation": {
            "label": "Testing Data Misinterpretation",
            "definition": "Concept representing testing data being misinterpreted",
            "broader": ("https://w3id.org/dpv/ai#TestingDataRisk",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#TestingDataNoise": {
            "label": "Testing Data Noise",
            "definition": "Concept representing testing data being noisy",
            "broader": ("https://w3id.org/dpv/ai#TestingDataRisk",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#TestingDataOutdated": {
            "label": "Testing Data Outdated",
            "definition": "Concept representing testing data being outdated",
            "broader": ("https://w3id.org/dpv/ai#TestingDataRisk",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#TestingDataRisk": {
            "label": "Testing Data Risk",
            "definition": "Risks and risk concepts related to testing data",
            "broader": ("https://w3id.org/dpv/ai#DataRisk",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#TestingDataSelectionError": {
            "label": "Testing Data Selection Error",
            "definition": "Concept representing an error in testing data selection",
            "broader": ("https://w3id.org/dpv/ai#TestingDataRisk",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#TestingDataSparse": {
            "label": "Testing Data Sparse",
            "definition": "Concept representing testing data being sparse",
            "broader": ("https://w3id.org/dpv/ai#TestingDataRisk",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#TestingDataUnrepresentative": {
            "label": "Testing Data Unrepresentative",
            "definition": "Concept representing testing data being unrepresentative",
            "broader": ("https://w3id.org/dpv/ai#TestingDataRisk",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#TestingDataUnstructured": {
            "label": "Testing Data Unstructured",
            "definition": "Concept representing testing data being unstructured",
            "broader": ("https://w3id.org/dpv/ai#TestingDataRisk",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#TestingDataUnverified": {
            "label": "Testing Data Unverified",
            "definition": "Concept representing testing data being unverified",
            "broader": ("https://w3id.org/dpv/ai#TestingDataRisk",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#TextClassification": {
            "label": "Text Classification",
            "definition": "Capability of assigning predefined labels to text data in order to automatically categorise it into groups",
            "broader": ("https://w3id.org/dpv/ai#NaturalLanguageProcessing",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#TextDataMining": {
            "label": "Text and Data Mining",
            "definition": "Capability of selecting and analysing large amounts of text or data resources to discover patterns, relationships, and semantic insights that provide valuable information for research and decision-making",
            "broader": ("https://w3id.org/dpv/ai#NaturalLanguageProcessing",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#TrainedModel": {
            "label": "Trained Model",
            "definition": "Model resulted from model training",
            "broader": ("https://w3id.org/dpv/ai#Model",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#TrainingData": {
            "label": "Training Data",
            "definition": "Data involved in the training of an AI system or model",
            "broader": ("https://w3id.org/dpv/ai#Data",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#TrainingTechnique": {
            "label": "Training Technique",
            "definition": "Process to determine or to improve the parameters of a machine learning model based on a machine learning algorithm by using training data",
            "broader": ("https://w3id.org/dpv#Use",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#TransferLearning": {
            "label": "TransferLearning",
            "definition": "a technique in machine learning in which knowledge learned from a task is re-used in order to boost performance on a related task",
            "broader": ("https://w3id.org/dpv/ai#DeepLearning",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#TransparencyRisk": {
            "label": "Transparency Risk",
            "definition": "Risk that an AI's design, performance, outputs, or other characteristics are not sufficiently transparent",
            "broader": ("https://w3id.org/dpv#RiskConcept",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#UnsupervisedLearning": {
            "label": "Unsupervised Learning",
            "definition": "Machine learning that makes only use of unlabelled data during training",
            "broader": ("https://w3id.org/dpv/ai#MachineLearning",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#UpdateStage": {
            "label": "Update Stage",
            "definition": "The stage in the lifecycle where an AI system is being or has been updated",
            "broader": ("https://w3id.org/dpv/ai#OperationStage",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#UserRisk": {
            "label": "User Risk",
            "definition": "Risks associated with Users of AI Systems",
            "broader": ("https://w3id.org/dpv/ai#RiskConcept",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#ValidationData": {
            "label": "Validation Data",
            "definition": "Data involved in the validation of an AI system or model",
            "broader": ("https://w3id.org/dpv/ai#Data",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#ValidationDataBias": {
            "label": "Validation Data Bias",
            "definition": "Concept representing validation data containing or potentially containing bias",
            "broader": ("https://w3id.org/dpv/ai#ValidationDataRisk",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#ValidationDataInaccurate": {
            "label": "Validation Data Inaccurate",
            "definition": "Concept representing validation data being inaccurate",
            "broader": ("https://w3id.org/dpv/ai#ValidationDataRisk",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#ValidationDataInappropriate": {
            "label": "Validation Data Inappropriate",
            "definition": "Concept representing validation data being inappropriate",
            "broader": ("https://w3id.org/dpv/ai#ValidationDataRisk",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#ValidationDataIncomplete": {
            "label": "Validation Data Incomplete",
            "definition": "Concept representing validation data being incomplete",
            "broader": ("https://w3id.org/dpv/ai#ValidationDataRisk",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#ValidationDataInconsistent": {
            "label": "Validation Data Inconsistent",
            "definition": "Concept representing validation data being inconsistent",
            "broader": ("https://w3id.org/dpv/ai#ValidationDataRisk",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#ValidationDataMisclassified": {
            "label": "Validation Data Misclassified",
            "definition": "Concept representing validation data being misclassified",
            "broader": ("https://w3id.org/dpv/ai#ValidationDataRisk",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#ValidationDataMisinterpretation": {
            "label": "Validation Data Misinterpretation",
            "definition": "Concept representing validation data being misinterpreted",
            "broader": ("https://w3id.org/dpv/ai#ValidationDataRisk",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#ValidationDataNoise": {
            "label": "Validation Data Noise",
            "definition": "Concept representing validation data being noisy",
            "broader": ("https://w3id.org/dpv/ai#ValidationDataRisk",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#ValidationDataOutdated": {
            "label": "Validation Data Outdated",
            "definition": "Concept representing validation data being outdated",
            "broader": ("https://w3id.org/dpv/ai#ValidationDataRisk",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#ValidationDataRisk": {
            "label": "Validation Data Risk",
            "definition": "Risks and risk concepts related to validation data",
            "broader": ("https://w3id.org/dpv/ai#DataRisk",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#ValidationDataSelectionError": {
            "label": "Validation Data Selection Error",
            "definition": "Concept representing an error in validation data selection",
            "broader": ("https://w3id.org/dpv/ai#ValidationDataRisk",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#ValidationDataSparse": {
            "label": "Validation Data Sparse",
            "definition": "Concept representing validation data being sparse",
            "broader": ("https://w3id.org/dpv/ai#ValidationDataRisk",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#ValidationDataUnrepresentative": {
            "label": "Validation Data Unrepresentative",
            "definition": "Concept representing validation data being unrepresentative",
            "broader": ("https://w3id.org/dpv/ai#ValidationDataRisk",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#ValidationDataUnstructured": {
            "label": "Validation Data Unstructured",
            "definition": "Concept representing validation data being unstructured",
            "broader": ("https://w3id.org/dpv/ai#ValidationDataRisk",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#ValidationDataUnverified": {
            "label": "Validation Data Unverified",
            "definition": "Concept representing validation data being unverified",
            "broader": ("https://w3id.org/dpv/ai#ValidationDataRisk",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#ValidationStage": {
            "label": "Validation Stage",
            "definition": "The stage in the lifecycle where the AI system is validated for requirements and objectives for an intended use or application",
            "broader": ("https://w3id.org/dpv/ai#LifecycleStage",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#VerificationStage": {
            "label": "Verification Stage",
            "definition": "The stage in the lifecycle where the AI system is being verified to satisfy requirements and meet objectives",
            "broader": ("https://w3id.org/dpv/ai#LifecycleStage",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#VideoGeneration": {
            "label": "Video Generation",
            "definition": "Capability to generate video",
            "broader": ("https://w3id.org/dpv/ai#ContentGeneration",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#VisualRecognition": {
            "label": "Visual Recognition",
            "definition": "Capability that identifies and categorises objects, scenes, activities, and other visual elements in images or video, and includes image classification, object detection, scene understanding, and visual pattern recognition",
            "broader": ("https://w3id.org/dpv/ai#ComputerVision",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#hasAI": {
            "label": "has AI",
            "definition": "Indicates the use of AI for the associated context",
            "broader": ("https://w3id.org/dpv#isImplementedUsingTechnology",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#hasAISystem": {
            "label": "has AI system",
            "definition": "Indicates the use of AI system for the associated context",
            "broader": ("https://w3id.org/dpv/ai#hasAI",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#hasCapability": {
            "label": "has capability",
            "definition": "Indicates the use of AI capability for the associated context",
            "broader": ("https://w3id.org/dpv/ai#hasAI",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#hasData": {
            "label": "has data",
            "definition": "Associates data with an AI system or model or implementation",
            "broader": ("https://w3id.org/dpv#hasData",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#hasGPAIModel": {
            "label": "has GPAI model",
            "definition": "Indicates the use of an GPAI model for the associated context",
            "broader": ("https://w3id.org/dpv/ai#hasModel",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#hasModel": {
            "label": "has model",
            "definition": "Indicates the use of an AI model for the associated context",
            "broader": ("https://w3id.org/dpv/ai#hasAI",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#hasTechnique": {
            "label": "has technique",
            "definition": "Indicates the use of AI technique for the associated context",
            "broader": ("https://w3id.org/dpv/ai#hasAI",),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#hasTestingData": {
            "label": "has testing data",
            "definition": "Associates the data used for testing AI",
            "broader": ("https://w3id.org/dpv/ai#hasData", "https://w3id.org/dpv/tech#hasInputData"),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#hasTrainingData": {
            "label": "has training data",
            "definition": "Associates the data used for training AI",
            "broader": ("https://w3id.org/dpv/ai#hasData", "https://w3id.org/dpv/tech#hasInputData"),
            "source_vocab": "ai",
        },
        "https://w3id.org/dpv/ai#hasValidationData": {
            "label": "has validation data",
            "definition": "Associates the data used for validating AI",
            "broader": ("https://w3id.org/dpv/ai#hasData", "https://w3id.org/dpv/tech#hasInputData"),
            "source_vocab": "ai",
        },
    }
)

__all__ = [
    "AGI",
    "AI",
    "GPAI",
    "LLM",
    "AIAgent",
    "AIBias",
    "AICapability",
    "AILifecycleStage",
    "AIProcess",
    "AISystem",
    "AISystemRisk",
    "AISystemType",
    "AITechnique",
    "ActionRecognition",
    "AdversarialAttack",
    "AlgorithmSelectionBias",
    "AudioCapability",
    "AudioGeneration",
    "AudioProcessing",
    "AutomaticSummarisation",
    "AutomationBias",
    "BayesianEstimation",
    "BayesianNetwork",
    "BayesianOptimisation",
    "BehaviourAnalysis",
    "Benchmarking",
    "BiasAssessment",
    "BiasDetection",
    "BiasMitigation",
    "BiasPrevention",
    "BiometricCapability",
    "BiometricCategorisation",
    "BiometricEmotionRecognition",
    "BiometricIdentification",
    "Capability",
    "ChatbotCapability",
    "CognitiveComputing",
    "ComputationalCreativity",
    "ComputerVision",
    "ContentBasedRetrieval",
    "ContentGeneration",
    "ContextAwareRetrieval",
    "ContinuousValidationStage",
    "ConvolutionalNeuralNetwork",
    "CyberphysicalSystem",
    "Data",
    "DataAggregation",
    "DataAggregationBias",
    "DataAnnotation",
    "DataBias",
    "DataCleaning",
    "DataCollection",
    "DataEnrichment",
    "DataLabelling",
    "DataLabellingProcessBias",
    "DataOperation",
    "DataPoisoning",
    "DataPreparation",
    "DataRisk",
    "DataUpdating",
    "DecisionTree",
    "DecommissionStage",
    "DeepLearning",
    "DeploymentStage",
    "DesignStage",
    "DevelopmentStage",
    "DialogueManagement",
    "DiscardStage",
    "DistributedTrainingBias",
    "EdgeAI",
    "EmotionRecognition",
    "EngineeringDecisionBias",
    "ExpertSystem",
    "ExplainabilityRisk",
    "FaceRecognition",
    "FeatureEngineeringBias",
    "FeedForwardNeuralNetwork",
    "FineTunedModel",
    "FrugalAISystem",
    "FrugalMachineLearning",
    "GPAIModel",
    "GenAI",
    "GeneticAlgorithm",
    "GestureRecognition",
    "HeuristicProgramming",
    "HumanIdentification",
    "HumanOrientedCapability",
    "HyperparameterTuningBias",
    "ImageClassification",
    "ImageGeneration",
    "ImageRecognition",
    "InceptionStage",
    "IncidentMonitoringStage",
    "InductiveProgramming",
    "IndustrialRobot",
    "InformationRetrieval",
    "InformativenessBias",
    "InputDataBias",
    "InputDataInaccurate",
    "InputDataInappropriate",
    "InputDataIncomplete",
    "InputDataInconsistent",
    "InputDataMisclassified",
    "InputDataMisinterpretation",
    "InputDataNoise",
    "InputDataOutdated",
    "InputDataRisk",
    "InputDataSelectionError",
    "InputDataSparse",
    "InputDataUnrepresentative",
    "InputDataUnstructured",
    "InputDataUnverified",
    "IntelligentControlSystem",
    "KnowledgeRepresentation",
    "KnowledgeTechnique",
    "LanguageCapability",
    "LieDetection",
    "LifecycleStage",
    "LocalBiometricIdentification",
    "LogicTechnique",
    "LongShortTermMemory",
    "MachineLearning",
    "MachineLearningModel",
    "MachineLearningPlatform",
    "MachineTranslation",
    "MissingFeaturesBias",
    "Model",
    "ModelBias",
    "ModelEvasion",
    "ModelExpressivenessBias",
    "ModelFineTuning",
    "ModelInteractionBias",
    "ModelInversion",
    "ModelRisk",
    "ModelTraining",
    "MotionAnalysis",
    "MultiModalRetrieval",
    "MusicInformationRetrieval",
    "NamedEntityRecognition",
    "NarrowAI",
    "NaturalLanguageGeneration",
    "NaturalLanguageProcessing",
    "NeuralNetwork",
    "NonRepresentativeSamplingBias",
    "ObjectDetection",
    "ObjectRecognition",
    "OperationStage",
    "OptimisationMethod",
    "PartOfSpeechTagging",
    "PatternRecognition",
    "PerceptionBasedAI",
    "PersonalityTraitAnalysis",
    "PostTimeBiometricIdentification",
    "Profiling",
    "QuestionAnswering",
    "RealTimeBiometricIdentification",
    "ReasoningSystem",
    "ReasoningTechnique",
    "RecurrentNeuralNetwork",
    "ReevaluationStage",
    "ReinforcementLearning",
    "RelationshipExtraction",
    "RemoteBiometricIdentification",
    "RemoteSensing",
    "RepairStage",
    "ReplaceStage",
    "RetirementStage",
    "RiskConcept",
    "Robot",
    "RoboticProcessAutomation",
    "Robotics",
    "RuleBasedTechnique",
    "SearchMethod",
    "SecurityAttack",
    "SelfSupervisedLearning",
    "SemiSupervisedLearning",
    "SentimentAnalysis",
    "ServiceRobot",
    "SocialRobot",
    "SoundSourceSeparation",
    "SoundSynthesis",
    "SpeakerRecognition",
    "SpeechRecognition",
    "SpeechSynthesis",
    "StatisticalTechnique",
    "SupervisedLearning",
    "SupportVectorMachine",
    "SymbolicReasoning",
    "Technique",
    "TestingData",
    "TestingDataBias",
    "TestingDataInaccurate",
    "TestingDataInappropriate",
    "TestingDataIncomplete",
    "TestingDataInconsistent",
    "TestingDataMisclassified",
    "TestingDataMisinterpretation",
    "TestingDataNoise",
    "TestingDataOutdated",
    "TestingDataRisk",
    "TestingDataSelectionError",
    "TestingDataSparse",
    "TestingDataUnrepresentative",
    "TestingDataUnstructured",
    "TestingDataUnverified",
    "TextClassification",
    "TextDataMining",
    "TrainedModel",
    "TrainingData",
    "TrainingTechnique",
    "TransferLearning",
    "TransparencyRisk",
    "UnsupervisedLearning",
    "UpdateStage",
    "UserRisk",
    "ValidationData",
    "ValidationDataBias",
    "ValidationDataInaccurate",
    "ValidationDataInappropriate",
    "ValidationDataIncomplete",
    "ValidationDataInconsistent",
    "ValidationDataMisclassified",
    "ValidationDataMisinterpretation",
    "ValidationDataNoise",
    "ValidationDataOutdated",
    "ValidationDataRisk",
    "ValidationDataSelectionError",
    "ValidationDataSparse",
    "ValidationDataUnrepresentative",
    "ValidationDataUnstructured",
    "ValidationDataUnverified",
    "ValidationStage",
    "VerificationStage",
    "VideoGeneration",
    "VisualRecognition",
    "hasAI",
    "hasAISystem",
    "hasCapability",
    "hasData",
    "hasGPAIModel",
    "hasModel",
    "hasTechnique",
    "hasTestingData",
    "hasTrainingData",
    "hasValidationData",
]
