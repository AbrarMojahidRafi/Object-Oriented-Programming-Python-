"""Write a class called Circle with the required constructor and methods to get the
following output.
Subtasks:
1. Create a class called Circle.
2. Create the required constructor. Use Encapsulation to protect the variables. [Hint:
Assign the variables in private]
3. Create getRadius() and setRadius() method to access variables.
4. Create a method called area to calculate the area of circles.
5. Handle the operator overloading by using a special method to calculate the radius
and area of circle 3.
[You are not allowed to change the code below]
# Write your code here for subtasks 1-5
c1 = Circle(4)
print("First circle radius:" , c1.getRadius())
print("First circle area:" ,c1.area())
c2 = Circle(5)
print("Second circle radius:" ,c2.getRadius())
print("Second circle area:" ,c2.area())
c3 = c1 + c2
print("Third circle radius:" ,c3.getRadius())
print("Third circle area:" ,c3.area())

Output:
First circle radius: 4
First circle area: 50.26548245743669
Second circle radius: 5
Second circle area: 78.53981633974483
Third circle radius: 9
Third circle area: 254.46900494077323
"""




# solution:

import math
class Circle:
  def __init__(self, n):
    self.__num=None
    self.setRadius(n)
  def getRadius(self):
    return self.__num
  def area(self):
    return math.pi*(self.__num)**2
  def __add__(self, obj):
    return Circle(self.__num + obj.__num)
  def setRadius(self,n):
    self.__num=n



c1 = Circle(4)
print("First circle radius:" , c1.getRadius())
print("First circle area:" ,c1.area())
 
c2 = Circle(5)
print("Second circle radius:" ,c2.getRadius())
print("Second circle area:" ,c2.area())
 
c3 = c1 + c2 
print("Third circle radius:" ,c3.getRadius())
print("Third circle area:" ,c3.area())