"""Implement the design of the Course class so that the following output is produced:
Driver Code
# Write your code here

c1 = Course("CSE110", "TBA", 8)
c1.detail()
print("===============")
c2 = Course("CSE111", "TBA", 9)
c2.detail()

Output:
CSE110 - TBA - 8
===============
CSE111 - TBA - 9

"""



# solution:

class Course:
  def __init__(self, n, f, num):
    self.courseName=n
    self.facultyName=f
    self.number=num
  def detail(self): 
    print(f"{self.courseName} - {self.facultyName} - {self.number}")


c1 = Course("CSE110", "TBA", 8)
c1.detail()
print("===============")
c2 = Course("CSE111", "TBA", 9)
c2.detail()