"""Implement the design of the EPL_Team class so that the following output is produced:
Driver Code 

# Write your code here
manu = EPL_Team('Manchester United', 'Glory Glory Man United')
chelsea = EPL_Team('Chelsea')
print('===================')
print(manu.showClubInfo())
print('##################')
manu.increaseTitle()
print(manu.showClubInfo())
print('===================')
print(chelsea.showClubInfo())
chelsea.changeSong('Keep the blue flag flying high')
print(chelsea.showClubInfo())


Output
===================
Name: Manchester United
Song: Glory Glory Man United
Total No of title: 0
##################
Name: Manchester United
Song: Glory Glory Man United
Total No of title: 1
===================
Name: Chelsea
Song: No Slogan
Total No of title: 0
Name: Chelsea
Song: Keep the blue flag flying high
Total No of title: 0

"""



# solution:

class EPL_Team:
  def __init__(self,n=None,s=None):
    if n!=None and s!=None:
      self.name=n
      self.song=s
    elif n!=None and s==None:
      self.name=n
      self.song="No Slogan"
    self.title=0
  def showClubInfo(self):
    return (f"Name: {self.name} \nSong: {self.song} \nTotal No of title: {self.title}")
  def increaseTitle(self):
    self.title+=1
  def changeSong(self, oneParameter):
    self.song=oneParameter
  
manu = EPL_Team('Manchester United', 'Glory Glory Man United')
chelsea = EPL_Team('Chelsea')
print('===================')
print(manu.showClubInfo())
print('##################')
manu.increaseTitle()
print(manu.showClubInfo())
print('===================')
print(chelsea.showClubInfo())
chelsea.changeSong('Keep the blue flag flying high')
print(chelsea.showClubInfo())