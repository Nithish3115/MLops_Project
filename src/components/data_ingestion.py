
import pandas as pd
import numpy as np
from src.logger.logger_script import logging
from src.exception.exception import customexception

import os
import sys
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from pathlib import Path

class DataIngestionConfig:
    raw_data_path:str=os.path.join("artifacts","raw.csv")
    train_data_path:str=os.path.join("artifacts","train.csv")
    test_data_path:str=os.path.join("artifacts","test.csv")


class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()
        
    
    def initiate_data_ingestion(self):
        logging.info("data ingestion started")
        
        try:
            data=pd.read_csv(Path(os.path.join("Dataset","raw.csv")))
            logging.info(" i have read dataset as a df")
            data = pd.read_csv(Path(os.path.join("Dataset", "raw.csv")))
            logging.info("Dataset read as a DataFrame")

            # Check for NaN values
            if data.isnull().values.any():
                logging.warning("Data contains NaN values. Checking the number of NaNs in each column:")
                logging.warning(data.isnull().sum())

                # Handle NaN values: Example - Dropping rows with NaN values
                initial_shape = data.shape
                data.dropna(inplace=True)
                logging.info(f"Dropped {initial_shape[0] - data.shape[0]} rows with NaN values.")

            
            
            os.makedirs(os.path.dirname(os.path.join(self.ingestion_config.raw_data_path)),exist_ok=True)
            data.to_csv(self.ingestion_config.raw_data_path,index=False)
            logging.info(" i have saved the raw dataset in artifact folder")
            
            logging.info("here i have performed train test split")
            
            train_data,test_data=train_test_split(data,test_size=0.25)
            logging.info("train test split completed")
            
            train_data.to_csv(self.ingestion_config.train_data_path,index=False)
            test_data.to_csv(self.ingestion_config.test_data_path,index=False)
            
            logging.info("data ingestion part completed")
            
            return (
                 
                
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
            
            
        except Exception as e:
           logging.info("exception during occured at data ingestion stage")
           raise customexception(e,sys)
        
# if __name__=="__main__":
#    obj= DataIngestion()
#    obj.initiate_data_ingestion()
    
 