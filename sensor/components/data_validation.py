from sensor.entity import artifact_entity,config_entity
from sensor.exception import SensorException
from sensor.logger import logging
from scipy.stats import ks_2samp
import os,sys
import pandas as pd
from typing import Optional

class DataValidation:
    def __init__(self,data_validation_config:config_entity.DataIngestionConfig):
        try:
            logging.info(f"{'>>'*20} Data validation {'<<'*20}")
            self.data_validation_config = data_validation_config
        except Exception as e:
            raise SensorException
        
    def is_required_columns_exists(self,)->bool:
        pass

    def drop_missing_values_columns(self,df:pd.DataFrame,threshold:float=0.3)->Optional[pd.DataFrame]:
        """
        This function will dropcolumn which contain missing value more than specified threshold

        df: Accepts a pandas dataframe
        threshold: Percentage criteria to drop a column
        **************************************************
        returns Pandas DataFrame if atleast a single column is available after missing columns drop else None
        """
        try:
            pass
        except Exception as e:
            raise SensorException(e,sys)

    def initiate_data_validation(self)->artifact_entity.DataIngestionArtifact:
        pass
        
