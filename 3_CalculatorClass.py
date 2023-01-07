"""Implement the design of the Calculator class so that the following output is produced:

Driver Code

# Write your code here

c1 = Calculator()
print("==================")
val = c1.calculate(10, 20, '+')
print("Returned value:", val)
c1.showCalculation()
print("==================")
val = c1.calculate(val, 10, '-')
print("Returned value:", val)
c1.showCalculation()
print("==================")
val = c1.calculate(val, 5, '*')
print("Returned value:", val)
c1.showCalculation()
print("==================")
val = c1.calculate(val, 16, '/')
print("Returned value:", val)
c1.showCalculation()


Output

Calculator is ready!
==================
Returned value: 30
10 + 20 = 30
==================
Returned value: 20
30 - 10 = 20
==================
Returned value: 100
20 * 5 = 100
==================
Returned value: 6.25
100 / 16 = 6.25


"""


# solution:

class Calculator:
  def __init__(self):
    self.value1=0
    self.value2=0
    self.operator=None
    print("Calculator is ready!")

  def calculate(self,v1,v2,o):
    self.value1=v1
    self.value2=v2
    self.operator=o
    if self.operator=="+":
      return (self.value1+self.value2)
    elif self.operator=="-":
      return (self.value1-self.value2)
    elif self.operator=="*":
      return (self.value1*self.value2)
    elif self.operator=="/":
      return (self.value1/self.value2)
  def showCalculation(self):
    if self.operator=="+":
      print(f"{self.value1} {self.operator} {self.value2} = {self.value1+self.value2}")
    elif self.operator=="-":
      print(f"{self.value1} {self.operator} {self.value2} = {self.value1-self.value2}")
    elif self.operator=="*":
      print(f"{self.value1} {self.operator} {self.value2} = {self.value1*self.value2}")
    elif self.operator=="/":
      print(f"{self.value1} {self.operator} {self.value2} = {self.value1/self.value2}")

c1 = Calculator()
print("==================")
val = c1.calculate(10, 20, '+')
print("Returned value:", val)
c1.showCalculation()
print("==================")
val = c1.calculate(val, 10, '-')
print("Returned value:", val)
c1.showCalculation()
print("==================")
val = c1.calculate(val, 5, '*')
print("Returned value:", val)
c1.showCalculation()
print("==================")
val = c1.calculate(val, 16, '/')
print("Returned value:", val)
c1.showCalculation()

