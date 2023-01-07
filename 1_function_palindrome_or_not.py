"""Write a program which checks whether a given string is a palindrome or not. Note: A palindrome is a word, phrase, or sequence that reads the same backward as forward. For palindrome, any spaces in middle are not considered and should be trimmed.

Sample Input
‘madam’
‘hello’
‘nurses run’

Sample Output
Palindrome
Not a palindrome
Palindrome
"""



# solution:

user_input=input()

string=""
for i in user_input:
  if i != " ":
    string=string+i

if string==string[::-1]:
  print("Palindrome")
else:
  print("Not a palindrome")