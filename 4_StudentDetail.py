"""Implement the design of the Student class so that the following output is produced:

Driver Code 

# Write your code here
s1 = Student()
s1.quizcalc(10)
print('--------------------------------')
s1.printdetail()
s2 = Student('Harry')
s2.quizcalc(10,8)
print('--------------------------------')
s2.printdetail()
s3 = Student('Hermione')
s3.quizcalc(10,9,10)
print('--------------------------------')
s3.printdetail()

Output
--------------------------------
Hello default student
Your average quiz score is 3.3333333333333335
--------------------------------
Hello Harry
Your average quiz score is 6.0
--------------------------------
Hello Hermione
Your average quiz score is 9.666666666666666
"""



# solution:

class Student:
  def __init__(self,n=None):
    if n==None:
      self.name="default student"
    else:
      self.name=n
    self.avg=None
  def quizcalc(self, a=0, b=0, c=0):
    self.avg=(a+b+c)/3 
  def printdetail(self):
    print(f"Hello {self.name}")
    print(f"Your average quiz score is {self.avg}")


s1 = Student()
s1.quizcalc(10)
print('--------------------------------')
s1.printdetail()
s2 = Student('Harry')
s2.quizcalc(10,8)
print('--------------------------------')
s2.printdetail()
s3 = Student('Hermione')
s3.quizcalc(10,9,10)
print('--------------------------------')
s3.printdetail() 