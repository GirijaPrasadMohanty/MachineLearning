# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
import warnings

warnings.filterwarnings('ignore')

class data_generation:
    path=""
    def main(self):
        col_list = ['age','sex','chest_pain','blood_pressure','chol','bld_sugar','restecg','thalach','exang','oldpeak','slope','ca','thal','num']
        dataset=pd.read_csv(self.path,names = col_list)
       # master_data=self.data_clean(dataset)
        return dataset
    
    def data_clean(self,dataset):
        dataset['num_output']=np.where(dataset['num'] == 0 ,0 ,1)
        master_data=dataset.replace('?','NaN')
        master_data=master_data.drop(['num'],axis=1)
        master_data=master_data.replace('NaN',master_data.median())
        return master_data
    def train_test_data(self,master_data):
        Xtrain = master_data.drop(['num_output'], axis = 1)
        Ytrain = master_data['num_output']
        X_train, X_test, Y_train, Y_test = train_test_split(Xtrain, Ytrain, test_size=0.1, random_state=0)
        return X_train, X_test, Y_train, Y_test
    
    def __init__(self,file_path):
        #self.main(file_path)
        self.path=file_path