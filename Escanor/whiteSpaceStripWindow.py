from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd

class Ui_RemoveWhiteSpace(QtWidgets.QWidget):
    
    dfSignal = QtCore.pyqtSignal(pd.DataFrame)
    resultSignal = QtCore.pyqtSignal(str)
    pandasSignal = QtCore.pyqtSignal(str)

    def setupUi(self, RemoveWhiteSpace, df):
        global dfForStrip
        dfForStrip = df

        RemoveWhiteSpace.setObjectName("RemoveWhiteSpace")
        RemoveWhiteSpace.resize(381, 111)
        self.cleanButton = QtWidgets.QPushButton(RemoveWhiteSpace)
        self.cleanButton.setGeometry(QtCore.QRect(100, 60, 171, 32))
        self.cleanButton.setObjectName("cleanButton")
        self.columnToClean = QtWidgets.QLineEdit(RemoveWhiteSpace)
        self.columnToClean.setGeometry(QtCore.QRect(10, 20, 361, 21))
        self.columnToClean.setObjectName("columnToClean")
        self.cleanButton.clicked.connect(self.stripWhiteSpace)

        self.retranslateUi(RemoveWhiteSpace)
        QtCore.QMetaObject.connectSlotsByName(RemoveWhiteSpace)

    def retranslateUi(self, RemoveWhiteSpace):
        _translate = QtCore.QCoreApplication.translate
        RemoveWhiteSpace.setWindowTitle(_translate("RemoveWhiteSpace", "Form"))
        self.cleanButton.setText(_translate("RemoveWhiteSpace", "Strip White Space"))
        self.columnToClean.setText(_translate("RemoveWhiteSpace", "Column to Clean"))

    def stripWhiteSpace(self):
        try:
            columToStrip=str(self.columnToClean.text())
            df[columnToStrip] = df[columnToStrip].str.strip()
            self.dfSignalStrip.emit(df)
            self.pandasSignal.emit(f"df[{columnToStrip}] = df[{columnToStrip}].str.strip()")
        except Exception as e:
            self.resultSignal.emit('\n'+str(e)+'\n')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RemoveWhiteSpace = QtWidgets.QMainWindow()
    ui = Ui_Melter()
    ui.setupUi(RemoveWhiteSpace)
    RemoveWhiteSpace.show()
    sys.exit(app.exec_())