class square:
    def __init__(self,side):
        self.side = side
    def area(self):
        print("Circle's area is : " , self.side*self.side)
class triangle:
    def __init__(self,base,height):
        self.base = base
        self.height = height
    def area(self):
        print("Triangle's area is : " , 0.5*self.base*self.height)
class rectangle:
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        print("Rectangle's area is : ", self.length*self.breadth)
class circle:
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        print("Circle's area is : ", 3.14*self.radius*self.radius)

ob = square(side=14)
ob.side=14
ob.area()

ob = triangle(base=16,height=17)
ob.base=16
ob.height=17
ob.area()

orectangle = rectangle(88,98)
ocircle = circle(8)
for shape in (orectangle,ocircle):
    shape.area()