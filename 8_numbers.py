"""
Write the ComplexNumber class so that the following code generates the output
below.
class RealNumber:
def __init__(self, r=0):
self.__realValue = r
def getRealValue(self):
return self.__realValue
def setRealValue(self, r):
self.__realValue = r
def __str__(self):
return 'RealPart: '+str(self.getRealValue())

cn1 = ComplexNumber()
print(cn1)
print('---------')
cn2 = ComplexNumber(5,7)
print(cn2)

OUTPUT:
RealPart: 1.0
ImaginaryPart: 1.0
--------------------
RealPart: 5.0
ImaginaryPart: 7.0
"""


# solution:

class RealNumber:
  def __init__(self, r=0):
    self.__realValue = r  
  def getRealValue(self):
    return self.__realValue
  def setRealValue(self, r):
    self.__realValue = r
  def __str__(self):
    return 'RealPart: '+str(self.getRealValue())    

##############################################################################################################################

class ComplexNumber(RealNumber):
  def __init__(self, d1=None, d2=None):
    if d1==None and d2==None:
      super().setRealValue(1.0)
      self.digitTwo = 2.0 
    else:
      super().setRealValue(float(d1))
      self.digitTwo = float(d2)
  def __str__(self):
    return (f"{super().__str__()}\nImaginaryPart: {self.digitTwo}")



cn1 = ComplexNumber()
print(cn1)
print('---------')
cn2 = ComplexNumber(5,7)
print(cn2)