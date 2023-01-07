"""Create a string from two given strings by concatenating common characters of
the given strings.

Sample Input -------------------Sample Output
harry, hermione ----------------hrrhr
dean, tom ----------------------Nothing in common.
"""


# solution: 

user_input=input()

word=user_input.split(", ")

s=""
for i in word[0]:
  if i in word[1]:
    s=s+i
for i in word[1]:
  if i in word[0]:
    s=s+i
      
if len(s)!=0:
  print(s)
else:
  print("Nothing in common.")