"""Design a “Vehicle” class. A vehicle assumes that the whole world is a 2-dimensional graph paper. It maintains its x and y coordinates (both are integers). Any new object created of the Vehicle class will always start at the coordinates (0,0).
It must have methods to move up, down, left, right and a print_position() method for printing the current coordinate.
Note: All moves are 1 step. That means a single call to any move method changes the value of either x or y or both by 1.
[You are not allowed to change the code below]

# Write your class here

car = Vehicle()
car.print_position()
car.moveUp()
car.print_position()
car.moveLeft()
car.print_position()
car.moveDown()
car.print_position()
car.moveRight()



OUTPUT
(0,0)
(0,1)
(-1,1)
(-1,0)
"""



# solution:

class Vehicle:
  def __init__(self):
    self.x=0
    self.y=0
  def print_position(self):
    print(f"({self.x},{self.y})")
  
  def moveUp(self):
    self.y+=1
  def moveLeft(self):
    self.x-=1
  def moveDown(self):
    self.y-=1
  def moveRight(self):
    self.x+=1

car = Vehicle()
car.print_position()
car.moveUp()
car.print_position()
car.moveLeft()
car.print_position()
car.moveDown()
car.print_position()
car.moveRight()
