from Point import Point
from PointSet import PointSet
from Logger import Logger
import math
import MyJSONEncoder


class StripeFilter(MyJSONEncoder.AbstractJSONEncoder):

    def __init__(self, stripeWidthUm):
        self.numberOfPoints = 0
        self.maxPoint = Point()
        self.minPoint = Point()
        self.stripes = list()
        self.stripeWidthUm = stripeWidthUm

    def getNumberOfPoints(self):
        return self.numberOfPoints

    def setNumberOfPoints(self, nop):
        self.numberOfPoints = nop

    def getMax(self):
        return self.maxPoint

    def getMin(self):
        return self.minPoint

    def getStripe(self, index):
        if index >= len(self.stripes):
            return PointSet()
        return self.stripes[index]

    def buildStripeFromPointSet(self, ps: PointSet):

        points = ps.points
        Logger().info("Ordinamento inverso coordinate")
        points.sort(reverse=True)
        # prendo i punti della bounding box
        self.minPoint = ps.getMin()
        self.maxPoint = ps.getMax()
        self.numberOfPoints = len(ps.points)

        Logger().info("StripeFilter Min: " + str(self.minPoint.getX()) + "; " + str(self.minPoint.getY()))
        Logger().info("StripeFilter Max: " + str(self.maxPoint.getX()) + "; " + str(self.maxPoint.getY()))
        Logger().info("StripeFilter Num. Points: " + str(self.numberOfPoints))

        minX = self.minPoint.getX()
        maxX = self.maxPoint.getX()
        currentPointSetX = minX

        canContinue = True
        while canContinue:
            self.stripes.append(PointSet())
            currentPointSetX = currentPointSetX + self.stripeWidthUm
            if currentPointSetX > maxX:
                canContinue = False

        Logger().info("StripeFilter Num. Stripe: " + str(len(self.stripes)))

        while len(ps.points) > 0:
            p = ps.points.pop()
            listIndex = math.floor((p.getX() - self.minPoint.getX()) / self.stripeWidthUm)
            self.stripes[listIndex].addPoint(p)

    def clearAll(self):
        self.numberOfPoints = 0
        self.maxPoint = Point()
        self.minPoint = Point()
        self.stripes = list()

    def decodeJson(self):
        ret = {
            "NumberOfPoints": self.getNumberOfPoints(),
            "BoundingBox": {
                "Min": self.getMin(),
                "Max": self.getMax()
            },
            "Stripes": {
                "Size": len(self.stripes),
                "StripeWidthUm": self.stripeWidthUm,
                "Data": self.stripes
            }
        }
        return ret
