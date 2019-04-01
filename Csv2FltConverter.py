from Point import Point
from Filter import Filter
from os import path
import os
import json
import MyJSONEncoder
from Logger import Logger
from PointSet import PointSet


class PathNotFoundException(Exception):
    def __init__(self, filePath):
        self.path = filePath


class Csv2FltConverter(object):

    def __init__(self):
        pass

    def execute(self, filePath, destinationPath=""):

        Logger().info("Path file: " + filePath)

        if not path.exists(filePath):
            raise PathNotFoundException(filePath)
        if not path.exists(destinationPath):
            raise PathNotFoundException(destinationPath)

        base, ext = path.splitext(filePath)
        folder = path.split(filePath)[0]
        fileName = path.split(filePath)[1]

        if destinationPath == "":
            destinationPath = folder

        if ext != ".csv":
            return

        outputJsonFile = destinationPath + "\\" + fileName
        outputJsonFile = outputJsonFile.replace(".csv", ".json")

        if os.path.exists(outputJsonFile):
            Logger().info("Il file " + outputJsonFile + " esiste gia'")
            return

        currentFilter = Filter()
        set = PointSet()

        try:
            with open(filePath) as f:

                Logger().info("Apertura file in lettura: " + filePath)

                firstLine = f.readline().strip()
                if firstLine.startswith("Coordinates"):
                    f.readline()
                    f.readline()
                else:
                    f.readline()

                for line in f:
                    values = line.split(';')
                    x = int(values[0].strip())
                    y = int(values[1].strip())
                    p = Point(x, y)
                    if not set.addPoint(p):
                        Logger().error("Errore nell'inserimento del punto ["+str(x)+","+str(y)+"] nel PointSet")
                        return

        except OSError as err:
            Logger().error("Errore controllo file")
            Logger().error("Codice errore: " + str(err.errno))
            Logger().error("Descrizione errore: " + err.strerror)
            return
        except Exception as err:
            Logger().error("Errore generico: il file csv potrebbe essere corrotto")
            return

        if set.size() == 0:
            Logger().info("Il file .csv non contiene punti")
            return

        set.points.sort()
        currentFilter.setNumberOfPoints(set.size())
        currentFilter.setMin(set.getMin())
        currentFilter.setMax(set.getMax())
        currentFilter.setPointList(set.points)

        Logger().info("Numero punti: " + str(currentFilter.getNumberOfPoints()))
        Logger().info("Punto Min: " + str(currentFilter.getMin().getX()) + "; " + str(currentFilter.getMin().getY()))
        Logger().info("Punto Max: " + str(currentFilter.getMax().getX()) + "; " + str(currentFilter.getMax().getY()))


        tempOutputJsonFile = destinationPath+"\\~"+fileName
        tempOutputJsonFile = tempOutputJsonFile.replace(".csv", ".json")

        Logger().info("Percorso generazione file: " + outputJsonFile)
        Logger().info("Percorso generazione file temp: " + tempOutputJsonFile)
        Logger().info("Inizio creazione file json")

        with open(tempOutputJsonFile, 'w') as outfile:
            json.dump(currentFilter, outfile, indent=4, separators=(',', ': '), cls=MyJSONEncoder.FilterJSONEncoder)

        Logger().info("File json temporaneo creato")

        os.rename(tempOutputJsonFile, outputJsonFile)

        Logger().info("File json creato")
