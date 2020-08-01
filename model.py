from keras.models import Sequential
from keras.layers import Dense,Dropout
import pandas as pd 
import numpy as np
import os
import subprocess
from sklearn.preprocessing import StandardScaler
# https://askubuntu.com/questions/80448/what-would-cause-the-gi-module-to-be-missing-from-python
# import gi
# from gi.repository import Notify

BASE_DIR=os.path.dirname(__file__)
fname ="train_data.csv"
csv_path=os.path.join(BASE_DIR,fname)
ICON_PATH=os.path.join(BASE_DIR,"icon.png")
# Notify.init("Diabetes Prediction") 
# n=Notify.Notification.new("Hello", icon=ICON_PATH) 
# n.set_urgency(Notify.URGENCY_CRITICAL)
# n.set_timeout(5000)
# n.show()

class Prediction_Model():
    def __init__(self):
        if os.path.exists(csv_path):
            df=pd.read_csv(fname)
        else:    
            subprocess.Popen(["notify-send", "-i", ICON_PATH, "DIABETES PREDICTION", f"the file name {fname} does not exist"])
            # print(f"the file name {fname} does not exist")
            # n.update("","" )
            # n.show() 
            exit()
        df_mod = df[(df.BloodPressure != 0) & (df.BMI != 0) & (df.Glucose != 0)]
        self.feature_names = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']
        self.x = df_mod[self.feature_names]
        self.y = df_mod.Outcome
        self.scale = StandardScaler()
        self.x = self.scale.fit_transform(self.x)
        # n.update("Hi","Ho" )
        # n.show() 
        # print("data prepration completed !")
        self.s = Sequential()
        self.s.add(Dense(units=8,input_shape=(len(self.feature_names),),activation="relu",))
        self.s.add(Dense(units=16,activation="relu",))
        self.s.add(Dropout(.4))
        self.s.add(Dense(units=32,activation="relu",))
        self.s.add(Dense(units=1,activation="sigmoid",))
        self.s.compile(optimizer='Adam',loss='binary_crossentropy',metrics=["accuracy"])
        self.s.fit(x=self.x, y=self.y, batch_size=50, epochs=110)
        subprocess.Popen(["notify-send", "-i", ICON_PATH, "DIABETES PREDICTION","model training completed and deployed Proceed the prediction!"])

        # n.update("Lo","Love" )
        # n.show()    
        # print("model training completed and deployed !")

    def diabetes_model(self):
        return self.s

    def std_scaling(self,arr):
        return self.scale.transform(arr)
