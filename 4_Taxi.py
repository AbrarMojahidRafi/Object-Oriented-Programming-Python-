"""Using TaxiLagbe apps, users can share a single taxi with multiple people.
Implement the design of the TaxiLagbe class so that the following output is produced:
Hint:
1. Each taxi can carry maximum 4 passengers
2. addPassenger() method takes the last name of the passenger and ticket fare for that
person in an underscore (-) separated string.

Driver Code 

# Write your code here
# Do not change the following lines of code.

taxi1 = TaxiLagbe('1010-01', 'Dhaka')
print('-------------------------------')
taxi1.addPassenger('Walker_100', 'Wood_200')
taxi1.addPassenger('Matt_100')
taxi1.addPassenger('Wilson_105')
print('-------------------------------')
taxi1.printDetails()
print('-------------------------------')
taxi1.addPassenger('Karen_200')
print('-------------------------------')
taxi1.printDetails()
print('-------------------------------')
taxi2 = TaxiLagbe('1010-02', 'Khulna')
taxi2.addPassenger('Ronald_115')
taxi2.addPassenger('Parker_215')
print('-------------------------------')
taxi2.printDetails()


Output:
--------------------------------------
Dear Walker! Welcome to TaxiLagbe.
Dear Wood! Welcome to TaxiLagbe.
Dear Matt! Welcome to TaxiLagbe.
Dear Wilson! Welcome to TaxiLagbe.
--------------------------------------
Trip info for Taxi number: 1010-01
This taxi can cover only Dhaka area.
Total passengers: 4
Passenger lists:
Walker, Wood, Matt, Wilson
Total collected fare: 505 Taka
--------------------------------------
Taxi Full! No more passengers can be added.
--------------------------------------
Trip info for Taxi number: 1010-01
This taxi can cover only Dhaka area.
Total passengers: 4
Passenger lists:
Walker, Wood, Matt, Wilson
Total collected fare: 505 Taka
--------------------------------------
Dear Ronald! Welcome to TaxiLagbe.
Dear Parker! Welcome to TaxiLagbe.
--------------------------------------
Trip info for Taxi number: 1010-02
This taxi can cover only Khulna area.
Total passengers: 2
Passenger lists:
Ronald, Parker
Total collected fare: 330 Taka

"""




# solution:

class TaxiLagbe:
  def __init__(self, t,l):
    self.taxiNumber=t
    self.location=l
    self.numberOfPassenger=0
    self.fare=0
    self.passengerList=""
  def addPassenger(self, *args):
    if self.numberOfPassenger<4:
      splitedResult=[]
      for i in args:
        splitedResult=i.split("_")
        print(f"Dear {splitedResult[0]}! Welcome to TaxiLagbe.")
        self.passengerList=self.passengerList+splitedResult[0]+", "
        self.fare+=int(splitedResult[1])
        self.numberOfPassenger+=1
    else:
      print("Taxi Full! No more passengers can be added.")
  def printDetails(self):
    print("Trip info for Taxi number:",self.taxiNumber)
    print(f"This taxi can cover only {self.location} area.")
    print("Total passengers:", self.numberOfPassenger)
    print("Passenger lists:")
    print(self.passengerList[:-2])
    print(f"Total collected fare: {self.fare} Taka")

taxi1 = TaxiLagbe('1010-01', 'Dhaka')
print('-------------------------------')
taxi1.addPassenger('Walker_100', 'Wood_200')
taxi1.addPassenger('Matt_100')
taxi1.addPassenger('Wilson_105')
print('-------------------------------')
taxi1.printDetails()
print('-------------------------------')
taxi1.addPassenger('Karen_200')
print('-------------------------------')
taxi1.printDetails()
print('-------------------------------')
taxi2 = TaxiLagbe('1010-02', 'Khulna')
taxi2.addPassenger('Ronald_115')
taxi2.addPassenger('Parker_215')
print('-------------------------------')
taxi2.printDetails()