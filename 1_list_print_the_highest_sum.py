"""Write a python program that calculates the sum of N given lists and prints the highest
sum and its respective list. Input starts with N and followed by N lists.

Sample Input:
4
1 2 3
4 5 6
10 11 12
7 8 9

Sample Output:
33
[10, 11, 12]
"""



# solution:

numberOfList=int(input())

l=[]
for i in range(1, numberOfList+1):
  elementOfList=input()
  l.append(elementOfList)

max=-9999999999999999999999999999
maxList=[]

for i in l:
  iList=i.split(" ")
  intValue=[]
  for item in iList:
    intValue.append(int(item))

  sum=0
  for j in intValue:
    sum=sum+j
  if sum > max:
    max=sum
    maxList=intValue
  
print(max)
print(maxList)