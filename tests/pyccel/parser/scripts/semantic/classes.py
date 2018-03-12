#$ header class Point(public)
#$ header method __init__(Point, double, double)
#$ header method __del__(Point)
#$ header method translate(Point, double, double)

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.z = self.y

    def translate(self, a, b):
        self.x = self.x + a
        self.y = self.y + b