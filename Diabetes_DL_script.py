from keras.models import Sequential
from keras.layers import Dense,Dropout
import pandas as pd 
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler


df=pd.read_csv('diabetes2.csv')
df_mod = df[(df.BloodPressure != 0) & (df.BMI != 0) & (df.Glucose != 0)]
feature_names = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']
x = df_mod[feature_names]
y = df_mod.Outcome
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=.25,random_state=20,stratify = df_mod.Outcome)
print(len(x_train),len(y_train))
scale = MinMaxScaler((0,1))
x_train = scale.fit_transform(x_train)
x_test  = scale.fit_transform(x_test)

x_train = np.array(x_train)
y_train = np.array(y_train)

s = Sequential()
s.add(Dense(units=8,input_shape=(len(feature_names),),activation="relu",))
s.add(Dense(units=16,activation="relu",))
s.add(Dropout(.4))
s.add(Dense(units=32,activation="relu",))
s.add(Dense(units=1,activation="sigmoid",))
s.compile(optimizer='rmsprop',loss='binary_crossentropy',metrics=["accuracy"])
s.fit(x=x_train, y=y_train, batch_size=100, epochs=120, verbose=2,shuffle=True)
