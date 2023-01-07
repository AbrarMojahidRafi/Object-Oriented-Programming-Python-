"""Implement the design of the Author class so that the following output is produced:

Driver Code 

# Write your code here
auth1 = Author('Humayun Ahmed')
auth1.addBooks('Deyal', 'Megher Opor Bari')
auth1.printDetails()
print(‘===================’)
auth2 = Author()
print(auth2.name)
auth2.changeName('Mario Puzo')
auth2.addBooks('The Godfather', 'Omerta', 'The Sicilian')
print(‘===================’)
auth2.printDetails()
print(‘===================’)
auth3 = Author('Paolo Coelho', 'The Alchemist', 'The Fifth Mountain')
auth3.printDetails()


Output:
Author Name: Humayun Ahmed
--------
List of Books:
Deyal
Megher Opor Bari
===================
Default
===================
Author Name: Mario Puzo
--------
List of Books:
The Godfather
Omerta
The Sicilian
===================
Author Name: Paolo Coelho
--------
List of Books:
The Alchemist
The Fifth Mountain
"""



# solution:

class Author:
  def __init__(self, *args):
    if len(args)==1:
      self.name=args[0]
      self.books=None
    elif len(args)==0:
      self.name="Default"
      self.books=None
    elif len(args)==3:
      self.name=args[0] 
      args=list(args)
      self.books=args[1:3]
  def addBooks(self, *book):
    self.books=book
  def printDetails(self):
    print("Author Name:", self.name)
    print("--------")
    print("List of Books:")
    for i in self.books:
      print(i)
  def changeName(self,oneParameter):
    self.name=oneParameter


auth1 = Author('Humayun Ahmed')
auth1.addBooks('Deyal', 'Megher Opor Bari')
auth1.printDetails()
print("===================")
auth2 = Author()
print(auth2.name)
auth2.changeName('Mario Puzo')
auth2.addBooks('The Godfather', 'Omerta', 'The Sicilian')
print("===================")
auth2.printDetails()
print("===================")
auth3 = Author('Paolo Coelho', 'The Alchemist', 'The Fifth Mountain')
auth3.printDetails()