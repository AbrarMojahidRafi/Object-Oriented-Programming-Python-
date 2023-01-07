"""Design a class called Coordinates with an appropriate constructor. Then perform the
subtraction, multiplication and equality check operations in the given code using
operator overloading.
#Write your code here
#Do not change the following lines of code
p1 = Coordinates(int(input()),int(input()))
p2 = Coordinates(int(input()),int(input()))
p4 = p1 - p2
print(p4.detail())
p5 = p1 * p2
print(p5.detail())
point_check = (p4 == p5)
print(point_check)

Sample Input 1:
1
2
3
4
Sample Output 1:
(-2,-2)
(3,8)
The calculated coordinates are NOT the same.
Sample Input 2:
0
0
0
0
Sample Output 2:
(0,0)
(0,0)
The calculated coordinates are the same.
"""



# solution:

#Write your code here
class Coordinates:
  def __init__(self, input1, input2):
    self.input1=input1
    self.input2=input2
  def __sub__(self, obj):
    return Coordinates(self.input1-obj.input1 , self.input2-obj.input2)
  def __mul__(self, obj_1):
    return Coordinates(self.input1*obj_1.input1 , self.input2*obj_1.input2)
  def detail(self):
    return (f"({self.input1},{self.input2})")
  def __eq__(self,obj_2):
    if self.input1==obj_2.input1 and self.input2==obj_2.input2:
      return ("The calculated coordinates are the same.")
    else:
      return ("The calculated coordinates are NOT the same.")






#Do not change the following lines of code 

p1 = Coordinates(int(input()),int(input()))
p2 = Coordinates(int(input()),int(input()))

p4 = p1 - p2 
print(p4.detail())

p5 = p1 * p2
print(p5.detail())

point_check = (p4 == p5)
print(point_check)

