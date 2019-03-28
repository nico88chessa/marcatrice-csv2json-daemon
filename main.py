from CustomEventHandler import CustomEventHandler
from watchdog.observers import Observer
from ui import MainWindow
from PySide2 import QtCore, QtWidgets, QtGui
from Logger import Logger


if __name__ == "__main__":

    Logger().info("Apertura CSV2JSON")

    app = QtWidgets.QApplication([])
    mainWindow = MainWindow.MainWindow()
    mainWindow.show()
    app.exec_()
