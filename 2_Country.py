"""Design the Country class so that the code gives the expected output.
[You are not allowed to change the code below]

# Write your Class Code here
country = Country()
print('Name:',country.name)
print('Continent:',country.continent)
print('Capital:',country.capital)
print('Fifa Ranking:',country.fifa_ranking)
print('===================')
country.name = “Belgium”
country.continent = “Europe”
country.capital = “Brussels”
country.fifa_ranking = 1
print('Name:',country.name)
print('Continent:',country.continent)
print('Capital:',country.capital)
print('Fifa Ranking:',country.fifa_ranking)

Output:
Name: Bangladesh
Continent: Asia
Capital: Dhaka
Fifa Ranking: 187
===================
Name: Belgium
Continent: Europe
Capital: Brussels
Fifa Ranking: 1
"""



# solution:

class Country:
  def __init__(self):
    self.name="Bangladesh"
    self.continent="Asia"
    self.capital="Dhaka"
    self.fifa_ranking=187

country = Country()
print('Name:',country.name)
print('Continent:',country.continent)
print('Capital:',country.capital)
print('Fifa Ranking:',country.fifa_ranking)
print('===================')
country.name = "Belgium"
country.continent = "Europe"
country.capital = "Brussels"
country.fifa_ranking = 1
print('Name:',country.name)
print('Continent:',country.continent)
print('Capital:',country.capital)
print('Fifa Ranking:',country.fifa_ranking)

