from Point import Point
from Filter import Filter
from os import path
from threading import Thread
import os
import json
import MyJSONEncoder


class Csv2FltConverter(Thread):

    def __init__(self, path, destinationPath = ""):
        Thread.__init__(self)
        self.filePath = path
        self.destinationPath = destinationPath

    def run(self):

        print("Path:", self.filePath)

        if not path.exists(self.filePath):
            print("Path" + self.filePath + "non esiste")
            return

        base, ext = path.splitext(self.filePath)
        folder = path.split(self.filePath)[0]
        fileName = path.split(self.filePath)[1]

        if ext != ".csv":
            return

        currentFilter = Filter()
        points = []
        maxPoint = Point()
        minPoint = Point()
        # coordSize = 0

        with open(self.filePath) as f:

            print("Apertura file in lettura: " + self.filePath)

            firstLine = f.readline().strip()
            coordStr, coordSize = firstLine.split(':')
            coordStr = coordStr.strip()

            if coordStr != "Coordinates":
                print("Errore parsing: campo 'Coordinates' non trovato")
                return

            coordSize = int(coordSize.strip())

            if coordSize == 0:
                print("Errore parsing: file vuoto")
                return

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

        points.sort()
        currentFilter.setNumberOfPoints(coordSize)
        currentFilter.setMin(minPoint)
        currentFilter.setMax(maxPoint)
        currentFilter.setPointList(points)

        print("Numero punti: " + str(coordSize))
        print("Punto Max: " + str(maxPoint.getX()) + "; " + str(maxPoint.getY()))
        print("Punto Min: " + str(minPoint.getX()) + "; " + str(minPoint.getY()))

        # print(json.dumps(currentFilter, cls=MyJSONEncoder.FilterJSONEncoder, indent=0))
        if self.destinationPath == "":
            outputJsonPath = folder
        else:
            outputJsonPath = self.destinationPath

        outputJsonFile = outputJsonPath+"\\"+fileName
        tempOutputJsonFile = outputJsonPath+"\\~"+fileName
        outputJsonFile = outputJsonFile.replace(".csv", ".json")
        tempOutputJsonFile = tempOutputJsonFile.replace(".csv", ".json")

        print("Percorso generazione file: ", outputJsonFile)
        print("Percorso generazione file temp: ", tempOutputJsonFile)

        print("Inizio creazione file json...")

        tfo = open(tempOutputJsonFile, "w")
        with open(outputJsonFile, 'w') as outfile:
            json.dump(currentFilter, outfile, indent=4, separators=(',', ': '), cls=MyJSONEncoder.FilterJSONEncoder)

        print("Creazione file json completata.")

        tfo.close()
        os.remove(tempOutputJsonFile)

        print("Chiusura json file")
