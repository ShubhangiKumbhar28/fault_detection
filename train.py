from sensor.pipeline.training_pipeline import start_traninig_pipeline

file_path="D:/AllFam/ML/fault-detection/aps_failure_training_set1.csv"
print(__name__)

if __name__=="__main__":
    try:
        start_traninig_pipeline()
    except Exception as e:
        print(e)