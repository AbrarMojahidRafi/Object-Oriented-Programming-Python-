"""Given a string, print whether it is a number, word or mixed with digit andletters.
If all the characters are numeric values, print NUMBER. If they are all letters,
print WORD. If it is mixed, print MIXED.

Sample Input -------------Sample Output
213213 -------------------NUMBER
jhg231j213 ---------------MIXED
Hello --------------------WORD
"""



# solution: 


user_input=input()

num=False
word=False

for i in user_input:
  if "a"<=i<="z" or "A"<=i<="Z":
    word=True
  elif 0<=int(i)<=9:
    num=True

if num==True and word==True:
  print("MIXED")
elif num==True:
  print("NUMBER")
elif word==True:
  print("WORD")

