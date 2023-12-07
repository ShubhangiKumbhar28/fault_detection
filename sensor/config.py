import pymongo
import pandas as pd
import json
from dataclasses import dataclass
import os

## Provide the mongodb localhost url to connect python to mongodb.

@dataclass
class EnvironmentVariable:
    mongodb_url:str = os.getenv("MONGODB_URL")
    aws_access_key_id:str = os.getenv("AWS_ACCESS_KEY_ID")



env_var = EnvironmentVariable()

mongo_client = pymongo.MongoClient(env_var.mongodb_url)