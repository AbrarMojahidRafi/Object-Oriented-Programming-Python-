"""Write python code to invert a dictionary. It should print a dictionary where the keys
are values from the input dictionary and the values are lists of keys from the input
dictionary having the same value. Make sure the program handles multiple same
values.

Sample Input
key1 : value1, key2 : value2, key3 : value1

Sample Output
{"value1" : ["key1", "key3"], "value2" : ["key2"]}
"""



# solution:

user_input=input().split(", ")

forDict=[]
for i in user_input:
  tup=i.split(" : ")
  t=tuple(tup)
  forDict.append(t)

dictionary={}
for i in forDict:
  if i[1] in dictionary:
    dictionary[i[1]].append(i[0])
  else:
    dictionary[i[1]]=[]
    dictionary[i[1]].append(i[0])

print(dictionary)