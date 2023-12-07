from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:
    feature_store_file_path:str
    train_file_path:str
    test_file_path:str


class DataTransformationArtifact:
    report_file_path:str
    
class ModelTrainerArtifact:...
class ModelEvaluationArtifact:...
class MOdelPusherArtifact:...