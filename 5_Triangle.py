"""Write a class called Triangle with the required constructor and methods to get the
following output.
Subtasks:
1. Create a class called Triangle.
2. Create the required constructor. Use Encapsulation to protect the variables. [Hint:
Assign the variables in private]
3. Create getBase(), getHeight(), setBase and setHeight() method to access
variables.
4. Create a method called area to calculate the area of triangles.
5. Handle the operator overloading by using a special method to calculate the radius
and area of triangle 3.
[You are not allowed to change the code below]
# Write your code here for subtasks 1-5
t1 = Triangle(10, 5)
print("First Triangle Base:" , t1.getBase())
print("First Triangle Height:" , t1.getHeight())
print("First Triangle area:" ,t1.area())
t2 = Triangle(5, 3)
print("Second Triangle Base:" , t2.getBase())
print("Second Triangle Height:" , t2.getHeight())
print("Second Triangle area:" ,t2.area())
t3 = t1 - t2
print("Third Triangle Base:" , t3.getBase())
print("Third Triangle Height:" , t3.getHeight())
print("Third Triangle area:" ,t3.area())

Output:
First Triangle Base: 10
First Triangle Height: 5
First Triangle area: 25.0
Second Triangle Base: 5
Second Triangle Height: 3
Second Triangle area: 7.5
Third Triangle Base: 5
Third Triangle Height: 2
Third Triangle area: 5.0
"""



# solution:

class Triangle:
  def __init__(self, b, h):
    self.__base=None
    self.__height=None
    self.setBase(b)
    self.setHeight(h)
  def getBase(self):
    return self.__base
  def getHeight(self):
    return self.__height
  def area(self):
    return (self.__base*self.__height*0.5)
  def __sub__(self, obj):
    return Triangle(self.__base-obj.__base , self.__height-obj.__height)
  def setBase(self, b):
    self.__base=b
  def setHeight(self, h):
    self.__height=h



t1 = Triangle(10, 5)
print("First Triangle Base:" , t1.getBase())
print("First Triangle Height:" , t1.getHeight())
print("First Triangle area:" ,t1.area())
 
t2 = Triangle(5, 3)
print("Second Triangle Base:" , t2.getBase())
print("Second Triangle Height:" , t2.getHeight())
print("Second Triangle area:" ,t2.area())
 
t3 = t1 - t2 
print("Third Triangle Base:" , t3.getBase())
print("Third Triangle Height:" , t3.getHeight())
print("Third Triangle area:" ,t3.area())
