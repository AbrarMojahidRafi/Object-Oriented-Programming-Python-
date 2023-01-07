"""Design a class called Flower with the instance variables so that after executing the
following line of code the desired result shown in the output box will be printed.
[You are not allowed to change the code below]

#Write your class code here
flower1 = Flower()
flower1.name="Rose"
flower1.color="Red"
flower1.num_of_petal=6
print("Name of this flower:", flower1.name)
print("Color of this flower:",flower1.color)
print("Number of petal:",flower1.num_of_petal)
print(“=====================”)
flower2 = Flower()
flower2.name="Orchid"
flower2.color="Purple"
flower2.num_of_petal=4
print("Name of this flower:",flower2.name)
print("Color of this flower:",flower2.color)
print ("Number of petal:",flower2. num_of_petal)
#Write the code for subtask 2 and 3 here


Output:
Name of this flower: Rose
Color of this flower: Red
Number of petal: 6
=====================
Name of this flower: Orchid
Color of this flower: Purple
Number of petal: 4



Subtask:
1) Design the class Flower with default constructor to get the above output.
2) At the end of the given code, also print the address of flower1 and flower2 objects.
3) Do they point to the same address? Print (‘they are same’ or ‘they are different’) at
the very end to answer this question.
"""



#  solution:

class Flower: 
  def __init__(self):
    self.name=""
    self.color=""
    self.num_of_pertal=0

#####################################################################
flower1 = Flower()
flower1.name="Rose"
flower1.color="Red"
flower1.num_of_petal=6
print("Name of this flower:", flower1.name)
print("Color of this flower:",flower1.color)
print("Number of petal:",flower1.num_of_petal)
print("=====================")
flower2 = Flower()
flower2.name="Orchid"
flower2.color="Purple"
flower2.num_of_petal=4
print("Name of this flower:",flower2.name)
print("Color of this flower:",flower2.color)
print ("Number of petal:",flower2. num_of_petal)



print(flower1)
print(flower1)


if flower1 is flower2:
  print("they are same")
else:
  print("they are different")