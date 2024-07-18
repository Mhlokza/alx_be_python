import math


class Shape:
    def __init__(self,length,width):
        self.length =length
        self.width = width

    def area(self):
        NotImplementedError


class Rectangle(Shape):
    def area(self,length,width):
        area=length*width
        return f"The area of the Rectangle is: {area}"

class Circle(Shape):

    def area(self,radius):
        area=math.pi *radius**2
        "self.radius", "** 2"
        return f"The area of the Circle is: {area}"