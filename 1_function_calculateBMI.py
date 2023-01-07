"""You are one of the gym instructors at AmiKenoMota. You decide to provide a
customized diet and exercise plans based on the BMI of an individual. You
measure the weight in kilograms and height in meters and calculate the BMI
before a plan can be decided. Write a BMI function that takes in two values,
weight in kg and height in cm and print the score along with the condition. (Make
sure to convert cm into m before calculation)
BMI(height, weight)

BMI = kg/m2
Based on the BMI score return the following output.

● < 18.5- Underweight
● 18.5 - 24.9 - Normal
● 25 -30 - Overweight
● > 30 – Obese


Sample Input
(175, 96)
(152, 48)

Sample Output
Score is 31.3. You are Obese
Score is 20.8. You are Normal
"""



# solution:

def BMI(height, weight):
  height=height*0.01
  bmi=weight/(height*height)

  if bmi < 18.5:
    opinion="Underweight"
  elif 18.5 <= bmi <= 24.9:
    opinion="Normal"
  elif 25 <= bmi <= 30:
    opinion="Overweight"
  else:
    opinion="Obese"

  print("Score is {:.1f}. You are {}".format(bmi,opinion))

height=int(input())
weight=int(input())
BMI(height, weight)
