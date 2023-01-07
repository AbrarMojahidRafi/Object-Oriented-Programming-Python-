"""Implement the design of the Passenger class so that the following output is produced:
The assumption is Bus base-fare is 450 taka. A passenger can carry upto 20 kg for free.
50 taka will be added if bag weight is between 21 and 50 kg. 100 taka will be added if
bag weight is greater than 50 kg.
[You are not allowed to change the code below]
# Write your code here
print(“Total Passenger:”, Passenger.count)
p1 = Passenger(“Jack”)
p1.set_bag_weight(90)
p2 = Passenger(“Carol”)
p2.set_bag_weight(10)
p3 = Passenger(“Mike”)
p3.set_bag_weight(25)
print("=========================")
p1.printDetail()
print("=========================")
p2.printDetail()
print("=========================")
p3.printDetail()
print("=========================")
print(“Total Passenger:”, Passenger.count)

Output:
Total Passenger: 0
=========================
Name: Jack
Bus Fare: 550 taka
=========================
Name: Carol
Bus Fare: 450 taka
=========================
Name: Mike
Bus Fare: 500 taka
=========================
Total Passenger: 3

"""




# solution:

# Write your code here
class Passenger:
  count=0
  def __init__(self, n):
    self.name=n
    self.busFare=450
    Passenger.count+=1
  def set_bag_weight(self, w):
    if 20>=w:
      self.busFare=450
    elif 21<=w<=50:
      self.busFare+=50
    else:
      self.busFare+=100
  def printDetail(self):
    print("Name:", self.name)
    print("Bus Fare:", self.busFare, "taka")


print("Total Passenger:", Passenger.count)
p1 = Passenger("Jack")
p1.set_bag_weight(90)
p2 = Passenger("Carol")
p2.set_bag_weight(10)
p3 = Passenger("Mike")
p3.set_bag_weight(25)
print("=========================")
p1.printDetail()
print("=========================")
p2.printDetail()
print("=========================")
p3.printDetail()
print("=========================")
print("Total Passenger:", Passenger.count)