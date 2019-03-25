from PySide2.QtWidgets import QMainWindow, QPushButton, QApplication
from PySide2.QtCore import QFile, QIODevice
from watchdog.observers import Observer

from ui import UiMainWindow
import Constants
import CustomEventHandler

class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = UiMainWindow.Ui_MainWindow()
        self.setupUi()
        self.setupSignalsAndSlots()
        self.obs = Observer()

    def setupUi(self):
        self.ui.setupUi(self)
        with open(Constants.STYLESHEET_PATH) as fd:
            self.setStyleSheet(fd.read())

    def setupSignalsAndSlots(self):
        self.ui.pbStyle.clicked.connect(self.reloadStyle)
        self.ui.pbStart.clicked.connect(self.start)
        self.ui.pbStop.clicked.connect(self.stop)

    def reloadStyle(self):
        with open(Constants.STYLESHEET_PATH) as fd:
            self.setStyleSheet(fd.read())

    def start(self):
        path = self.ui.leSourcePath.text()
        eventHandler = CustomEventHandler.CustomEventHandler(path)
        self.obs.schedule(eventHandler, path)
        self.obs.start()
        self.obs.join()


    def stop(self):
        self.obs.stop()
