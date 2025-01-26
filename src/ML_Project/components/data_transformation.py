import os
from ML_Project import logger
from sklearn.model_selection import train_test_split
import pandas as pd
from ML_Project.entity.config_entity import DataTransformationConfig

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        
    # Note: we can add different data transformation techniques such as scaler, pca and all we can perform all kinds of EDA in mL cycle here before passing this data to the model.
    
    def train_test_splitting(self):
        data = pd.read_csv(self.config.data_path)
        
        #split the data into training and test sets.
        train, test = train_test_split(data)
        
        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index = False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index = False)
        
        logger.info("Splitted data into training and test sets")
        logger.info(train.shape)
        logger.info(test.shape)
        
        print(train.shape)
        print(test.shape)
        