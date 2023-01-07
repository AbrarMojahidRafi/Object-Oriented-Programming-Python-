"""BRACU has n students who are regular competitive programmers. According
to the ACM ICPC rules, each person can participate in the regional championship
at most 5 times.

The head of the BRACU ACM Chapter is recently gathering teams to participate
in this championship. Each team must consist of exactly three people, at that, any
person cannot be a member of two or more teams. What maximum number of teams
can the head make if he wants each team to participate in the world championship
with the same members at least k times?
The first line of input contains two integers, n and k. The next line contains n
integers: y1,y2, ...,yn (0≤ yi≤ 5), where yi shows the number of times the i-thperson
participated in the ACM ICPC Regional.
Write a python program that prints how many teams can be formed according to
the above problem statement.


Sample Input 1
5 2
0 4 5 1 0
Sample Input 2
6 4
0 1 2 3 4 5
Sample Input 3
6 5
0 0 0 0 0 0

Sample Output 1
1
Sample Output 2
0
Sample Output 3
2
"""



# solution:

user_input1=input()
user_input1=user_input1.split(" ")
list1=[]
for i in user_input1:
  list1.append(int(i))

user_input2=input()
user_input2=user_input2.split(" ")
list2=[]
for i in user_input2:
  list2.append(int(i))


maxMember = 3
v = list1[1]
eligible = 0

for i in list2:
  if (i + v) in range(1, 6):
    eligible += 1

maxTeam = eligible // maxMember
print("Maximum number of teams:", maxTeam)