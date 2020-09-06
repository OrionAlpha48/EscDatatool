from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd

class Ui_Melter(QtWidgets.QWidget):

    dfSignalMelter = QtCore.pyqtSignal(pd.DataFrame)
    resultSignal = QtCore.pyqtSignal(str)

    def setupUi(self, melterWindow, df):
        global dfForMelting
        dfForMelting = df

        melterWindow.setObjectName("melterWindow")
        melterWindow.resize(400, 199)

        self.verticalLayoutWidget = QtWidgets.QWidget(Melter)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 9, 381, 116))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.rowValues = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.rowValues.setObjectName("rowValues")
        self.verticalLayout.addWidget(self.rowValues)

        self.columnValues = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.columnValues.setObjectName("columnValues")
        self.verticalLayout.addWidget(self.columnValues)

        self.pivotColumns = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.pivotColumns.setObjectName("pivotColumns")
        self.verticalLayout.addWidget(self.pivotColumns)

        self.pivotWithColumns = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.pivotWithColumns.setObjectName("pivotWithColumns")
        self.verticalLayout.addWidget(self.pivotWithColumns)

        self.meltButton = QtWidgets.QPushButton(Melter)
        self.meltButton.setGeometry(QtCore.QRect(140, 140, 113, 32))
        self.meltButton.setObjectName("meltButton")

        self.meltButton.clicked.connect(self.melter)
        self.retranslateUi(melterWindow)
        QtCore.QMetaObject.connectSlotsByName(melterWindow)

    def retranslateUi(self, melterWindow):
        _translate = QtCore.QCoreApplication.translate
        melterWindow.setWindowTitle(_translate("Melter", "Form"))
        self.rowValues.setText(_translate("Melter", "Value Vars"))
        self.columnValues.setText(_translate("Melter", "Value Name"))
        self.pivotColumns.setText(_translate("Melter", "ID Vars"))
        self.pivotWithColumns.setText(_translate("Melter", "Value Vars"))
        self.meltButton.setText(_translate("Melter", "Unpivot"))

    def melter(self, df):
        ##make sure your variables follow the same pattern in how their written for readability
        try:
            nameOfRowValues= rowvalue.get()
            nameOfColumnValues= colvalue.get()
            pivotOnColumns=pivoncolumns.get()
            pivotWithColumns=pivwithcolumns.get()
            df=df
            df=pd.melt(df, id_vars=pivotOnColumns,
                 value_vars=pivotWithColumns.split(', '),
                 value_name=nameOfRowValues,
                 var_name=nameOfColumnValues)
            self.OutputText.insertPlainText(df.to_string())
            self.PandasCode.insertPlainText(f"""\npd.melt(df, id_vars={[pivotOnColumns]},
                value_vars={pivotWithColumns}.split(', '),
                value_name={nameOfRowValues},
                var_name={nameOfColumnValues})""")
            self.OutputText.repaint()
        except Exception as e:
            self.resultSignal.emit('\n'+str(e)+'\n')
            self.OutputText.repaint()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    melterWindow = QtWidgets.QMainWindow()
    ui = Ui_Melter()
    ui.setupUi(melterWindow)
    melterWindow.show()
    sys.exit(app.exec_())