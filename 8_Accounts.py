"""Write the CheckingAccount class so that the following code generates the output
below:

class Account:
def __init__(self, balance):
self._balance = balance
def getBalance(self):
return self._balance

print('Number of Checking Accounts: ', CheckingAccount.numberOfAccount)
print(CheckingAccount())
print(CheckingAccount(100.00))
print(CheckingAccount(200.00))
print('Number of Checking Accounts: ', CheckingAccount.numberOfAccount)

OUTPUT:
Number of Checking
Accounts: 0
Account Balance: 0.0
Account Balance: 100.00
Account Balance: 200.00
Number of Checking
Accounts: 3
"""



# solution:

class Account: 
  def __init__(self, balance):
    self._balance = balance
  def getBalance(self):
    return self._balance

############################################################################################################################## 

class CheckingAccount(Account):
  numberOfAccount = 0
  def __init__(self, num=0.0):
    if num==0.0:
      super().__init__(num)
    else:
      num = "%.2f" % num 
      super().__init__(num)
    CheckingAccount.numberOfAccount += 1
  def __str__(self):
    return (f"Account Balance: {super().getBalance()}")
    
    
print('Number of Checking Accounts: ', CheckingAccount.numberOfAccount)
print(CheckingAccount())
print(CheckingAccount(100.00))
print(CheckingAccount(200.00))
print('Number of Checking Accounts: ', CheckingAccount.numberOfAccount)