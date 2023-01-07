"""Observe the given code carefully. Try to understand from the given code and the
outputs what to write in your class Dolls.
# Write your code here
obj_1 = Dolls("Tweety", 2500)
print(obj_1.detail())
if obj_1 > obj_1:
print("Congratulations! You get the Tweety as a gift!")
else:
print("Thank you!")
print("=========================")
obj_2 = Dolls("Daffy Duck", 1800)
print(obj_2.detail())
if obj_2 > obj_1:
print("Congratulations! You get the Tweety as a gift!")
else:
print("Thank you!")
print("=========================")
obj_3 = Dolls("Bugs Bunny", 3000)
print(obj_3.detail())
if obj_3 > obj_1:
print("Congratulations! You get the Tweety as a gift!")
else:
print("Thank you!")
print("=========================")
obj_4 = Dolls("Porky Pig", 1500)
print(obj_4.detail())
if obj_4 > obj_1:
print("Congratulations! You get the Tweety as a gift!")
else:
print("Thank you!")
print("=========================")
obj_5 = obj_2 + obj_3
print(obj_5.detail())
if obj_5 > obj_1:
print("Congratulations! You get the Tweety as a gift!")
else:
print("Thank you!")

Output:
Doll: Tweety
Total Price: 2500 taka
Thank you!
=========================
Doll: Daffy Duck
Total Price: 1800 taka
Thank you!
=========================
Doll: Bugs Bunny
Total Price: 3000 taka
Congratulations! You get the Tweety as a gift!
=========================
Doll: Porky Pig
Total Price: 1500 taka
Thank you!
=========================
Dolls: Daffy Duck Bugs Bunny
Total Price: 4800 taka
Congratulations! You get the Tweety as a gift!

[You are not allowed to change the code above]
Subtasks:
1. Create a Doll class.
2. Create the required constructor.
3. Write a method to print the name and the price of the object
4. Use operator overloading for the addition operators.
5. Write a method to handle operator overloading for the “>” logical operator that
compares the price of the objects.
Hints:
● Notice that the price of each object is being checked with the price of obj in the
given code.
● Notice the word Doll in the first 4 outputs and the last output. You have to print
exactly as represented here.
"""



# solution:

# Write your code here
class Dolls:
  def __init__(self, d, p, cons=""):
    self.doll=d
    self.price=p
    self.cons=cons
  def detail(self):
    if self.cons=="addRun":
      return (f"Dolls: {self.doll}\nTotal Price: {self.price} taka")
    else:
      return (f"Doll: {self.doll}\nTotal Price: {self.price} taka")
  def __gt__(self, obj):
    if self.price>obj.price:
      return True
    return False
  def __add__(self, obj_1):
    return Dolls(self.doll+" "+obj_1.doll , self.price+obj_1.price, "addRun")

    

obj_1 = Dolls("Tweety", 2500)
print(obj_1.detail())
if obj_1 > obj_1:
    print("Congratulations! You get the Tweety as a gift!")
else:
    print("Thank you!")

print("=========================")
obj_2 = Dolls("Daffy Duck", 1800) 
print(obj_2.detail())
if obj_2 > obj_1:
    print("Congratulations! You get the Tweety as a gift!")
else:
    print("Thank you!")

print("=========================")
obj_3 = Dolls("Bugs Bunny", 3000)
print(obj_3.detail())
if obj_3 > obj_1:
    print("Congratulations! You get the Tweety as a gift!")
else:
    print("Thank you!")

print("=========================")
obj_4 = Dolls("Porky Pig", 1500)
print(obj_4.detail())
if obj_4 > obj_1:
    print("Congratulations! You get the Tweety as a gift!")
else:
    print("Thank you!")

print("=========================")
obj_5 = obj_2 + obj_3
print(obj_5.detail())
if obj_5 > obj_1:
    print("Congratulations! You get the Tweety as a gift!")
else:
    print("Thank you!")

    