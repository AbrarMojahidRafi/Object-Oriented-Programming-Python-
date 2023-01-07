"""Design the Shinobi class such a way so that the following code provides the expected
output.
Hint:
• Write the constructor with appropriate default value for arguments. Set the initial
salary and mission to 0.
• Write the changeRank() method with appropriate argument.
• Write the calSalary() method with appropriate argument. Check the following
suggestions
➢ Update the number of mission from the given argument.
➢ If rank == 'Genin' then salary = #mission * 50
➢ If rank == 'Chunin' then salary = #mission * 100
➢ else salary = #mission * 500
• Write the printInfo() method with appropriate printing.
[You are not allowed to change the code below]



# Write your code here.
naruto = Shinobi("Naruto", "Genin")
naruto.calSalary(5)
naruto.printInfo()
print('====================')
shikamaru = Shinobi('Shikamaru', "Genin")
shikamaru.printInfo()
shikamaru.changeRank("Chunin")
shikamaru.calSalary(10)
shikamaru.printInfo()
print('====================')
neiji = Shinobi("Neiji", "Jonin")
neiji.calSalary(5)
neiji.printInfo()

OUTPUT:
Name: Naruto
Rank: Genin
Number of mission: 5
Salary: 250
====================
Name: Shikamaru
Rank: Genin
Number of mission: 0
Salary: 0
Name: Shikamaru
Rank: Chunin
Number of mission: 10
Salary: 1000
====================
Name: Neiji
Rank: Jonin
Number of mission: 5
Salary: 2500

"""



# solution:

class Shinobi:
  def __init__(self,n,r):
    self.name=n
    self.rank=r
    self.mission=0
    self.salary=0
  def calSalary(self,mission):
    self.mission=mission
    if self.rank == 'Genin':
      self.salary=self.mission*50
    elif self.rank == 'Chunin':
      self.salary=self.mission*100
    else: 
      self.salary=self.mission*500
  def printInfo(self):
    print(f"Name: {self.name}")
    print(f"Rank: {self.rank}")
    print(f"Number of mission: {self.mission}")
    print(f"Salary: {self.salary}")
  def changeRank(self,rank):
    self.rank=rank

naruto = Shinobi("Naruto", "Genin")
naruto.calSalary(5)
naruto.printInfo()
print('====================')
shikamaru = Shinobi('Shikamaru', "Genin")
shikamaru.printInfo()
shikamaru.changeRank("Chunin")
shikamaru.calSalary(10)
shikamaru.printInfo()
print('====================')
neiji = Shinobi("Neiji", "Jonin")
neiji.calSalary(5)
neiji.printInfo()
