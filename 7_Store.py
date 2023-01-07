"""Given the following classes, write the code for the Book and the CD class so that the
following output is printed.

class Product:
def __init__(self,id, title, price):
self.__id = id
self.__title = title
self.__price = price
def get_id_title_price(self):
return "ID: "+str(self.__id)+" Title:"+self.__title+
"Price: "+str(self.__price)
#write your code here
book = Book(1,"The Alchemist",500,"97806","HarperCollins")
print(book.printDetail())
print("-----------------------")
cd = CD(2,"Shotto",300,"Warfaze",50,"Hard Rock")
print(cd.printDetail())

OUTPUT:
ID: 1 Title: The Alchemist Price: 500
ISBN: 97806 Publisher: HarperCollins
-----------------------
ID: 2 Title: Shotto Price: 300
Band: Warfaze Duration: 50minutes
Genre: Hard Rock
"""



# solution:

class Product:
  def __init__(self,id, title, price):
    self.__id = id
    self.__title = title
    self.__price = price
  def get_id_title_price(self):
    return "ID: "+str(self.__id)+" Title:"+self.__title+"Price: "+str(self.__price)
#write your code here

class Book(Product):
  def __init__(self, id, title, price, isbn, publisher):
    super().__init__(id, title, price)
    self.isbn=isbn
    self.publisher=publisher
  def printDetail(self):
    return (f"{super().get_id_title_price()} ISBN: {self.isbn} Publisher: {self.publisher}")
class CD(Product):
  def __init__(self, id, title, price, brand, duration, genre):
    super().__init__(id, title, price)
    self.brand=brand
    self.duration=duration
    self.genre=genre
  def printDetail(self):
    return (f"{super().get_id_title_price()} Band: {self.brand} Duration: {self.duration} minutes Genre: {self.genre}")
    

book = Book(1,"The Alchemist",500,"97806","HarperCollins")
print(book.printDetail())
print("-----------------------")
cd = CD(2,"Shotto",300,"Warfaze",50,"Hard Rock")
print(cd.printDetail())