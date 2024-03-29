from Point import Point
import MyJSONEncoder


class Filter(MyJSONEncoder.AbstractJSONEncoder):

    def __init__(self):
        self.numberOfPoints = 0
        self.maxPoint = Point()
        self.minPoint = Point()
        self.centerPoint = Point()
        self.points = list()
        self.yMinDistance = 0

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

    def getCenter(self):
        return self.centerPoint

    def setCenter(self, p):
        self.centerPoint = p

    def getPointList(self):
        return self.points

    def setPointList(self, l):
        self.points = l

    def addPoint(self, p: Point):
        self.points.append(p)

    def clearPointList(self):
        self.points.clear()

    def getYMinDistance(self):
        return self.yMinDistance

    def setYMinDistance(self, yMinDistance):
        self.yMinDistance = yMinDistance

    def decodeJson(self):
        ret = {
            "NumberOfPoints": self.getNumberOfPoints(),
            "BoundingBox": {
                "Min": self.getMin(),
                "Max": self.getMax()
            },
            "Center": self.getCenter(),
            "Coordinate": self.getPointList(),
            "YMinDistance": self.getYMinDistance()
        }
        return ret
