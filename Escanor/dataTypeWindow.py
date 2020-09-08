from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd

class Ui_DataTypeWindow(QtWidgets.QWidget):

    dfSignalDataType = QtCore.pyqtSignal(pd.DataFrame)
    resultSignal = QtCore.pyqtSignal(str)
    pandasSignal = QtCore.pyqtSignal(srt)

    def setupUi(self, dataTypeWindow, df):
        global dfForDataTypes
        dfForDataTypes = df
        
        dataTypeWindow.setObjectName("dataTypeWindow")
        dataTypeWindow.resize(346, 165)
        self.dataTypesButtonGroup = QtWidgets.QButtonGroup()

        self.verticalLayoutWidget = QtWidgets.QWidget(dataTypeWindow)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 341, 161))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.dataTypeWindow = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.dataTypeWindow.setObjectName("dataTypeWindow")
        self.verticalLayout.addWidget(self.dataTypeWindow)
        
        self.targetColumn = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.targetColumn.setMaximumSize(QtCore.QSize(16777215, 164))
        self.targetColumn.setObjectName("targetColumn")
        self.verticalLayout.addWidget(self.targetColumn)
        
        self.Button1 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.Button1.setObjectName("Button1")
        self.verticalLayout.addWidget(self.Button1)
        self.dataTypesButtonGroup.addButton(self.Button1, 1)

        self.Button2 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.Button2.setObjectName("Button2")
        self.verticalLayout.addWidget(self.Button2)
        self.dataTypesButtonGroup.addButton(self.Button2, 2)
        
        self.Button3 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.Button3.setObjectName("Button3")
        self.verticalLayout.addWidget(self.Button3)
        self.dataTypesButtonGroup.addButton(self.Button3, 3)
        
        self.castButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.castButton.setObjectName("castButton")
        self.verticalLayout.addWidget(self.castButton)
        

        self.castButton.clicked.connect(self.executeDataCast)
        self.retranslateUi(dataTypeWindow)
        QtCore.QMetaObject.connectSlotsByName(dataTypeWindow)


    def retranslateUi(self, dataTypeWindow):
        _translate = QtCore.QCoreApplication.translate
        dataTypeWindow.setWindowTitle(_translate("dataTypeWindow", "Form"))
        self.dataTypeWindow.setText(_translate("dataTypeWindow", "Column to Change Format of:"))
        self.Button1.setText(_translate("dataTypeWindow", "str"))
        self.Button2.setText(_translate("dataTypeWindow", "int"))
        self.Button3.setText(_translate("dataTypeWindow", "float"))
        self.castButton.setText(_translate("dataTypeWindow", "Cast Type"))

    def executeDataCast(self, df):
        try:
            dataType = self.dataTypesButtonGroup.checkedButton().text()
            column=self.targetColumn.text()
            dfForDataTypes[column] = dfForDataTypes[column].astype(dataType)
            self.dfSignalDataType.emit(dfForDataTypes)
            self.pandasSignal.emit(f"dfForDataTypes[{column}].astype({dataType})")
        except Exception as e:
            self.resultSignal.emit('\n'+str(e)+'\n')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dataTypeWindow = QtWidgets.QMainWindow()
    ui = Ui_DataTypeWindow()
    ui.setupUi(dataTypeWindow)
    dataTypeWindow.show()
    sys.exit(app.exec_())

