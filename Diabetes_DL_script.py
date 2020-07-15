from keras.models import Sequential
from keras.layers import Dense,Dropout
import pandas as pd 
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

class Prediction_Model():
    def __init__(self):
        df=pd.read_csv('diabetes2.csv')
        df_mod = df[(df.BloodPressure != 0) & (df.BMI != 0) & (df.Glucose != 0)]
        self.feature_names = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']
        self.x = df_mod[self.feature_names]
        self.y = df_mod.Outcome
        # x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=.25,random_state=20,stratify = df_mod.Outcome)
        self.scale = StandardScaler()
        self.x = self.scale.fit_transform(self.x)
        # x_test  = scale.fit_transform(x_test)
        # x_train = np.array(x_train)
        # y_train = np.array(y_train)
        print("data prepration completed !")
        self.s = Sequential()
        self.s.add(Dense(units=8,input_shape=(len(self.feature_names),),activation="relu",))
        self.s.add(Dense(units=16,activation="relu",))
        self.s.add(Dropout(.4))
        self.s.add(Dense(units=32,activation="relu",))
        self.s.add(Dense(units=1,activation="sigmoid",))
        self.s.compile(optimizer='Adam',loss='binary_crossentropy',metrics=["accuracy"])
        self.s.fit(x=self.x, y=self.y, batch_size=50, epochs=130)
        print("model training completed and deployed !")

    def diabetes_model(self):
        return self.s

    def std_scaling(self,arr):
        return self.scale.transform(arr)


# s=diabetes_model()
# arr = np.array([12.,12.,12.,12.,12.,12.,12.,12.])
# y_=s.predict(arr.reshape(1,8))
# print(y_)