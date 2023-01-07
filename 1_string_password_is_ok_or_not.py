"""Again, you have lost your USIS password!! You went to the registrar office
and requested for a new password. This time, you need to follow some rules to
set your password. Otherwise, they won't change it. The rules are
At least one lowercase letter
At least one uppercase letter
At least one digit (0-9)
At least one special character (_ , $ , #, @)
Your task is to find whether a given password follows all those rules. If it breaks
any rule, you have to print Lowercase Missing, Uppercase Missing, Digit Missing
or Special Missing respective to the missing case. For more than one rule break,
print all the rules that were broken (order doesn't matter). If the password is ok,
print OK.

Sample Input:
ohMyBR@CU
ohmybracu
OhMyBR@CU20

Sample Output:
Digit missing
Uppercase character missing, Digit missing, Special character missing
OK

"""




# solution:

userPassword=input("Enter input: ")

upperCase=False
lowerCase=False
specialChar=False
digit=False

for i in userPassword:
  if "A" <= i <= "Z":
    upperCase=True
  elif "a" <= i <= "z":
    lowerCase=True
  elif i in "_$#@":
    specialChar=True
  elif i in "012345689":
    digit=True

dictionary={}
dictionary["Uppercase character missing"]=upperCase
dictionary["Lowercase character missing"]=lowerCase
dictionary["Special character missing"]=specialChar
dictionary["Digit missing"]=digit

falseList=[]
for i in dictionary:
  if dictionary[i]==False:
    falseList.append(i)

if len(falseList)==0:
  print("OK")
else:
  for i in falseList:
    if i==falseList[-1]:
      print(i)
    else:
      print(i, end=", ")