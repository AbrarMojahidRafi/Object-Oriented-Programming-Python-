"""The Giant Panda Protection and Research Center in the Sichuan province of southwest
China, actually employs a category of workers known as panda nannies. The primary
responsibility is to play with adorable panda cubs and name them, determine gender,
keep track of their age and hours they sleep. So being a programmer panda nanny, you
will create a code that will do all these works for you.
1. Create a class named Panda and also write the constructor.
2. Access the instance attributes and print them in the given format.
3. Call instance methods to keep track of their daily hours of sleep.
4. Suppose consulting with other panda nannies you have set some criteria based
on which you will make their diet plans. The criteria are:
** Mixed Veggies for pandas having 3 to 5 hours (included) of sleep daily.
** Eggplant & Tofu for pandas having 6 to 8 hours (included) of sleep daily.
** Broccoli Chicken for pandas having 9 to 11 hours (included) of sleep daily.
** Lastly if no arguments are passed then just give it bamboo leaves.
Now handle this problem modifying the method designed to keep track of their daily
hours of sleep and determine diet plan using method overloading.
[You are not allowed to change the code below]


#Write your code here for subtasks 1-4.
panda1 = Panda("Kunfu","Male", 5)
panda2=Panda("Pan Pan","Female",3)
panda3=Panda("Ming Ming","Female",8)
print("{} is a {} Panda Bear who is {} years
old".format(panda1.name,panda1.gender,panda1.age))
print("{} is a {} Panda Bear who is {} years
old".format(panda2.name,panda2.gender,panda2.age))
print("{} is a {} Panda Bear who is {} years
old".format(panda3.name,panda3.gender,panda3.age))
print("===========================")
print(panda2.sleep(10))
print(panda1.sleep(4))
print(panda3.sleep())

OUTPUT:
Kunfu is a Male Panda Bear who is 5 years
old
Pan Pan is a Female Panda Bear who is 3
years old
Ming Ming is a Female Panda Bear who is 8
years old
===========================
Pan Pan sleeps 10 hours daily and should
have Broccoli Chicken
Kunfu sleeps 4 hours daily and should have
Mixed Veggies
Ming Ming's duration is unknown thus should
have only bamboo leaves
"""



# solution:

class Panda:
  def __init__(self,n,g,a):
    self.name=n
    self.gender=g
    self.age=a 
  def sleep(self,num=None):
    self.sleep=num 
    if self.sleep==None: 
      return (f"{self.name}'s duration is unknown thus should have only  bamboo leaves")
    elif (3 <= self.sleep <= 5) and self.sleep!=None:
      return (f"{self.name} sleeps {self.sleep} hours daily and should have Mixed Veggies")
    elif (6 <= self.sleep <= 8) and self.sleep!=None:
      return (f"{self.name} sleeps {self.sleep} hours daily and should have Eggplant & Tofu")
    elif (9 <= self.sleep <= 11) and self.sleep!=None:
      return (f"{self.name} sleeps {self.sleep} hours daily and should have Broccoli Chicken")


panda1 = Panda("Kunfu","Male", 5)
panda2=Panda("Pan Pan","Female",3)
panda3=Panda("Ming Ming","Female",8)
print("{} is a {} Panda Bear who is {} years old".format(panda1.name,panda1.gender,panda1.age))
print("{} is a {} Panda Bear who is {} years old".format(panda2.name,panda2.gender,panda2.age))
print("{} is a {} Panda Bear who is {} years old".format(panda3.name,panda3.gender,panda3.age))
print("===========================")
print(panda2.sleep(10))
print(panda1.sleep(4))
print(panda3.sleep())