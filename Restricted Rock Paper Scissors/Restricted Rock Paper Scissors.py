#Functions:-
def DisplayCards(a,b,c,d,e):
  print("Player",d,"   ",e,"points")
  print("You have",a,"amount of Rock cards left")
  print("You have",b,"amount of Paper cards left")
  print("You have",c,"amount of Scissors cards left")
#Restricted Rock Paper Scissors (Completed)
import random as r
print("Restricted Rock Paper Scissors against a Computer")
xn=input("Enter your name: ")
print("Type 1 for Rock")
print("Type 2 for Paper")
print("Type 3 for Scissors")
#Assigning Values
x1=4
x2=4
x3=4
y1=4
y2=4
y3=4
yp=0
xp=0
l=[1,2,3]
Time=12
#The Brains
T=True
while(T):
  #Restrictions for the Player
  x=int(input(": "))
  if x1==0 and x==1:
    print("You don't have any of those card left... Choose your other options")
    continue
  elif x2==0 and x==2:
    print("You don't have any of those card left... Choose your other options")
    continue
  elif x3==0 and x==3:
    print("You don't have any of those card left... Choose your other options")
    continue
  y=r.choice(l)
  yn="Computer"
  #Readying the choices for the players
  if x==1 and x1>0:
    X="Rock"
    x1-=1
  if x==2 and x2>0:
    X="Paper"
    x2-=1
  if x==3 and x3>0:
    X="Scissors"
    x3-=1
  if y==1 and y1>0:
    Y="Rock"
    y1-=1
  if y==2 and y2>0:
    Y="Paper"
    y2-=1
  if y==3 and y3>0:
    Y="Scissors"
    y3-=1
  print(xn,"puts",X)
  print(yn,"puts",Y)
  #Point deciding conditions
  if x==y:
    print("It's a Draw!")
  elif x==1 and y==2:
    print(yn,"Wins!")
    yp+=1
  elif x==1 and y==3:
    print(xn,"Wins!")
    xp+=1
  elif x==2 and y==1:
    print(xn,"Wins!")
    xp+=1
  elif x==2 and y==3:
    print(yn,"Wins!")
    yp+=1
  elif x==3 and y==1:
    print(yn,"Wins!")
    yp+=1
  elif x==3 and y==2:
    print(xn,"Wins!")
    xp+=1
  #Computer choice removal
  if y1==0 and 1 in l:
    l.remove(1)
  if y2==0 and 2 in l:
    l.remove(2)
  if y3==0 and 3 in l:
    l.remove(3)
  #Display of results after each round
  DisplayCards(x1,x2,x3,xn,xp)
  DisplayCards(y1,y2,y3,yn,yp)
  Time-=1
  if Time==0:
    break
if xp>yp:
  print("Player",xn,"WINS THE ENTIRE GAME!!!!")
elif xp<yp:
  print("Player",yn,"WINS THE ENTIRE GAME!!!!")
elif xp==yp:
  print("It's a Draw!!! Both participants have equal points...")