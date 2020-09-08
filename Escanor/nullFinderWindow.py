import pandas as pd
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Unnull(QtWidgets.QWidget):
    dfSignalNulls = QtCore.pyqtSignal(pd.DataFrame)
    resultSignal = QtCore.pyqtSignal(str)

    def setupUi(self, nullFinderWindow, df):
        global dfFindNulls
        dfFindNulls = df

        nullFinderWindow.setObjectName("nullFinderWindow")
        nullFinderWindow.resize(424, 116)
        self.verticalLayoutWidget = QtWidgets.QWidget(nullFinderWindow)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 401, 31))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.columnWithNulls = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.columnWithNulls.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.columnWithNulls)
        self.unNullButton = QtWidgets.QPushButton(nullFinderWindow)
        self.unNullButton.setGeometry(QtCore.QRect(160, 70, 113, 32))
        self.unNullButton.setObjectName("pushButton")
        self.unNullButton.clicked.connect(self.executeFindNulls)

        self.retranslateUi(nullFinderWindow)
        QtCore.QMetaObject.connectSlotsByName(nullFinderWindow)

    def retranslateUi(self, nullFinderWindow):
        _translate = QtCore.QCoreApplication.translate
        nullFinderWindow.setWindowTitle(_translate("nullFinderWindow", "nullFinderWindow"))
        self.columnWithNulls.setText(_translate("nullFinderWindow", "Column to Find Nulls In"))
        self.unNullButton.setText(_translate("nullFinderWindow", "Delete Nulls"))


    def executeFindNulls(self, df):
        try:
            df=dfFindNulls
            column=str(self.columnWithNulls.text())
            dfnulls=df[df[column].isna()]
            self.dfSignalNulls.emit(dfnulls)
        except Exception as e:
            self.resultSignal.emit('\n'+str(e)+'\n')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    nullFinderWindow = QtWidgets.QMainWindow()
    ui = Ui_Melter()
    ui.setupUi(nullFinderWindow)
    nullFinderWindow.show()
    sys.exit(app.exec_())
