"""Given the following classes, write the code for the Player and the Manager class so that the
following output is printed. To calculate the match earning use the following formula:
1. Player: (total_goal * 1000) + (total_match * 10)
2. Manager: match_win * 1000

class Football:
def __init__(self, team_name, name, role):
self.__team = team_name
self.__name = name
self.role = role
self.earning_per_match = 0
def get_name_team(self):
return 'Name: '+self.__name+', Team Name: ' +self.__team
#write your code here
player_one = Player('Juventus', 'Ronaldo', 'Striker', 25, 32)
player_one.calculate_ratio()
player_one.print_details()
print('------------------------------------------')
manager_one = Manager('Real Madrid', 'Zidane', 'Manager', 25)
manager_one.print_details()

OUTPUT:
Name: Ronaldo, Team Name: Juventus
Team Role: Striker
Total Goal: 25, Total Played: 32
Goal Ratio: 0.78125
Match Earning: 25320K
----------------------------------
Name: Zidane, Team Name: Real Madrid
Team Role: Manager
Total Win: 25
Match Earning: 25000K
"""



# solution:

class Football:
  def __init__(self, team_name, name, role):
    self.__team = team_name
    self.__name = name
    self.role = role
    self.earning_per_match = 0

  def get_name_team(self):
    return 'Name: '+self.__name+', Team Name: ' +self.__team

#write your code here

class Player(Football):
  def __init__(self, team_name, name, role, goal, total_played):
    super().__init__(team_name, name, role)
    self.goal=goal
    self.total_played=total_played
    self.goalRatio = 0
    self.earning_per_match=0
  def calculate_ratio(self):
    self.goalRatio = self.goal / self.total_played
  def print_details(self):
    print(super().get_name_team())
    print("Team Role:", self.role)
    print(f"Total Goal: {self.goal}, Total Played: {self.total_played}")
    print("Goal Ratio:", self.goalRatio)
    self.earning_per_match=self.goal*1000+self.total_played*10
    print(f"Match Earning: {self.earning_per_match}K")

class Manager(Football):
  def __init__(self, team_name, name, role, goal):
    super().__init__(team_name, name, role)
    self.goal=goal
  def print_details(self):
    print(super().get_name_team())
    print("Team Role:", self.role)
    print(f"Total Win: {self.goal}")
    print(f"Match Earning: {self.goal*1000}K")



player_one = Player('Juventus', 'Ronaldo', 'Striker', 25, 32)
player_one.calculate_ratio()
player_one.print_details()
print('------------------------------------------')
manager_one = Manager('Real Madrid', 'Zidane', 'Manager', 25)
manager_one.print_details()
