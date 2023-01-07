"""Implement the design of the Patient class so that the following output is produced:
[For BMI, the formula is BMI = weight/height^2, where weight is in kg and height in meters] 
Driver Code
# Write your code here

p1 = Patient("A", 55, 63.0, 158.0)
p1.printDetails()
print("====================")
p2 = Patient("B", 53, 61.0, 149.0)
p2.printDetails()

Output
Name: A
Age: 55
Weight: 63.0 kg
Height: 158.0 cm
BMI: 25.236340330075304
====================
Name: B
Age: 53
Weight: 61.0 kg
Height: 149.0 cm
BMI: 27.476239809017613 


"""


# solution:

class Patient:
  def __init__(self, n, a, w, h):
    self.name=n
    self.age=a
    self.weight=w
    self.height=h

  def printDetails(self):
    print("Name:", self.name)
    print("Age:", self.age)
    print("Weight:", self.weight, "kg")
    print("Height:", self.height, "cm")
    he=self.height*0.01
    bmi=self.weight/(he*he)
    print("BMI:",bmi)


p1 = Patient("A", 55, 63.0, 158.0)
p1.printDetails()
print("====================")
p2 = Patient("B", 53, 61.0, 149.0)
p2.printDetails()