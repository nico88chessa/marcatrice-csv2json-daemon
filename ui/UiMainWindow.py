# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '..\..\src\ui\MainWindow.ui',
# licensing of '..\..\src\ui\MainWindow.ui' applies.
#
# Created: Mon Mar 25 22:23:34 2019
#      by: pyside2-uic  running on PySide2 5.12.1
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
        self.gridLayout.setSpacing(2)
        self.gridLayout.setContentsMargins(2, 2, 2, 2)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 2)
        self.leSourcePath = MDLineEdit(self.wMain)
        self.leSourcePath.setStyleSheet("")
        self.leSourcePath.setProperty("labelX", 14)
        self.leSourcePath.setProperty("labelY", 28)
        self.leSourcePath.setProperty("labelTextWidth", 12)
        self.leSourcePath.setProperty("labelColor", QtGui.QColor(0, 0, 0))
        self.leSourcePath.setProperty("labelFocusColor", QtGui.QColor(46, 125, 50, 87))
        self.leSourcePath.setObjectName("leSourcePath")
        self.gridLayout.addWidget(self.leSourcePath, 0, 0, 1, 2)
        self.glButton = QtWidgets.QGridLayout()
        self.glButton.setSpacing(2)
        self.glButton.setContentsMargins(0, 0, 0, 0)
        self.glButton.setObjectName("glButton")
        self.pbStart = QtWidgets.QPushButton(self.wMain)
        self.pbStart.setObjectName("pbStart")
        self.glButton.addWidget(self.pbStart, 0, 1, 1, 1)
        self.pbStop = QtWidgets.QPushButton(self.wMain)
        self.pbStop.setObjectName("pbStop")
        self.glButton.addWidget(self.pbStop, 0, 2, 1, 1)
        self.cbIsRunning = QtWidgets.QCheckBox(self.wMain)
        self.cbIsRunning.setText("")
        self.cbIsRunning.setObjectName("cbIsRunning")
        self.glButton.addWidget(self.cbIsRunning, 0, 5, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.glButton.addItem(spacerItem1, 0, 4, 1, 1)
        self.pbStyle = QtWidgets.QPushButton(self.wMain)
        self.pbStyle.setObjectName("pbStyle")
        self.glButton.addWidget(self.pbStyle, 0, 3, 1, 1)
        self.gridLayout.addLayout(self.glButton, 1, 0, 1, 2)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.wMain)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout.addWidget(self.plainTextEdit, 3, 0, 1, 2)
        MainWindow.setCentralWidget(self.wMain)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.leSourcePath, self.pbStart)
        MainWindow.setTabOrder(self.pbStart, self.pbStop)
        MainWindow.setTabOrder(self.pbStop, self.pbStyle)
        MainWindow.setTabOrder(self.pbStyle, self.cbIsRunning)
        MainWindow.setTabOrder(self.cbIsRunning, self.plainTextEdit)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "Csv2Json Converter", None, -1))
        self.leSourcePath.setProperty("label", QtWidgets.QApplication.translate("MainWindow", "Source Path", None, -1))
        self.pbStart.setText(QtWidgets.QApplication.translate("MainWindow", "Start", None, -1))
        self.pbStop.setText(QtWidgets.QApplication.translate("MainWindow", "Stop", None, -1))
        self.pbStyle.setText(QtWidgets.QApplication.translate("MainWindow", "Style", None, -1))

from ui.MDLineEdit import MDLineEdit
