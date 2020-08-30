from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd

class Ui_DataTypeWindow(QtWidgets.QWidget):

    dfSignalDataType = QtCore.pyqtSignal(pd.DataFrame)
    resultSignal = QtCore.pyqtSignal(str)

    def setupUi(self, DataTypeWindow, df):
        global dfForDataTypes
        dfForDataTypes = df
        
        DataTypeWindow.setObjectName("DataTypeWindow")
        DataTypeWindow.resize(346, 165)
        self.dataTypesButtonGroup = QtWidgets.QButtonGroup()

        self.verticalLayoutWidget = QtWidgets.QWidget(DataTypeWindow)
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
        self.retranslateUi(DataTypeWindow)
        QtCore.QMetaObject.connectSlotsByName(DataTypeWindow)

    def executeDataCast(self, df):
        try:
            dataType = self.dataTypesButtonGroup.checkedButton().text()
            column=self.targetColumn.text()
            dfForDataTypes[column] = dfForDataTypes[column].astype(dataType)
            self.dfSignalDataType.emit(dfForDataTypes)
        except Exception as e:
            self.resultSignal.emit('\n'+str(e)+'\n')

    def retranslateUi(self, DataTypeWindow):
        _translate = QtCore.QCoreApplication.translate
        DataTypeWindow.setWindowTitle(_translate("DataTypeWindow", "Form"))
        self.dataTypeWindow.setText(_translate("DataTypeWindow", "Column to Change Format of:"))
        self.Button1.setText(_translate("DataTypeWindow", "str"))
        self.Button2.setText(_translate("DataTypeWindow", "int"))
        self.Button3.setText(_translate("DataTypeWindow", "float"))
        self.castButton.setText(_translate("DataTypeWindow", "Cast Type"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dataTypeWindow = QtWidgets.QMainWindow()
    ui = Ui_summerWindow()
    ui.setupUi(sumColumnWindow)
    dataTypeWindow.show()
    sys.exit(app.exec_())

