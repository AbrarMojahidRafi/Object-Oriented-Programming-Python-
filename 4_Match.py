"""Design the Match class such a way so that the following code provides the expected
# Write your code here.
match1 = Match("Rangpur Riders-Cumilla Victorians")
print("=========================")
match1.add_run(4)
match1.add_run(6)
match1.add_over(1)
print(match1.print_scoreboard())
print("=========================")
match1.add_over(5)
print("=========================")
match1.add_wicket(1)
print(match1.print_scoreboard())

OUTPUT:
5..4..3..2..1.. Play !!!
============================
Batting Team: Rangpur Riders
Bowling Team: Cumilla Victorians
Total Runs: 11 Wickets: 0 Overs: 1
============================
Warning! Cannot add 5 over/s (5 over match)
============================
Batting Team: Rangpur Riders
Bowling Team: Cumilla Victorians
Total Runs: 11 Wickets: 1 Overs: 1
"""




# solution:

class Match: 
  def __init__(self, string):
    string=string.split("-")
    self.batting=string[0]
    self.bowling=string[1]
    print("5..4..3..2..1.. Play !!!")
    self.addRun=0
    self.addOver=0
    self.wickets=0
  def add_run(self, run):
    self.addRun+=run
  def add_over(self, over):
    if self.addOver+over>=5:
      print("Warning! Cannot add 5 over/s (5 over match)")
    else:
      self.addOver+=over
  def add_wicket(self,wickets):
    self.wickets+=wickets
  def print_scoreboard(self):
    return (f"Batting Team: {self.batting}\nBowling Team: {self.bowling}\nTotal Runs: {self.addRun} Wickets: {self.wickets} Overs: {self.addOver}")
  


match1 = Match("Rangpur Riders-Cumilla Victorians")
print("=========================")
match1.add_run(4)
match1.add_run(6)
match1.add_over(1)
print(match1.print_scoreboard())
print("=========================")
match1.add_over(5)
print("=========================")
match1.add_wicket(1)
print(match1.print_scoreboard())
