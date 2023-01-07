"""Write a class called Customer with the required constructor and methods to get the
following output.

Subtasks:
1. Create a class called Customer.
2. Create the required constructor.
3. Create a method called greet that works if no arguments are passed or if one
argument is passed. (Hint: You may need to use the keyword NONE)
4. Create a method called purchase that can take as many arguments as the user
wants to give.

[You are not allowed to change the code below]

# Write your codes for subtasks 1-4 here.

customer_1 = Customer("Sam")
customer_1.greet()
customer_1.purchase("chips", "chocolate", "orange juice")
print("-----------------------------")
customer_2 = Customer("David")
customer_2.greet("David")
customer_2.purchase("orange juice")

OUTPUT:
Hello!
Sam, you purchased 3 item(s):
chips
chocolate
orange juice
-----------------------------
Hello David!
David, you purchased 1 item(s):
orange juice
"""




# solution:

class Customer:
  def __init__(self,n):
    self.name=n
  def greet(self,n=None):
    if n==None:
      print(f"Hello!")
    else:
      print(f"Hello {self.name}!")
  def purchase(self, *items):
    print(f"{self.name}, you purchased {len(items)} item(s):")
    for i in items:
      print(i)

customer_1 = Customer("Sam")
customer_1.greet()
customer_1.purchase("chips", "chocolate", "orange juice")
print("-----------------------------")
customer_2 = Customer("David")
customer_2.greet("David")
customer_2.purchase("orange juice")