"""Look at the code and the sample inputs and outputs below to design the program
accordingly.
1. Write a class called Color that only adds the 3 primary colors (red, blue and
yellow).
2. Write a required constructor for the class.
3. You have to use operator overloading to get the desired outputs as shown.
Hint:
There will be only one constructor and only one method tackling the addition operation.
No other methods are required.
Note: Order of the color given as input should not matter. For example, in sample input
1, if the first input was yellow and then red, the output would still be orange.

#Write your code here
#Do not change the following lines of code
C1 = Color(input("First Color: ").lower())
C2 = Color(input("Second Color: ").lower())
C3 = C1 + C2
print("Color formed:", C3.clr)

Sample Input 1:
First Color: red
Second Color: yellow
Sample Output 1:
Color formed: Orange
Sample Input 2:
First Color: red
Second Color: blue
Sample Output 2:
Color formed: Violet
Sample Input 3:
First Color: yellow
Second Color: BLUE
Sample Output 3:
Color formed: Green

"""



# solution:

#Write your code here
class Color:
  def __init__(self, color):
    self.clr=color
  def __add__(self,obj):
    if (self.clr=="red" and obj.clr=="yellow") or (self.clr=="yellow" and obj.clr=="red") :
      return Color("Orange")
    elif (self.clr=="red" and obj.clr=="blue") or (self.clr=="blue" and obj.clr=="red") :
      return Color("Violet")
    #elif (self.clr=="yellow" and obj.clr=="blue") or (self.clr=="blue" and obj.clr=="yellow") :
    else:
      return Color("Green")


#Do not change the following lines of code    
    
C1 = Color(input("First Color: ").lower())
C2 = Color(input("Second Color: ").lower())
C3 = C1 + C2
print("Color formed:", C3.clr)