"""Design the Student class such a way so that the following code provides the expected
output.
Hint:
• Write the constructor with appropriate default value for arguments.
• Write the dailyEffort() method with appropriate argument.
• Write the prinDetails() method. For printing suggestions check the following
instructions.
➢ If hour <= 2 print 'Suggestion: Should give more effort!'
➢ If hour <= 4 print 'Suggestion: Keep up the good work!'
➢ Else print 'Suggestion: Excellent! Now motivate others.'

[You are not allowed to change the code below]


# Write your code here.
harry = Student('Harry Potter', 123)
harry.dailyEffort(3)
harry.printDetails()
print('========================')
john = Student("John Wick", 456, "BBA")
john.dailyEffort(2)
john.printDetails()
print('========================')
naruto = Student("Naruto Uzumaki", 777, "Ninja")
naruto.dailyEffort(6)
naruto.printDetails()

OUTPUT:
Name: Harry Potter
ID: 123
Department: CSE
Daily Effort: 3 hour(s)
Suggestion: Keep up the good work!
========================
Name: John Wick
ID: 456
Department: BBA
Daily Effort: 2 hour(s)
Suggestion: Should give more effort!
========================
Name: Naruto Uzumaki
ID: 777
Department: Ninja
Daily Effort: 6 hour(s)
Suggestion: Excellent! Now motivate others.
"""


# solution:

class Student:
  def __init__(self, n, id, d=None):
    self.name=n
    self.id=id
    if d==None:
      self.department="CSE"
    else:
      self.department=d
    self.hour=None
  def dailyEffort(self,hour):
    self.hour=hour
  def printDetails(self): 
    print("Name:", self.name)
    print("ID:", self.id)
    print("Department:", self.department)
    print(f"Daily Effort: {self.hour} hour(s)")
    if self.hour<=2:
      print("Suggestion: Should give more effort!")
    elif self.hour<=4:
      print("Suggestion: Keep up the good work!")
    else: 
      print("Suggestion: Excellent! Now motivate others.")

harry = Student('Harry Potter', 123)
harry.dailyEffort(3)
harry.printDetails()	
print('========================')
john = Student("John Wick", 456, "BBA")
john.dailyEffort(2)
john.printDetails()
print('========================')
naruto = Student("Naruto Uzumaki", 777, "Ninja")
naruto.dailyEffort(6)
naruto.printDetails()