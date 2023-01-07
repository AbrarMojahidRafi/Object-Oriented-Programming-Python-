"""Create an Employee Class that will have
● Two instance variable: name and workingPeriod
● A class method named employeeByJoiningYear():
o To create an Employee object by joining year for calculating the working
period
o It will have two Parameter name and year
● A static method experienceCheck() to check if an Employee is experienced or not
o It will take working period and gender as parameter
o If an employee’s working period is less than 3, he or she is not experienced

[You are not allowed to change the code below]
# Write your code here
employee1 = Employee('Dororo', 3)
employee2 = Employee.employeeByJoiningYear('Harry', 2016)
print(employee1.workingPeriod)
print(employee2.workingPeriod)
print(employee1.name)
print(employee2.name)
print(Employee.experienceCheck(2, "male"))
print(Employee.experienceCheck(3, "female"))

Output
3
6
Dororo
Harry
He is not experienced
She is experienced
"""





# solution:

# Write your code here
class Employee:
  def __init__(self, n, h):
    self.name=n
    self.workingPeriod=h
  @classmethod
  def employeeByJoiningYear(cls, n, year):
    year=str(year)[-1]
    return Employee(n, int(year))
  @staticmethod
  def experienceCheck(num, gender):
    if num<3:
      if gender=="male":
        return ("He is not experienced")
      else:
        return ("She is not experienced")
    else:
      if gender=="male":
        return ("He is experienced")
      else:
        return ("She is experienced")
  def workingPeriod(self):
    return self.workingPeriod

employee1 = Employee('Dororo', 3)
employee2 = Employee.employeeByJoiningYear('Harry', 2016)
print(employee1.workingPeriod)
print(employee2.workingPeriod)
print(employee1.name)
print(employee2.name)
print(Employee.experienceCheck(2, "male"))
print(Employee.experienceCheck(3, "female"))