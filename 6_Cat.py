"""Design Cat class for the following code to get the output as shown.
You have already solved this problem in assignment 4 using constructor overloading.
Now, solve this again but this time DO NOT USE CONSTRUCTOR OVERLOADING.
Hint: You will have to use classmethods.
[You are not allowed to change the code below]
# Write your code here
print("Total number of cats:", Cat.Number_of_cats)
c1 = Cat.no_parameter()
c2 = Cat.first_parameter("Black")
c3 = Cat("Brown", "jumping")
c4 = Cat("Red", "purring")
c5 = Cat.second_parameter("playing")
print("=======================")
c1.printCat()
c2.printCat()
c3.printCat()
c4.printCat()
c5.printCat()
c1.changeColor("Blue")
c3.changeColor("Purple")
c1.printCat()
c3.printCat()
print("=======================")
print("Total number of cats:", Cat.Number_of_cats)

Output:
Total number of cats: 0
=======================
White cat is sitting
Black cat is sitting
Brown cat is jumping
Red cat is purring
Grey cat is playing
Blue cat is sitting
Purple cat is jumping
=======================
Total number of cats: 5
"""



#solution:

# Write your code here
class Cat:
  Number_of_cats=0
  def __init__(self, first, second):
    Cat.Number_of_cats+=1
    self.first=first
    self.second=second

  @classmethod
  def no_parameter(cls):
    first="White"
    second="sitting"
    return cls(first, second)

  @classmethod
  def first_parameter(cls, fp):
    first=fp
    second="sitting"
    return cls(first, second)

  @classmethod
  def second_parameter(cls, sp):
    first="Grey"
    second=sp
    return cls(first, second)

  def changeColor(self, c):
    self.first=c
    
  def printCat(self):
    print(f"{self.first} cat is {self.second}")


print("Total number of cats:", Cat.Number_of_cats)
c1 = Cat.no_parameter()
c2 = Cat.first_parameter("Black")
c3 = Cat("Brown", "jumping")
c4 = Cat("Red", "purring")
c5 = Cat.second_parameter("playing")
print("=======================")
c1.printCat()
c2.printCat()
c3.printCat()
c4.printCat()
c5.printCat()
c1.changeColor("Blue")
c3.changeColor("Purple")
c1.printCat()
c3.printCat()
print("=======================")
print("Total number of cats:", Cat.Number_of_cats)