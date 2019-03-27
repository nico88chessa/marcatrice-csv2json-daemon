from PySide2.QtWidgets import QMainWindow, QPushButton, QApplication
from PySide2.QtCore import QFile, QIODevice
from watchdog.observers import Observer

import CustomEventHandler
from ui import UiMainWindow
from Logger import Logger
from Settings import Settings

class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        Logger().debug("Creazione oggetto MainWindow")

        self.ui = UiMainWindow.Ui_MainWindow()
        self.setupUi()
        self.setupSignalsAndSlots()
        self.obs = Observer()

    def setupUi(self):
        self.ui.setupUi(self)
        with open(Settings().getStyleSheetPath()) as fd:
            self.setStyleSheet(fd.read())

    def setupSignalsAndSlots(self):
        Logger().debug("Aggancio segnali signals/slots")
        self.ui.pbStyle.clicked.connect(self.reloadStyle)
        self.ui.pbStart.clicked.connect(self.start)
        self.ui.pbStop.clicked.connect(self.stop)

    def reloadStyle(self):
        Logger().debug("Ricarico foglio di stile")
        with open(Settings().getStyleSheetPath()) as fd:
            self.setStyleSheet(fd.read())

    def start(self):
        Logger().info("Start thread daemon")
        path = self.ui.leSourcePath.text()
        Logger().info("Path daemon: "+path)
        eventHandler = CustomEventHandler.CustomEventHandler(path)
        self.obs.schedule(eventHandler, path)
        self.obs.start()
        self.obs.join()


    def stop(self):
        self.obs.stop()
