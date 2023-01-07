"""Implement the design of the Travel class so that the following output is produced:
[You are not allowed to change the code below]
# Write your code here
print(“No. of Traveller =”, Travel.count)
print("=======================")
t1 = Travel("Dhaka","India")
print(t1.display_travel_info())
print("=======================")
t2 = Travel("Kuala Lampur","Dhaka")
t2.set_time(23)
print(t2.display_travel_info())
print("=======================")
t3 = Travel("Dhaka","New_Zealand")
t3.set_time(15)
t3.set_destination("Germany")
print(t3.display_travel_info())
print("=======================")
t4 = Travel("Dhaka","India")
t4.set_time(9)
t4.set_source("Malaysia")
t4.set_destination("Canada")
print(t4.display_travel_info())
print("=======================")
print(“No. of Traveller =”, Travel.count)

Output
No. of Traveller = 0
=======================
Source: Dhaka
Destination:India
Flight Time:1:00
=======================
Source: Kuala Lampur
Destination:Dhaka
Flight Time:23:00
=======================
Source: Dhaka
Destination:Germany
Flight Time:15:00
=======================
Source: Malaysia
Destination:Canada
Flight Time:9:00
=======================
No of Traveller = 4
"""



# solution:

# Write your code here

class Travel:
  count=0
  def __init__(self, s, d):
    self.source=s
    self.destination=d
    Travel.count+=1
    self.time=1
  def display_travel_info(self):
    return (f"Source: {self.source}\nDestination:{self.destination}\nFlight Time:{self.time}:00")
  def set_time(self, t):
    self.time=t
  def set_destination(self, c):
    self.destination=c
  def set_source(self, s):
    self.source=s

print("No. of Traveller =", Travel.count)
print("=======================")
t1 = Travel("Dhaka","India")
print(t1.display_travel_info()) # time count
print("=======================")
t2 = Travel("Kuala Lampur","Dhaka")
t2.set_time(23)
print(t2.display_travel_info())
print("=======================")
t3 = Travel("Dhaka","New_Zealand")
t3.set_time(15)
t3.set_destination("Germany")
print(t3.display_travel_info())
print("=======================")
t4 = Travel("Dhaka","India")
t4.set_time(9)
t4.set_source("Malaysia")
t4.set_destination("Canada")
print(t4.display_travel_info())
print("=======================")
print("No. of Traveller =", Travel.count)