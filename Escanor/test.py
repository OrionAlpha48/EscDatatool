from PyQt5.Qt import *
from PyQt5.QtWidgets import QInputDialog, QLineEdit, QDialog, QApplication
from PyQt5 import QtCore, QtGui, QtWidgets

#Imports
import pandas as pd
import numpy as np
import boto3
import io
import os
import datetime
import sys, traceback
from sumWindow import Ui_Summer
from dataTypeWindow import Ui_DataTypeWindow

class Ui_DataSpanner(QtWidgets.QWidget):

    def setupUi(self, DataSpanner):
        DataSpanner.setObjectName("DataSpanner")
        DataSpanner.resize(1440, 783)
        self.centralwidget = QtWidgets.QWidget(DataSpanner)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 731, 731))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.Outputs = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.Outputs.setContentsMargins(0, 4, 0, 0)
        self.Outputs.setObjectName("Outputs")
        self.Outputs_Label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Avenir")
        font.setPointSize(20)
        self.Outputs_Label.setFont(font)
        self.Outputs_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Outputs_Label.setObjectName("Outputs_Label")
        self.Outputs.addWidget(self.Outputs_Label)
        self.CheckDataFrame = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.CheckDataFrame.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CheckDataFrame.sizePolicy().hasHeightForWidth())
        self.CheckDataFrame.setSizePolicy(sizePolicy)
        self.CheckDataFrame.setIconSize(QtCore.QSize(10, 16))
        self.CheckDataFrame.setObjectName("CheckDataFrame")
        self.Outputs.addWidget(self.CheckDataFrame)
        self.frame = QtWidgets.QFrame(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.OutputText = QtWidgets.QPlainTextEdit(self.frame)
        self.OutputText.setGeometry(QtCore.QRect(10, 0, 701, 321))
        font = QtGui.QFont()
        font.setFamily("Avenir")
        font.setPointSize(12)
        self.OutputText.setFont(font)
        self.OutputText.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.OutputText.setObjectName("OutputText")
        self.Outputs.addWidget(self.frame)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(739, 0, 701, 771))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.Tools = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.Tools.setContentsMargins(0, 0, 0, 0)
        self.Tools.setObjectName("Tools")
        self.ToolsLabel = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ToolsLabel.sizePolicy().hasHeightForWidth())
        self.ToolsLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Avenir")
        font.setPointSize(20)
        self.ToolsLabel.setFont(font)
        self.ToolsLabel.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.ToolsLabel.setObjectName("ToolsLabel")
        self.Tools.addWidget(self.ToolsLabel)
        self.UtilitiesBox = QtWidgets.QGroupBox(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.UtilitiesBox.sizePolicy().hasHeightForWidth())
        self.UtilitiesBox.setSizePolicy(sizePolicy)
        self.UtilitiesBox.setObjectName("UtilitiesBox")
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.UtilitiesBox)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(9, 19, 681, 171))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.UtilitiesLayout = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.UtilitiesLayout.setContentsMargins(0, 0, 0, 0)
        self.UtilitiesLayout.setObjectName("UtilitiesLayout")
        DataSpanner.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(DataSpanner)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1440, 22))
        self.menubar.setNativeMenuBar(False)
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuImport_Data = QtWidgets.QMenu(self.menubar)
        self.menuImport_Data.setObjectName("menuImport_Data")
        self.menuExport_Data = QtWidgets.QMenu(self.menubar)
        self.menuExport_Data.setObjectName("menuExport_Data")
        self.menuCloud_Settings = QtWidgets.QMenu(self.menubar)
        self.menuCloud_Settings.setObjectName("menuCloud_Settings")
        DataSpanner.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(DataSpanner)
        self.statusbar.setObjectName("statusbar")
        DataSpanner.setStatusBar(self.statusbar)
        self.CredentialsAWS = QtWidgets.QAction(DataSpanner)
        self.CredentialsAWS.setObjectName("CredentialsAWS")
        self.CredentialsAzure = QtWidgets.QAction(DataSpanner)
        self.CredentialsAzure.setObjectName("CredentialsAzure")
        self.ExportCSV = QtWidgets.QAction(DataSpanner)
        self.ExportCSV.setObjectName("ExportCSV")
        self.ExportPSV = QtWidgets.QAction(DataSpanner)
        self.ExportPSV.setObjectName("ExportPSV")
        self.ExportExcel = QtWidgets.QAction(DataSpanner)
        self.ExportExcel.setObjectName("ExportExcel")
        self.ExportText = QtWidgets.QAction(DataSpanner)
        self.ExportText.setObjectName("ExportText")
        self.ImportCSV = QtWidgets.QAction(DataSpanner)
        self.ImportCSV.setObjectName("ImportCSV")
        self.ImportExcel = QtWidgets.QAction(DataSpanner)
        self.ImportExcel.setObjectName("ImportExcel")
        self.Quit = QtWidgets.QAction(DataSpanner)
        self.Quit.setObjectName("Quit")
        self.menuFile.addAction(self.Quit)
        self.menuImport_Data.addAction(self.ImportCSV)
        self.menuImport_Data.addAction(self.ImportExcel)
        self.menuExport_Data.addAction(self.ExportCSV)
        self.menuExport_Data.addAction(self.ExportPSV)
        self.menuExport_Data.addAction(self.ExportExcel)
        self.menuExport_Data.addAction(self.ExportText)
        self.menuCloud_Settings.addAction(self.CredentialsAWS)
        self.menuCloud_Settings.addAction(self.CredentialsAzure)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuImport_Data.menuAction())
        self.menubar.addAction(self.menuExport_Data.menuAction())
        self.menubar.addAction(self.menuCloud_Settings.menuAction())
        self.SumColumnButton = QtWidgets.QToolButton(self.gridLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SumColumnButton.sizePolicy().hasHeightForWidth())
        self.SumColumnButton.setSizePolicy(sizePolicy)
        self.SumColumnButton.setObjectName("SumColumnButton")
        self.UtilitiesLayout.addWidget(self.SumColumnButton, 0, 2, 1, 1)
        
        self.w = None

        self.retranslateUi(DataSpanner)
        QtCore.QMetaObject.connectSlotsByName(DataSpanner)

