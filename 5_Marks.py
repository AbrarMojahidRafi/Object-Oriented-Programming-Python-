"""Write a class called Marks with a required constructor. Then perform the addition using
operator overloading
#Write your code here
#Do not change the following lines of code
Q1 = Marks(int(input("Quiz 1 (out of 10): ")))
Q2 = Marks(int(input("Quiz 2 (out of 10): ")))
Lab = Marks(int(input("Lab (out of 30): ")))
Mid = Marks(int(input("Mid (out of 20): ")))
Final = Marks(int(input("Final (out of 30): ")))
total = Q1 + Q2 + Lab + Mid + Final
print("Total marks: {}".format(total.mark))

Sample Input 1:
Quiz 1 (out of 10): 10
Quiz 2 (out of 10): 10
Lab (out of 30): 30
Mid (out of 20): 20
Final (out of 30): 30
Sample Output 1:
Total marks: 100
Sample Input 2:
Quiz 1 (out of 10): 10
Quiz 2 (out of 10): 8
Lab (out of 30): 30
Mid (out of 20): 20
Final (out of 30): 29
Sample Output 2:
Total marks: 97
"""



# solution:

#Write your code here

class Marks:
  def __init__(self, intNum):
    self.mark=intNum
  def __add__(self, obj):
    n = self.mark + obj.mark
    return Marks(n)


#Do not change the following lines of code    
Q1 = Marks(int(input("Quiz 1 (out of 10): ")))
Q2 = Marks(int(input("Quiz 2 (out of 10): ")))
Lab = Marks(int(input("Lab (out of 30): ")))
Mid = Marks(int(input("Mid (out of 20): ")))
Final = Marks(int(input("Final (out of 30): ")))
total = Q1 + Q2 + Lab + Mid + Final
print("Total marks: {}".format(total.mark))