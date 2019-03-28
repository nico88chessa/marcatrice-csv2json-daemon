# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui\MainWindow.ui',
# licensing of '.\ui\MainWindow.ui' applies.
#
# Created: Wed Mar 27 15:03:22 2019
#      by: pyside2-uic  running on PySide2 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(673, 497)
        self.wMain = QtWidgets.QWidget(MainWindow)
        self.wMain.setObjectName("wMain")
        self.gridLayout = QtWidgets.QGridLayout(self.wMain)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.content = QtWidgets.QFrame(self.wMain)
        self.content.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.content.setFrameShadow(QtWidgets.QFrame.Plain)
        self.content.setObjectName("content")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.content)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.cbIsRunning = QtWidgets.QCheckBox(self.content)
        self.cbIsRunning.setText("")
        self.cbIsRunning.setObjectName("cbIsRunning")
        self.gridLayout_2.addWidget(self.cbIsRunning, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 1, 0, 1, 1)
        self.leSourcePath = MDLineEdit(self.content)
        self.leSourcePath.setStyleSheet("")
        self.leSourcePath.setProperty("labelX", 14)
        self.leSourcePath.setProperty("labelY", 28)
        self.leSourcePath.setProperty("labelTextWidth", 12)
        self.leSourcePath.setProperty("labelColor", QtGui.QColor(0, 0, 0))
        self.leSourcePath.setProperty("labelFocusColor", QtGui.QColor(46, 125, 50, 87))
        self.leSourcePath.setObjectName("leSourcePath")
        self.gridLayout_2.addWidget(self.leSourcePath, 0, 0, 1, 2)
        self.pteEditor = QtWidgets.QPlainTextEdit(self.content)
        self.pteEditor.setObjectName("pteEditor")
        self.gridLayout_2.addWidget(self.pteEditor, 2, 0, 1, 2)
        self.gridLayout.addWidget(self.content, 0, 0, 1, 1)
        self.bottom = QtWidgets.QFrame(self.wMain)
        self.bottom.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.bottom.setFrameShadow(QtWidgets.QFrame.Plain)
        self.bottom.setObjectName("bottom")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.bottom)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pbStyle = QtWidgets.QPushButton(self.bottom)
        self.pbStyle.setObjectName("pbStyle")
        self.horizontalLayout.addWidget(self.pbStyle)
        self.pbStart = QtWidgets.QPushButton(self.bottom)
        self.pbStart.setObjectName("pbStart")
        self.horizontalLayout.addWidget(self.pbStart)
        self.pbStop = QtWidgets.QPushButton(self.bottom)
        self.pbStop.setObjectName("pbStop")
        self.horizontalLayout.addWidget(self.pbStop)
        self.gridLayout.addWidget(self.bottom, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.wMain)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "Csv2Json Converter", None, -1))
        self.leSourcePath.setProperty("label", QtWidgets.QApplication.translate("MainWindow", "Source Path", None, -1))
        self.pbStyle.setText(QtWidgets.QApplication.translate("MainWindow", "Style", None, -1))
        self.pbStart.setText(QtWidgets.QApplication.translate("MainWindow", "Start", None, -1))
        self.pbStop.setText(QtWidgets.QApplication.translate("MainWindow", "Stop", None, -1))

from ui.MDLineEdit import MDLineEdit
