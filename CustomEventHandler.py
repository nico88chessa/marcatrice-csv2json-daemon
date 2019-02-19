from watchdog.events import FileSystemEventHandler
from os import path
from Csv2FltConverter import Csv2FltConverter
import time


class CustomEventHandler(FileSystemEventHandler):

    def __init__(self):
        FileSystemEventHandler.__init__(self)

    def on_created(self, event):
        print("File creato")

        # def on_modified(self, event):

        filename = event.src_path
        print("Rilevato nuovo file: " + filename)

        if not event.event_type == "created":
            return

        try:
            historicalSize = -1
            while historicalSize != path.getsize(filename):
                historicalSize = path.getsize(filename)
                time.sleep(1)
        except:
            print("Errore nel controllo del file")
            return

        print("Trasferimento completato del file: " + filename)

        converter = Csv2FltConverter(filename)
        converter.start()
        converter.join()

        print("Elaborazione conclusa file: "+filename)
