class Circle:
    def __init__(self, x,y,radius):
        self.x = x
        self.y = y
        rself.radius = radius
        self.pi  = 3.14159
    def getArea(self):
        return self.pi * (radius ** 2)
    def getPerimeter(self):
        return 2 * self.pi * radius
    def move(self,newX,newY):
        self.x = newX
        self.y= newY
    
