"""Write the ScienceExam class so that the following code generates the output below:

class Exam:
def __init__(self,marks):
self.marks = marks
self.time = 60
def examSyllabus(self):
return "Maths , English"
def examParts(self):
return "Part 1 - Maths\nPart 2 - English\n"

engineering = ScienceExam(100,90,"Physics","HigherMaths")
print(engineering)
print('----------------------------------')
print(engineering.examSyllabus())
print(engineering.examParts())
print('==================================')
architecture =
ScienceExam(100,120,"Physics","HigherMaths","Drawing")
print(architecture)
print('----------------------------------')
print(architecture.examSyllabus())
print(architecture.examParts())

OUTPUT:
Marks: 100 Time: 90 minutes Number of
Parts: 4
----------------------------------
Maths , English , Physics , HigherMaths
Part 1 - Maths
Part 2 - English
Part 3 - Physics
Part 4 - HigherMaths
==================================
Marks: 100 Time: 120 minutes Number of
Parts: 5
----------------------------------
Maths , English , Physics , HigherMaths
, Drawing
Part 1 - Maths
Part 2 - English
Part 3 - Physics
Part 4 - HigherMaths
Part 5 - Drawing
"""



# solution:

class Exam:
  def __init__(self,marks):
    self.marks = marks
    self.time = 60
      
  def examSyllabus(self):
    return "Maths , English"
  def examParts(self):
    return "Part 1 - Maths\nPart 2 - English\n"

#############################################################################

class ScienceExam(Exam):
  def __init__(self, *args):
    super().__init__(args[0])
    self.time = args[1]
    self.numberOfParts = len(args)
    self.syllabus=args[2:]

  def __str__(self):
    return (f"Marks: {self.marks} Time: {self.time} minutes Number of Parts: {self.numberOfParts}")
  
  def examSyllabus(self):
    s=""
    for i in self.syllabus:
      s = s + i + " , "
    return (f"{super().examSyllabus()} , {s[:-3]}")
  
  def examParts(self):
    p=""
    for i in range(3, self.numberOfParts+1):
      p = p + (f"Part {i} - {self.syllabus[i-3]}") + "\n"
    return (f"{super().examParts()}{p[:-1]}")

    
engineering = ScienceExam(100,90,"Physics","HigherMaths")
print(engineering)
print('----------------------------------')
print(engineering.examSyllabus())
print(engineering.examParts())
print('==================================') 
architecture = ScienceExam(100,120,"Physics","HigherMaths","Drawing")
print(architecture)
print('----------------------------------')
print(architecture.examSyllabus())
print(architecture.examParts())

