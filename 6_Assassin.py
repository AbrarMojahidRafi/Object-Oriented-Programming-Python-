"""Write the Assassin class so that the given code provides the expected output.
1. Create Assassin class
2. Create 1 class variable
3. Create 1 class method titled ‘failureRate()’
4. Create 1 class method titled ‘failurePercentage()’
5. Maximum success_rate is 100
[You are not allowed to change the code below]
# Write your code here
john_wick = Assassin('John Wick', 100)
john_wick.printDetails()
print('================================')
nagisa = Assassin.failureRate("Nagisa", 20)
nagisa.printDetails()
print('================================')
akabane = Assassin.failurePercentage("Akabane", "10%")
akabane.printDetails()

Output:
Name: John Wick
Success rate: 100%
Total number of Assassin: 1
============================
Name: Nagisa
Success rate: 80%
Total number of Assassin: 2
============================
Name: Akabane
Success rate: 90%
Total number of Assassin: 3
"""



# solution:

class Assassin:
  totalNumberOfAssassin=0
  def __init__(self, n,r):
    self.name=n
    self.rate=r
    Assassin.totalNumberOfAssassin+=1
  def printDetails(self):
    print("Name:", self.name)
    print(f"Success rate: {self.rate}%")
    print("Total number of Assassin:", Assassin.totalNumberOfAssassin)
  
  @classmethod
  def failureRate(cls, n,r):
    name=n
    rate=100-r
    return cls(name,rate)
  @classmethod
  def failurePercentage(cls, n, s):
    name=n
    rate=100-int(s[:-1])
    return cls(name,rate)


john_wick = Assassin('John Wick', 100)
john_wick.printDetails()
print('================================')
nagisa = Assassin.failureRate("Nagisa", 20)
nagisa.printDetails()
print('================================')
akabane = Assassin.failurePercentage("Akabane", "10%")
akabane.printDetails()