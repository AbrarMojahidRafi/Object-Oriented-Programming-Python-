"""Design the Programmer class such a way so that the following code provides the
expected output.
Hint:

o Write the constructor with appropriate printing and multiple arguments.
o Write the addExp() method with appropriate printing and argument.
o Write the prinDetails() method

[You are not allowed to change the code below]

# Write your code here.
p1 = Programmer("Ethen Hunt", "Java", 10)
p1.printDetails()
print('--------------------------')
p2 = Programmer("James Bond", "C++", 7)
p2.printDetails()
print('--------------------------')
p3 = Programmer("Jon Snow", "Python", 4)
p3.printDetails()
p3.addExp(5)
p3.printDetails()

OUTPUT:
Horray! A new programmer is born
Name: Ethen Hunt
Language: Java
Experience: 10 years.
--------------------------
Horray! A new programmer is born
Name: James Bond
Language: C++
Experience: 7 years.
--------------------------
Horray! A new programmer is born
Name: Jon Snow
Language: Python
Experience: 4 years.
Updating experience of Jon Snow
Name: Jon Snow
Language: Python
Experience: 9 years.

"""




# solution:

class Programmer:
  def __init__(self, n, l, e):
    self.name=n
    self.language=l
    self.experience=e
    print("Horray! A new programmer is born")
  def printDetails(self):
    print(f"Name: {self.name}")
    print(f"Language: {self.language}")
    print(f"Experience: {self.experience} years.")
  def addExp(self, experience):
    self.experience+=experience
    print("Updating experience of Jon Snow")


p1 = Programmer("Ethen Hunt", "Java", 10)
p1.printDetails()
print('--------------------------')
p2 = Programmer("James Bond", "C++", 7)
p2.printDetails()
print('--------------------------')
p3 = Programmer("Jon Snow", "Python", 4)
p3.printDetails()
p3.addExp(5)
p3.printDetails() 