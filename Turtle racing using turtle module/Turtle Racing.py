#Turtle race Starting
import turtle
t=turtle.Turtle()
w=turtle.Screen()
w.title("Turtle race")
#Race Borders
t.pensize(10)
t.up()
t.goto(-255,-300)
t.down()
for i in range(4):
    if i==0 or i==2:
        t.forward(500)
        t.left(90)
    if i==1 or i==3:
        t.forward(600)
        t.left(90)
#Finish line pattern
t.pensize(1)
t.speed(10)
t.up()
t.goto(-250,220)
t.down()
t.color("black")
t.begin_fill()
t.forward(10)
for z in range(49):
    if (z%2)==0:
        for x in range(4):
            if x <= 2:
                t.left(90)
                t.forward(10)
            if x == 3:
                t.left(90)
                t.forward(20)
    if (z%2)==1:
        for y in range(4):
            if y <= 2:
                t.right(90)
                t.forward(10)
            if y == 3:
                t.right(90)
                t.forward(20)
t.end_fill()
#The Racing starting point line
t.speed(2)
t.pensize(3)
t.up()
t.goto(-255,-230)
t.down()
t.forward(500)
t.hideturtle()
#The Turtles
a=turtle.Turtle()#First Turtle 'a'
a.up()
a.shape("turtle")
a.color("Red")
a.goto(-210,-250)
a.left(90)
a.down()
a.speed(1)
a.pensize(2)
b=turtle.Turtle()#Second Turtle 'b'
b.up()
b.shape("turtle")
b.color("Blue")
b.goto(-110,-250)
b.left(90)
b.down()
b.speed(1)
b.pensize(2)
c=turtle.Turtle()#Third Turtle 'c'
c.up()
c.shape("turtle")
c.color("Purple")
c.goto(-10,-250)
c.left(90)
c.down()
c.speed(1)
c.pensize(2)
d=turtle.Turtle()#Fourth Turtle 'd'
d.up()
d.shape("turtle")
d.color("LightGreen")
d.goto(90,-250)
d.left(90)
d.down()
d.speed(1)
d.pensize(2)
e=turtle.Turtle()#Fifth Turtle 'e'
e.up()
e.shape("turtle")
e.color("Orange")
e.goto(190,-250)
e.left(90)
e.down()
e.speed(1)
e.pensize(2)
#Mechanics of the race
import random
Ia=0
Ib=0
Ic=0
Id=0
Ie=0
Z=1
for X in range(1000):
    for A in range(1):
        la=[0,0,Z,0]
        if random.choice(la)==1:
            a.forward(20)
            Ia += 1
        if Ia==23:
            print("Red Turtle won!")
            Z=0
            Ia=0
    for B in range(1):
        lb=[0,0,Z,0]
        if random.choice(lb)==1:
            b.forward(20)
            Ib += 1
        if Ib==23:
            print("Blue Turtle won!")
            Z=0
            Ib=0
    for C in range(1):
        lc=[0,0,Z,0]
        if random.choice(lc)==1:
            c.forward(20)
            Ic += 1
        if Ic==23:
            print("Purple Turtle won!")
            Z=0
            Ic=0
    for D in range(1):
        ld=[0,0,Z,0]
        if random.choice(ld)==1:
            d.forward(20)
            Id += 1
        if Id==23:
            print("Light Green Turtle won!")
            Z=0
            Id=0
    for E in range(1):
        le=[0,0,Z,0]
        if random.choice(le)==1:
            e.forward(20)
            Ie += 1
        if Ie==23:
            print("Orange Turtle won!")
            Z=0
            Ie=0
        





                





        
