from PyQt5.Qt import *
from PyQt5.QtWidgets import QInputDialog, QLineEdit, QDialog, QApplication
from PyQt5 import QtCore, QtGui, QtWidgets

#Imports
import pandas as pd
import numpy as np
import boto3, io
import os
import datetime
import sys, traceback
from sumWindow import Ui_Summer
from dataTypeWindow import Ui_DataTypeWindow
from melterWindow import Ui_Melter
from nullFinderWindow import Ui_Unnull
from whiteSpaceStripWindow import Ui_RemoveWhiteSpace
from replacerWindow import Ui_Replacer
from basicMathWindow import Ui_basicMathWindow

class Ui_DataSpanner(QMainWindow):

    
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
        self.CodeSwitch = QtWidgets.QTabWidget(self.verticalLayoutWidget)
        self.CodeSwitch.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CodeSwitch.sizePolicy().hasHeightForWidth())
        self.CodeSwitch.setSizePolicy(sizePolicy)
        self.CodeSwitch.setObjectName("CodeSwitch")
        
        #Pandas outputs area
        self.Pandas = QtWidgets.QWidget()
        self.Pandas.setObjectName("Pandas")
        self.PandasScrollArea = QtWidgets.QScrollArea(self.Pandas)
        self.PandasScrollArea.setGeometry(QtCore.QRect(0, 0, 731, 321))
        self.PandasScrollArea.setWidgetResizable(True)
        self.PandasScrollArea.setObjectName("PandasScrollArea")
        self.PandasScrollAreaWidget = QtWidgets.QWidget()
        self.PandasScrollAreaWidget.setGeometry(QtCore.QRect(0, 0, 729, 319))
        self.PandasScrollAreaWidget.setObjectName("PandasScrollAreaWidget")
        self.PandasCode = QtWidgets.QPlainTextEdit(self.PandasScrollAreaWidget)
        self.PandasCode.setGeometry(QtCore.QRect(0, 0, 731, 321))
        font = QtGui.QFont()
        font.setFamily("Avenir")
        font.setPointSize(12)
        self.PandasCode.setFont(font)
        self.PandasCode.setObjectName("PandasCode")
        self.PandasScrollArea.setWidget(self.PandasScrollAreaWidget)
        self.CodeSwitch.addTab(self.Pandas, "")
        
        #PySpark outputs area
        self.PySpark = QtWidgets.QWidget()
        self.PySpark.setObjectName("PySpark")
        self.PySparkScrollArea = QtWidgets.QScrollArea(self.PySpark)
        self.PySparkScrollArea.setGeometry(QtCore.QRect(0, 0, 731, 321))
        self.PySparkScrollArea.setWidgetResizable(True)
        self.PySparkScrollArea.setObjectName("PySparkScrollArea")
        self.PySparkScrollAreaWidget = QtWidgets.QWidget()
        self.PySparkScrollAreaWidget.setGeometry(QtCore.QRect(0, 0, 729, 319))
        self.PySparkScrollAreaWidget.setObjectName("PySparkScrollAreaWidget")
        self.PysparkCode = QtWidgets.QPlainTextEdit(self.PySparkScrollAreaWidget)
        self.PysparkCode.setGeometry(QtCore.QRect(10, 0, 691, 321))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PysparkCode.sizePolicy().hasHeightForWidth())
        self.PysparkCode.setSizePolicy(sizePolicy)
        self.PysparkCode.setObjectName("PysparkCode")
        self.PySparkScrollArea.setWidget(self.PySparkScrollAreaWidget)
        self.CodeSwitch.addTab(self.PySpark, "")
        self.Outputs.addWidget(self.CodeSwitch)
        self.CheckDataFrame = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.CheckDataFrame.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CheckDataFrame.sizePolicy().hasHeightForWidth())
        
        #Check DataFrame button
        self.CheckDataFrame.setSizePolicy(sizePolicy)
        self.CheckDataFrame.setIconSize(QtCore.QSize(10, 16))
        self.CheckDataFrame.setObjectName("CheckDataFrame")
        self.Outputs.addWidget(self.CheckDataFrame)
        self.frame = QtWidgets.QFrame(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        
        #output text formattings
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
        
        #Tools/Buttons box and layout
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
        
        #Utilities box
        self.UtilitiesBox = QtWidgets.QGroupBox(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        #sizePolicy.setVerticalStretch(0)
        #sizePolicy.setHeightForWidth(self.UtilitiesBox.sizePolicy().hasHeightForWidth())
        self.UtilitiesBox.setSizePolicy(sizePolicy)
        self.UtilitiesBox.setObjectName("UtilitiesBox")
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.UtilitiesBox)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(9, 19, 400, 171))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.UtilitiesLayout = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.UtilitiesLayout.setContentsMargins(0, 0, 0, 0)
        self.UtilitiesLayout.setObjectName("UtilitiesLayout")
        
        #makeCSV Button Set up
        self.MakeCSVButton = QtWidgets.QToolButton(self.gridLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        #sizePolicy.setHeightForWidth(self.MakeCSVButton.sizePolicy().hasHeightForWidth())
        self.MakeCSVButton.setSizePolicy(sizePolicy)
        self.MakeCSVButton.setObjectName("MakeCSVButton")
        self.UtilitiesLayout.addWidget(self.MakeCSVButton, 0, 2, 1, 1)
        
        #Restore DF Set up
        self.RestoreDFButton = QtWidgets.QToolButton(self.gridLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RestoreDFButton.sizePolicy().hasHeightForWidth())
        self.RestoreDFButton.setSizePolicy(sizePolicy)
        self.RestoreDFButton.setObjectName("RestoreDFButton")
        self.UtilitiesLayout.addWidget(self.RestoreDFButton, 0, 1, 1, 1)
        
        #Save DF Button
        self.SaveDFButton = QtWidgets.QToolButton(self.gridLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SaveDFButton.sizePolicy().hasHeightForWidth())
        self.SaveDFButton.setSizePolicy(sizePolicy)
        self.SaveDFButton.setObjectName("SaveDFButton")
        self.UtilitiesLayout.addWidget(self.SaveDFButton, 0, 0, 1, 1)
        self.Tools.addWidget(self.UtilitiesBox)

        
        #clean box set up
        self.CleanBox = QtWidgets.QGroupBox(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CleanBox.sizePolicy().hasHeightForWidth())
        self.CleanBox.setSizePolicy(sizePolicy)
        self.CleanBox.setObjectName("CleanBox")
        self.gridLayoutWidget = QtWidgets.QWidget(self.CleanBox)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 20, 681, 171))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.CleanLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.CleanLayout.setContentsMargins(0, 0, 0, 0)
        self.CleanLayout.setSpacing(0)
        self.CleanLayout.setObjectName("CleanLayout")
        
        #remove value in column
        self.RemoveValueInColumnButton = QtWidgets.QToolButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RemoveValueInColumnButton.sizePolicy().hasHeightForWidth())
        self.RemoveValueInColumnButton.setSizePolicy(sizePolicy)
        self.RemoveValueInColumnButton.setObjectName("RemoveValueInColumnButton")
        self.CleanLayout.addWidget(self.RemoveValueInColumnButton, 1, 0, 1, 1)
        
        #column titles to lower case
        self.ColumnTitlesLowerCaseButton = QtWidgets.QToolButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ColumnTitlesLowerCaseButton.sizePolicy().hasHeightForWidth())
        self.ColumnTitlesLowerCaseButton.setSizePolicy(sizePolicy)
        self.ColumnTitlesLowerCaseButton.setObjectName("ColumnTitlesLowerCaseButton")
        self.CleanLayout.addWidget(self.ColumnTitlesLowerCaseButton, 0, 1, 1, 1)
        
        #DropblankColumns
        self.DropBlankColumnsButton = QtWidgets.QToolButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DropBlankColumnsButton.sizePolicy().hasHeightForWidth())
        self.DropBlankColumnsButton.setSizePolicy(sizePolicy)
        self.DropBlankColumnsButton.setObjectName("DropBlankColumnsButton")
        self.CleanLayout.addWidget(self.DropBlankColumnsButton, 0, 0, 1, 1)
        
        #Remove White Space In Headers
        self.RemoveWhiteSpaceInHeadersButton = QtWidgets.QToolButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RemoveWhiteSpaceInHeadersButton.sizePolicy().hasHeightForWidth())
        self.RemoveWhiteSpaceInHeadersButton.setSizePolicy(sizePolicy)
        self.RemoveWhiteSpaceInHeadersButton.setObjectName("RemoveWhiteSpaceInHeadersButton")
        self.CleanLayout.addWidget(self.RemoveWhiteSpaceInHeadersButton, 0, 2, 1, 1)
        
        #strip whitespace in column
        self.StripWhiteSpaceInColumnsButton = QtWidgets.QToolButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.StripWhiteSpaceInColumnsButton.sizePolicy().hasHeightForWidth())
        self.StripWhiteSpaceInColumnsButton.setSizePolicy(sizePolicy)
        self.StripWhiteSpaceInColumnsButton.setObjectName("StripWhiteSpaceInColumnsButton")
        self.CleanLayout.addWidget(self.StripWhiteSpaceInColumnsButton, 1, 1, 1, 1)
        self.Tools.addWidget(self.CleanBox)
        
        #Set Up Transform Box
        self.TransformBox = QtWidgets.QGroupBox(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TransformBox.sizePolicy().hasHeightForWidth())
        self.TransformBox.setSizePolicy(sizePolicy)
        self.TransformBox.setObjectName("TransformBox")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.TransformBox)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 20, 681, 171))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.TransformLayout = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.TransformLayout.setContentsMargins(0, 0, 0, 0)
        self.TransformLayout.setSpacing(0)
        self.TransformLayout.setObjectName("TransformLayout")
        
        #advanced Mathematics button
        self.AdvancedMathematicsButton = QtWidgets.QToolButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AdvancedMathematicsButton.sizePolicy().hasHeightForWidth())
        self.AdvancedMathematicsButton.setSizePolicy(sizePolicy)
        self.AdvancedMathematicsButton.setObjectName("AdvancedMathematicsButton")
        self.TransformLayout.addWidget(self.AdvancedMathematicsButton, 1, 2, 1, 1)
        
        #Melt Data Button
        self.MeltTransposeDataButton = QtWidgets.QToolButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MeltTransposeDataButton.sizePolicy().hasHeightForWidth())
        self.MeltTransposeDataButton.setSizePolicy(sizePolicy)
        self.MeltTransposeDataButton.setObjectName("MeltTransposeDataButton")
        self.TransformLayout.addWidget(self.MeltTransposeDataButton, 0, 1, 1, 1)
        
        #Cast Data type button 
        self.CastDataTypesButton = QtWidgets.QToolButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CastDataTypesButton.sizePolicy().hasHeightForWidth())
        self.CastDataTypesButton.setSizePolicy(sizePolicy)
        self.CastDataTypesButton.setObjectName("CastDataTypesButton")
        self.TransformLayout.addWidget(self.CastDataTypesButton, 0, 0, 1, 1)
        
        #Basic Mathematics button
        self.BasicMathematicsButton = QtWidgets.QToolButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BasicMathematicsButton.sizePolicy().hasHeightForWidth())
        self.BasicMathematicsButton.setSizePolicy(sizePolicy)
        self.BasicMathematicsButton.setObjectName("BasicMathematicsButton")
        self.TransformLayout.addWidget(self.BasicMathematicsButton, 0, 2, 1, 1)
        
        #Substitute Values Button
        self.SubstituteValuesButton = QtWidgets.QToolButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SubstituteValuesButton.sizePolicy().hasHeightForWidth())
        self.SubstituteValuesButton.setSizePolicy(sizePolicy)
        self.SubstituteValuesButton.setObjectName("SubstituteValuesButton")
        self.TransformLayout.addWidget(self.SubstituteValuesButton, 1, 0, 1, 1)
        self.Tools.addWidget(self.TransformBox)
        
        #analyse Box
        self.AnalyseBox = QtWidgets.QGroupBox(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AnalyseBox.sizePolicy().hasHeightForWidth())
        self.AnalyseBox.setSizePolicy(sizePolicy)
        self.AnalyseBox.setObjectName("AnalyseBox")
        self.gridLayoutWidget_5 = QtWidgets.QWidget(self.AnalyseBox)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(10, 20, 681, 141))
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")
        self.AnalyseLayout = QtWidgets.QGridLayout(self.gridLayoutWidget_5)
        self.AnalyseLayout.setContentsMargins(0, 0, 0, 0)
        self.AnalyseLayout.setSpacing(0)
        self.AnalyseLayout.setObjectName("AnalyseLayout")
        self.CountRowsButton = QtWidgets.QToolButton(self.gridLayoutWidget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CountRowsButton.sizePolicy().hasHeightForWidth())
        self.CountRowsButton.setSizePolicy(sizePolicy)
        self.CountRowsButton.setObjectName("CountRowsButton")
        self.AnalyseLayout.addWidget(self.CountRowsButton, 0, 3, 1, 1)
        self.sumColumnButton = QtWidgets.QToolButton(self.gridLayoutWidget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sumColumnButton.sizePolicy().hasHeightForWidth())
        self.sumColumnButton.setSizePolicy(sizePolicy)
        self.sumColumnButton.setObjectName("sumColumnButton")
        self.AnalyseLayout.addWidget(self.sumColumnButton, 0, 2, 1, 1)
        self.PrintDataTypesButton = QtWidgets.QToolButton(self.gridLayoutWidget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PrintDataTypesButton.sizePolicy().hasHeightForWidth())
        self.PrintDataTypesButton.setSizePolicy(sizePolicy)
        self.PrintDataTypesButton.setObjectName("PrintDataTypesButton")
        self.AnalyseLayout.addWidget(self.PrintDataTypesButton, 0, 0, 1, 1)
        self.MemoryUsageEstimateButton = QtWidgets.QToolButton(self.gridLayoutWidget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MemoryUsageEstimateButton.sizePolicy().hasHeightForWidth())
        self.MemoryUsageEstimateButton.setSizePolicy(sizePolicy)
        self.MemoryUsageEstimateButton.setObjectName("MemoryUsageEstimateButton")
        self.AnalyseLayout.addWidget(self.MemoryUsageEstimateButton, 1, 0, 1, 1)
        self.FindNullsButton = QtWidgets.QToolButton(self.gridLayoutWidget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FindNullsButton.sizePolicy().hasHeightForWidth())
        self.FindNullsButton.setSizePolicy(sizePolicy)
        self.FindNullsButton.setObjectName("FindNullsButton")
        self.AnalyseLayout.addWidget(self.FindNullsButton, 0, 1, 1, 1)
        self.StorageUsageEstimateButton = QtWidgets.QToolButton(self.gridLayoutWidget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.StorageUsageEstimateButton.sizePolicy().hasHeightForWidth())
        self.StorageUsageEstimateButton.setSizePolicy(sizePolicy)
        self.StorageUsageEstimateButton.setObjectName("StorageUsageEstimateButton")
        self.AnalyseLayout.addWidget(self.StorageUsageEstimateButton, 1, 1, 1, 1)
        self.PrintDataTypesButton.raise_()
        self.FindNullsButton.raise_()
        self.sumColumnButton.raise_()
        self.CountRowsButton.raise_()
        self.MemoryUsageEstimateButton.raise_()
        self.StorageUsageEstimateButton.raise_()
        self.Tools.addWidget(self.AnalyseBox)
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
        self.w = None

        self.retranslateUi(DataSpanner)
        self.CodeSwitch.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(DataSpanner)

