"""Design the program to get the output as shown.
Subtasks:
1. You will need to create 2 classes: Team and Player
2. Make all the variables in the Team class private.
3. Make all the variables in the Player class public.
4. Write the required codes in the Team and Player classes
Hints:
• Create a list in team class to store the player’s name in that list
• Use constructor overloading technique for Team class

[You are not allowed to change the code below]

# Write your code here for subtasks 1-4
b = Team()
b.setName('Bangladesh')
mashrafi = Player("Mashrafi")
b.addPlayer(mashrafi)
tamim = Player("Tamim")
b.addPlayer(tamim)
b.printDetail()
a = Team("Australia")
ponting = Player("Ponting")
a.addPlayer(ponting)
lee = Player("Lee")
a.addPlayer(lee)
a.printDetail()

Output:
=====================
Team: Bangladesh
List of Players:
['Mashrafi', 'Tamim']
=====================
=====================
Team: Australia
List of Players:
['Ponting', 'Lee']
=====================
"""



# solution:

class Team:
  def __init__(self, cN=None):
    if cN==None:
      self.__countryName=None
    else:
      self.__countryName=cN
    self.__player=[]
  def setName(self, c):
    self.__countryName=c
  def addPlayer(self, obj):
    self.__player.append(obj.playerName)
  def printDetail(self):
    print("===================")
    print("Team", self.__countryName)
    print("List of Players:")
    print(self.__player)
    print("===================")

class Player:
  def __init__(self, playerName):
    self.playerName=playerName





b = Team()
b.setName('Bangladesh')
mashrafi = Player("Mashrafi")
b.addPlayer(mashrafi)
tamim = Player("Tamim")
b.addPlayer(tamim)
b.printDetail()
a = Team("Australia")
ponting = Player("Ponting")
a.addPlayer(ponting)
lee = Player("Lee")
a.addPlayer(lee)
a.printDetail()