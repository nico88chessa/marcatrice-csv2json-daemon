from Point import Point
from Filter import Filter
from os import path
import os
import json
import MyJSONEncoder
from Logger import Logger


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

        currentFilter = Filter()
        points = []
        maxPoint = Point()
        minPoint = Point()
        count = 0
        # coordSize = 0

        try:
            with open(filePath) as f:

                Logger().info("Apertura file in lettura: " + filePath)

                firstLine = f.readline().strip()
                coordStr, coordSize = firstLine.split(':')
                coordStr = coordStr.strip()

                if coordStr != "Coordinates":
                    Logger().error("Errore parsing: campo 'Coordinates' non trovato")
                    return

                coordSize = int(coordSize.strip())

                if coordSize == 0:
                    Logger().error("Errore parsing: file vuoto")
                    return

                count += 1
                f.readline()
                f.readline()

                # leggo il primo numero
                line = f.readline()
                values = line.split(';')
                x = int(values[0].strip())
                y = int(values[1].strip())
                maxPoint.setX(x)
                maxPoint.setY(y)
                minPoint.setX(x)
                minPoint.setY(y)

                points.append(maxPoint)

                for line in f:
                    values = line.split(';')
                    x = int(values[0].strip())
                    y = int(values[1].strip())
                    p = Point(x, y)
                    if p < minPoint:
                        minPoint = p
                    if p > maxPoint:
                        maxPoint = p
                    points.append(p)
                    count += 1

        except OSError as err:
            Logger().error("Errore controllo file")
            Logger().error("Codice errore: " + str(err.errno))
            Logger().error("Descrizione errore: " + err.strerror)
            return

        points.sort()
        # currentFilter.setNumberOfPoints(coordSize)
        currentFilter.setNumberOfPoints(count)
        currentFilter.setMin(minPoint)
        currentFilter.setMax(maxPoint)
        currentFilter.setPointList(points)

        Logger().info("Numero punti: " + str(coordSize))
        Logger().info("Punto Max: " + str(maxPoint.getX()) + "; " + str(maxPoint.getY()))
        Logger().info("Punto Min: " + str(minPoint.getX()) + "; " + str(minPoint.getY()))

        outputJsonFile = destinationPath+"\\"+fileName
        tempOutputJsonFile = destinationPath+"\\~"+fileName
        outputJsonFile = outputJsonFile.replace(".csv", ".json")
        tempOutputJsonFile = tempOutputJsonFile.replace(".csv", ".json")

        Logger().info("Percorso generazione file: " + outputJsonFile)
        Logger().info("Percorso generazione file temp: " + tempOutputJsonFile)
        Logger().info("Inizio creazione file json")

        with open(tempOutputJsonFile, 'w') as outfile:
            json.dump(currentFilter, outfile, indent=4, separators=(',', ': '), cls=MyJSONEncoder.FilterJSONEncoder)

        Logger().info("File json temporaneo creato")

        os.rename(tempOutputJsonFile, outputJsonFile)

        Logger().info("File json creato")
