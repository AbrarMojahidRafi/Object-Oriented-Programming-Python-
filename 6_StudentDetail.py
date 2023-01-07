"""Write the Student class so that the given code provides the expected output.
1. Create Student class
2. Create 3 class variable
3. Create 1 class method for object creation
4. Create 1 class method for printing
[You are not allowed to change the code below]

# Write your code here
Student.printDetails()
print('#########################')
mikasa = Student('Mikasa Ackerman', "CSE")
mikasa.individualDetail()
print('------------------------------------------')
Student.printDetails()
print('========================')
harry = Student.createStudent('Harry Potter', "Defence Against Dark
Arts", "Hogwarts School")
harry.individualDetail()
print('-------------------------------------------')
Student.printDetails()
print('=========================')
levi = Student.createStudent("Levi Ackerman", "CSE")
levi.individualDetail()
print('--------------------------------------------')
Student.printDetails()

Output:
Total Student(s): 0
BRAC University Student(s): 0
Other Institution Student(s): 0
################################
Name: Mikasa Ackerman
Department: CSE
Institution: BRAC University
------------------------------------------------------
Total Student(s): 1
BRAC University Student(s): 1
Other Institution Student(s): 0
===============================
Name: Harry Potter
Department: Defence Against Dark Arts
Institution: Hogwarts School
------------------------------------------------------
Total Student(s): 2
BRAC University Student(s): 1
Other Institution Student(s): 1
===============================
Name: Levi Ackerman
Department: CSE
Institution: BRAC University
------------------------------------------------------
Total Student(s): 3
BRAC University Student(s): 2
Other Institution Student(s): 1
"""



# solution:

# Write your code here

class Student:
  totalStudent=0
  bracUniStudent=0
  otherInstiStudent=0
  def __init__(self, n, d, i="BRAC University"):
    self.name=n
    self.department=d
    self.institution=i
    if i=="BRAC University":
      Student.bracUniStudent+=1
    else:
      Student.otherInstiStudent+=1
    Student.totalStudent+=1
  
  @classmethod
  def printDetails(cls):
    print(f"Total Student(s): {cls.totalStudent}")
    print(f"BRAC University Student(s): {cls.bracUniStudent}")
    print(f"Other Institution Student(s): {cls.otherInstiStudent}")

  def individualDetail(self):
    print("Name:", self.name)
    print("Department:", self.department)
    print("Institution:", self.institution)

  @classmethod
  def createStudent(cls, n,d,i=None):
    if i!=None:
      return Student(n,d,i)
    else:
      return Student(n,d,"BRAC University")

Student.printDetails()
print('#########################')

mikasa = Student('Mikasa Ackerman', "CSE")
mikasa.individualDetail()
print('------------------------------------------')
Student.printDetails()

print('========================')

harry = Student.createStudent('Harry Potter', "Defence Against Dark Arts", "Hogwarts School")
harry.individualDetail()
print('-------------------------------------------')
Student.printDetails()

print('=========================')

levi = Student.createStudent("Levi Ackerman", "CSE")
levi.individualDetail()
print('--------------------------------------------')
Student.printDetails()