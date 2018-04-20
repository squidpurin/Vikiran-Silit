import math
from precision import *

class Circle:
    def __init__(self, x,y,radius):
        if (type(x) == int or type(x) == float) or \
           (type(y) == int or type(y) == float) or \
           (type(radius) == int or type(radius) == float):
            pass
        else:
            raise TypeError
        self.x = x
        self.y = y
        self.radius = radius
        self.pi = math.pi
    def getArea(self):
        return self.pi * (self.radius ** 2)
    def getPerimeter(self):
        return 2 * self.pi * self.radius
    def move(self,newX,newY):
        if (type(newX) == int or type(newX) == float) or \
           (type(newY) == int or type(newY) == float):
            pass
        else:
            raise TypeError
        self.x = newX
        self.y = newY

    
