"""Write the SultansDine class so that the given code provides the expected output.
[You are not allowed to change the code below]
# Write your code here
SultansDine.details()
print('########################')
dhanmodi = SultansDine('Dhanmondi')
dhanmodi.sellQuantity(25)
dhanmodi.branchInformation()
print('-----------------------------------------')
SultansDine.details()
print('========================')
baily_road = SultansDine('Baily Road')
baily_road.sellQuantity(15)
baily_road.branchInformation()
print('-----------------------------------------')
SultansDine.details()
print('========================')
gulshan = SultansDine('Gulshan')
gulshan.sellQuantity(9)
gulshan.branchInformation()
print('-----------------------------------------')
SultansDine.details()

Output:
Total Number of branch(s): 0
Total Sell: 0 Taka
#################################
Branch Name: Dhanmondi
Branch Sell: 10000 Taka
-----------------------------------------
Total Number of branch(s): 1
Total Sell: 10000 Taka
Branch Name: Dhanmondi, Branch Sell: 10000 Taka
Branch consists of total sell's: 100.00%
================================
Branch Name: Baily Road
Branch Sell: 5250 Taka
-----------------------------------------
Total Number of branch(s): 2
Total Sell: 15250 Taka
Branch Name: Dhanmondi, Branch Sell: 10000 Taka
Branch consists of total sell's: 65.57%
Branch Name: Baily Road, Branch Sell: 5250 Taka
Branch consists of total sell's: 34.43%
================================
Branch Name: Gulshan
Branch Sell: 2700 Taka
-----------------------------------------
Total Number of branch(s): 3
Total Sell: 17950 Taka
Branch Name: Dhanmondi, Branch Sell: 10000 Taka
Branch consists of total sell's: 55.71%
Branch Name: Baily Road, Branch Sell: 5250 Taka
Branch consists of total sell's: 29.25%
Branch Name: Gulshan, Branch Sell: 2700 Taka
Branch consists of total sell's: 15.04%

Subtaks:
1. Create SultansDine class

2. Create 2 class variable and 1 class list
3. Create 1 class method
4. Calculation of branch sell is given below
a. If sellQuantity < 10:
i. Branch_sell = quantity * 300
b. Else if sellQuantity < 20:
i. Branch_sell = quantity * 350
c. Else
i. Branch_sell = quantity * 400

5. Calculation of branch’s sell percentage = (branch’s sell / total sell) * 100

"""


# solution:

# Write your code here
class SultansDine:

  totalNumOfBranch=0
  totalSell=0
  classList=[]

  def __init__(self, loc):
    self.location=loc
    self.branchSell=0
    SultansDine.totalNumOfBranch+=1

  def sellQuantity(self, num):
    if num<10:
      self.branchSell+=num*300 
      temList=[self.location, self.branchSell]
      SultansDine.classList.append(temList)
      SultansDine.totalSell+=self.branchSell
    elif num<20:
      self.branchSell+=num*350
      temList=[self.location, self.branchSell]
      SultansDine.classList.append(temList)
      SultansDine.totalSell+=self.branchSell
    else:
      self.branchSell+=num*400
      temList=[self.location, self.branchSell]
      SultansDine.classList.append(temList)
      SultansDine.totalSell+=self.branchSell

  def branchInformation(self):
    print("Branch Name:", self.location)
    print("Branch Sell:", self.branchSell, "Taka")

  @classmethod
  def details(cls):
    print(f"Total Number of branch(s): {cls.totalNumOfBranch}")
    print(f"Total Sell: {cls.totalSell} Taka")
    for i in range(len(cls.classList)):
      print(f"Branch Name: {cls.classList[i][0]}, Branch Sell: {cls.classList[i][1]} Taka")
      percentage = ( cls.classList[i][1] / cls.totalSell)*100
      print("Branch consists of total sell's: {:.2f}%".format(percentage))


SultansDine.details()
print('########################')
dhanmodi = SultansDine('Dhanmondi')
dhanmodi.sellQuantity(25)
dhanmodi.branchInformation()
print('-----------------------------------------')
SultansDine.details()

print('========================')

baily_road = SultansDine('Baily Road')
baily_road.sellQuantity(15)
baily_road.branchInformation()
print('-----------------------------------------')
SultansDine.details()

print('========================')

gulshan = SultansDine('Gulshan')
gulshan.sellQuantity(9)
gulshan.branchInformation()
print('-----------------------------------------')
SultansDine.details()
