"""Write a Python program to combine two dictionaries into one by adding values for
common keys. Input contains two comma separated dictionaries. Print the new
dictionary and create a tuple which contains unique values in sorted order.

Sample Input
a: 100, b: 100, c: 200, d: 300
a: 300, b: 200, d: 400, e: 200

Sample Output
{'a': 400, 'b': 300, 'c': 200,'d': 700, 'e': 200}
Values: (200, 300, 400, 700)

"""



# solution:

twoDict=[]
for i in range(2):
  user_input=input().split(", ")
  twoDict.append(user_input)

#print(twoDict)

forDict=[]

for i in twoDict:
  for j in i:
    item=j.split(": ")
    tup=tuple(item)
    forDict.append(tup)

#print(forDict)

emptyDict={}
for i in forDict:
  if i[0] in emptyDict:
    emptyDict[i[0]]=emptyDict[i[0]]+int(i[1])
  else:
    emptyDict[i[0]]=int(i[1])
  
print(emptyDict)

valuesList=[]
for i in emptyDict:
  if emptyDict[i] not in valuesList:
    valuesList.append(emptyDict[i])

valuesList.sort()

print("Values:", tuple(valuesList))