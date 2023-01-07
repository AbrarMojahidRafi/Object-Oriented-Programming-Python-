"""Write a function which will take 3 arguments minimum, maximum and
divisor. You have to find all the numbers that are divisible by the divisor where
minimum value is inclusive and maximum value is exclusive. Add all the
numbers and return the value.

Sample Input
(0, 10, 2)
(3, 16, 3)

Sample Output
20
45
"""




# solution:

def add(minimum, maximum, divisor):
  sum=0
  for i in range(minimum, maximum):
    if i%divisor==0:
      sum+=i
  return sum
  
user_input=input()
user_input=user_input[1:-1]
user_input=user_input.split(", ")

listOfItem=[]
for i in user_input:
  if i not in listOfItem:
    listOfItem.append(int(i))
listOfItem=tuple(listOfItem)
minimum, maximum, divisor=listOfItem

returnValue=add(minimum, maximum, divisor)
print(returnValue)