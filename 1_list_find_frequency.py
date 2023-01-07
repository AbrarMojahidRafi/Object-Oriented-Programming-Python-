"""Write a python program which prints the frequency of the numbers that were given
as input by the user. Stop taking input when you find the string “STOP”. Do not
print the frequency of numbers that were not given as input.

Sample Input:
10
20
20
30
10
50
90
STOP

Sample Output:
10 - 2 times
20 - 2 times
30 - 1 times
50 - 1 times
90 - 1 times
"""



# solution:

l=[]
while True:
  user=input()
  if user=="STOP":
    break
  else:
    l.append(user)

intList=[]
for i in l:
  intList.append(int(i))

uniqueList=[]
for i in intList:
  if i not in uniqueList:
    uniqueList.append(i)


for i in uniqueList:
  count=intList.count(i)
  print(f"{i} - {count} times")