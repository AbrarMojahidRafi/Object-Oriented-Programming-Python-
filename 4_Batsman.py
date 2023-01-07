"""Implement the design of the Batsman class so that the following output is produced:
Hint: Batting strike rate (s/r) = runsScored / ballsFaced x 100.
Driver Code 

# Write your code here
b1 = Batsman(6101, 7380)
b1.printCareerStatistics()
print("============================")
b2 = Batsman("Liton Das", 678, 773)
b2.printCareerStatistics()
print("----------------------------")
print(b2.battingStrikeRate())
print("============================")
b1.setName("Shakib Al Hasan")
b1.printCareerStatistics()
print("----------------------------")
print(b1.battingStrikeRate())


Output
Name: New Batsman
Runs Scored: 6101 , Balls Faced: 7380
============================
Name: Liton Das
Runs Scored: 678 , Balls Faced: 773
----------------------------
87.71021992238033
============================
Name: Shakib Al Hasan
Runs Scored: 6101 , Balls Faced: 7380
----------------------------
82.66937669376694
"""



# solution:

class Batsman:
  def __init__(self, *args):
    if len(args)==2:
      self.name="New Batsman"
      self.run=args[0]
      self.ball=args[1]
    elif len(args)==3:
      self.name=args[0]
      self.run=args[1]
      self.ball=args[2]
  def printCareerStatistics(self):
    print("Name:", self.name)
    print(f"Runs Scored: {self.run} , Balls Faced: {self.ball}")
  def setName(self,s):
    self.name=s
  def battingStrikeRate(self): 
    return (self.run / self.ball)*100
    

b1 = Batsman(6101, 7380)
b1.printCareerStatistics()
print("============================")
b2 = Batsman("Liton Das", 678, 773)
b2.printCareerStatistics()
print("----------------------------")
print(b2.battingStrikeRate())
print("============================")
b1.setName("Shakib Al Hasan")
b1.printCareerStatistics()
print("----------------------------")
print(b1.battingStrikeRate())