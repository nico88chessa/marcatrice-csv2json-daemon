import logging

from logging.handlers import RotatingFileHandler
from PySide2.QtCore import QStandardPaths
import os

from Singleton import Singleton
from Settings import Settings


class Logger(metaclass=Singleton):

    def __init__(self):

        # folder = QStandardPaths.writableLocation(QStandardPaths.AppLocalDataLocation)
        # folder += "/" + Constants.LOG_FILE_PATH
        # folder += "/" + Settings().getLoggingPath().LOG_FILE_PATH

        folder = Settings().getLoggingPath()

        if not os.path.exists(folder):
            os.makedirs(folder)

        # logFile = folder + "/" + Constants.LOG_FILE_NAME
        logFile = Settings().getLoggingFilepath()

        handler = RotatingFileHandler(filename=logFile, maxBytes=0, backupCount=6, delay=True)
        formatter = logging.Formatter("${asctime} ${levelname} ${message}", style='$')
        handler.setFormatter(formatter)

        needRollover = os.path.exists(logFile)
        if needRollover:
            handler.doRollover()

        self._logger = logging.getLogger("logger")
        self._logger.addHandler(handler)
        level = Settings().getLoggingCurrentLevel()
        self._logger.setLevel(level)

    def debug(self, msg):
        self._logger.debug(msg)

    def info(self, msg):
        self._logger.info(msg)

    def warning(self, msg):
        self._logger.warning(msg)

    def error(self, msg):
        self._logger.error(msg)

    def critical(self, msg):
        self._logger.critical(msg)
