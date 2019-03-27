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

# if __name__ == "__main__":
#     print("Avvio test main")
#
#     # converter = Csv2FltConverter("C:\\Users\\nicola\\Desktop\\15x15-tile15p5-um-d.csv")
#     # converter.start()
#     # converter.join()
#
#     watchedDogPath = "C:\\Users\\nicola\\Desktop"
#     destinationPath = "C:\\Users\\nicola\\Desktop"
#     # eventHandler = CustomEventHandler(watchedDogPath)
#     eventHandler = CustomEventHandler(watchedDogPath, destinationPath)
#     obs = Observer()
#     try:
#         obs.schedule(eventHandler, watchedDogPath)
#         obs.start()
#         obs.join()
#     except FileNotFoundError as fnfEx:
#         print("Path di osservazione non trovata")
