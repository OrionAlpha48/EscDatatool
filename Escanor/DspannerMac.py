from PyQt5 import QtCore, QtGui, QtWidgets
#Imports
import pandas as pd
import numpy as np
import boto3
import io
import os
import datetime
import sys, traceback
import tkinter as tk

class Ui_MainWindow(object):
    def setupUi(self, DSpanner):
        DSpanner.setObjectName("DSpanner")
        DSpanner.resize(1440, 783)
        self.centralwidget = QtWidgets.QWidget(DSpanner)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 1, 711, 771))
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
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CodeSwitch.sizePolicy().hasHeightForWidth())
        self.CodeSwitch.setSizePolicy(sizePolicy)
        self.CodeSwitch.setObjectName("CodeSwitch")
        self.Pandas = QtWidgets.QWidget()
        self.Pandas.setObjectName("Pandas")
        self.PandasScrollArea = QtWidgets.QScrollArea(self.Pandas)
        self.PandasScrollArea.setGeometry(QtCore.QRect(0, 0, 699, 366))
        self.PandasScrollArea.setWidgetResizable(True)
        self.PandasScrollArea.setObjectName("PandasScrollArea")
        self.PandasScrollAreaWidget = QtWidgets.QWidget()
        self.PandasScrollAreaWidget.setGeometry(QtCore.QRect(0, 0, 697, 364))
        self.PandasScrollAreaWidget.setObjectName("PandasScrollAreaWidget")
        self.PandasCode = QtWidgets.QPlainTextEdit(self.PandasScrollAreaWidget)
        self.PandasCode.setGeometry(QtCore.QRect(0, 0, 681, 341))
        self.PandasCode.setObjectName("PandasCode")
        self.PandasScroll = QtWidgets.QScrollBar(self.PandasScrollAreaWidget)
        self.PandasScroll.setGeometry(QtCore.QRect(680, 0, 16, 341))
        self.PandasScroll.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.PandasScroll.setOrientation(QtCore.Qt.Vertical)
        self.PandasScroll.setObjectName("PandasScroll")
        self.PandasScrollArea.setWidget(self.PandasScrollAreaWidget)
        self.CodeSwitch.addTab(self.Pandas, "")
        self.PySpark = QtWidgets.QWidget()
        self.PySpark.setObjectName("PySpark")
        self.PySparkScrollArea = QtWidgets.QScrollArea(self.PySpark)
        self.PySparkScrollArea.setGeometry(QtCore.QRect(0, 0, 691, 341))
        self.PySparkScrollArea.setWidgetResizable(True)
        self.PySparkScrollArea.setObjectName("PySparkScrollArea")
        self.PySparkScrollAreaWidget = QtWidgets.QWidget()
        self.PySparkScrollAreaWidget.setGeometry(QtCore.QRect(0, 0, 689, 339))
        self.PySparkScrollAreaWidget.setObjectName("PySparkScrollAreaWidget")
        self.PysparkCode = QtWidgets.QPlainTextEdit(self.PySparkScrollAreaWidget)
        self.PysparkCode.setGeometry(QtCore.QRect(3, -2, 681, 341))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PysparkCode.sizePolicy().hasHeightForWidth())
        self.PysparkCode.setSizePolicy(sizePolicy)
        self.PysparkCode.setObjectName("PysparkCode")
        self.PySparkScroll = QtWidgets.QScrollBar(self.PySparkScrollAreaWidget)
        self.PySparkScroll.setGeometry(QtCore.QRect(670, 0, 16, 321))
        self.PySparkScroll.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.PySparkScroll.setOrientation(QtCore.Qt.Vertical)
        self.PySparkScroll.setObjectName("PySparkScroll")
        self.PySparkScrollArea.setWidget(self.PySparkScrollAreaWidget)
        self.CodeSwitch.addTab(self.PySpark, "")
        self.Outputs.addWidget(self.CodeSwitch)
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
        self.ScrollPandas = QtWidgets.QScrollArea(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ScrollPandas.sizePolicy().hasHeightForWidth())
        self.ScrollPandas.setSizePolicy(sizePolicy)
        self.ScrollPandas.setWidgetResizable(True)
        self.ScrollPandas.setObjectName("ScrollPandas")
        self.ScollPandasArea = QtWidgets.QWidget()
        self.ScollPandasArea.setGeometry(QtCore.QRect(0, 0, 697, 343))
        self.ScollPandasArea.setObjectName("ScollPandasArea")
        self.OutputText = QtWidgets.QTextEdit(self.ScollPandasArea)
        self.OutputText.setGeometry(QtCore.QRect(3, -2, 681, 371))
        self.OutputText.setObjectName("OutputText")
        self.OutputScroll = QtWidgets.QScrollBar(self.ScollPandasArea)
        self.OutputScroll.setGeometry(QtCore.QRect(680, 0, 16, 361))
        self.OutputScroll.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.OutputScroll.setOrientation(QtCore.Qt.Vertical)
        self.OutputScroll.setObjectName("OutputScroll")
        self.ScrollPandas.setWidget(self.ScollPandasArea)
        self.Outputs.addWidget(self.ScrollPandas)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(739, 0, 701, 771))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.Tools = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.Tools.setContentsMargins(0, 0, 0, 0)
        self.Tools.setObjectName("Tools")
        self.ToolsLabel = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
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
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(-1, 19, 701, 181))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.UtilitiesLayout = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.UtilitiesLayout.setContentsMargins(0, 0, 0, 0)
        self.UtilitiesLayout.setObjectName("UtilitiesLayout")
        self.MakeCSVButton = QtWidgets.QToolButton(self.gridLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MakeCSVButton.sizePolicy().hasHeightForWidth())
        self.MakeCSVButton.setSizePolicy(sizePolicy)
        self.MakeCSVButton.setObjectName("MakeCSVButton")
        self.UtilitiesLayout.addWidget(self.MakeCSVButton, 0, 2, 1, 1)
        self.RestoreDFButton = QtWidgets.QToolButton(self.gridLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RestoreDFButton.sizePolicy().hasHeightForWidth())
        self.RestoreDFButton.setSizePolicy(sizePolicy)
        self.RestoreDFButton.setObjectName("RestoreDFButton")
        self.UtilitiesLayout.addWidget(self.RestoreDFButton, 0, 1, 1, 1)
        self.SaveDFButton = QtWidgets.QToolButton(self.gridLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SaveDFButton.sizePolicy().hasHeightForWidth())
        self.SaveDFButton.setSizePolicy(sizePolicy)
        self.SaveDFButton.setObjectName("SaveDFButton")
        self.UtilitiesLayout.addWidget(self.SaveDFButton, 0, 0, 1, 1)
        self.Tools.addWidget(self.UtilitiesBox)
        self.CleanBox = QtWidgets.QGroupBox(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CleanBox.sizePolicy().hasHeightForWidth())
        self.CleanBox.setSizePolicy(sizePolicy)
        self.CleanBox.setObjectName("CleanBox")
        self.gridLayoutWidget = QtWidgets.QWidget(self.CleanBox)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 20, 701, 171))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.CleanLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.CleanLayout.setContentsMargins(0, 0, 0, 0)
        self.CleanLayout.setSpacing(0)
        self.CleanLayout.setObjectName("CleanLayout")
        self.RemoveValueInColumnButton = QtWidgets.QToolButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RemoveValueInColumnButton.sizePolicy().hasHeightForWidth())
        self.RemoveValueInColumnButton.setSizePolicy(sizePolicy)
        self.RemoveValueInColumnButton.setObjectName("RemoveValueInColumnButton")
        self.CleanLayout.addWidget(self.RemoveValueInColumnButton, 1, 0, 1, 1)
        self.ColumnTitlesLowerCaseButton = QtWidgets.QToolButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ColumnTitlesLowerCaseButton.sizePolicy().hasHeightForWidth())
        self.ColumnTitlesLowerCaseButton.setSizePolicy(sizePolicy)
        self.ColumnTitlesLowerCaseButton.setObjectName("ColumnTitlesLowerCaseButton")
        self.CleanLayout.addWidget(self.ColumnTitlesLowerCaseButton, 0, 1, 1, 1)
        self.DropBlankColumnsButton = QtWidgets.QToolButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DropBlankColumnsButton.sizePolicy().hasHeightForWidth())
        self.DropBlankColumnsButton.setSizePolicy(sizePolicy)
        self.DropBlankColumnsButton.setObjectName("DropBlankColumnsButton")
        self.CleanLayout.addWidget(self.DropBlankColumnsButton, 0, 0, 1, 1)
        self.RemoveWhiteSpaceInHeadersButton = QtWidgets.QToolButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RemoveWhiteSpaceInHeadersButton.sizePolicy().hasHeightForWidth())
        self.RemoveWhiteSpaceInHeadersButton.setSizePolicy(sizePolicy)
        self.RemoveWhiteSpaceInHeadersButton.setObjectName("RemoveWhiteSpaceInHeadersButton")
        self.CleanLayout.addWidget(self.RemoveWhiteSpaceInHeadersButton, 0, 2, 1, 1)
        self.StripWhiteSpaceInColumnsButton = QtWidgets.QToolButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.StripWhiteSpaceInColumnsButton.sizePolicy().hasHeightForWidth())
        self.StripWhiteSpaceInColumnsButton.setSizePolicy(sizePolicy)
        self.StripWhiteSpaceInColumnsButton.setObjectName("StripWhiteSpaceInColumnsButton")
        self.CleanLayout.addWidget(self.StripWhiteSpaceInColumnsButton, 1, 1, 1, 1)
        self.Tools.addWidget(self.CleanBox)
        self.TransformBox = QtWidgets.QGroupBox(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TransformBox.sizePolicy().hasHeightForWidth())
        self.TransformBox.setSizePolicy(sizePolicy)
        self.TransformBox.setObjectName("TransformBox")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.TransformBox)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(0, 20, 701, 171))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.TransformLayout = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.TransformLayout.setContentsMargins(0, 0, 0, 0)
        self.TransformLayout.setSpacing(0)
        self.TransformLayout.setObjectName("TransformLayout")
        self.AdvancedMathematicsButton = QtWidgets.QToolButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AdvancedMathematicsButton.sizePolicy().hasHeightForWidth())
        self.AdvancedMathematicsButton.setSizePolicy(sizePolicy)
        self.AdvancedMathematicsButton.setObjectName("AdvancedMathematicsButton")
        self.TransformLayout.addWidget(self.AdvancedMathematicsButton, 1, 2, 1, 1)
        self.BasicMathematicsButton = QtWidgets.QToolButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BasicMathematicsButton.sizePolicy().hasHeightForWidth())
        self.BasicMathematicsButton.setSizePolicy(sizePolicy)
        self.BasicMathematicsButton.setObjectName("BasicMathematicsButton")
        self.TransformLayout.addWidget(self.BasicMathematicsButton, 0, 2, 1, 1)
        self.CastDataTypesButton = QtWidgets.QToolButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CastDataTypesButton.sizePolicy().hasHeightForWidth())
        self.CastDataTypesButton.setSizePolicy(sizePolicy)
        self.CastDataTypesButton.setObjectName("CastDataTypesButton")
        self.TransformLayout.addWidget(self.CastDataTypesButton, 0, 0, 1, 1)
        self.MeltTransposeDataButton = QtWidgets.QToolButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MeltTransposeDataButton.sizePolicy().hasHeightForWidth())
        self.MeltTransposeDataButton.setSizePolicy(sizePolicy)
        self.MeltTransposeDataButton.setObjectName("MeltTransposeDataButton")
        self.TransformLayout.addWidget(self.MeltTransposeDataButton, 0, 1, 1, 1)
        self.SubstituteValuesButton = QtWidgets.QToolButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SubstituteValuesButton.sizePolicy().hasHeightForWidth())
        self.SubstituteValuesButton.setSizePolicy(sizePolicy)
        self.SubstituteValuesButton.setObjectName("SubstituteValuesButton")
        self.TransformLayout.addWidget(self.SubstituteValuesButton, 1, 0, 1, 1)
        self.Tools.addWidget(self.TransformBox)
        self.AnalyseBox = QtWidgets.QGroupBox(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AnalyseBox.sizePolicy().hasHeightForWidth())
        self.AnalyseBox.setSizePolicy(sizePolicy)
        self.AnalyseBox.setObjectName("AnalyseBox")
        self.gridLayoutWidget_5 = QtWidgets.QWidget(self.AnalyseBox)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(0, 20, 699, 171))
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
        self.SumColumnButton = QtWidgets.QToolButton(self.gridLayoutWidget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SumColumnButton.sizePolicy().hasHeightForWidth())
        self.SumColumnButton.setSizePolicy(sizePolicy)
        self.SumColumnButton.setObjectName("SumColumnButton")
        self.AnalyseLayout.addWidget(self.SumColumnButton, 0, 2, 1, 1)
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
        self.SumColumnButton.raise_()
        self.CountRowsButton.raise_()
        self.MemoryUsageEstimateButton.raise_()
        self.StorageUsageEstimateButton.raise_()
        self.Tools.addWidget(self.AnalyseBox)
        DSpanner.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(DSpanner)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1440, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuImport_Data = QtWidgets.QMenu(self.menubar)
        self.menuImport_Data.setObjectName("menuImport_Data")
        self.menuExport_Data = QtWidgets.QMenu(self.menubar)
        self.menuExport_Data.setObjectName("menuExport_Data")
        self.menuCloud_Settings = QtWidgets.QMenu(self.menubar)
        self.menuCloud_Settings.setObjectName("menuCloud_Settings")
        DSpanner.setMenuBar(self.menubar)
        self.menubar.setNativeMenuBar(False)
        self.statusbar = QtWidgets.QStatusBar(DSpanner)
        self.statusbar.setObjectName("statusbar")
        DSpanner.setStatusBar(self.statusbar)
        self.CredentialsAWS = QtWidgets.QAction(DSpanner)
        self.CredentialsAWS.setObjectName("CredentialsAWS")
        self.CredentialsAzure = QtWidgets.QAction(DSpanner)
        self.CredentialsAzure.setObjectName("CredentialsAzure")
        self.ExportCSV = QtWidgets.QAction(DSpanner)
        self.ExportCSV.setObjectName("ExportCSV")
        self.ExportPSV = QtWidgets.QAction(DSpanner)
        self.ExportPSV.setObjectName("ExportPSV")
        self.ExportExcel = QtWidgets.QAction(DSpanner)
        self.ExportExcel.setObjectName("ExportExcel")
        self.ExportText = QtWidgets.QAction(DSpanner)
        self.ExportText.setObjectName("ExportText")
        self.ImportCSV = QtWidgets.QAction(DSpanner)
        self.ImportCSV.setObjectName("ImportCSV")
        self.ImportExcel = QtWidgets.QAction(DSpanner)
        self.ImportExcel.setObjectName("ImportExcel")
        self.Quit = QtWidgets.QAction(DSpanner)
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

        self.retranslateUi(DSpanner)
        self.CodeSwitch.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(DSpanner)


