"""Implement the design of the Account class so that the following output is produced:

Driver Code 

# Write your code here
a1 = Account()
print(a1.details())
print("------------------------")
a1.name = "Oliver"
a1.balance = 10000.0
print(a1.details())
print("------------------------")
a2 = Account("Liam")
print(a2.details())
print("------------------------")
a3 = Account("Noah",400)
print(a3.details())
print("------------------------")
a1.withdraw(6930)
print("------------------------")
a2.withdraw(600)
print("------------------------")
a1.withdraw(6929)


Output:
Default Account
0.0
------------------------
Oliver
10000.0
------------------------
Liam
0.0
------------------------
Noah
400.0
------------------------
Sorry, Withdraw unsuccessful! The account
balance after deducting withdraw amount is
equal to or less than minimum.
------------------------
Sorry, Withdraw unsuccessful! The account
balance after deducting withdraw amount is
equal to or less than minimum.
------------------------
Withdraw successful! New balance is: 3071.0

"""



# solution:

class Account:
  def __init__(self, name="Default Account", balance=0.0):
    self.name=name
    self.balance=balance
  def details(self):
    return (f"{self.name} \n{float(self.balance)}")
  def withdraw(self,withdraw):
    amount=self.balance-withdraw
    if amount<=3070:
      print("Sorry, Withdraw unsuccessful! The account balance after deducting withdraw amount is equal to or less than minimum.")
    else:
      print(f"Withdraw successful! New balance is: {amount}")
a1 = Account()
print(a1.details())
print("------------------------")
a1.name = "Oliver"
a1.balance = 10000.0
print(a1.details())
print("------------------------")
a2 = Account("Liam")
print(a2.details())
print("------------------------")
a3 = Account("Noah",400)
print(a3.details())
print("------------------------")
a1.withdraw(6930)
print("------------------------")
a2.withdraw(600)
print("------------------------")
a1.withdraw(6929)