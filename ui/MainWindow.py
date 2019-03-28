from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import QObject, Signal, Slot, QThread, QMetaObject, Qt, QTimer, QCoreApplication
from watchdog.observers import Observer
import CustomEventHandler
import time
from ui import UiMainWindow
from Logger import Logger
from Settings import Settings


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        Logger().debug("Creazione oggetto MainWindow")
        super(MainWindow, self).__init__(parent)
        self.ui = UiMainWindow.Ui_MainWindow()
        self.setupUi()
        self.setupSignalsAndSlots()
        self.obs = None
        self.tailer = None
        self.tailerThread = None
        self.startTailerListener()

    def closeEvent(self, event):
        Logger().debug("Chiusura applicazione")
        res = QMetaObject.invokeMethod(self.tailer, "stopProcess", Qt.BlockingQueuedConnection)
        QCoreApplication.processEvents()
        self.tailer.thread().wait()
        Logger().debug("Tailer listener thread terminato")
        super(MainWindow, self).closeEvent(event)


    def startTailerListener(self):
        Logger().debug("Creazione listener Tailer per visualizzazione file di log")
        self.tailerThread = QThread()
        self.tailer = Tailer()
        self.tailer.moveToThread(self.tailerThread)
        self.tailerThread.started.connect(self.tailer.startProcess)
        self.tailer.newLineSignal.connect(self.addLine)
        self.tailer.stopSignal.connect(self.tailerThread.quit)
        Logger().debug("Avvio listener thread")
        self.tailerThread.start()

    def setupUi(self):
        self.ui.setupUi(self)
        self.ui.cbIsRunning.setEnabled(False)
        self.ui.leSourcePath.setText(Settings().getSpoolPath())
        with open(Settings().getStyleSheetPath()) as fd:
            self.setStyleSheet(fd.read())

    def setupSignalsAndSlots(self):
        Logger().debug("Aggancio segnali signals/slots")
        self.ui.pbStyle.clicked.connect(self.reloadStyle)
        self.ui.pbStart.clicked.connect(self.start)
        self.ui.pbStop.clicked.connect(self.stop)

    def reloadStyle(self):
        Logger().debug("Caricamento foglio di stile")
        with open(Settings().getStyleSheetPath()) as fd:
            self.setStyleSheet(fd.read())

    def start(self):
        Logger().info("Avvio listener dei file CSV")
        self.obs = Observer()
        path = self.ui.leSourcePath.text()
        Logger().info("Path in ascolto: " + path)
        eventHandler = CustomEventHandler.CustomEventHandler(path)
        self.obs.schedule(eventHandler, path)
        self.obs.start()
        self.ui.leSourcePath.setReadOnly(True)
        self.ui.cbIsRunning.setChecked(True)
        Logger().info("Listener dei file CSV avviato")

    def stop(self):
        Logger().info("Chiusura listener dei file CSV")
        if self.obs.isAlive():
            self.obs.stop()
            self.obs.join()

        self.obs = None

        self.ui.leSourcePath.setReadOnly(False)
        self.ui.cbIsRunning.setChecked(False)
        Logger().info("Listener dei file CSV terminato")

    @Slot(str)
    def addLine(self, line):
        self.ui.pteEditor.appendPlainText(line)


class Tailer(QObject):

    startSignal = Signal()
    stopSignal = Signal()
    newLineSignal = Signal(str)

    def __init__(self):
        QObject.__init__(self)
        self.filePath = Settings().getLoggingFilepath()
        self.timer = QTimer(self)
        refershIntervalMs = Settings().getTailerRefreshTimeMs()
        self.timer.setInterval(int(refershIntervalMs))
        self.fp = None
        self.setupSignalsAndSlots()

    def setupSignalsAndSlots(self):
        self.timer.timeout.connect(self.processFile)

    @Slot()
    def stopProcess(self):
        self.timer.stop()
        self.fp.close()
        self.stopSignal.emit()

    @Slot()
    def startProcess(self):
        try:
            self.fp = open(self.filePath, "r")
            self.timer.start()
            self.startSignal.emit()
        except OSError as err:
            Logger().error("Errore apertura file: " + self.filePatherr)
            Logger().error("Codice Errore: " + str(err.errno))
            Logger().error("Descrizione Errore: " + err.strerror)
            QTimer.singleShot(self.startProcess, 1000)

        # with open(filepath, mode="r") as fp:
        #     while not self.stopped:
        #         line = fp.readline()
        #         if line:
        #             self.newLineSignal.emit(line.strip())
        #         else:
        #             time.sleep(self.waitTimeSec)
        #         QCoreApplication.processEvents()
        # self.stopSignal.emit()

    @Slot()
    def processFile(self):
        line = self.fp.readline()
        if line:
            self.newLineSignal.emit(line.strip())
        else:
            time.sleep(self.waitTimeSec)

