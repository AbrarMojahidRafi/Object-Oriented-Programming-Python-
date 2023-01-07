"""Write a Student class to get the desired output as shown below.
1. Create a Student class and a class variable called ID initialized with 0.
2. Create a constructor that takes 4 parameters: name, department, age and cgpa.
3. Write a get_details() method to represent all the details of a Student
4. Write a class method from_String() that takes 1 parameter which includes
name, department, age and cgpa all four attributes in string.
#Write your code here for subtasks 1-6.
s1 = Student("Samin", "CSE", 21, 3.91)
s1.get_details()
print("-----------------------")
s2 = Student("Fahim", "ECE", 21, 3.85)
s2.get_details()
print("-----------------------")
s3 = Student("Tahura", "EEE", 22, 3.01)
s3.get_details()
print("-----------------------")
s4 = Student.from_String("Sumaiya-BBA-23-3.96")
s4.get_details()

# Write the answer of subtask 5 here
# Write the answer of subtask 6 here

#You are not allowed to change the code above

OUTPUT
ID: 1
Name: Samin
Department: CSE
Age: 21
CGPA: 3.91
-----------------------
ID: 2
Name: Fahim
Department: ECE
Age: 21
CGPA: 3.85
-----------------------
ID: 3
Name: Tahura
Department: EEE
Age: 22
CGPA: 3.01
-----------------------
ID: 4
Name: Sumaiya
Department: BBA
Age: 23
CGPA: 3.96

5. Explain the difference between a class variable and an instance variable. Print
your answer at the very end of your code.
6. What is the difference between an instance method and class method? Print your
answer at the very end
"""



# solution:

class Student:
  id=0
  def __init__(self, n,d,a,c):
    self.name=n
    self.department=d
    self.age=a
    self.cgpa=c
    Student.id+=1
  def get_details(self):
    print("ID:", Student.id)
    print("Name:", self.name)
    print("Department:", self.department)
    print("Age:", self.age)
    print("CGPA:", self.cgpa)
  
  @classmethod
  def from_String(cls, s):
    l=s.split("-")
    n=l[0]
    d=l[1]
    a=l[2]
    c=l[3]
    return cls(n,d,a,c)


s1 = Student("Samin", "CSE", 21, 3.91)
s1.get_details()
print("-----------------------")
s2 = Student("Fahim", "ECE", 21, 3.85)
s2.get_details()
print("-----------------------")
s3 = Student("Tahura", "EEE", 22, 3.01)
s3.get_details() 
print("-----------------------")
s4 = Student.from_String("Sumaiya-BBA-23-3.96")
s4.get_details() 