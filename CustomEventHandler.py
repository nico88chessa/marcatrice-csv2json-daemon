from watchdog.events import FileSystemEventHandler
from os import path
from os import error
from Csv2FltConverter import Csv2FltConverter
from Csv2FltConverter import PathNotFoundException
import time


class CustomEventHandler(FileSystemEventHandler):

    def __init__(self, watchedPath):
        FileSystemEventHandler.__init__(self)
        self.watchedPath = watchedPath

    def on_created(self, event):

        if not event.event_type == "created":
            return

        filename = event.src_path

        print("Rilevato nuovo file: " + filename)

        if path.isdir(filename):
            # if self.destinationPath:
            #     print("Creata una nuova cartella")
            #     # indexSubStr = filename.find(self.watchedPath)
            #     # if not indexSubStr == -1:
            #     watchedPathLen = len(self.watchedPath)
            #     folderName = filename[watchedPathLen:]
            #     print("Nome nuova cartella: " + folderName)
            #     newDestinationFolderPath = self.destinationPath + "\\" + folderName
            #     print("Verifico percorso cartella nella cartella di destinazione: " + newDestinationFolderPath)
            #     if not path.exists(newDestinationFolderPath):
            #         print("Creazione cartella nel percorso di destinazione: " + newDestinationFolderPath)
            #         os.makedirs(newDestinationFolderPath)
            #     else:
            #         print("Cartella gia' presente")
            print("Rilevata nuova cartella")
            return
        else:
            filenameExt = path.splitext(filename)[1]
            if not filenameExt == ".csv":
                return

        try:
            historicalSize = -1
            while historicalSize != path.getsize(filename):
                historicalSize = path.getsize(filename)
                time.sleep(1)
        except error:
            print("Errore nel controllo del file")
            return

        print("Trasferimento completato del file: " + filename)

        # dstPath = self.destinationPath
        # if self.destinationPath:
        #     relpath = path.relpath(filename, self.watchedPath)
        #     if relpath:
        #         relpath = path.dirname(relpath)
        #         dstPath += "\\" + relpath

        #     folderNewFile = path.split(filename)[0]
        #     watchedPathLen = len(self.watchedPath)
        #     subFolderIndex = filename.find(self.watchedPath)
        #     subFolderName = filename[watchedPathLen:]
        #     dstPath += subFolderName

        converter = Csv2FltConverter()
        destinationPath = path.dirname(filename)
        try:
            converter.execute(filename, destinationPath)
        except PathNotFoundException as pnfEx:
            print("Path non trovata: " + pnfEx.path)

        # converter.start()
        # converter.join()

        print("Elaborazione conclusa file: " + filename)
