# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/Orion 1/Desktop/sumColumnWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd


class Ui_Summer(QtWidgets.QWidget):
    
    resultSignal = QtCore.pyqtSignal(str)
    dfSignal = QtCore.pyqtSignal(pd.DataFrame)

    def setupUi(self, sumColumnWindow, df, OutputText):
        global dftosum
        dftosum = df
        sumColumnWindow.setObjectName("sumColumnWindow")
        sumColumnWindow.resize(400, 201)
        self.groupByColumns = QtWidgets.QLineEdit(sumColumnWindow)
        self.groupByColumns.setGeometry(QtCore.QRect(10, 100, 381, 31))
        self.groupByColumns.setObjectName("groupByColumns")
        self.columnToSum = QtWidgets.QLineEdit(sumColumnWindow)
        self.columnToSum.setGeometry(QtCore.QRect(10, 40, 381, 31))
        self.columnToSum.setObjectName("columnToSum")
        self.label = QtWidgets.QLabel(sumColumnWindow)
        self.label.setGeometry(QtCore.QRect(10, 20, 321, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(sumColumnWindow)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 161, 16))
        self.label_2.setObjectName("label_2")
        self.sumColumnButton = QtWidgets.QToolButton(sumColumnWindow)
        self.sumColumnButton.setGeometry(QtCore.QRect(140, 140, 101, 41))
        self.sumColumnButton.setObjectName("sumColumnButton")
        self.sumColumnButton.clicked.connect(self.SummOp)

        self.retranslateUi(sumColumnWindow)
        QtCore.QMetaObject.connectSlotsByName(sumColumnWindow)

    def retranslateUi(self, sumColumnWindow):
        _translate = QtCore.QCoreApplication.translate
        sumColumnWindow.setWindowTitle(_translate("sumColumnWindow", "sumColumnWindow"))
        self.label.setText(_translate("sumColumnWindow", "Group By Columns (eg Sum by Date, Business unit)"))
        self.label_2.setText(_translate("sumColumnWindow", "Column to Sum (eg Sales)"))
        self.sumColumnButton.setText(_translate("sumColumnWindow", "Sum Column"))


    def SummOp(self):
        try:
            #print(df)
            groupCol = str(self.groupByColumns.text())
            sumCol = str(self.columnToSum.text())
            res=dftosum.groupby([groupCol])[sumCol].sum()
            self.dfSignal.emit(res.to_frame())
            #OutputText.insertPlainText(res)
            #Ui_DSpanner.PandasCode.insertPlainText(f"""res=df.groupby([{groupByColumns}])[{columnToSum}].sum()""")
            #OutputText.repaint()
            #return res
        except Exception as e:
            self.resultSignal.emit('\n'+str(e)+'\n')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    sumColumnWindow = QtWidgets.QMainWindow()
    ui = Ui_summerWindow()
    ui.setupUi(sumColumnWindow)
    sumColumnWindow.show()
    sys.exit(app.exec_())
