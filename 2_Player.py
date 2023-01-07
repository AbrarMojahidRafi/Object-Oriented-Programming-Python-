"""Design the Player class so that the code gives the expected output.
[You are not allowed to change the code below]

# Write Your Class Code Here
player1 = Player()
player1.name = "Ronaldo"
player1.jersy_number = 9
player1.position = "Striker"
print("Name of the Player:", player1.name)
print("Jersey Number of player:", player1.jersy_number)
print("Position of player:", player1.position)
print(“===========================”)
player2 = Player()
player2.name = "Neuer"
player2.jersy_number = 1
player2.position = "Goal Keeper"
print("Name of the player:", player2.name)
print("Jersey Number of player:", player2.jersy_number)
print("Position of player:", player2.position)

Output:
Name of the Player: Ronaldo
Jersy Number of player: 9
Position of player: Striker
===========================
Name of the player: Neuer
Jersy Number of player: 1
Position of player: Goal Keeper
"""




# solution:

class Player:
  def __init__(self):
    self.name=""
    self.jersy_number=0
    self.position=""


player1 = Player()
player1.name = "Ronaldo"
player1.jersy_number = 9
player1.position = "Striker"
print("Name of the Player:", player1.name)
print("Jersey Number of player:", player1.jersy_number)
print("Position of player:", player1.position)
print("===========================")
player2 = Player()
player2.name = "Neuer"
player2.jersy_number = 1
player2.position = "Goal Keeper"
print("Name of the player:", player2.name)
print("Jersey Number of player:", player2.jersy_number)
print("Position of player:", player2.position)