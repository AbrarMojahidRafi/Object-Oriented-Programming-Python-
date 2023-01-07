"""In a given string, there will be two uppercase letters in between some lowercase
letters. Print the substring from the first uppercase letter to the last uppercase
letter excluding them. If there are no letters in between them, print the word
BLANK. It is guaranteed that there will be only two uppercase letters in the
string.

Sample Input ------------Sample Output
baNgladEsh --------------glad
coDIng ------------------BLANK
"""


# solution: 

user_input=input("Enter Input: ")

for i in user_input:
  if "A" <= i <= "Z":
    start=user_input.find(i)
    break

user_input=user_input[::-1]
for i in user_input:
  if "A" <= i <= "Z":
    end=user_input.find(i)
    break

ans= user_input[start+1 : len(user_input)-end-1]

if len(ans)!=0:
  print(ans[::-1])
else:
    print("BLANK")


