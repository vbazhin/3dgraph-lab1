import sys, math


class Point(object):
    def __init__(self, x=0.0, y=0.0):
        self.x = float(x)
        self.y = float(y)

    def getCoord(self):
        coord = (self.x, self.y)
        return coord

    def getCoordStr(self):
        coordStr = "(%f, %f)" % (self.x, self.y)
        return coordStr

class Line(object):
    def __init__(self, p1, p2):
        self.p1 = Point(x1, y1)
        self.p2 = Point(x2, y2)

    def getLineStr(self):
        x1, y1 = self.p1.x, self.p1.y
        x2, y2 = self.p2.x, self.p2.y
        lineStr = "((%f, %f), (%f, %f))" % (x1, y1, x2, y2)
        return lineStr


