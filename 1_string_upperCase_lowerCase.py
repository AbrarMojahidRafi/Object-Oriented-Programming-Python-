"""From a given string, print the string in all uppercase if the number ofuppercase
letters is more than lowercase letters. Otherwise, if lowercase is greater or equal
to uppercase letters, print all lowercase. The inputs will contain letters (A-Z, a-z)
only.

Sample Input --------Sample Output
HOusE ---------------HOUSE
ApplE ---------------apple
BaNaNa --------------banana
"""


# solution: 

user_input=input("Enter Input: ")

lowerCount=0
upperCount=0
for i in user_input:
  if "a" <= i <= "z":
    lowerCount += 1
  elif "A" <= i <="Z":
    upperCount += 1
  

if lowerCount >= upperCount:
  print(user_input.lower())
else:
  print(user_input.upper())