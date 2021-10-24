# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIDesign.ui'
#
# Created by: PyQt5 UI code generator 5.15.5
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from imageProcess import *
from database import*

class Ui_Dialog(object):
    foodname="unknown"
    weight=0
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(807, 662)

        self.foodGraphic = QtWidgets.QLabel(Dialog)
        self.foodGraphic.setGeometry(QtCore.QRect(60, 90, 341, 301))
        self.foodGraphic.setObjectName("foodGraphic")
     
        self.nameText = QtWidgets.QTextBrowser(Dialog)
        self.nameText.setGeometry(QtCore.QRect(470, 90, 261, 40))
        self.nameText.setObjectName("nameText")

        self.weightText = QtWidgets.QTextBrowser(Dialog)
        self.weightText.setGeometry(QtCore.QRect(470, 140, 150, 40))
        self.weightText.setObjectName("weightText")
        self.weightText.setText("Weight(in grams): ")
        self.weightText.setFont(QtGui.QFont('Times font', 10))
        self.weightText.setStyleSheet("background-color: transparent;")
        self.weightText.setFrameStyle(0)

        self.weightEdit = QtWidgets.QLineEdit(Dialog)
        self.weightEdit.setGeometry(QtCore.QRect(630, 140, 100, 40))
        self.weightEdit.setObjectName("weightEdit")
        self.weightEdit.setFont(QtGui.QFont('Times font', 10))

        self.nutrientText = QtWidgets.QTextBrowser(Dialog)
        self.nutrientText.setGeometry(QtCore.QRect(470, 190, 261, 201))
        self.nutrientText.setObjectName("nutrientText")

        self.imageButton = QtWidgets.QPushButton(Dialog)
        self.imageButton.setGeometry(QtCore.QRect(70, 470, 200, 100))
        self.imageButton.setObjectName("processButton")
        self.imageButton.setFont(QtGui.QFont('Times font', 11))

        self.addButton = QtWidgets.QPushButton(Dialog)
        self.addButton.setGeometry(QtCore.QRect(530, 470, 200, 100))
        self.addButton.setObjectName("imageButton")
        self.addButton.setFont(QtGui.QFont('Times font', 11))

        self.weightButton = QtWidgets.QPushButton(Dialog)
        self.weightButton.setGeometry(QtCore.QRect(300, 470, 200, 100))
        self.weightButton.setObjectName("weightButton")
        self.weightButton.setText("Input Weight")
        self.weightButton.setFont(QtGui.QFont('Times font', 11))

        self.imageButton.clicked.connect(self.imageButtonClicked)
        self.weightButton.clicked.connect(self.weightButtonClicked)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def imageButtonClicked(self):
            imageProcesser = imageProcess()
            imageProcesser.takeImage()
            image_path = 'output.jpg' #path to your image file
            image_profile = QtGui.QImage(image_path) #QImage object
            image_profile = image_profile.scaled(400,350, aspectRatioMode=QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation) # To scale image for example and keep its Aspect Ration    
            self.foodGraphic.setPixmap(QtGui.QPixmap.fromImage(image_profile)) 
            self.foodname = imageProcesser.foodname
            self.nameText.setText("Name: "+imageProcesser.foodname)
            self.nameText.setFont(QtGui.QFont('Times font', 14))

    def weightButtonClicked(self):
        self.weight = int(self.weightEdit.text())
        nutrient= database.getNutrition(database.getID(self.foodname),self.weight)
        self.nutrientText.setText("Nutrient Fact \n" +nutrient)
        self.nutrientText.setFont(QtGui.QFont('Times font', 14))


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Food Analyzer"))
        self.imageButton.setText(_translate("Dialog", "Take Image"))
        self.addButton.setText(_translate("Dialog", "Add to Today"))
        self.nameText.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Name:</span></p></body></html>"))
        self.nutrientText.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Nutrition Fact</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
