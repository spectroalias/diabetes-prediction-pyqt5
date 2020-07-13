# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DiabetesPred.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(589, 353)
        self.ConfirmBox = QtWidgets.QDialogButtonBox(Dialog)
        self.ConfirmBox.setGeometry(QtCore.QRect(400, 220, 164, 19))
        self.ConfirmBox.setOrientation(QtCore.Qt.Horizontal)
        self.ConfirmBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.ConfirmBox.setObjectName("ConfirmBox")
        self.Result = QtWidgets.QLCDNumber(Dialog)
        self.Result.setGeometry(QtCore.QRect(90, 220, 64, 23))
        self.Result.setObjectName("Result")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(210, 10, 171, 41))
        self.label_9.setObjectName("label_9")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 60, 521, 111))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.diab = QtWidgets.QLabel(self.layoutWidget)
        self.diab.setObjectName("diab")
        self.gridLayout.addWidget(self.diab, 2, 0, 1, 1)
        self.glucose_2 = QtWidgets.QTextEdit(self.layoutWidget)
        self.glucose_2.setObjectName("glucose_2")
        self.gridLayout.addWidget(self.glucose_2, 0, 1, 1, 1)
        self.skinthickness = QtWidgets.QLabel(self.layoutWidget)
        self.skinthickness.setObjectName("skinthickness")
        self.gridLayout.addWidget(self.skinthickness, 3, 2, 1, 1)
        self.dP = QtWidgets.QTextEdit(self.layoutWidget)
        self.dP.setObjectName("dP")
        self.gridLayout.addWidget(self.dP, 2, 1, 1, 1)
        self.bmi_2 = QtWidgets.QTextEdit(self.layoutWidget)
        self.bmi_2.setObjectName("bmi_2")
        self.gridLayout.addWidget(self.bmi_2, 1, 3, 1, 1)
        self.preg_2 = QtWidgets.QTextEdit(self.layoutWidget)
        self.preg_2.setObjectName("preg_2")
        self.gridLayout.addWidget(self.preg_2, 1, 1, 1, 1)
        self.glucose = QtWidgets.QLabel(self.layoutWidget)
        self.glucose.setObjectName("glucose")
        self.gridLayout.addWidget(self.glucose, 0, 0, 1, 1)
        self.bp = QtWidgets.QLabel(self.layoutWidget)
        self.bp.setObjectName("bp")
        self.gridLayout.addWidget(self.bp, 2, 2, 1, 1)
        self.sthickness = QtWidgets.QTextEdit(self.layoutWidget)
        self.sthickness.setObjectName("sthickness")
        self.gridLayout.addWidget(self.sthickness, 3, 3, 1, 1)
        self.insu = QtWidgets.QLabel(self.layoutWidget)
        self.insu.setObjectName("insu")
        self.gridLayout.addWidget(self.insu, 3, 0, 1, 1)
        self.textEdit_8 = QtWidgets.QTextEdit(self.layoutWidget)
        self.textEdit_8.setObjectName("textEdit_8")
        self.gridLayout.addWidget(self.textEdit_8, 0, 3, 1, 1)
        self.preg = QtWidgets.QLabel(self.layoutWidget)
        self.preg.setObjectName("preg")
        self.gridLayout.addWidget(self.preg, 1, 0, 1, 1)
        self.age = QtWidgets.QLabel(self.layoutWidget)
        self.age.setObjectName("age")
        self.gridLayout.addWidget(self.age, 0, 2, 1, 1)
        self.bp_2 = QtWidgets.QTextEdit(self.layoutWidget)
        self.bp_2.setObjectName("bp_2")
        self.gridLayout.addWidget(self.bp_2, 2, 3, 1, 1)
        self.insulin = QtWidgets.QTextEdit(self.layoutWidget)
        self.insulin.setObjectName("insulin")
        self.gridLayout.addWidget(self.insulin, 3, 1, 1, 1)
        self.bmi = QtWidgets.QLabel(self.layoutWidget)
        self.bmi.setObjectName("bmi")
        self.gridLayout.addWidget(self.bmi, 1, 2, 1, 1)

        self.retranslateUi(Dialog)
        self.ConfirmBox.accepted.connect(Dialog.accept)
        self.ConfirmBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_9.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; text-decoration: underline; color:#204a87;\">Diabetes Prediction </span></p></body></html>"))
        self.diab.setText(_translate("Dialog", "<html><head/><body><p align=\"right\">*Diabets pedigree:</p></body></html>"))
        self.skinthickness.setText(_translate("Dialog", "<html><head/><body><p align=\"right\">Skin Thickness: </p></body></html>"))
        self.glucose.setText(_translate("Dialog", "<html><head/><body><p align=\"right\">*Glucose:</p></body></html>"))
        self.bp.setText(_translate("Dialog", "<html><head/><body><p align=\"right\">Blood Pressure :</p></body></html>"))
        self.insu.setText(_translate("Dialog", "<html><head/><body><p align=\"right\">Insulin :</p></body></html>"))
        self.preg.setText(_translate("Dialog", "<html><head/><body><p align=\"right\">*Pregnancies:</p></body></html>"))
        self.age.setText(_translate("Dialog", "<html><head/><body><p align=\"right\">*Age:</p></body></html>"))
        self.bmi.setText(_translate("Dialog", "<html><head/><body><p align=\"right\">*BMI:</p></body></html>"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
