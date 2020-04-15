from PyQt5 import QtCore, QtGui, QtWidgets
#Imports
from tkinter import *
from tkinter import filedialog
import pandas as pd
import numpy as np
import boto3
import io
import os
import datetime
import sys, traceback
import tkinter as tk

class Ui_DSpanner(object):
    def setupUi(self, DSpanner):
        DSpanner.setObjectName("DSpanner")
        DSpanner.resize(1440, 783)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DSpanner.sizePolicy().hasHeightForWidth())
        DSpanner.setSizePolicy(sizePolicy)
        DSpanner.setMinimumSize(QtCore.QSize(10, 10))
        self.verticalLayoutWidget = QtWidgets.QWidget(DSpanner)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 711, 781))
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
        self.CheckDataFrame.clicked.connect(self.checker)
        self.ScrollPandas = QtWidgets.QScrollArea(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ScrollPandas.sizePolicy().hasHeightForWidth())
        self.ScrollPandas.setSizePolicy(sizePolicy)
        self.ScrollPandas.setWidgetResizable(True)
        self.ScrollPandas.setObjectName("ScrollPandas")
        self.ScollPandasArea = QtWidgets.QWidget()
        self.ScollPandasArea.setGeometry(QtCore.QRect(0, 0, 697, 348))
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
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(DSpanner)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(739, -1, 701, 781))
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

        self.retranslateUi(DSpanner)
        self.CodeSwitch.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(DSpanner)

    def retranslateUi(self, DSpanner):
        _translate = QtCore.QCoreApplication.translate
        DSpanner.setWindowTitle(_translate("DSpanner", "Dialog"))
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
     
    def executeDataCast():
        global df
        try:
            df=df
            dataType=v.get()
            column=nameofColumnToChangeDataType.get()
            df[column] = df[column].astype(dataType)
            self.PandasCode.insertPlainText( f"\ndf[{column}] = df[{column}].astype[{dataType}]")
        except Exception as e:
            self.OutputText.insertPlainText('\n'+str(e)+'\n')

    ## TO DO: this needs its output written  
    def executefindnulls():
        global dfnulls
        global df
        try:
            df=df
            column=nameofColumnToCheckForNulls.get()
            dfnulls=df[df[column].isna()]
            output.insert('1.0', dfnulls.to_string())
            self.PandasCode.insertPlainText( f"\ndf=df[df[{column}].isna()]")
        except Exception as e:
            self.OutputText.insertPlainText('\n'+str(e)+'\n')
      
                    

    def melter():
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
            output.insert('1.0', df)
            self.PandasCode.insertPlainText(f"""\npd.melt(df, id_vars={[pivotOnColumns]},
                value_vars={pivotWithColumns}.split(', '),
                value_name={nameOfRowValues},
                var_name={nameOfColumnValues})""")
        except Exception as e:
            self.OutputText.insertPlainText('\n'+str(e)+'\n')

    ## you can easily make a xls version of this, remember to alter the inital dir
    # def opencsv():
    #     try:
    #         path=filedialog.askopenfilename(initialdir="/Desktop",title="Select a file")
    #         global df
    #         df=pd.read_csv(filepath_or_buffer=str(path))
    #     except Exception as e:
    #         output.insert('1.0', '\n'+str(e)+'\n')

    # def openxls():
    #     try:
    #         path=filedialog.askopenfilename(initialdir="/Desktop",title="Select a file")
    #         global df
    #         df=pd.read_excel(filepath_or_buffer=str(path))
    #     except Exception as e:
    #         output.insert('1.0', '\n'+str(e)+'\n')

        
    # ## TO DO: let them name their results themselves, not you. 
    # def makecsv():
    #     try:
    #         df.to_csv(path_or_buf=str(path)+ "results.csv")
    #     except Exception as e:
    #                     output.insert('1.0', '\n'+str(e)+'\n')   



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DSpanner = QtWidgets.QDialog()
    ui = Ui_DSpanner()
    ui.setupUi(DSpanner)
    DSpanner.show()
    sys.exit(app.exec_())



