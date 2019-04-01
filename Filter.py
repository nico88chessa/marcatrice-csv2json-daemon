from Point import Point
import MyJSONEncoder


class Filter(MyJSONEncoder.AbstractJSONEncoder):

    def __init__(self):
        self.numberOfPoints = 0
        self.maxPoint = Point()
        self.minPoint = Point()
        self.points = list()

    def getNumberOfPoints(self):
        return self.numberOfPoints

    def setNumberOfPoints(self, nop):
        self.numberOfPoints = nop

    def getMax(self):
        return self.maxPoint

    def setMax(self, p):
        self.maxPoint = p

    def getMin(self):
        return self.minPoint

    def setMin(self, p):
        self.minPoint = p

    def getPointList(self):
        return self.points

    def setPointList(self, l):
        self.points = l

    def addPoint(self, p: Point):
        self.points.append(p)

    def clearPointList(self):
        self.points.clear()

    def decodeJson(self):
        ret = {
            "NumberOfPoints": self.getNumberOfPoints(),
            "BoundingBox": {
                "Min": self.getMin(),
                "Max": self.getMax()
            },
            "Coordinate": self.getPointList()
        }
        return ret
