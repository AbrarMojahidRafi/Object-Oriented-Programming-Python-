"""A class has been designed for this question. Solve the questions to get the desired
result as shown in the output box.
[You are not allowed to change the code below]


class Wadiya:
  def __init__(self):
    self.name = 'Aladeen'
    self.designation = 'President Prime Minister Admiral General'
    self.num_of_wife = 100
    self.dictator = True
    
#Write your code for subtask 1, 2, 3 and 4 here

Output:
Part 1:
Name of President: Aladeen
Designation: President Prime Minister Admiral General
Number of wife: 100
Is he/she a dictator: True
Part 2:
Name of President: Donald Trump
Designation: President
Number of wife: 1
Is he/she a dictator: False

Subtask:
1) Create an object named wadiya.
2) Use the object to print the values as shown in part 1 (Also print the sentence Part 1)
3) Use the same object to change and print the values in part 2 (Also print the sentence
Part 2)
4) Did changing the instance variable values using the same object, affect the previous
values of Part 1? (Print ‘previous information lost’ or ‘No, changing had no effect on
previous value’)

"""



# solution:

class Wadiya:
  def __init__(self):
    self.name = 'Aladeen'
    self.designation = 'President Prime Minister Admiral General'
    self.num_of_wife = 100
    self.dictator = True
    
###########################################################################
print("Part 1:")
wadiya=Wadiya()
print("Name of President:", wadiya.name)
print("Designation:", wadiya.designation)
print("Number of wife:", wadiya.num_of_wife)
print("Is he/she a dictator:", wadiya.dictator)

print("Part 2:")
wadiya.name="Donald Trump"
wadiya.designation="President"
wadiya.num_of_wife=1
wadiya.dictator=False

print("Name of President:", wadiya.name)
print("Designation:", wadiya.designation)
print("Number of wife:", wadiya.num_of_wife)
print("Is he/she a dictator:", wadiya.dictator)


