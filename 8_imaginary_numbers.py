"""Write the ComplexNumber class so that the following code generates the output
below.
class RealNumber:
def __init__(self, number=0):
self.number = number
def __add__(self, anotherRealNumber):
return self.number + anotherRealNumber.number
def __sub__(self, anotherRealNumber):
return self.number - anotherRealNumber.number
def __str__(self):
return str(self.number)
r1 = RealNumber(3)
r2 = RealNumber(5)
print(r1+r2)
cn1 = ComplexNumber(2, 1)
print(cn1)
cn2 = ComplexNumber(r1, 5)
print(cn2)
cn3 = cn1 + cn2
print(cn3)
cn4 = cn1 - cn2
print(cn4)

OUTPUT:
8
2 + 1i
3 + 5i
5 + 6i
-1 - 4i
"""



# solution:

class RealNumber:
  def __init__(self, number=0):
    self.number = number
  def __add__(self, anotherRealNumber):
    return self.number + anotherRealNumber.number
  def __sub__(self, anotherRealNumber):
    return self.number - anotherRealNumber.number
  def __str__(self):
    return str(self.number)

##############################################################################################################################

class ComplexNumber(RealNumber):
  def __init__(self, num1, num2):
    if type(num1)==int:
      super().__init__(num1)
      self.numberTwo = num2
    else:
      super().__init__(num1.number)
      self.numberTwo = num2
  def __str__(self):
    return (f"{self.number} + {self.numberTwo}i")
  def __add__(self, obj):
    x = super().__add__(obj)
    y = self.numberTwo + obj.numberTwo
    return ComplexNumber(x,y)
  def __sub__(self, obj):
    x = super().__sub__(obj)
    y = self.numberTwo - obj.numberTwo
    return ComplexNumber(x,y)


r1 = RealNumber(3)
r2 = RealNumber(5)
print(r1+r2)
cn1 = ComplexNumber(2, 1)
print(cn1)
cn2 = ComplexNumber(r1, 5)
print(cn2)
cn3 = cn1 + cn2
print(cn3)
cn4 = cn1 - cn2
print(cn4)