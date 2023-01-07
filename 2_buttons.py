"""Design the required class from the given code and the outputs.
[You are not allowed to change the code below]
Hint:
Number of the border characters for the top and the bottom
= 1 + Number of spaces between the left side border and the first character
of the button name + Length of the button name + Number of spaces between the right side border and the last character
of the button name + 1
NOTE: Don’t count the space or any character from the button representation to solve this problem.

#Write your class code here
word = "CANCEL"
spaces = 10
border = 'x'
b1 = buttons(word, spaces, border)
print("=======================================================")
b2 = buttons("Notify",3, '!')
print("=======================================================")
b3 = buttons('SAVE PROGRESS', 5, '$')
Output:
CANCEL Button Specifications:
Button name: CANCEL
Number of the border characters for the top and the bottom: 28
Number of spaces between the left side border and the first character of the button
name: 10
Number of spaces between the right side border and the last character of the button
name: 10
Characters representing the borders: x
xxxxxxxxxxxxxxxxxxxxxxxxxxxx
x CANCEL x
xxxxxxxxxxxxxxxxxxxxxxxxxxxx
=========================================================

Notify Button Specifications:
Button name: Notify
Number of the border characters for the top and the bottom: 14
Number of spaces between the left side border and the first character of the button
name: 3
Number of spaces between the right side border and the last character of the button
name: 3
Characters representing the borders: !
!!!!!!!!!!!!!!
! Notify !
!!!!!!!!!!!!!!
=========================================================
SAVE PROGRESS Button Specifications:
Button name: SAVE PROGRESS
Number of the border characters for the top and the bottom: 25
Number of spaces between the left side border and the first character of the button
name: 5
Number of spaces between the right side border and the last character of the button
name: 5
Characters representing the borders: $
$$$$$$$$$$$$$$$$$$$$$$$$$
$ SAVE PROGRESS $
$$$$$$$$$$$$$$$$$$$$$$$$$

"""




# solution:

class buttons:
  def __init__(self, word, spaces, border):
    self.word=word
    self.spaces=spaces
    self.border=border
    print("CANCEL Button Specifications:")
    print("Button name:", word)
    b=1+spaces+len(word)+spaces+1
    print("Number of the border characters for the top and the bottom:", b)
    print("Number of spaces between the left side border and the first character of the button name:", self.spaces)
    print("Number of spaces between the right side border and the last character of the button name:", self.spaces)
    print("Characters representing the borders:", self.border)
    print(self.border*b)
    print(self.border + " "*self.spaces + self.word + " "*self.spaces + self.border)
    print(self.border*b)


###########################################################################
word = "CANCEL"
spaces = 10
border = 'x'
b1 = buttons(word, spaces, border)
print("=======================================================")
b2 = buttons("Notify",3, '!')
print("=======================================================")
b3 = buttons('SAVE PROGRESS', 5, '$')