#button connections      
        self.CheckDataFrame.clicked.connect(self.checker)
        self.SumColumnButton.clicked.connect(self.sumColumnWindowOpen)


#menu connections
        self.ImportCSV.triggered.connect(self.openCSV)


    @QtCore.pyqtSlot(str)
    def updateOutput(self, Output):
        self.OutputText.insertPlainText(Output)
        self.OutputText.repaint()

    def sumColumnWindowOpen(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Summer()
        self.ui.setupUi(self.window, dfSignal self.OutputText)
        self.ui.resultSignal.connect(self.updateOutput)
        self.window.show()

    def retranslateUi(self, DataSpanner):
        _translate = QtCore.QCoreApplication.translate
        DataSpanner.setWindowTitle(_translate("DataSpanner", "DataSpanner"))
        self.Outputs_Label.setText(_translate("DataSpanner", "Outputs"))
        self.CheckDataFrame.setText(_translate("DataSpanner", "Check Data Frame"))
        self.ToolsLabel.setText(_translate("DataSpanner", "Tools"))
        self.UtilitiesBox.setTitle(_translate("DataSpanner", "Utilities"))
        self.menuFile.setTitle(_translate("DataSpanner", "File"))
        self.menuImport_Data.setTitle(_translate("DataSpanner", "Import Data"))
        self.menuExport_Data.setTitle(_translate("DataSpanner", "Export Data"))
        self.menuCloud_Settings.setTitle(_translate("DataSpanner", "Cloud Settings"))
        self.CredentialsAWS.setText(_translate("DataSpanner", "AWS"))
        self.CredentialsAzure.setText(_translate("DataSpanner", "Azure"))
        self.ExportCSV.setText(_translate("DataSpanner", "CSV"))
        self.ExportPSV.setText(_translate("DataSpanner", "PSV"))
        self.ExportExcel.setText(_translate("DataSpanner", "Excel"))
        self.ExportText.setText(_translate("DataSpanner", "Text"))
        self.ImportCSV.setText(_translate("DataSpanner", "CSV"))
        self.ImportExcel.setText(_translate("DataSpanner", "Excel"))
        self.Quit.setText(_translate("DataSpanner", "Quit"))

    def checker(self):
        try:
            self.OutputText.insertPlainText("Data as at: " + str(datetime.datetime.now()) +'\n' + df.to_string() + '\n\n')
            self.OutputText.repaint()
        except Exception as e:
            self.OutputText.insertPlainText('\n'+str(e)+'\n')
            self.OutputText.repaint()
    
                    

    dfSignal = QtCore.pyqtSignal(pd.DataFrame)
    # you can easily make a xls version of this, remember to alter the inital dir
    def openCSV(self):
        try:
            path = QtWidgets.QFileDialog.getOpenFileName(None, "Select CSV", "/Desktop")[0]
            df=pd.read_csv(filepath_or_buffer=path)
            self.dfSignal.emit(df)
            self.OutputText.repaint()
        except Exception as e:
            self.OutputText.insertPlainText('\n'+str(e)+'\n')
            self.OutputText.repaint()







if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DataSpanner = QtWidgets.QMainWindow()
    ui = Ui_DataSpanner()
    ui.setupUi(DataSpanner)
    DataSpanner.show()
    sys.exit(app.exec_())



