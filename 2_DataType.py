"""Write a class that for running the following codes:
[You are not allowed to change the code below]

#Write your class code here
data_type1 = DataType(‘Integer’, 1234)
print(data_type1.name)
print(data_type1.value)
print('=====================')
data_type2 = DataType(‘String’, ‘Hello’)
print(data_type2.name)
print(data_type2.value)
print('=====================')
data_type3 = DataType(‘Float’, 4.0)
print(data_type3.name)
print(data_type3.value)

Output:
Integer
1234
=====================
String
Hello
=====================
Float
4.0


Subtasks:
1. Create a class named DataType with the required constructor.
2. Assign name and values in constructor according to the output.
"""




# solution:

class DataType:
  def __init__ (self, name, value):
    self.name=name
    self.value=value

#####################################################################
data_type1 = DataType("Integer", 1234)
print(data_type1.name)
print(data_type1.value)
print('=====================')
data_type2 = DataType("String", "Hello")
print(data_type2.name)
print(data_type2.value)
print('=====================')
data_type3 = DataType("Float", 4.0)
print(data_type3.name)
print(data_type3.value) 

