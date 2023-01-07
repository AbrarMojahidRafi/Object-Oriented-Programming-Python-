"""Let there are N numbers in a list and that list is said to be a UB Jumper if the
absolute values of the difference between the successive elements take on all the
values 1 through N − 1. For example, 2 1 4 6 10 is a UB Jumper because the absolute
differences between them are 1 3 2 4 which is all numbers from 1 to (5 - 1) or 4.
Write a python program that takes a number sequence as input and prints
whether it is a UB Jumper or Not UB Jumper. Input will stop after getting
“STOP” as input. (Number order or absolute difference order doesn’t follow any
sequence.)


Sample Input
1 4 2 3
2 1 4 6 10
1 4 2 -1 6
STOP

Sample Output
UB Jumper
UB Jumper
Not UB Jumper
"""



# solution:

emptyString = ""

while True:
  user_input = input()
  if user_input != 'STOP':
    list1 = [int(i) for i in user_input.split(' ')]

    flag = True
    for i in range(len(list1)-1):
      subtract = abs(list1[i] - list1[i+1])
    
      if subtract not in range(1, len(list1)+1):
        flag = False
        break
    
    if flag == True:
      emptyString += 'UB Jumper, '
    else:
      emptyString += 'Not UB Jumper, '
  
  else:
    break


finalList = emptyString.split(', ')
for i in finalList:
  if i != '':
    print(i)