#Self Dependant Buttons      
        self.CheckDataFrame.clicked.connect(self.checker)
        self.RestoreDFButton.clicked.connect(self.RestoreDF)
        self.SaveDFButton.clicked.connect(self.SaveDF)
        self.ColumnTitlesLowerCaseButton.clicked.connect(self.columnLowerCase)
        self.DropBlankColumnsButton.clicked.connect(self.dropBlankColumns)
        self.RemoveWhiteSpaceInHeadersButton.clicked.connect(self.RemoveSpacesInColumnTitle)
        self.CountRowsButton.clicked.connect(self.RowCount)
        self.PrintDataTypesButton.clicked.connect(self.printDatatypes)
        self.MemoryUsageEstimateButton.clicked.connect(self.memoryUsage)
        self.ImportCSV.triggered.connect(self.openCSV)
        self.ImportExcel.triggered.connect(self.openxls)
        self.StorageUsageEstimateButton.clicked.connect(self.StorageUsage)

#Open Window Button
        
        self.CastDataTypesButton.clicked.connect(self.dataTypeWindowOpen)
        self.StripWhiteSpaceInColumnsButton.clicked.connect(self.whiteSpaceStripWindowOpen)
        self.sumColumnButton.clicked.connect(self.sumColumnWindowOpen)
        self.MeltTransposeDataButton.clicked.connect(self.melterWindowOpen)
        self.FindNullsButton.clicked.connect(self.nullFinderWindowOpen)
        self.SubstituteValuesButton.clicked.connect(self.subValueWindowOpen)
        self.BasicMathematicsButton.clicked.connect(self.basicMathWindowOpen)

    #slot connections
    @QtCore.pyqtSlot(str)
    def updateOutput(self, Output):
        self.OutputText.insertPlainText(Output)
        self.OutputText.repaint()

    @QtCore.pyqtSlot(pd.DataFrame)
    def updateDF(self, df):
        self.OutputText.insertPlainText(df.to_string())
        self.OutputText.repaint()

    @QtCore.pyqtSlot(str)
    def addPythoncode(self, newCode):
        self.PandasCode.insertPlainText(newCode)
        self.PandasCode.repaint()

    #Window Definitions
    def subValueWindowOpen(self):
        try:
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_Replacer()
            self.ui.setupUi(self.window, df)
            self.ui.resultSignal.connect(self.updateOutput)
            self.ui.dfSignalReplacer.connect(self.updateDF)
            self.ui.pandasSignal.connect(self.addPythoncode)
            self.window.show()
        except Exception as e:
            self.OutputText.insertPlainText('\n'+str(e)+'\n')
            self.OutputText.repaint()

    def sumColumnWindowOpen(self):
        try:
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_Summer()
            self.ui.setupUi(self.window, df, self.OutputText)
            self.ui.resultSignal.connect(self.updateOutput)
            self.ui.dfSignalSum.connect(self.updateDF)
            self.ui.pandasSignal.connect(self.addPythoncode)
            self.window.show()
        except Exception as e:
            self.OutputText.insertPlainText('\n'+str(e)+'\n')
            self.OutputText.repaint()    

    def melterWindowOpen(self):
        try:
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_Melter()
            self.ui.setupUi(self.window, df)
            self.ui.resultSignal.connect(self.updateOutput)
            self.ui.dfSignalMelter.connect(self.updateDF)
            self.ui.pandasSignal.connect(self.addPythoncode)
            self.window.show()
        except Exception as e:
            self.OutputText.insertPlainText('\n'+str(e)+'\n')
            self.OutputText.repaint()

    def dataTypeWindowOpen(self):
        try:
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_DataTypeWindow()
            self.ui.setupUi(self.window, df)
            self.ui.resultSignal.connect(self.updateOutput)
            self.ui.dfSignalDataType.connect(self.updateDF)
            self.ui.pandasSignal.connect(self.addPythoncode)
            self.window.show()
        except Exception as e:
            self.OutputText.insertPlainText('\n'+str(e)+'\n')
            self.OutputText.repaint()

    def nullFinderWindowOpen(self):
        try:
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_Unnull()
            self.ui.setupUi(self.window, df)
            self.ui.resultSignal.connect(self.updateOutput)
            self.ui.dfSignalNulls.connect(self.updateDF)
            self.ui.pandasSignal.connect(self.addPythoncode)
            self.window.show()
        except Exception as e:
            self.OutputText.insertPlainText('\n'+str(e)+'\n')
            self.OutputText.repaint()

    def whiteSpaceStripWindowOpen(self):
        try:
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_RemoveWhiteSpace()
            self.ui.setupUi(self.window, df)
            self.ui.resultSignal.connect(self.updateOutput)
            self.ui.dfSignal.connect(self.updateDF)
            self.ui.pandasSignal.connect(self.addPythoncode)
            self.window.show()
        except Exception as e:
            self.OutputText.insertPlainText('\n'+str(e)+'\n')
            self.OutputText.repaint()

    def basicMathWindowOpen(self):
        try:
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_basicMathWindow()
            self.ui.setupUi(self.window, df)
            self.ui.resultSignal.connect(self.updateOutput)
            self.ui.dfSignal.connect(self.updateDF)
            self.ui.pandasSignal.connect(self.addPythoncode)
            self.window.show()
        except Exception as e:
            self.OutputText.insertPlainText('\n'+str(e)+'\n')
            self.OutputText.repaint()


    def retranslateUi(self, DataSpanner):
        _translate = QtCore.QCoreApplication.translate
        DataSpanner.setWindowTitle(_translate("DataSpanner", "DataSpanner"))
        self.Outputs_Label.setText(_translate("DataSpanner", "Outputs"))
        self.CodeSwitch.setTabText(self.CodeSwitch.indexOf(self.Pandas), _translate("DataSpanner", "Pandas"))
        self.CodeSwitch.setTabText(self.CodeSwitch.indexOf(self.PySpark), _translate("DataSpanner", "PySpark"))
        self.CheckDataFrame.setText(_translate("DataSpanner", "Check Data Frame"))
        self.ToolsLabel.setText(_translate("DataSpanner", "Tools"))
        self.UtilitiesBox.setTitle(_translate("DataSpanner", "Utilities"))
        self.MakeCSVButton.setText(_translate("DataSpanner", "Make CSV"))
        self.RestoreDFButton.setText(_translate("DataSpanner", "Restore DF"))
        self.SaveDFButton.setText(_translate("DataSpanner", "Save DF"))
        self.CleanBox.setTitle(_translate("DataSpanner", "Clean"))
        self.RemoveValueInColumnButton.setText(_translate("DataSpanner", "Remove Value in Column"))
        self.ColumnTitlesLowerCaseButton.setText(_translate("DataSpanner", "Column Titles Lower Case"))
        self.DropBlankColumnsButton.setText(_translate("DataSpanner", "Drop Blank Columns"))
        self.RemoveWhiteSpaceInHeadersButton.setText(_translate("DataSpanner", "Remove White Space In Headers"))
        self.StripWhiteSpaceInColumnsButton.setText(_translate("DataSpanner", "Strip White Space in Columns"))
        self.TransformBox.setTitle(_translate("DataSpanner", "Transform"))
        self.AdvancedMathematicsButton.setText(_translate("DataSpanner", "Advanced Mathematic Functions"))
        self.MeltTransposeDataButton.setText(_translate("DataSpanner", "Melt/Transpose Data"))
        self.CastDataTypesButton.setText(_translate("DataSpanner", "Cast Data Types"))
        self.BasicMathematicsButton.setText(_translate("DataSpanner", "Basic Mathematics"))
        self.SubstituteValuesButton.setText(_translate("DataSpanner", "Substitute Values"))
        self.AnalyseBox.setTitle(_translate("DataSpanner", "Analyse"))
        self.CountRowsButton.setText(_translate("DataSpanner", "Count Rows"))
        self.sumColumnButton.setText(_translate("DataSpanner", "Sum Column"))
        self.PrintDataTypesButton.setText(_translate("DataSpanner", "Print Data Types"))
        self.MemoryUsageEstimateButton.setText(_translate("DataSpanner", "Memory Usage Estimate"))
        self.FindNullsButton.setText(_translate("DataSpanner", "Find Nulls"))
        self.StorageUsageEstimateButton.setText(_translate("DataSpanner", "Storage Usage Estimate"))
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
            self.OutputText.insertPlainText("\nData as at: " + str(datetime.datetime.now()) +'\n' + df.to_string() + '\n\n')
            self.OutputText.repaint()
        except Exception as e:
            self.OutputText.insertPlainText('\n'+str(e)+'\n')
            self.OutputText.repaint()
    
    def dropBlankColumns(self):
        global df
        try:
            df=df
            df=df.loc[:, ~df.columns.str.contains('^Unnamed')]
            self.PandasCode.insertPlainText("\ndf=df.loc[:, ~df.columns.str.contains('^Unnamed')]")
            self.OutputText.repaint()
        except Exception as e:
            self.OutputText.insertPlainText('\n'+str(e)+'\n')
            self.OutputText.repaint()
      
                    
    # you can easily make a xls version of this, remember to alter the inital dir
    def openCSV(self):
        try:
            path = QtWidgets.QFileDialog.getOpenFileName(None, "Select CSV", "*/Escanor")[0]
            global df
            df=pd.read_csv(filepath_or_buffer=path)
            self.OutputText.repaint()
        except Exception as e:
            self.OutputText.insertPlainText('\n'+str(e)+'\n')
            self.OutputText.repaint()

    def openxls(self):
        try:
            path = QtWidgets.QFileDialog.getOpenFileName(None, "xls", "/Desktop")[0]
            global df
            df=pd.read_excel(io=path, filepath_or_buffer=path)
            self.OutputText.repaint()
        except Exception as e:
            self.OutputText.insertPlainText('\n'+str(e)+'\n')
            self.OutputText.repaint()

        
    # ## TO DO: let them name their results themselves, not you. 
    # def makecsv():
    #     try:
    #         df.to_csv(path_or_buf=str(path)+ "results.csv")
    #self.OutputText.repaint()
    #     except Exception as e:
    #                     self.OutputText.insertPlainText('\n'+str(e)+'\n')   
    #self.OutputText.repaint()


    def printDatatypes(self):
        global df
        try:
            df=df
            self.OutputText.insertPlainText(str(df.dtypes))
            self.PandasCode.insertPlainText(f"""\n(df.dtypes)""")
            self.OutputText.repaint()
        except Exception as e:
            self.OutputText.insertPlainText('\n'+str(e)+'\n')
            self.OutputText.repaint()
    
    def columnLowerCase(self):
        global df
        try:
            df=df
            df.columns=map(str.lower, df.columns)
            self.PandasCode.insertPlainText(f"""\ndf.columns=map(str.lower, df.columns)""")
            self.OutputText.repaint()
        except Exception as e:
            self.OutputText.insertPlainText('\n'+str(e)+'\n')
            self.OutputText.repaint()
    
    def RemoveSpacesInColumnTitle(self):
        global df
        try:
            df=df
            df.columns=df.columns.str.replace(' ', '_')
            self.PandasCode.insertPlainText(f"""\ndf.columns=df.columns.str.replace(' ', '_')""")
            self.OutputText.repaint()
        except Exception as e:
            self.OutputText.insertPlainText('\n'+str(e)+'\n')
            self.OutputText.repaint()


    def SaveDF(self):
        global df
        global dfsaved
        try:
            dfsaved=df
            self.OutputText.repaint()
        except Exception as e:
                    self.OutputText.insertPlainText('\n'+str(e)+'\n')
                    self.OutputText.repaint()

    def RestoreDF(self):
        global df
        global dfsaved
        try:
            df=dfsaved
            self.OutputText.repaint()
        except Exception as e:
            self.OutputText.insertPlainText('\n'+str(e)+'\n')
            self.OutputText.repaint()

    def RowCount(self):
        global df
        try:
            self.OutputText.insertPlainText('\n'+str(len(df)+'\n'))
            self.OutputText.repaint()
        except Exception as e:
            self.OutputText.insertPlainText('\n'+str(e)+'\n')
            self.OutputText.repaint()

    def memoryUsage(self):
        global df
        try:
            self.OutputText.insertPlainText('\n'+ str(df.memory_usage(index=True).sum())+' mb\n')
            self.OutputText.repaint()
        except Exception as e:
            self.OutputText.insertPlainText('\n'+str(e)+'\n')
            self.OutputText.repaint()

    def StorageUsage(self):
        global df
        try:
            self.OutputText.insertPlainText('\n'+ str(float(sys.getsizeof(df)/1000000))+'GB\n')
            self.OutputText.repaint()
        except Exception as e:
            self.OutputText.insertPlainText('\n'+str(e)+'\n')
            self.OutputText.repaint()

