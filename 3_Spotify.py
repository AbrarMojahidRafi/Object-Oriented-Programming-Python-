"""Implement the design of the Spotify class so that the following output is produced:
Driver Code 

# Write your code here
user1 = Spotify(["See You Again", "Uptown Funk", "Hello"])
print("=========================")
print(user1.playing_number(4))
user1.add_to_playlist("Dusk Till Dawn")
print(user1.playing_number(3))
print(user1.playing_number(4))

Output:
Welcome to Spotify!
=========================
4 number song not found. Your playlist
has 3 songs only.
##########################
Playing 3 number song for you
Song name: Hello
##########################
Playing 4 number song for you
Song name: Dusk Till Dawn

"""



# solution:

class Spotify:
  def __init__(self, songList):
    self.songList=songList
    print("Welcome to Spotify!")
  def playing_number(self, num):
    if num<=len(self.songList):
      return ( f"Playing {num} number song for you \nSong name: {self.songList[num-1]} \n##########################" )
    else:
      return (f"{num} number song not found. Your playlist has {len(self.songList)} songs only. \n##########################")
    
  def add_to_playlist(self, newSong):
    self.songList.append(newSong)


user1 = Spotify(["See You Again", "Uptown Funk", "Hello"])
print("=========================")
print(user1.playing_number(4))
user1.add_to_playlist("Dusk Till Dawn")
print(user1.playing_number(3))
print(user1.playing_number(4))

