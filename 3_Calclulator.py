"""Suppose your little sibling wants your help to check his math homework. He is done with his homework but wants you to see if all his results are correct. Since the student with all correct results gets 3 stars. However, you want your brother to check this on his own. So, you design a calculator for him in python. You could have given your scientific calculator but you wanted to give him a basic calculator and also wanted to see if you can even design one.
Subtasks:
Create a class called Calculator.
Your class shall have 1 constructor and 4 methods, namely add, subtract, multiply and divide.
Now, create an object of your class. After creating an object, it should print “Let’s Calculate!”
Then take 3 inputs from the user: first value, operator, second value
Now based on the given operator, call the required method and print the result.

Sample Input:
1
+
2
Sample Output:
Let’s Calculate!
Value 1: 1
Operator: +
Value 2: 2
Result:  3

"""




# solution:

class Calculator:
  def __init__(self, v1, v2, o):
    self.first_value=v1
    self.second_value=v2
    self.operator=o
    print("Let’s Calculate!")
    print("Value 1:", self.first_value)
    print("operator:", self.operator)
    print("Value 2:", self.second_value)
  
  def add(self,first_value,second_value): 
    return (first_value + second_value)

  def subtract(self,first_value,second_value): 
    return (first_value - second_value)

  def multiply(self,first_value,second_value): 
    return (first_value * second_value)


  def divide(self,first_value,second_value): 
    return (first_value / second_value)


first_value=int(input())
operator=input()
second_value=int(input())


c1=Calculator(first_value, second_value, operator)

if operator=="+":
  var=c1.add(first_value, second_value)
  print("Result:",var)
elif operator=="-":
  var=c1.subtract(first_value, second_value)
  print("Result:",var)
elif operator=="*":
  var=c1.multiply(first_value, second_value)
  print("Result:",var)
elif operator=="/":
  var=c1.divide(first_value, second_value)
  print("Result:",var)


