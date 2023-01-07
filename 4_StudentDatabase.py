"""Implement the design of the StudentDatabase class so that the following output is
produced:
GPA = Sum of (Grade Points * Credits)/ Credits attempted

Driver Code 

# Write your code here
# Do not change the following lines of code.

s1 = StudentDatabase('Pietro', '10101222')
s1.calculateGPA(['CSE230: 4.0', 'CSE220: 4.0', 'MAT110: 4.0'],
'Summer2020')
s1.calculateGPA(['CSE250: 3.7', 'CSE330: 4.0'], 'Summer2021')
print(f'Grades for {s1.name}\n{s1.grades}')
print('------------------------------------------------------')
s1.printDetails()
s2 = StudentDatabase('Wanda', '10103332')
s2.calculateGPA(['CSE111: 3.7', 'CSE260: 3.7', 'ENG101: 4.0'],
'Summer2022')
print('------------------------------------------------------')
print(f'Grades for {s2.name}\n{s2.grades}')
print('------------------------------------------------------')
s2.printDetails()


Output:
Grades for Pietro
{'Summer2020': {('CSE230', 'CSE220',
'MAT110'): 4.0}, 'Summer2021':
{('CSE250', 'CSE330'): 3.85}}
-----------------------------------------------
Name: Pietro
ID: 10101222
Courses taken in Summer2020:
CSE230
CSE220
MAT110
GPA: 4.0
Courses taken in Summer2021:
CSE250
CSE330
GPA: 3.85
-----------------------------------------------
Grades for Wanda
{'Summer2022': {('CSE111', 'CSE260',
'ENG101'): 3.8}}
-----------------------------------------------
Name: Wanda
ID: 10103332
Courses taken in Summer2022:
CSE111
CSE260
ENG101
GPA: 3.8

"""


# solution:

class StudentDatabase:
  def __init__(self, name, id):
    self.name=name
    self.id=int(id)
    self.grades={}
    self.credit=3
  def calculateGPA(self, courseResult, deadline):
    courseList=[]
    cgpa=0
    for i in courseResult:
      l=i.split(": ")
      courseList.append(l[0])
      cgpa+=float(l[1])
    cgpa=(cgpa*self.credit)/(len(courseList)*self.credit)
    tempDictionary={}
    cgpa="%.2f" % cgpa
    tempDictionary[tuple(courseList)]=cgpa
    self.grades[deadline]=tempDictionary
  def printDetails(self):
    print("Name:", self.name)
    print("ID:", self.id)
    for i in self.grades:
      print(f"Courses taken in {i}:")
      for k,v in self.grades[i].items():
        for item in k:
          print(item)
      print("GPA",v)


s1 = StudentDatabase('Pietro', '10101222')
s1.calculateGPA(['CSE230: 4.0', 'CSE220: 4.0', 'MAT110: 4.0'], 'Summer2020')
s1.calculateGPA(['CSE250: 3.7', 'CSE330: 4.0'], 'Summer2021')
print(f'Grades for {s1.name}\n{s1.grades}')
print('------------------------------------------------------')
s1.printDetails()
s2 = StudentDatabase('Wanda', '10103332')
s2.calculateGPA(['CSE111: 3.7', 'CSE260: 3.7', 'ENG101: 4.0'], 'Summer2022')
print('------------------------------------------------------')
print(f'Grades for {s2.name}\n{s2.grades}')
print('------------------------------------------------------')
s2.printDetails()