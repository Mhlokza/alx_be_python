import math


class Shape:
    def area(self):
        return NotImplementedError

class Rectangle(Shape):
    def __init__(self,length,width):
        super().__init__()
        self.length = length
        self.width = width
    def area(self):
        area=self.length*self.width
        return area

class Circle(Shape):
    def __init__(self,radius):
        super(). __init__()
        self.radius = radius
        self.pi = math.pi

    def area(self):
        area=self.pi *self.radius**2
        return area