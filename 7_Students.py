"""Given the following classes, write the code for the BBA_Student class so that the
following output is printed:

class Student:
def __init__(self, name='Just a student', dept='nothing'):
self.__name = name
self.__department = dept
def set_department(self, dept):
self.__department = dept
def get_name(self):
return self.__name
def set_name(self,name):
self.__name = name
def __str__(self):
return 'Name: '+self.__name+' Department: '+self.__department
#write your code here
print(BBA_Student())
print(BBA_Student('Humpty Dumpty'))
print(BBA_Student('Little Bo Peep'))

Output:
Name: default Department: BBA
Name: Humpty Dumpty Department: BBA
Name: Little Bo Peep Department: BBA
"""



# Solution:

class Student:
  def __init__(self, name='Just a student', dept='nothing'):
    self.__name = name
    self.__department = dept
  def set_department(self, dept):
    self.__department = dept
  def get_name(self):
    return self.__name
  def set_name(self,name):
    self.__name = name
  def __str__(self):
    return 'Name: '+self.__name+' Department: '+self.__department

#write your code here

class BBA_Student(Student):
  def __init__(self, a=None):
    if a==None:
      super().set_name("default")
      super().set_department("BBA")
    else:
      super().set_name(a)
      super().set_department("BBA")

print(BBA_Student())
print(BBA_Student('Humpty Dumpty'))
print(BBA_Student('Little Bo Peep'))