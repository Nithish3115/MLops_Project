from src.components.data_ingestion import DataIngestion

from src.components.data_transformation import DataTransformation

from src.components.model_trainer import ModelTrainer

from src.components.model_evaluation import ModelEvaluation


import os
import sys
from src.logger.logger_script import logging
from src.exception.exception import customexception
import pandas as pd

data_ingestion=DataIngestion()

train_data_path,test_data_path=data_ingestion.initiate_data_ingestion()
data_transformation = DataTransformation()
train_arr,test_arr=data_transformation.initialize_data_transformation(train_data_path,test_data_path)
model_trainer=ModelTrainer()
model_trainer.initate_model_training(train_arr,test_arr)         



class TrainingPipeline:
    def start_data_ingestion(self):
        try:
            data_ingestion=DataIngestion()
            train_data_path,test_data_path=data_ingestion.initiate_data_ingestion()
            return train_data_path,test_data_path
        except Exception as e:
            raise customexception(e,sys)
        
    def start_data_transformation(self,train_data_path,test_data_path):
        
        try:
            data_transformation = DataTransformation()
            train_arr,test_arr=data_transformation.initialize_data_transformation(train_data_path,test_data_path)
            return train_arr,test_arr
        except Exception as e:
            raise customexception(e,sys)
    
    def start_model_training(self,train_arr,test_arr):
        try:
            model_trainer=ModelTrainer()
            model_trainer.initate_model_training(train_arr,test_arr)
        except Exception as e:
            raise customexception(e,sys)
                
    def start_trainig(self):
        try:
            train_data_path,test_data_path=self.start_data_ingestion()
            train_arr,test_arr=self.start_data_transformation(train_data_path,test_data_path)
            self.start_model_training(train_arr,test_arr)
        except Exception as e:
            raise customexception(e,sys)
        
if __name__=="__main__":
    obj=TrainingPipeline
    obj.start_data_ingestion
    obj.start_data_transformation
    obj.start_model_training
    obj.start_trainig