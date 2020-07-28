from keras.models import Sequential
from keras.layers import Dense,Dropout
import pandas as pd 
import numpy as np
import os
from sklearn.preprocessing import StandardScaler

BASE_DIR=os.path.dirname(__file__)
fname ="train_data.csv"
csv_path=os.path.join(BASE_DIR,fname)

class Prediction_Model():
    def __init__(self):
        if os.path.exists(csv_path):
            df=pd.read_csv(fname)
        else:    
            print(f"the file name {fname} does not exist")
            exit()
        df_mod = df[(df.BloodPressure != 0) & (df.BMI != 0) & (df.Glucose != 0)]
        self.feature_names = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']
        self.x = df_mod[self.feature_names]
        self.y = df_mod.Outcome
        self.scale = StandardScaler()
        self.x = self.scale.fit_transform(self.x)
        print("data prepration completed !")
        self.s = Sequential()
        self.s.add(Dense(units=8,input_shape=(len(self.feature_names),),activation="relu",))
        self.s.add(Dense(units=16,activation="relu",))
        self.s.add(Dropout(.4))
        self.s.add(Dense(units=32,activation="relu",))
        self.s.add(Dense(units=1,activation="sigmoid",))
        self.s.compile(optimizer='Adam',loss='binary_crossentropy',metrics=["accuracy"])
        self.s.fit(x=self.x, y=self.y, batch_size=50, epochs=120)
        print("model training completed and deployed !")

    def diabetes_model(self):
        return self.s

    def std_scaling(self,arr):
        return self.scale.transform(arr)
