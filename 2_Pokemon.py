"""Design a class called Pokemon using a parameterized constructor so that after
executing the following line of code the desired result shown in the output box will be
printed. First object along with print has been done for you, you also need to create
other objects and print accordingly to get the output correctly.
[You are not allowed to change the code below]

#Write your code for class here
team_pika = Pokemon('pikachu', 'charmander', 90, 60, 10)
print('=======Team 1=======')
print('Pokemon 1:',team_pika.pokemon1_name,
team_pika.pokemon1_power)
print('Pokemon 2:',team_pika.pokemon2_name,
team_pika.pokemon2_power)
pika_combined_power = (team_pika.pokemon1_power +
team_pika.pokemon2_power) * team_pika.damage_rate
print('Combined Power:', pika_combined_power)
#Write your code for subtask 2,3,4 here

Output:
=======Team 1=======
Pokemon 1: pikachu 90
Pokemon 2: charmander 60
Combined Power: 1500
=======Team 2=======
Pokemon 1: bulbasaur 80
Pokemon 2: squirtle 70
Combined Power: 1350

Subtask:
1) Design the Pokemon class using a parameterized constructor. The 5 values that are
being passed through the constructor are pokemon 1 name, pokemon 2 name,
pokemon 1 power, pokemon 2 power, damage rate respectively.
After designing the class, if you run the above code the details in Team 1 will be printed.
2) Create an object named team_bulb and pass the value ‘bulbasaur’, ‘squirtle’, 80, 70,
9 respectively.
3) Use print statements accordingly to print the desired result of Team 2.

Note: Power is always being calculated using the instance variables. Example:
(team_pika.pokemon1_power + team_pika.pokemon2_power) * team_pika.damage_rate

"""




# solution:

class Pokemon:
  def __init__(self, pn1, pn2,pp1, pp2, dr):
    self.pokemon1_name=pn1
    self.pokemon2_name=pn2
    self.pokemon1_power=pp1
    self.pokemon2_power=pp2
    self.damage_rate=dr

team_pika = Pokemon('pikachu', 'charmander', 90, 60, 10)
print('=======Team 1=======')
print('Pokemon 1:',team_pika.pokemon1_name, team_pika.pokemon1_power)
print('Pokemon 2:',team_pika.pokemon2_name, team_pika.pokemon2_power)
pika_combined_power = (team_pika.pokemon1_power + team_pika.pokemon2_power) * team_pika.damage_rate
print('Combined Power:', pika_combined_power)


team_pika = Pokemon('pikachu', 'charmander', 90, 60, 10)
print('=======Team 2=======')
print('Pokemon 1:',team_pika.pokemon1_name, team_pika.pokemon1_power)
print('Pokemon 2:',team_pika.pokemon2_name, team_pika.pokemon2_power)
pika_combined_power = (team_pika.pokemon1_power + team_pika.pokemon2_power) * team_pika.damage_rate
print('Combined Power:', pika_combined_power)

