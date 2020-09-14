from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd

class Ui_basicMathWindow(QtWidgets.QWidget):

    dfSignal = QtCore.pyqtSignal(pd.DataFrame)
    resultSignal = QtCore.pyqtSignal(str)
    pandasSignal = QtCore.pyqtSignal(str)

    def setupUi(self, basicMathWindow, df):
        global dfForOperations
        dfForOperations = df

        basicMathWindow.setObjectName("basicMathWindow")
        basicMathWindow.resize(274, 332)
        self.operationsButtonGroup = QtWidgets.QButtonGroup()

        self.newColumnName = QtWidgets.QLineEdit(basicMathWindow)
        self.newColumnName.setGeometry(QtCore.QRect(10, 30, 251, 21))
        self.newColumnName.setObjectName("newColumnName")
        self.firstColumn = QtWidgets.QLineEdit(basicMathWindow)
        self.firstColumn.setGeometry(QtCore.QRect(10, 70, 251, 21))
        self.firstColumn.setObjectName("firstColumn")
        self.secondColumn = QtWidgets.QLineEdit(basicMathWindow)
        self.secondColumn.setGeometry(QtCore.QRect(10, 110, 251, 21))
        self.secondColumn.setObjectName("secondColumn")
        self.operationsLable = QtWidgets.QLabel(basicMathWindow)
        self.operationsLable.setGeometry(QtCore.QRect(10, 150, 91, 16))
        self.operationsLable.setObjectName("operationsLable")
        self.sumRB = QtWidgets.QRadioButton(basicMathWindow)
        self.sumRB.setGeometry(QtCore.QRect(10, 190, 61, 20))
        self.sumRB.setObjectName("sumRB")
        self.subtractRB = QtWidgets.QRadioButton(basicMathWindow)
        self.subtractRB.setGeometry(QtCore.QRect(100, 190, 100, 20))
        self.subtractRB.setObjectName("subtractRB")
        self.divideRB = QtWidgets.QRadioButton(basicMathWindow)
        self.divideRB.setGeometry(QtCore.QRect(10, 230, 81, 20))
        self.divideRB.setObjectName("divideRB")
        self.multiplyRB = QtWidgets.QRadioButton(basicMathWindow)
        self.multiplyRB.setGeometry(QtCore.QRect(100, 230, 100, 20))
        self.multiplyRB.setObjectName("multiplyRB")
        self.operateButton = QtWidgets.QPushButton(basicMathWindow)
        self.operateButton.setGeometry(QtCore.QRect(70, 280, 113, 32))
        self.operateButton.setObjectName("operateButton")

        self.operationsButtonGroup.addButton(self.sumRB)
        self.operationsButtonGroup.addButton(self.multiplyRB)
        self.operationsButtonGroup.addButton(self.divideRB)
        self.operationsButtonGroup.addButton(self.subtractRB)
        self.operateButton.clicked.connect(self.executeMathematics)

        self.retranslateUi(basicMathWindow)
        QtCore.QMetaObject.connectSlotsByName(basicMathWindow)

    def retranslateUi(self, basicMathWindow):
        _translate = QtCore.QCoreApplication.translate
        basicMathWindow.setWindowTitle(_translate("basicMathWindow", "Form"))
        self.newColumnName.setText(_translate("basicMathWindow", "New Column Name"))
        self.firstColumn.setText(_translate("basicMathWindow", "First Column"))
        self.secondColumn.setText(_translate("basicMathWindow", "Second Column"))
        self.operationsLable.setText(_translate("basicMathWindow", "Operations"))
        self.sumRB.setText(_translate("basicMathWindow", "Sum"))
        self.subtractRB.setText(_translate("basicMathWindow", "Subtract"))
        self.divideRB.setText(_translate("basicMathWindow", "Divide"))
        self.multiplyRB.setText(_translate("basicMathWindow", "Multiply"))
        self.operateButton.setText(_translate("basicMathWindow", "Operate"))

    def executeMathematics(self):
        try:
            df=dfForOperations
            operation = self.operationsButtonGroup.checkedButton().text()
            resultColumnName=self.newColumnName.text()
            firstColumn=self.firstColumn.text()
            secondColumn=self.secondColumn.text()

            if operation == "Sum":
                df[resultColumnName] = df[firstColumn] + df[secondColumn]
                self.pandasSignal.emit(f"\ndf[{resultColumnName}] = df[{firstColumn}] + df[{secondColumn}]")
                self.dfSignal.emit(df)
            elif operation == "Subtract":
                df[resultColumnName] = df[firstColumn] - df[secondColumn]
                self.pandasSignal.emit(f"\ndf[{resultColumnName}] = df[{firstColumn}] - df[{secondColumn}]")
                self.dfSignal.emit(df)
            elif operation == "Mulitiply":
                df[resultColumnName] = df[firstColumn] * df[secondColumn]
                self.pandasSignal.emit(f"\ndf[{resultColumnName}] = df[{firstColumn}] * df[{secondColumn}]")
                self.dfSignal.emit(df)
            elif operation == "Divide":
                df[resultColumnName] = df[firstColumn] / df[secondColumn]
                self.pandasSignal.emit(f"\ndf[{resultColumnName}] = df[{firstColumn}] / df[{secondColumn}]")
                self.dfSignal.emit(df)
        except Exception as e:
            self.resultSignal.emit('\n'+str(e)+'\n')



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    basicMathWindow = QtWidgets.QMainWindow()
    ui = Ui_basicMathWindow()
    ui.setupUi(basicMathWindow)
    basicMathWindow.show()
    sys.exit(app.exec_())
