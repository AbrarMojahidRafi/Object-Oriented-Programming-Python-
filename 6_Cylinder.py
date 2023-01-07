"""Write a Cylinder class to get the desired output as shown below.
1. You will have to create a Cylinder class.
2. You will have to create 2 class variables.
3. Create a required constructor.
4. Write 2 class methods:
• One that takes the height first and then the radius and then swaps
• One that takes a string where the radius and height values are separated
with a hyphen.
Write 2 static methods:

• One that calculates the area of a whole cylinder (formula: 2πr
2 + 2πrh)

• Another that calculates the volume of a cylinder (formula: πr
2h)

**Observe the output values carefully to understand how the radius and height values
are changing.
[You are not allowed to change the code below]
# Write your code here
c1 = Cylinder(0,0)
Cylinder.area(c1.radius,c1.height)
Cylinder.volume(c1.radius,c1.height)
print("===============================")
c2 = Cylinder.swap(8,3)
c2.area(c2.radius,c2.height)
c2.volume(c2.radius,c2.height)
print("===============================")
c3 = Cylinder.changeFormat("7-13")
c3.area(c3.radius,c3.height)
c3.volume(c3.radius,c3.height)
print("===============================")
Cylinder(0.3,5.56).area(Cylinder.radius,Cylinder.height)
print("===============================")
Cylinder(3,5).volume(Cylinder.radius,Cylinder.height))

Output:
Default radius=5 and height=18.
Updated: radius=0 and height=0.
Area: 0.0
Volume: 0.0
===============================
Default radius=0 and height=0.
Updated: radius=3 and height=8.
Area: 207.34511513692635
Volume: 226.1946710584651
===============================
Default radius=3 and height=8.
Updated: radius=7.0 and height=13.0.
Area: 879.645943005142
Volume: 2001.1945203366981
===============================
Default radius=7.0 and height=13.0.
Updated: radius=0.3 and height=5.56.
Area: 11.045839770021713
===============================
Default radius=0.3 and height=5.56.
Updated: radius=3 and height=5.
Volume: 141.3716694115407
"""




# solution:

# Write your code here
import math
class Cylinder:
  defaultRadius=5
  defaultHeight=18
  radius=None
  height=None
  def __init__(self, r, h):
    print(f"Default radius={Cylinder.defaultRadius} and height={Cylinder.defaultHeight}.")
    Cylinder.defaultRadius = r
    Cylinder.defaultHeight = h 
    self.r = r
    self.h = h 
    print(f"Updated: radius={self.r} and height={self.h}.")
    Cylinder.radius = r 
    Cylinder.height = h
    
  @classmethod
  def area(cls, r, h):
    cls.radius=r
    cls.height=h
    a = 2*math.pi*cls.radius**2 + 2*math.pi*cls.radius*cls.height
    print(f"Area: {a}")
  
  @classmethod
  def volume(cls, r, h):
    cls.radius=r
    cls.height=h
    v = math.pi*cls.radius**2*cls.height
    print("Volume:", v)

  @classmethod
  def swap(cls, num1, num2): 
    cls.radius=num2
    cls.height=num1
    return cls(cls.radius, cls.height)

  @classmethod
  def changeFormat(cls, s):
    r,h=s.split("-")
    return cls(float(r), float(h))



c1 = Cylinder(0,0)
Cylinder.area(c1.radius,c1.height)
Cylinder.volume(c1.radius,c1.height)
print("===============================")
c2 = Cylinder.swap(8,3)
c2.area(c2.radius,c2.height)
c2.volume(c2.radius,c2.height)
print("===============================")
c3 = Cylinder.changeFormat("7-13")
c3.area(c3.radius,c3.height)
c3.volume(c3.radius,c3.height)
print("===============================")
Cylinder(0.3,5.56).area(Cylinder.radius,Cylinder.height)
print("===============================")
Cylinder(3,5).volume(Cylinder.radius,Cylinder.height)