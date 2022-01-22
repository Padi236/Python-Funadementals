#Inheritance allows to inherit attributes and methods from parent class to child class
#Or from Base class to derived class
#Allows to reuse the code for different classes and avoid code redundancy
#Makes our code organised 

class Polygon:                    #Base class
    def __init__(self, sides):
        self.sides = sides

    def CornersEdges(self):
        print("We have corners and edges")

    def getParameter(self):
        perimeter = sum(self.sides)
        return perimeter

    def display_info(self): 
        print("It is 2 dimensional shape made of straight lines")        

class Triangle(Polygon):          #Triangle class inherits Shape class
    #def __init__():
        #super().__init__()

    def TriangleCornerEdges(self):
        print("We have 3 corners and 3 edges")

    def display_info(self):
        print("It is a polygon with 3 edges")

class Quadrilateral(Polygon):
    #def __init__():
        #super().__init__()

    def display_info(self):
        print("It is a polygon with 4 edges")

triangle1 = Triangle([3, 4, 5])
triangle1.TriangleCornerEdges()         #Derived class accessing derived class method         
triangle1.CornersEdges()                #Derived class accessing base class method
print(triangle1.getParameter())

#Method Overriding
#If the same method is defined in both base class and derived class
#then the method of the derived class overrides the method of the base class
triangle1.display_info()