from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd

class Ui_Replacer(QtWidgets.QWidget):
    
    dfSignalReplacer = QtCore.pyqtSignal(pd.DataFrame)
    resultSignal = QtCore.pyqtSignal(str)
    pandasSignal = QtCore.pyqtSignal(str)


    def setupUi(self, replacerWindow, df):
        global dfForReplacing
        dfForReplacing = df
        replacerWindow.setObjectName("replacerWindow")
        replacerWindow.resize(523, 190)
        self.replaceButton = QtWidgets.QPushButton(replacerWindow)
        self.replaceButton.setGeometry(QtCore.QRect(210, 140, 113, 32))
        self.replaceButton.setObjectName("replaceButton")
        self.targetColumn = QtWidgets.QLineEdit(replacerWindow)
        self.targetColumn.setGeometry(QtCore.QRect(20, 20, 481, 31))
        self.targetColumn.setObjectName("targetColumn")
        self.oldValue = QtWidgets.QLineEdit(replacerWindow)
        self.oldValue.setGeometry(QtCore.QRect(20, 60, 481, 31))
        self.oldValue.setObjectName("oldValue")
        self.newValue = QtWidgets.QLineEdit(replacerWindow)
        self.newValue.setGeometry(QtCore.QRect(20, 100, 481, 31))
        self.newValue.setObjectName("newValue")
        self.replaceButton.clicked.connect(self.replacer)

        self.retranslateUi(replacerWindow)
        QtCore.QMetaObject.connectSlotsByName(replacerWindow)

    def retranslateUi(self, replacerWindow):
        _translate = QtCore.QCoreApplication.translate
        replacerWindow.setWindowTitle(_translate("replacerWindow", "replacerWindow"))
        self.replaceButton.setText(_translate("replacerWindow", "Replace"))
        self.targetColumn.setText(_translate("replacerWindow", "Target Column"))
        self.oldValue.setText(_translate("replacerWindow", "Value To Replace"))
        self.newValue.setText(_translate("replacerWindow", "Value To Replace With"))

    def replacer(self):
        try:
            df=dfForReplacing
            df[self.targetColumn.text()] = df[self.targetColumn.text()].replace(self.oldValue.text(), self.newValue.text())
            self.dfSignalReplacer.emit(df)
            self.pandasSignal.emit(f"df[{self.targetColumn.text()}].replace({self.oldValue.text()}, {self.newValue.text()}")
        except Exception as e:
            self.resultSignal.emit('\n'+str(e)+'\n')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    replacerWindow = QtWidgets.QMainWindow()
    ui = Ui_Replacer()
    ui.setupUi(replacerWindow)
    replacerWindow.show()
    sys.exit(app.exec_())
