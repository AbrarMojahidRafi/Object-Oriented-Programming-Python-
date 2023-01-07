"""On some basic cell phones, text messages can be sent using the numeric keypad.
Because each key has multiple letters associated with it, multiple key presses are
needed for most letters. Pressing the number once generates the first character listed
for that key. Pressing the number 2, 3, 4 or 5 times generates the second, third, fourth or fifth character.


Key ------------------Symbols
1 --------------------.,?!:
2 --------------------ABC
3 --------------------DEF
4 --------------------GHI
5 --------------------JKL
6 --------------------MNO
7 --------------------PQRS
8 --------------------TUV
9 --------------------WXYZ
0 --------------------Space

Write a program that displays the key presses needed for a message entered by the user.
Construct a dictionary that maps from each letter or symbol to the key presses needed togenerate it. Then use the dictionary to create and display the presses needed for the user’s message.

Sample Input
Hello, World!

Sample Output
4433555555666110966677755531111
"""





# solution:

dictionary={"1":".,?!:", "2":"ABC", "3":"DEF", "4":"GHI", "5":"JKL", "6":"MNO", "7":"PQRS", "8":"TUV", "9":"WXYZ", "0":" "}

user=input().upper()

for i in user:
  for k,v in dictionary.items():
    if i in v:
      position=v.find(i)
      print(k*(position+1), end="")