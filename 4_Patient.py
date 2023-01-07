"""Implement the design of the Patient class so that the following output is produced:
[You are not allowed to change the code below]
# Write your code here.
p1 = Patient(“Thomas”, 23)
p1.add_Symptom(“Headache”)
p2 = Patient(“Carol”, 20)
p2.add_Symptom(“Vomiting”, “Coughing”)
p3 = Patient(“Mike”, 25)
p3.add_Symptom(“Fever”, “Headache”, “Coughing”)
print("=========================")
p1.printPatientDetail()
print("=========================")
p2.printPatientDetail()
print("=========================")
p3.printPatientDetail()

OUTPUT:
=========================
Name: Thomas
Age: 23
Symptoms: Headache
=========================
Name: Carol
Age: 20
Symptoms: Vomiting, Coughing
=========================
Name: Mike
Age: 25
Symptoms: Fever, Headache, Coughing
"""



# solution:

class Patient:
  def __init__(self, n, a):
    self.name=n
    self.age=a
    self.symptom=None
  def add_Symptom(self,*disease):
    s=""
    for i in disease:
      if i!=disease[-1]:
        s=s+i+", "
      else:
        s=s+i
    self.symptom=s
  def printPatientDetail(self):
    print("Name:", self.name)
    print("Age:", self.age)
    print("Symptoms:", self.symptom)

p1 = Patient("Thomas", 23)
p1.add_Symptom("Headache")
p2 = Patient("Carol", 20)
p2.add_Symptom("Vomiting", "Coughing")
p3 = Patient("Mike", 25)
p3.add_Symptom("Fever", "Headache", "Coughing")
print("=========================")
p1.printPatientDetail()
print("=========================")
p2.printPatientDetail()
print("=========================")
p3.printPatientDetail()