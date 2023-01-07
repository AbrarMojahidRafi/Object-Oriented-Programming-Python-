"""You want to order Burger from Chillox through the FoodPanda App. You have to
calculate the total price. Write a function which will take the name of the burger
and place(Mohakhali/Outside of Mohakhali) as input. Use default argument
technique for taking place input.


Menu ----------------------------Price(Tk)
BBQ Chicken Cheese Burger --------250
Beef Burger ----------------------170
Naga Drums -----------------------200

Hint: Total Price = meal_cost + delivery_charge + tax 

Note that:
● If your home is in Mohakhali area then your delivery charge is 40
taka else 60 taka
● Your tax rate is 8% of your meal.

Sample Input
(‘Beef Burger’, ‘Dhanmondi’)
(‘Beef Burger’)

Sample Output
243.6
223.6
"""



# solution:

menu={"BBQ Chicken Cheese Burger":250, "Beef Burger":170, "Naga Drums":200}

def calculate_price(name, place="mohakhali"):
  totalPrice=0
  for i in menu:
    if name==i:
      totalPrice=totalPrice+menu[i]
      if place != "mohakhali":
        totalPrice=totalPrice+60+menu[i]*(8/100)
      else:
        totalPrice=totalPrice+40+menu[i]*(8/100)
  
  print(totalPrice)

name=input()
place=input().lower()
calculate_price(name, place)
calculate_price(name)

