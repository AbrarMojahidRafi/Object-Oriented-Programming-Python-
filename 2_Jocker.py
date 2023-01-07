"""Design a class Joker with parameterized constructor so that the following line of code
prints the result shown in the output box.
[You are not allowed to change the code below]

#Write your class code here
j1 = Joker('Heath Ledger', 'Mind Game', False)
print(j1.name)
print(j1.power)
print(j1.is_he_psycho)
print(“=====================”)
j2 = Joker('Joaquin Phoenix', 'Laughing out Loud', True)
print(j2.name)
print(j2.power)
print(j2.is_he_psycho)
print(“=====================”)
if j1 == j2:
  print('same')
else:
  print('different')
j2.name = 'Heath Ledger'
if j1.name == j2.name:
  print('same')
else:
  print('different')
#Write your code for 2,3 here

Subtask:
1) Design the class using a parameterized constructor.
2) The first if/else block prints the output as ‘different’, but why? Explain your answer
and print your explanation at the very end.
3) The second if/else block prints the output as ‘same’, but why? Explain your answer
and print your explanation at the very end.

Output:
Heath Ledger
Mind Game
False
=====================
Joaquin Phoenix
Laughing out Loud
True
=====================
different
same
"""




# solution:

class Joker:
  def __init__(self, name, power, is_he_psycho):
    self.name=name
    self.power=power
    self.is_he_psycho=is_he_psycho
    
#####################################################################
j1 = Joker('Heath Ledger', 'Mind Game', False)
print(j1.name)
print(j1.power)
print(j1.is_he_psycho)
print("=====================")
j2 = Joker('Joaquin Phoenix', 'Laughing out Loud', True)
print(j2.name)
print(j2.power)
print(j2.is_he_psycho)
print("=====================")
if j1 == j2:
  print('same')
else:
  print('different')
j2.name = 'Heath Ledger'
if j1.name == j2.name:
  print('same')
else:
  print('different')