# def AWSreader():
#     credFNameEntry.delete('1.0', END)
#     credEntry.delete('1.0', END)
#     global credFName
#     credFName=filedialog.askopenfilename(initialdir=r"")
#     credFNameEntry.insert(END, credFName)
#     with open(credFName, "r") as f:
#                     credEntry.insert(END, f.read())
 
# def AWSwriter():
#     fileName=credFNameEntry.get('1.0', END)
#     with open(fileName.rstrip(), 'w') as cred_obj:
#                     cred_obj.write(credEntry.get('1.0', 'end-1c'))
#     cred_obj.close()
 
# def S3BucketData():
#     global df
#     targetObject=s3_client.get_object(Bucket=bucketEntry.get('1.0', 'end-1c'), Key=keyEntry.get('1.0', 'end-1c'))['Body'].read()
#     if sheetEntry.get('1.0', 'end-1c') == '':
#                     df=pd.read_excel(io.BytesIO(targetObject), encoding='utf-8')
#     else:
#                     df=pd.read_excel(io.BytesIO(targetObject), encoding='utf-8', sheet_name=sheetEntry.get('1.0', 'end-1c'))


## TO DO:
## row sum
## row multi
## row divide
## filter for value - see and shape
## rename columns function
## none of your entry fields have descriptions to prompt
## join function
## union function




    def dropper(self):
        global df
        global columnsToDrop
        try:
            df=df.drop(columns=columnsToDrop.get().split(', '))
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



