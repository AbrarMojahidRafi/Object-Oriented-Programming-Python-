"""class Vehicle:
def __init__(self):
self.x = 0
self.y = 0
def moveUp(self):
self.y+=1
def moveDown(self):
self.y-=1
def moveRight(self):
self.x+=1
def moveLeft(self):
self.x-=1
def __str__(self):
return '('+str(self.x)+' , '+str(self.y)+')'
#write your code here
print('Part 1')
print('------')
car = Vehicle()
print(car)
car.moveUp()
print(car)
car.moveLeft()
print(car)
car.moveDown()
print(car)
car.moveRight()
print(car)
print('------')
print('Part 2')
print('------')
car1 = Vehicle2010()
print(car1)
car1.moveLowerLeft()
print(car1)
car2 = Vehicle2010()
car2.moveLeft()
print(car1.equals(car2))
car2.moveDown()
print(car1.equals(car2))

OUTPUT:
Part 1
------
(0 , 0)
(0 , 1)
(-1 , 1)
(-1 , 0)
(0 , 0)
------
Part 2
------
(0 , 0)
(-1 , -1)
False
True

A vehicle assumes that the whole world is a 2-dimensional graph paper. It maintains its
x and y coordinates (both are integers). The vehicle gets manufactured (constructed) at
(0, 0) coordinate.
Subtasks:
1. Design a Vehicle2010 class which inherits movement methods from Vehicle
and adds new methods called move UpperRight, UpperLeft, LowerRight,
LowerLeft. Each of these diagonal move methods must re-use two inherited and
appropriate move methods.
2. Write an “equals” method which tests if significant class properties are the
same (in this case x and y).
Note: All moves are 1 step. That means a single call to any move method changes
value of either x or y or both by 1.
"""



# solution:

class Vehicle:
  def __init__(self):
    self.x = 0
    self.y = 0
  def moveUp(self):
    self.y+=1
  def moveDown(self):
    self.y-=1
  def moveRight(self):
    self.x+=1
  def moveLeft(self):
    self.x-=1
  def __str__(self):
    return '('+str(self.x)+' , '+str(self.y)+')'
#write your code here

class Vehicle2010(Vehicle):
  def moveLowerLeft(self):
    super().moveDown()
    super().moveLeft()
  def equals(self, obj):
    if self.x==obj.x and self.y==obj.y:
      return ("True")
    else:
      return ("False")    
  def moveUpperRight(self):
    super().moveUp()
    super().moveRight()
  def moveUpperLeft(self):
    super().moveUp()
    super().moveLeft()
  def moveLowerRight(self):
    super().moveDown()
    super().moveRight()
  def moveLowerLeft(self):
    super().moveDown()
    super().moveLeft()


print('Part 1')
print('------')
car = Vehicle()
print(car)
car.moveUp()
print(car)
car.moveLeft()
print(car)
car.moveDown()
print(car)
car.moveRight()
print(car)
print('------')
print('Part 2')
print('------')
car1 = Vehicle2010()
print(car1)
car1.moveLowerLeft()
print(car1)
car2 = Vehicle2010()
car2.moveLeft()
print(car1.equals(car2))
car2.moveDown()
print(car1.equals(car2))