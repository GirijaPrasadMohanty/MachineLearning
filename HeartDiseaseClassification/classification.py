# -*- coding: utf-8 -*-
from sklearn.linear_model import LogisticRegression
from data_generation import data_generation
from sklearn.metrics import accuracy_score
import warnings
from sklearn.metrics import confusion_matrix
warnings.filterwarnings('ignore')

import pickle

class Learning:
    def main(self,path,max_iter):
        path=path
        #model = LogisticRegression(max_iter=max_iter,random_state=1)
        model = LogisticRegression(max_iter=8,random_state=1)
        data_obj=data_generation(path)
        dataset=data_obj.main()
        master_data=data_obj.data_clean(dataset)
        X_train, X_test, Y_train, Y_test=data_obj.train_test_data(master_data)
        trained_model=self.train(model,X_train,Y_train)
        self.test(trained_model,X_test,Y_test)
        
        pkl_file=open('C:/Users/girijamohanty/Documents/my_study_material/production', 'wb')
        serl = pickle.dumps(trained_model)
        pkl_file.write(serl)
        pkl_file.close()
        
    def train(self,model,X_train,Y_train):
        #col_list = ['age','sex','chest_pain','blood_pressure','chol','bld_sugar','restecg','thalach','exang','oldpeak','slope','ca','thal','num']
        #dataset=pd.read_csv('C:/Users/girijamohanty/Documents/my_study_material/data/HeartDisease.csv',names = col_list)
        #dataset=pd.read_csv(path,names = col_list)
        model.fit(X_train, Y_train)
        return model
        
        
    def valididation(self,model,X_test,Y_test):
        Y_pred=model.predict(X_test)
        print("Coefficients=")
        print(model.coef_)
        self.evaluate(Y_pred,Y_test)
    
    
    def evaluate(self,Y_pred,Y_test):
        print(confusion_matrix(Y_test, Y_pred.round()))
        print(accuracy_score(Y_pred.round(),Y_test))
    
    def __init__(self,path):
        path=path
        for f in range(2,100):
            print("========================================")
            print("Iteration number"+str(f))
            self.main(path,f)
            print("========================================")

#max_iter=9