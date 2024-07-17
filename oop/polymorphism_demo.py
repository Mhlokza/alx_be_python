import math


class Shape:

    def area(self):
        NotImplementedError


class Rectangle(Shape):
    def area(self,length,width):
        area=length*width
        return f"The area of the Rectangle is: {area}"

class Cycle(Shape):

    def area(self,radius):
        area=math.pi *radius**radius
        return f"The area of the Circle is: {area}"