from BoundingBox import BoundingBox
from Point import Point
from Logger import Logger


class PointSet:

    def __init__(self):
        self.points = []
        self.boundingBox = BoundingBox()

    def addPoint(self, p):
        if not isinstance(p, Point):
            Logger().error("PointSet: il punto passato alla bounding box non e' un punto valido")
            return False

        self.points.append(p)
        if not self.boundingBox.updateBoundingBox(p):
            Logger().error("PointSet: errore nell'update della bounding box")
            return False
        return True

    def getMin(self):
        return self.boundingBox.getMin()

    def getMax(self):
        return self.boundingBox.getMax()

    def size(self):
        return len(self.points)
