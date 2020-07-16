from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtGui import QDoubleValidator
import sys
import numpy as np
import pickle
import Diabetes_DL_script
from Diabetes_DL_script import Prediction_Model
from PyQt5.QtGui import QDoubleValidator, QValidator
from sys import float_info

class DoubleValidator(QDoubleValidator):
    

    def __init__(self, bottom = float_info.min, top = float_info.max, decimals = float_info.dig, parent = None):
        super(DoubleValidator, self).__init__(bottom, top, decimals, parent)

    def validate(self, input_value, pos):
        print(pos,input_value)
        state,_, pos = QDoubleValidator.validate(self, input_value, pos)
        
        if input_value=='' or input_value == '.':
            return QValidator.Intermediate, pos
        
        if state != QValidator.Acceptable:
            return QValidator.Invalid, pos
        
        return QValidator.Acceptable, pos


class Prediction_Meter(object):
    def __init__(self):
        self.model = Prediction_Model()

    def setupUi(self, Prediction_Meter):
        Prediction_Meter.setObjectName("Prediction_Meter")
        Prediction_Meter.setFixedSize(561, 336)
       
       
        self.Heading = QtWidgets.QLabel(Prediction_Meter)
        self.Heading.setGeometry(QtCore.QRect(0, 10, 561, 41))
        self.Heading.setObjectName("Heading")

        self.layoutWidget = QtWidgets.QWidget(Prediction_Meter)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 60, 521, 121))
        self.layoutWidget.setObjectName("layoutWidget")
        
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        
        self.dp = QtWidgets.QLabel(self.layoutWidget)
        self.dp.setObjectName("dp")
        self.gridLayout.addWidget(self.dp, 2, 0, 1, 1)
        
        self.glucose_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.glucose_2.setObjectName("glucose_2")
        self.glucose_2.setValidator(QDoubleValidator(70.00, 180.00, 3))
        self.gridLayout.addWidget(self.glucose_2, 0, 1, 1, 1)
        self.glucose_2.setPlaceholderText("70-180 mg/dl")

        self.sk_thick = QtWidgets.QLabel(self.layoutWidget)
        self.sk_thick.setObjectName("sk_thick")
        self.gridLayout.addWidget(self.sk_thick, 3, 2, 1, 1)
        
        self.dp_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.dp_2.setObjectName("dp_2")
        self.gridLayout.addWidget(self.dp_2, 2, 1, 1, 1)
        self.dp_2.setPlaceholderText("diabetes pedigree index 0-3")
        self.dp_2.setValidator(QDoubleValidator(.00, 3.00, 3))
        
        self.bmi_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.bmi_2.setObjectName("bmi_2")
        self.gridLayout.addWidget(self.bmi_2, 1, 3, 1, 1)
        self.bmi_2.setPlaceholderText("10-50")
        self.bmi_2.setValidator(QDoubleValidator(10.00, 50.00, 2))
        
        self.preg_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.preg_2.setObjectName("preg_2")
        self.gridLayout.addWidget(self.preg_2, 1, 1, 1, 1)
        self.preg_2.setPlaceholderText("0 if male")
        self.preg_2.setValidator(QDoubleValidator(0,100,0))
        
        self.glucose = QtWidgets.QLabel(self.layoutWidget)
        self.glucose.setObjectName("glucose")
        self.gridLayout.addWidget(self.glucose, 0, 0, 1, 1)
        
        self.bp = QtWidgets.QLabel(self.layoutWidget)
        self.bp.setObjectName("bp")
        self.gridLayout.addWidget(self.bp, 2, 2, 1, 1)
        
        self.sk_thick_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.sk_thick_2.setObjectName("sk_thick_2")
        self.gridLayout.addWidget(self.sk_thick_2, 3, 3, 1, 1)
        self.sk_thick_2.setPlaceholderText("triceps SkinThickness 10-50mm")
        self.sk_thick_2.setValidator(QDoubleValidator(10.00, 50.00, 2))
        
        self.insu = QtWidgets.QLabel(self.layoutWidget)
        self.insu.setObjectName("insu")
        self.gridLayout.addWidget(self.insu, 3, 0, 1, 1)
        
        self.age_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.age_2.setObjectName("age_2")
        self.gridLayout.addWidget(self.age_2, 0, 3, 1, 1)
        self.age_2.setPlaceholderText("1-100 is recommended")
        self.age_2.setValidator(QDoubleValidator(0, 110, 0))
        
        self.preg = QtWidgets.QLabel(self.layoutWidget)
        self.preg.setObjectName("preg")
        self.gridLayout.addWidget(self.preg, 1, 0, 1, 1)
        
        self.age = QtWidgets.QLabel(self.layoutWidget)
        self.age.setObjectName("age")
        self.gridLayout.addWidget(self.age, 0, 2, 1, 1)
        
        self.bp_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.bp_2.setObjectName("bp_2")
        self.gridLayout.addWidget(self.bp_2, 2, 3, 1, 1)
        self.bp_2.setPlaceholderText("80-140mm Hg")
        self.bp_2.setValidator(QDoubleValidator(70.00, 150.00, 2))
        
        self.insu_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.insu_2.setObjectName("insu_2")
        self.gridLayout.addWidget(self.insu_2, 3, 1, 1, 1)
        self.insu_2.setPlaceholderText("15-276mu U/ml")
        self.insu_2.setValidator(QDoubleValidator(15.00, 300.00, 2))
        
        self.bmi = QtWidgets.QLabel(self.layoutWidget)
        self.bmi.setObjectName("bmi")
        self.gridLayout.addWidget(self.bmi, 1, 2, 1, 1)
        
        self.Prediction = QtWidgets.QPushButton(Prediction_Meter,clicked=self.calculation)
        self.Prediction.setGeometry(QtCore.QRect(450, 220, 80, 19))
        self.Prediction.setObjectName("Prediction")
        
        self.clear = QtWidgets.QPushButton(Prediction_Meter,clicked=self.clearall)
        self.clear.setGeometry(QtCore.QRect(30, 220, 80, 19))
        self.clear.setObjectName("clear")
        
        self.result = QtWidgets.QLabel(Prediction_Meter)
        self.result.setGeometry(QtCore.QRect(10, 270, 291, 61))
        self.result.setObjectName("result")
        
        self.Result = QtWidgets.QLCDNumber(Prediction_Meter)
        self.Result.setGeometry(QtCore.QRect(420, 290, 81, 20))
        self.Result.setStyleSheet("background-color: rgb(85, 87, 83);border-color: rgb(137, 29, 29);")
        self.Result.setObjectName("Result")

        self.percent_label = QtWidgets.QLabel(Prediction_Meter)
        self.percent_label.setGeometry(QtCore.QRect(510, 290, 31, 21))
        self.percent_label.setObjectName("percent_label")

        self.retranslateUi(Prediction_Meter)
        QtCore.QMetaObject.connectSlotsByName(Prediction_Meter)

    def retranslateUi(self, Prediction_Meter):
        _translate = QtCore.QCoreApplication.translate
        Prediction_Meter.setWindowTitle(_translate("Prediction_Meter", "Prediction Meter"))
        
        self.Heading.setText(_translate("Prediction_Meter", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; text-decoration: underline; color:#204a87;\">Diabetes Prediction </span></p></body></html>"))
        self.dp.setText(_translate("Prediction_Meter", "<html><head/><body><p align=\"right\">*Diabets pedigree:</p></body></html>"))
        self.sk_thick.setText(_translate("Prediction_Meter", "<html><head/><body><p align=\"right\">Skin Thickness: </p></body></html>"))
        self.glucose.setText(_translate("Prediction_Meter", "<html><head/><body><p align=\"right\">*Glucose:</p></body></html>"))
        self.bp.setText(_translate("Prediction_Meter", "<html><head/><body><p align=\"right\">Blood Pressure :</p></body></html>"))
        self.insu.setText(_translate("Prediction_Meter", "<html><head/><body><p align=\"right\">Insulin :</p></body></html>"))
        self.preg.setText(_translate("Prediction_Meter", "<html><head/><body><p align=\"right\">*Pregnancies:</p></body></html>"))
        self.age.setText(_translate("Prediction_Meter", "<html><head/><body><p align=\"right\">*Age:</p></body></html>"))
        self.bmi.setText(_translate("Prediction_Meter", "<html><head/><body><p align=\"right\">*BMI:</p></body></html>"))
        self.Prediction.setText(_translate("Prediction_Meter", "Result"))
        self.clear.setText(_translate("Prediction_Meter", "Clear"))
        self.result.setText(_translate("Prediction_Meter", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600; font-style:italic; color:#a40000;\">Results will be displayed here :</span></p></body></html>"))
        self.Result.setToolTip(_translate("Prediction_Meter", "<html><head/><body><p align=\"center\"><span style=\" font-size:8pt; font-style:italic; color:#fce94f;\">prediction</span></p></body></html>"))
        self.percent_label.setText(_translate("Prediction_Meter", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; font-style:italic; color:#a40000;\">%</span></p></body></html>"))

    def calculation(self):
        #feature_names ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']
        s       =self.model.diabetes_model()
        arr     =[self.preg_2.text(),self.glucose_2.text(),self.bp_2.text(),self.sk_thick_2.text(),self.insu_2.text(),self.bmi_2.text(),self.dp_2.text(),self.age_2.text()]
        arr     =list(map(float,arr))
        # print(arr)
        arr     =np.array([np.array(arr)])
        arr     =self.model.std_scaling(arr)
        pred    =s.predict(arr.reshape(-1,1,8))
        # print(pred) 
        self.Result.display(float(pred[0][0][0]*100))

    def clearall(self):
        self.age_2.clear()
        self.bmi_2.clear()
        self.insu_2.clear()
        self.bp_2.clear()
        self.glucose_2.clear()
        self.dp_2.clear()
        self.sk_thick_2.clear()
        self.preg_2.clear()

        self.Result.display(0.000)
        

app = QtWidgets.QApplication(sys.argv)
Dialog = QtWidgets.QDialog()
ui = Prediction_Meter()
ui.setupUi(Dialog)
Dialog.show()
sys.exit(app.exec_())

    