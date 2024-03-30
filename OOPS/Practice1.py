'''
Define a circle class a circle with radious r using the constructor  
Define an area() method of class which calculate the area of circle 
Definea Perimeter() method of the class which allows you to calculate the perimeter of the circle
'''

class Circle:
    def __init__(self,radious):
        self.radious = radious
    def area(self):
        return 3.14 * (self.radious **2)
    def perimeter(self):
        return 2 * 3.14 * (self.radious)
    
c1 =Circle(21)
print("Area of the circle: ",c1.area())
print("Perimeter of the circle: ",c1.perimeter())