"""Write a python program which prints the frequency of the numbers that were
given as input by the user. Stop taking input when you find the string “STOP”.Do
not print the frequency of numbers that were not given as input. Use a dictionary
to solve the problem

Sample Input
10
20
20
30
10
50
90
STOP

Sample Output
10 - 2 times
20 - 2 times
30 - 1 times
50 - 1 times
90 - 1 times
"""



# solution:

dictionary={}

while True:
  userInput=input()
  if userInput=="STOP":
    break
  else:
    if userInput not in dictionary:
      dictionary[userInput]=1
    else:
      dictionary[userInput]=dictionary[userInput]+1

for i in dictionary:
  print(f"{int(i)} - {dictionary[i]} times")

  