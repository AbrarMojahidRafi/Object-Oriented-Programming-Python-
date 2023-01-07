"""Design a class Shape for the given code below.
• Write a class Shape.
• Write the required constructor that takes 3 parameters and initialize the instance variables accordingly.
• Write a method area() that prints the area.
Hint: the area method can calculate only for the shapes: Triangle, Rectangle, Rhombus, and Square. So, you have to use conditions inside this method
For this task, assume that --
for a triangle, the arguments passed are the base and height
for a rhombus, the arguments passed are the diagonals
for a square or rectangle, the arguments passed are the sides.


Driver Code
# Write your code here

triangle = Shape("Triangle",10,25)
triangle.area()
print("==========================")
square = Shape("Square",10,10)
square.area()
print("==========================")
rhombus = Shape("Rhombus",18,25)
rhombus.area()
print("==========================")
rectangle = Shape("Rectangle",15,30)
rectangle.area()
print("==========================")
trapezium = Shape("Trapezium",15,30)
trapezium.area()

Output
Area: 125.0
==========================
Area: 100
==========================
Area: 225.0
==========================
Area: 450
==========================
Area: Shape unknown 

"""



# solution:

class Shape:
  def __init__(self, s, v1, v2):
    self.shape=s
    self.value1=v1
    self.value2=v2
  def area(self):
    if self.shape=="Triangle" or self.shape=="Rhombus":
      print("Area:", 0.5*self.value1*self.value2)
    elif self.shape=="Square" or self.shape=="Rectangle":
      print("Area:", self.value1*self.value2)
    else:
      print("Area: Shape unknown")


triangle = Shape("Triangle",10,25)
triangle.area()
print("==========================")
square = Shape("Square",10,10)
square.area()
print("==========================")
rhombus = Shape("Rhombus",18,25)
rhombus.area()
print("==========================")
rectangle = Shape("Rectangle",15,30)
rectangle.area()
print("==========================")
trapezium = Shape("Trapezium",15,30)
trapezium.area()
