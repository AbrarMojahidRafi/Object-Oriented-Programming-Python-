"""Write the PokemonExtra class so that the following code generates the output below:

class PokemonBasic:
def __init__(self, name = 'Default', hp = 0,
weakness = 'None', type = 'Unknown'):
self.name = name
self.hit_point = hp
self.weakness = weakness
self.type = type
def get_type(self):
return 'Main type: ' + self.type
def get_move(self):
return 'Basic move: ' + 'Quick Attack'
def __str__(self):
return "Name: " + self.name + ", HP: " +
str(self.hit_point) + ", Weakness: " + self.weakness
print('\n------------Basic Info:--------------')
pk = PokemonBasic()
print(pk)
print(pk.get_type())
print(pk.get_move())
print('\n------------Pokemon 1 Info:-------------')
charmander = PokemonExtra('Charmander', 39, 'Water',
'Fire')
print(charmander)
print(charmander.get_type())
print(charmander.get_move())
print('\n------------Pokemon 2 Info:-------------')
charizard = PokemonExtra('Charizard', 78, 'Water',
'Fire', 'Flying', ('Fire Spin', 'Fire Blaze'))
print(charizard)
print(charizard.get_type())
print(charizard.get_move())

OUTPUT:
------------Basic Info:--------------
Name: Default, HP: 0, Weakness: None
Main type: Unknown
Basic move: Quick Attack
------------Pokemon 1 Info:--------------
Name: Charmander, HP: 39, Weakness: Water
Main type: Fire
Basic move: Quick Attack
------------Pokemon 2 Info:--------------
Name: Charizard, HP: 78, Weakness: Water
Main type: Fire, Secondary type: Flying
Basic move: Quick Attack
Other move: Fire Spin, Fire Blaze
"""



# solution:

class PokemonBasic:

  def __init__(self, name = 'Default', hp = 0, weakness = 'None', type = 'Unknown'):
    self.name = name
    self.hit_point = hp
    self.weakness = weakness
    self.type = type

  def get_type(self):
    return 'Main type: ' + self.type

  def get_move(self):
    return 'Basic move: ' + 'Quick Attack'

  def __str__(self):
    return "Name: " + self.name + ", HP: " + str(self.hit_point) + ", Weakness: " + self.weakness

##############################################################################################################################

class PokemonExtra(PokemonBasic):
  def __init__(self, n, hp, w, mT, sT=None, oM=None):
    super().__init__(n, hp, w, mT)
    self.secondaryType = sT
    self.otherMove = oM 

  def get_type(self):
    if self.secondaryType == None:
      return super().get_type()
    else:
      return (f"{super().get_type()}, Secondary type: {self.secondaryType}")
  
  def get_move(self):
    if type(self.otherMove) == tuple:
      s=""
      for i in self.otherMove:
        s = s + i + ", "
      return (f"{super().get_move()}\nOther move: {s[:-2]}")
    else:
      return super().get_move()


print('------------Basic Info:--------------')
pk = PokemonBasic()
print(pk)
print(pk.get_type())
print(pk.get_move())

print('\n------------Pokemon 1 Info:-------------')
charmander = PokemonExtra('Charmander', 39, 'Water', 'Fire')
print(charmander)
print(charmander.get_type())
print(charmander.get_move())

print('\n------------Pokemon 2 Info:-------------')
charizard = PokemonExtra('Charizard', 78, 'Water', 'Fire', 'Flying', ('Fire Spin', 'Fire Blaze'))
print(charizard)
print(charizard.get_type())
print(charizard.get_move())
