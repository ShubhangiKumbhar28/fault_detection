import pymongo
import pandas as pd
import json

## Provide the mongodb localhost url to connect python to mongodb.

client = pymongo.MongoClient("mongodb+srv://shubhangikumbhar28:Shubhangi@cluster0.kakvj4a.mongodb.net/")
DATA_FILE_PATH = "D:/AllFam/ML/fault-detection/aps_failure_training_set1.csv"
DATABASE_NAME="aps"
COLLECTION_NAME="sensor"

if __name__=="__main__":
    df = pd.read_csv(DATA_FILE_PATH)
    print(f"Rows and columns : {df.shape}")

    ## convert dataframe into json format so that we can dump dataframe into mongoDB
    df.reset_index(drop=True, inplace=True)

    json_record = list(json.loads(df.T.to_json()).values()) #each record is one row in list
    print(json_record[0]) # one record

    ## insert converted json record to mongoDB
    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)
    print("json_record inserted into mongoDB successfully")