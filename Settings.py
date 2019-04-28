from Singleton import Singleton
from PySide2.QtCore import QStandardPaths
import os
import configparser


class Settings(metaclass=Singleton):

    _filepath = "DV"
    _filename = "CSV2JSON.ini"

    def __init__(self):
        folder = QStandardPaths.writableLocation(QStandardPaths.AppDataLocation)
        folder += "/" + Settings._filepath
        if not os.path.exists(folder):
            os.makedirs(folder)

        filepath = folder + "/" + Settings._filename
        if not os.path.exists(filepath):
            config = configparser.ConfigParser()
            config["Constants"] = {
                "styleSheetPath": "./ui/stylesheet.qss",
                "tailerRefreshTimeMs": "500",
                "spoolPath": "C:\\Users\\nicola\\Desktop\\Spool"
            }
            config["Configuration"] = {
                "styleButtonVisible": "0",
                "maxLogRowCount": "10"
            }
            config["Logging"] = {
                "path": QStandardPaths.writableLocation(QStandardPaths.AppLocalDataLocation)+"/DV/CSV2JSON/logs/",
                "filename": "CSV2JSON.txt",
                "levels": "CRITICAL, ERROR, WARNING, INFO, DEBUG, NOTSET",
                "currentLevel": "DEBUG"
            }
            config["JsonConfiguration"] = {
                "StripWidthUm": "100000"
            }
            with open(filepath, 'w') as fp:
                config.write(fp)

        config = configparser.ConfigParser()
        config.read(filepath)

        self.styleSheetPath = config["Constants"]["styleSheetPath"]
        self.tailerRefreshTimeMs = config["Constants"]["tailerRefreshTimeMs"]
        self.styleButtonVisible = config["Configuration"]["styleButtonVisible"]
        self.maxLogRowCount = config["Configuration"]["maxLogRowCount"]
        self.spoolPath = config["Constants"]["spoolPath"]
        self.loggingPath = config["Logging"]["path"]
        self.loggingFilename = config["Logging"]["filename"]
        self.loggingLevels = config["Logging"]["levels"]
        self.loggingCurrentLevel = config["Logging"]["currentLevel"]
        self.jsonConfigurationStripWidthUm = config["JsonConfiguration"]["StripWidthUm"]

    def getStyleSheetPath(self):
        return self.styleSheetPath

    def getTailerRefreshTimeMs(self):
        return self.tailerRefreshTimeMs

    def getSpoolPath(self):
        return self.spoolPath

    def isStyleButtonVisible(self):
        return int(self.styleButtonVisible)!=0

    def getMaxLogRowCount(self):
        return int(self.maxLogRowCount)

    def getLoggingPath(self):
        return self.loggingPath

    def getLoggingFilename(self):
        return self.loggingFilename

    def getLoggingFilepath(self):
        return self.loggingPath + "/" + self.loggingFilename

    def getLoggingLevels(self):
        return self.loggingLevels

    def getLoggingCurrentLevel(self):
        return self.loggingCurrentLevel

    def getJsonConfigurationStripWidthUm(self):
        return int(self.jsonConfigurationStripWidthUm)