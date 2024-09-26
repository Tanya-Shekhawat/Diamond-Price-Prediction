# data to traintest data 
import os # to creat path making and fetching 
import sys # for logging and exception 
from src.logger import logging 
from src.exception import CustomException 

import pandas as pd 
from sklearn.model_selection import train_test_split 

from dataclasses import dataclass

## initialize the data ingestion configuration 

@dataclass 
class DataIngestionconfig: 
    # def __init__(self,m): we do like this normaly but with @dataclass we can directly write our variables name 
    train_data_path:str = os.path.join('artifacts', 'train.csv') #place to save train and test data 
    test_data_path:str = os.path.join('artifacts', 'test.csv')
    raw_data_path:str = os.path.join('artifacts', 'raw.csv') 

# data ingestion class
class DataIngestion: 
    def __init__(self):
        self.ingestion_config = DataIngestionconfig() 

    def initiate_data_ingestion(self): 
        logging.info('Data Ingestion method starts') 

        try: 
            df = pd.read_csv(os.path.join('notebooks/data', 'gemstone.csv')) 
            logging.info('Dataset read as pandas Dataframe') 

            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path), exist_ok=True)  
            df.to_csv(self.ingestion_config.raw_data_path, index=False)
            logging.info('Raw data created') 

            train_set, test_set = train_test_split(df, test_size=0.30, random_state=42) # reason to do this way is as we need entier test data in one file and entire train data in one file 

            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header= True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header= True)
            logging.info('Train Test data created')

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            ) # return the test and train data paths 


        except Exception as e:
            logging.info('Exception occured at Data Ingestion Stage')
            raise CustomException(e, sys)  

