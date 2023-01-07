"""Design the ParcelKoro class such a way so that the following code provides the expected
output.
Hint: total_fee = (total_weight * 20) + location_charge.
Note: For the method calculate fee: if the delivery location is not given, the
location_charge will be 50 taka or else 100 taka. Also, while calculating total fee, if the
product weight is 0 the total_fee should also be 0.
Assume only these 3 ways you can create an object of a class.
[You are not allowed to change the code below]

# Write your code here.
print("**********************")
p1 = ParcelKoro()
p1.calculateFee()
p1.printDetails()
print("**********************")
p2 = ParcelKoro('Bob The Builder')
p2.calculateFee()
p2.printDetails()
print("----------------------------")
p2.product_weight = 15
p2.calculateFee()
p2.printDetails(
print("**********************")
p3 = ParcelKoro('Dora The Explorer', 10)
p3.calculateFee('Dhanmondi')
p3.printDetails()

OUTPUT:
**********************
Customer Name: No name set
Product Weight: 0
Total fee: 0
**********************
Customer Name: Bob The Builder
Product Weight: 0
Total fee: 0
----------------------------
Customer Name: Bob The Builder
Product Weight: 15
Total fee: 350
**********************
Customer Name: Dora The Explorer
Product Weight: 10
Total fee: 300
"""



# solution:

class ParcelKoro:
  def __init__(self,name=None,product_weight=None):
    if name==None and product_weight==None:
      self.name="No name set"
      self.product_weight=0
    elif name!=None and product_weight==None:
      self.name=name
      self.product_weight=0
    elif name!=None and product_weight!=None:
      self.name=name
      self.product_weight=product_weight
    self.location_charge=0
    self.total_fee=0
  def calculateFee(self, location=None):
    if self.product_weight==0 and location==None:
      self.total_fee=0
    elif self.product_weight!=0 and location==None:
      self.location_charge=50
      self.total_fee = (self.product_weight * 20) + self.location_charge
    elif self.product_weight!=0 and location!=None:
      self.location_charge=100
      self.total_fee = (self.product_weight * 20) + self.location_charge

  def printDetails(self): 
    print("Customer Name:", self.name)
    print("Product Weight:", self.product_weight)
    print("Total fee:", self.total_fee)
    

print("**********************")
p1 = ParcelKoro()
p1.calculateFee()
p1.printDetails()
print("**********************")
p2 = ParcelKoro('Bob The Builder')
p2.calculateFee()
p2.printDetails()
print("----------------------------")
p2.product_weight = 15     # <-------------------------------------------------question 
p2.calculateFee()
p2.printDetails()
print("**********************")
p3 = ParcelKoro("Dora The Explorer", 10)
p3.calculateFee('Dhanmondi')
p3.printDetails()