"""Given the following classes, write the code for the Cricket_Tournament and the
Tennis_Tournment class so that the following output is printed.
class Tournament:
def __init__(self,name='Default'):
self.__name = name
def set_name(self,name):
self.__name = name
def get_name(self):
return self.__name
#write your code here
ct1 = Cricket_Tournament()
print(ct1.detail())
print("-----------------------")
ct2 = Cricket_Tournament("IPL",10,"t20")
print(ct2.detail())
print("-----------------------")
tt = Tennis_Tournament("Roland Garros",128)
print(tt.detail())

OUTPUT:
Cricket Tournament Name: Default
Number of Teams: 0
Type: No type
-----------------------
Cricket Tournament Name: IPL
Number of Teams: 10
Type: t20
-----------------------
Tennis Tournament Name: Roland Garros
Number of Players: 128
"""



# solution:

class Tournament:
    def __init__(self,name='Default'):
        self.__name = name
    def set_name(self,name):
        self.__name = name
    def get_name(self):
        return self.__name

#write your code here

class Cricket_Tournament(Tournament):
  def __init__(self, name=None, teams=0, types="No type"):
    if name==None:
      super().set_name(name)
    else: 
      super().set_name(name)
    self.teams=teams
    self.types=types
  def detail(self):
    return (f"Cricket Tournament Name: {super().get_name()}\nNumber of Teams: {self.teams}\nType: {self.types}")

class Tennis_Tournament(Tournament):
  def __init__(self, name, players):
    super().set_name(name)
    self.players=players
  def detail(self):
    return (f"Tennis Tournament Name: {super().get_name()}\nNumber of Players: {self.players}")


ct1 = Cricket_Tournament()
print(ct1.detail())
print("-----------------------")
ct2 = Cricket_Tournament("IPL",10,"t20")
print(ct2.detail())
print("-----------------------")
tt = Tennis_Tournament("Roland Garros",128)
print(tt.detail())