#button connections      
        self.CheckDataFrame.clicked.connect(self.checker)
        self.RestoreDFButton.clicked.connect(self.RestoreDF)
        self.SaveDFButton.clicked.connect(self.SaveDF)
        self.ColumnTitlesLowerCaseButton.clicked.connect(self.columnLowerCase)
        self.DropBlankColumnsButton.clicked.connect(self.dropBlankColumns)
        self.RemoveWhiteSpaceInHeadersButton.clicked.connect(self.stripWhiteSpace)
        self.CastDataTypesButton.clicked.connect(self.executeDataCast)
        self.CountRowsButton.clicked.connect(self.RowCount)
        self.PrintDataTypesButton.clicked.connect(self.printDatatypes)
        self.MemoryUsageEstimateButton.clicked.connect(self.memoryUsage)
        self.FindNullsButton.clicked.connect(self.executefindnulls)
        self.StorageUsageEstimateButton.clicked.connect(self.StorageUsage)

#menu connections
        self.menuImport_Data.triggered.connect(self.openCSV)

    def retranslateUi(self, DSpanner):
        _translate = QtCore.QCoreApplication.translate
        DSpanner.setWindowTitle(_translate("DSpanner", "MainWindow"))
        self.Outputs_Label.setText(_translate("DSpanner", "Outputs"))
        self.CodeSwitch.setTabText(self.CodeSwitch.indexOf(self.Pandas), _translate("DSpanner", "Pandas"))
        self.CodeSwitch.setTabText(self.CodeSwitch.indexOf(self.PySpark), _translate("DSpanner", "PySpark"))
        self.CheckDataFrame.setText(_translate("DSpanner", "Check Data Frame"))
        self.OutputText.setHtml(_translate("DSpanner", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.ToolsLabel.setText(_translate("DSpanner", "Tools"))
        self.UtilitiesBox.setTitle(_translate("DSpanner", "Utilities"))
        self.MakeCSVButton.setText(_translate("DSpanner", "Make CSV"))
        self.RestoreDFButton.setText(_translate("DSpanner", "Restore DF"))
        self.SaveDFButton.setText(_translate("DSpanner", "Save DF"))
        self.CleanBox.setTitle(_translate("DSpanner", "Clean"))
        self.RemoveValueInColumnButton.setText(_translate("DSpanner", "Remove Value in Column"))
        self.ColumnTitlesLowerCaseButton.setText(_translate("DSpanner", "Column Titles Lower Case"))
        self.DropBlankColumnsButton.setText(_translate("DSpanner", "Drop Blank Columns"))
        self.RemoveWhiteSpaceInHeadersButton.setText(_translate("DSpanner", "Remove White Space In Headers"))
        self.StripWhiteSpaceInColumnsButton.setText(_translate("DSpanner", "Strip White Space in Columns"))
        self.TransformBox.setTitle(_translate("DSpanner", "Transform"))
        self.AdvancedMathematicsButton.setText(_translate("DSpanner", "Advanced Mathematic Functions"))
        self.BasicMathematicsButton.setText(_translate("DSpanner", "Basic Mathematics"))
        self.CastDataTypesButton.setText(_translate("DSpanner", "Cast Data Types"))
        self.MeltTransposeDataButton.setText(_translate("DSpanner", "Melt/Transpose Data"))
        self.SubstituteValuesButton.setText(_translate("DSpanner", "Substitute Values"))
        self.AnalyseBox.setTitle(_translate("DSpanner", "Analyse"))
        self.CountRowsButton.setText(_translate("DSpanner", "Count Rows"))
        self.SumColumnButton.setText(_translate("DSpanner", "Sum Column"))
        self.PrintDataTypesButton.setText(_translate("DSpanner", "Print Data Types"))
        self.MemoryUsageEstimateButton.setText(_translate("DSpanner", "Memory Usage Estimate"))
        self.FindNullsButton.setText(_translate("DSpanner", "Find Nulls"))
        self.StorageUsageEstimateButton.setText(_translate("DSpanner", "Storage Usage Estimate"))
        self.menuFile.setTitle(_translate("DSpanner", "File"))
        self.menuImport_Data.setTitle(_translate("DSpanner", "Import Data"))
        self.menuExport_Data.setTitle(_translate("DSpanner", "Export Data"))
        self.menuCloud_Settings.setTitle(_translate("DSpanner", "Cloud Settings"))
        self.CredentialsAWS.setText(_translate("DSpanner", "AWS"))
        self.CredentialsAzure.setText(_translate("DSpanner", "Azure"))
        self.ExportCSV.setText(_translate("DSpanner", "CSV"))
        self.ExportPSV.setText(_translate("DSpanner", "PSV"))
        self.ExportExcel.setText(_translate("DSpanner", "Excel"))
        self.ExportText.setText(_translate("DSpanner", "Text"))
        self.ImportCSV.setText(_translate("DSpanner", "CSV"))
        self.ImportExcel.setText(_translate("DSpanner", "Excel"))
        self.Quit.setText(_translate("DSpanner", "Quit"))


        

    ##Functions start here##
    def checker(self):
        try:
            self.OutputText.insertPlainText("Data as at: " + str(datetime.datetime.now()) +'\n' + df.to_string() + '\n\n')
        except Exception as e:
            self.OutputText.insertPlainText('\n'+str(e)+'\n')

    """
    def reader():
        credFNameEntry.delete('1.0', END)
        credEntry.delete('1.0', END)
        global credFName
        credFName=filedialog.askopenfilename(initialdir=r"")
        credFNameEntry.insert(END, credFName)
        with open(credFName, "r") as f:
                        credEntry.insert(END, f.read())
     
    def writer():
        fileName=credFNameEntry.get('1.0', END)
        with open(fileName.rstrip(), 'w') as cred_obj:
                        cred_obj.write(credEntry.get('1.0', 'end-1c'))
        cred_obj.close()
     
    def S3BucketData():
        global df
        targetObject=s3_client.get_object(Bucket=bucketEntry.get('1.0', 'end-1c'), Key=keyEntry.get('1.0', 'end-1c'))['Body'].read()
        if sheetEntry.get('1.0', 'end-1c') == '':
                        df=pd.read_excel(io.BytesIO(targetObject), encoding='utf-8')
        else:
                        df=pd.read_excel(io.BytesIO(targetObject), encoding='utf-8', sheet_name=sheetEntry.get('1.0', 'end-1c'))
    """               
     
    def dropBlankColumns(self):
        global df
        try:
            df=df
            df=df.loc[:, ~df.columns.str.contains('^Unnamed')]
            self.PandasCode.insertPlainText("df=df.loc[:, ~df.columns.str.contains('^Unnamed')]")
        except Exception as e:
            self.OutputText.insertPlainText('\n'+str(e)+'\n')
     
    def executeDataCast(self):
        global df
        try:
            df=df
            dataType=v.get()
            column=nameofColumnToChangeDataType.get()
            df[column] = df[column].astype(dataType)
            self.PandasCode.insertPlainText( f"\ndf[{column}] = df[{column}].astype[{dataType}]")
        except Exception as e:
            self.OutputText.insertPlainText('\n'+str(e)+'\n')
 
    def executefindnulls(self):
        global dfnulls
        global df
        try:
            df=df
            column=nameofColumnToCheckForNulls.get()
            dfnulls=df[df[column].isna()]
            self.OutputText.insertPlainText(dfnulls.to_string())
            self.PandasCode.insertPlainText(f"\ndf=df[df[{column}].isna()]")
        except Exception as e:
            self.OutputText.insertPlainText('\n'+str(e)+'\n')
      
                    

    def melter(self):
        ##make sure your variables follow the same pattern in how their written for readability
        global df
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
        except Exception as e:
            self.OutputText.insertPlainText('\n'+str(e)+'\n')

    # you can easily make a xls version of this, remember to alter the inital dir
    def openCSV(self):
        try:
            path = QtWidgets.QFileDialog.getOpenFileName(None, "Select CSV", "/Users/Orion 1/Desktop")[0]
            global df
            df=pd.read_csv(filepath_or_buffer=path)
        except Exception as e:
            self.OutputText.insertPlainText('\n'+str(e)+'\n')

    # def openxls():
    #     try:
    #         path=filedialog.askopenfilename(initialdir="/Desktop",title="Select a file")
    #         global df
    #         df=pd.read_excel(filepath_or_buffer=str(path))
    #     except Exception as e:
    #         self.OutputText.insertPlainText('\n'+str(e)+'\n')

        
    # ## TO DO: let them name their results themselves, not you. 
    # def makecsv():
    #     try:
    #         df.to_csv(path_or_buf=str(path)+ "results.csv")
    #     except Exception as e:
    #                     self.OutputText.insertPlainText('\n'+str(e)+'\n')   


    def printDatatypes(self):
        global df
        try:
            df=df
            output.insert('1.0',(df.dtypes))
            self.PandasCode.insertPlainText(f"""\n(df.dtypes)""")
        except Exception as e:
                    self.OutputText.insertPlainText('\n'+str(e)+'\n')
    
    def columnLowerCase(self):
        global df
        try:
            df=df
            df.columns=map(str.lower, df.columns)
            self.PandasCode.insertPlainText(f"""\ndf.columns=map(str.lower, df.columns)""")
        except Exception as e:
                        self.OutputText.insertPlainText('\n'+str(e)+'\n')
    
    def columnRemoveSpaces(self):
        global df
        try:
            df=df
            df.columns=df.columns.str.replace(' ', '_')
            self.PandasCode.insertPlainText(f"""\ndf.columns=df.columns.str.replace(' ', '_')""")
        except Exception as e:
                        self.OutputText.insertPlainText('\n'+str(e)+'\n')

## TO DO: This is cute, but what if its the sum of two columns per row.
## probably will never need the sum of all
    def SummOp(self):
        global df
        try:
            df=df
            res=df.groupby([groupByColumns.get()])[columnToSum.get()].sum()
            self.OutputText.insertPlainText(res)
            self.PandasCode.insertPlainText(f"""res=df.groupby([{groupByColumns}.get()])[{columnToSum}.get()].sum()""")
        except Exception as e:
            self.OutputText.insertPlainText('\n'+str(e)+'\n')


    def stripWhiteSpace(self):
        global df
        try:
            df=df
            columToStrip=columnsToStrip.get()
            df[columnToStrip] = df[columnToStrip].str.strip()
            self.OutputText.insertPlainText(df.to_string)
            self.PandasCode.insertPlainText(f"""df[{columnToStrip}] = df[{columnToStrip}].str.strip()""")
        except Exception as e:
                    self.OutputText.insertPlainText('\n'+str(e)+'\n')

# def summerPop(self):
#     summerPopUp=Toplevel(root, height=100, width=100)
#     global groupByColumns
#     global df
#     global columnToSum
#     df=df
#     groupByColumns=Entry(summerPopUp)
#     groupByColumns.insert(END, 'Group by Columns')
#     columnToSum=Entry(summerPopUp)
#     columnToSum.insert(END, 'Column to Sum')
#     groupByColumns.grid(row=0, column=0)
#     columnToSum.grid(row=1, column=0)
#     SummColumnButton=Button(summerPopUp, command=SummOp, text='Sum Column', highlightbackground="goldenrod2")
#     SummColumnButton.grid(row=2, column=0, pady=10, sticky= 'ew')


# def stripPop(self):
#     stripPopUp=Toplevel(root, height=100, width=100)
#     global columnToStrip
#     global df
#     df=df
#     columnsToStrip=Entry(stripPopUp)
#     columnsToStrip.grid(row=0, column=0)
#     stripColumnButton=Button(stripPopUp, command=stripWhiteSpace, text='strip White Space', highlightbackground="goldenrod2")
#     stripColumnButton.grid(row=1, column=0, pady=10, sticky= 'ew')


    def replacer(self):
        global df
        global valuetoReplace
        global relaceWith
        try:
            df=df
            df[columnToRep.get()] = df[columnToRep.get()].replace(valuetoReplace.get(), replaceWith.get())
            self.OutputText.insertPlainText(df.to_string)
            self.PandasCode.insertPlainText(f"""df[{columnToRep.get()}] = df[{columnToRep.get()}].replace({valuetoReplace.get()}, {replaceWith.get()})""")
        except Exception as e:
                    self.OutputText.insertPlainText('\n'+str(e)+'\n')

# def replacerPop(self):
#     replacerPopUp=Toplevel(root, height=100, width=100)
#     global columnToRep
#     global df
#     global valuetoReplace
#     global replaceWith
#     df=df
#     columnToRep=Entry(replacerPopUp)
#     valuetoReplace=Entry(replacerPopUp)
#     replaceWith=Entry(replacerPopUp)
#     columnToRep.grid(row=0, column=0)
#     valuetoReplace.grid(row=1, column=0)
#     replaceWith.grid(row=2, column=0)
#     replacerButton=Button(replacerPopUp, command=replacer, text='Replace', highlightbackground="goldenrod2")
#     replacerButton.grid(row=3, column=0, pady=10, sticky= 'ew')

    def SaveDF(self):
        global df
        global dfsaved
        try:
            dfsaved=df
        except Exception as e:
                    self.OutputText.insertPlainText('\n'+str(e)+'\n')

    def RestoreDF(self):
        global df
        global dfsaved
        try:
            df=dfsaved
        except Exception as e:
                    self.OutputText.insertPlainText('\n'+str(e)+'\n')

    def RowCount(self):
        global df
        try:
            self.OutputText.insertPlainText(len(df.index))
        except Exception as e:
            self.OutputText.insertPlainText('\n'+str(e)+'\n')

    def memoryUsage(self):
        global df
        try:
            self.OutputText.insertPlainText('\n'+ str(df.memory_usage(index=True).sum())+' mb\n')
        except Exception as e:
            self.OutputText.insertPlainText('\n'+str(e)+'\n')

    def StorageUsage(self):
        global df
        try:
            self.OutputText.insertPlainText('\n'+ str(float(sys.getsizeof(df)/1000000))+'\n')
        except Exception as e:
            self.OutputText.insertPlainText('\n'+str(e)+'\n')


    # def mathematicsFeatures(self):
    #             mathWindow=Toplevel(root, height=100, width=100)
    #             global resultColumnName
    #             global firstColumn
    #             global secondColumn
    #             resultColumnName=Entry(mathWindow)
    #             resultColumnName.pack()
    #             firstColumn=Entry(mathWindow)
    #             firstColumn.pack()
    #             secondColumn=Entry(mathWindow)
    #             secondColumn.pack()
    #             for text, operation in MATHAMATICS:
    #                             button=Radiobutton(mathWindow, text=text, variable=v, value=operation).pack()
    #             enterButton=Button(mathWindow,command=executeMathematics, text="Operate!", highlightbackground="goldenrod2").pack()
 
    def executeMathematics(self):
                global df
                global resultColumnName
                global firstColumn
                global secondColumn
                try:
                    df=df
                    resultColumnName=resultColumnName.get()
                    firstColumn=firstColumn.get()
                    secondColumn=secondColumn.get()
                    op=v.get()
                    if op == "Sum":
                        df[resultColumnName] = df[firstColumn] + df[secondColumn]
                        self.PandasCode.insertPlainText(f"\ndf[{resultColumnName}] = df[{firstColumn}] + df[{secondColumn}]")
                    elif op == "Subtract":
                        df[resultColumnName] = df[firstColumn] - df[secondColumn]
                        self.PandasCode.insertPlainText(f"\ndf[{resultColumnName}] = df[{firstColumn}] - df[{secondColumn}]")
                    elif op == "Mulitiply":
                        df[resultColumnName] = df[firstColumn] * df[secondColumn]
                        self.PandasCode.insertPlainText(f"\ndf[{resultColumnName}] = df[{firstColumn}] * df[{secondColumn}]")
                    elif op == "Divide":
                        df[resultColumnName] = df[firstColumn] / df[secondColumn]
                        self.PandasCode.insertPlainText(f"\ndf[{resultColumnName}] = df[{firstColumn}] / df[{secondColumn}]")
                except Exception as e:
                    self.OutputText.insertPlainText('\n'+str(e)+'\n')
    

## TO DO:
## row sum
## row multi
## row divide
## filter for value - see and shape
## rename columns function
## none of your entry fields have descriptions to prompt
## join function
## union function


# def dropPop(self):
#     replacerPopUp=Toplevel(root, height=100, width=100)
#     global columnsToDrop
#     global df
#     df=df
#     columnsToDrop=Entry(replacerPopUp).pack()
#     replacerButton=Button(dropPop, command=dropper, text='Replace', highlightbackground="goldenrod2")
#     replacerButton.pack()


    def dropper(self):
        global df
        global columnsToDrop
        try:
            df=df.drop(columns=columnsToDrop.get().split(', '))
        except Exception as e:
                    self.OutputText.insertPlainText('\n'+str(e)+'\n')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())




