from Point import Point
from Logger import Logger


class BoundingBox:

    def __init__(self):
        self.m = None
        self.M = None

    def getMin(self):
        return self.m

    def getMax(self):
        return self.M

    def updateBoundingBox(self, p):

        if not isinstance(p, Point):
            Logger().error("BoundingBox: il punto passato alla bounding box non e' un punto valido")
            return False

        if self.m is None and self.M is None:
            self.m = Point(p.getX(), p.getY())
            self.M = Point(p.getX(), p.getY())
        else:
            if p.getX() < self.m.getX():
                self.m.setX(p.getX())
            if p.getY() < self.m.getY():
                self.m.setY(p.getY())
            if p.getX() > self.M.getX():
                self.M.setX(p.getX())
            if p.getY() > self.M.getY():
                self.M.setY(p.getY())
        return True
