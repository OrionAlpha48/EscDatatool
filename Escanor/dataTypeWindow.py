# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dataTypeWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DataTypeWindow(object):
    def setupUi(self, DataTypeWindow):
        DataTypeWindow.setObjectName("DataTypeWindow")
        DataTypeWindow.resize(346, 165)
        self.verticalLayoutWidget = QtWidgets.QWidget(DataTypeWindow)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 341, 161))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.dataTypeWindow = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.dataTypeWindow.setObjectName("dataTypeWindow")
        self.verticalLayout.addWidget(self.dataTypeWindow)
        self.targetColumn = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget)
        self.targetColumn.setMaximumSize(QtCore.QSize(16777215, 164))
        self.targetColumn.setObjectName("targetColumn")
        self.verticalLayout.addWidget(self.targetColumn)
        self.stringButton = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.stringButton.setObjectName("stringButton")
        self.verticalLayout.addWidget(self.stringButton)
        self.integerButton = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.integerButton.setObjectName("integerButton")
        self.verticalLayout.addWidget(self.integerButton)
        self.floatButton = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.floatButton.setObjectName("floatButton")
        self.verticalLayout.addWidget(self.floatButton)
        self.castButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.castButton.setObjectName("castButton")
        self.verticalLayout.addWidget(self.castButton)

        self.retranslateUi(DataTypeWindow)
        QtCore.QMetaObject.connectSlotsByName(DataTypeWindow)

    def executeDataCast(self):
        global df
        try:
            df=df
            dataType=v.get()
            column=nameofColumnToChangeDataType.get()
            df[column] = df[column].astype(dataType)
            self.PandasCode.insertPlainText( f"\ndf[{column}] = df[{column}].astype[{dataType}]")
            self.OutputText.repaint()
        except Exception as e:
            self.OutputText.insertPlainText('\n'+str(e)+'\n')
            self.OutputText.repaint()

    def retranslateUi(self, DataTypeWindow):
        _translate = QtCore.QCoreApplication.translate
        DataTypeWindow.setWindowTitle(_translate("DataTypeWindow", "Form"))
        self.dataTypeWindow.setText(_translate("DataTypeWindow", "Column to Change Format of:"))
        self.stringButton.setText(_translate("DataTypeWindow", "String"))
        self.integerButton.setText(_translate("DataTypeWindow", "Integer"))
        self.floatButton.setText(_translate("DataTypeWindow", "Float"))
        self.castButton.setText(_translate("DataTypeWindow", "Cast Type"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dataTypeWindow = QtWidgets.QMainWindow()
    ui = Ui_summerWindow()
    ui.setupUi(sumColumnWindow)
    dataTypeWindow.show()
    sys.exit(app.exec_())

