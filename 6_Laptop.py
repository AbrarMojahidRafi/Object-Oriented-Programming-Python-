"""Implement the design of the Laptop class so that the following output is produced
[You are not allowed to change the code below]
# Write your code here
lenovo = Laptop("Lenovo", 5);
dell = Laptop("Dell", 7);
print(lenovo.name, lenovo.count)
print(dell.name, dell.count)
print("Total number of Laptops", Laptop.laptopCount)
Laptop.advantage()
Laptop.resetCount()
print("Total number of Laptops", Laptop.laptopCount)

Output
Lenovo 5
Dell 7
Total number of Laptops 12
Laptops are portable
Total number of Laptops 0
"""



# solution:

# Write your code here
class Laptop:
  laptopCount=0
  def __init__(self, n, num):
    self.name=n
    self.count=num
    Laptop.laptopCount+=self.count

  @staticmethod
  def advantage(): 
    print("Laptops are portable") 
  
  @classmethod
  def resetCount(cls):
    Laptop.laptopCount=0

lenovo = Laptop("Lenovo", 5);
dell = Laptop("Dell", 7);
print(lenovo.name, lenovo.count)
print(dell.name, dell.count)
print("Total number of Laptops", Laptop.laptopCount)
Laptop.advantage()
Laptop.resetCount()
print("Total number of Laptops", Laptop.laptopCount)