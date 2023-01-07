"""Implement the design of the Student class so that the following output is produced:
Assume the credit for each course to be 3. For example: [3.3,4] can be calculated as: 
CGPA = ((3.3 * 3) + (4 * 3)) / 6 
[Here, for each course, the grade point is multiplied by 3. Total credit is the number of courses multiplied by 3. Since the example has 2 courses, therefore a total of 6 credits]
CGPA = sum of individual (grade point * credit) / total credit
Academic Standing Rule: [CGPA>3.80 Highest Distinction, CGPA>3.65 High Distinction, CGPA>3.50 Distinction, CGPA>2.00 Satisfactory, CGPA<2.00 Can’t Graduate]


Driver Code
# Write your code here

s1 = Student('Dora', '15995599','CSE', [4,3.7,3.7,4])
s1.calculate_CGPA()
print("==========================")
s1.print_details()
print("==========================")
s2 = Student('Pingu', '12312322', 'EEE', [1.7,1.3,1.3,1.3,1])
s2.calculate_CGPA()
print("==========================")
s2.print_details()
print("==========================") 
s3 = Student('Bob', '13311331', 'CSE', [2,3,3,3.7,2.7,2.7])
s3.calculate_CGPA()
print("==========================")
s3.print_details()


Output
==========================
Name: Dora, ID: 15995599
Department: CSE 
CGPA: 3.85
Your academic standing is 'Highest Distinction'
==========================
==========================
Name: Pingu, ID: 12312322
Department: CSE 
CGPA: 1.32
Sorry, you cannot graduate
==========================
==========================
Name: Bob, ID: 13311331
Department: CSE 
CGPA: 2.85
Your academic standing is 'Satisfactory'

"""


# solution:

class Student:
  def __init__(self, n, id, d, cgList):
    self.name=n
    self.id=id
    self.department=d
    self.cgpa=cgList

  def calculate_CGPA(self):
    sum=0
    for i in self.cgpa:
      sum+=i*3
    finalCGPA=sum/(len(self.cgpa)*3)
    self.cgpa=finalCGPA

  def print_details(self):
    print(f"Name: {self.name}, ID: {self.id}")
    print("Department:", self.department)
    print("CGPA:", self.cgpa)
    if self.cgpa>3.80:
      print('Your academic standing is "Highest Distinction"')
    elif self.cgpa>3.65:
      print('Your academic standing is "High Distinction"')
    elif self.cgpa>3.50:
      print('Your academic standing is "Distinction"')
    elif self.cgpa>2.00:
      print('Your academic standing is "Satisfactory"')
    elif self.cgpa<2.00:
      print("Sorry, you cannot graduate")
    

s1 = Student('Dora', '15995599','CSE', [4,3.7,3.7,4])
s1.calculate_CGPA()
print("==========================")
s1.print_details()
print("==========================")
s2 = Student('Pingu', '12312322', 'EEE', [1.7,1.3,1.3,1.3,1])
s2.calculate_CGPA()
print("==========================")
s2.print_details()
print("==========================")
s3 = Student('Bob', '13311331', 'CSE', [2,3,3,3.7,2.7,2.7])
s3.calculate_CGPA()
print("==========================")
s3.print_details()
