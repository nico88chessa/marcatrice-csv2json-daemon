from watchdog.events import FileSystemEventHandler
from os import path
from os import error
from Csv2FltConverter import Csv2FltConverter
from Csv2FltConverter import PathNotFoundException
import time
from Logger import Logger


class CustomEventHandler(FileSystemEventHandler):

    def __init__(self, watchedPath):
        FileSystemEventHandler.__init__(self)
        self.watchedPath = watchedPath

    def on_modified(self, event):

        # if not event.event_type == "created":
        #     return

        filename = event.src_path

        Logger().info("Rilevato nuovo file: " + filename)

        if path.isdir(filename):
            Logger().info("Il file e' una cartella: " + filename)
            return
        else:
            filenameExt = path.splitext(filename)[1]
            if not filenameExt == ".csv":
                Logger().info("Il file non e' un file csv")
                return

        Logger().info("Il file e' un file csv")
        try:
            historicalSize = -1
            while historicalSize != path.getsize(filename):
                Logger().info("In attesa che la copia sia terminata")
                historicalSize = path.getsize(filename)
                time.sleep(1)
        except error as err:
            Logger().error("Errore controllo file")
            Logger().error("Codice errore: " + str(err.errno))
            Logger().error("Descrizione errore: " + err.strerror)
            return

        Logger().info("Trasferimento file completato: " + filename)

        converter = Csv2FltConverter()
        Logger().info("Inizio conversione file da csv a json: ")
        destinationPath = path.dirname(filename)
        try:
            converter.execute(filename, destinationPath)
        except PathNotFoundException as pnfEx:
            Logger().error("Path non trovata: " + pnfEx.path)

        Logger().info("Elaborazione conclusa file: " + filename)
