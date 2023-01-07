"""Implement the design of the UberEats class so that the following output is produced:
[For simplicity, you can assume that a customer will always order exact 2 items]


Driver Code 

# Write your code here
order1 = UberEats("Shakib", "01719658xxx", "Mohakhali")
print("=========================")
order1.add_items("Burger", "Coca Cola", 220, 50)
print("=========================")
print(order1.print_order_detail())
print("=========================")
order2 = UberEats ("Siam", "01719659xxx", "Uttara")
print("=========================")
order2.add_items("Pineapple", "Dairy Milk", 80, 70)
print("=========================")
print(order2.print_order_detail())


Output:
Shakib, welcome to UberEats!
=========================
=========================
User details: Name: Shakib, Phone:
01719658xxx, Address: Mohakhali
Orders: {'Burger': 220, 'Coca Cola': 50}
Total Paid Amount: 270
=========================
Siam, welcome to UberEats!
=========================
=========================
User details: Name: Siam, Phone:
01719659xxx, Address: Uttara
Orders: {'Pineapple': 80, 'Dairy Milk': 70}
Total Paid Amount: 150
"""


# solution:

class UberEats:
  def __init__(self, n, p, a):
    self.name=n
    self.phone=p
    self.address=a
    self.order={}
    self.price=0
    print(f"{self.name}, welcome to UberEats!")

  def add_items(self,*args):
    x=0
    y=len(args)//2
    while x<(len(args)//2):
      self.order[args[x]]=args[y]
      x+=1
      y+=1

    for i in range(len(args)//2, len(args)):
      self.price+=args[i]

  def print_order_detail(self):
    return (f"User details: Name: {self.name}, Phone: {self.phone}, Address: {self.address} \nOrders: {self.order} \nTotal Paid Amount: {self.price} ")



order1 = UberEats("Shakib", "01719658xxx", "Mohakhali")
print("=========================")
order1.add_items("Burger", "Coca Cola", 220, 50)
print("=========================")
print(order1.print_order_detail())
print("=========================")
order2 = UberEats ("Siam", "01719659xxx", "Uttara")
print("=========================")
order2.add_items("Pineapple", "Dairy Milk", 80, 70)
print("=========================")
print(order2.print_order_detail())