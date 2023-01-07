"""Write the box class so that the code gives the expected output.

#Write your class code here
print("Box 1")
b1 = box([10,10,10])
print("=========================")
print("Height:", b1.height)
print("Width:", b1.width)
print("Breadth:", b1.breadth)
print("-------------------------")
print("Box 2")
b2 = box((30,10,10))
print("=========================")
print("Height:", b2.height)
print("Width:", b2.width)
print("Breadth:", b2.breadth)
b2.height = 300
print("Updating Box 2!")
print("Height:", b2.height)
print("Width:", b2.width)
print("Breadth:", b2.breadth)
print("-------------------------")
print("Box 3")
b3 = b2
print("Height:", b3.height)
print("Width:", b3.width)
print("Breadth:", b3.breadth)

Output:
Box 1
Creating a Box!
Volume of the box is 1000 cubic units.
=========================
Height: 10
Width: 10
Breadth: 10
---------------------------------------------
Box 2
Creating a Box!
Volume of the box is 3000 cubic units.
=========================
Height: 30
Width: 10
Breadth: 10
Updating Box 2!
Height: 300
Width: 10
Breadth: 10
---------------------------------------------
Box 3
Height: 300
Width: 10
Breadth: 10

"""




# solution:

class box:
  def __init__(self, l):
    self.height=l[0]
    self.width=l[1]
    self.breadth=l[2]
    print("Creating a Box!")
    print(f"Volume of the box is {self.height * self.width * self.breadth} cubic units.")

print("Box 1")
b1 = box([10,10,10])
print("=========================")
print("Height:", b1.height)
print("Width:", b1.width)
print("Breadth:", b1.breadth)
print("-------------------------")
print("Box 2")
b2 = box((30,10,10))
print("=========================")
print("Height:", b2.height)
print("Width:", b2.width)
print("Breadth:", b2.breadth)
b2.height = 300
print("Updating Box 2!")
print("Height:", b2.height)
print("Width:", b2.width)
print("Breadth:", b2.breadth)
print("-------------------------")
print("Box 3")
b3 = b2
print("Height:", b3.height)
print("Width:", b3.width)
print("Breadth:", b3.breadth)
