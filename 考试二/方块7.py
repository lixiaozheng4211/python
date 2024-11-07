import turtle as t
t.speed(0)
a=[-150,-225]
d=[[-140,180],[120,-220],[-135,170],[120,-165],[-110,140],[60,140],[-110,0],[60,0],[-110,-140],[60,-140],[-25,60]]
def card(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.begin_fill()
    t.color("red","white")
    for i in range(2):
        t.forward(300)
        t.left(90)
        t.forward(450)
        t.left(90)
    t.end_fill()

def number(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.begin_fill()
    t.color("red")
    t.write("7",font=("Courier",30,"normal"))
    t.end_fill()

def fp1(x,y):
    t.penup()
    t.goto(x,y)
    t.setheading(-55)
    t.pendown()
    t.begin_fill()
    t.color("red","red")
    for i in range(2):
        t.forward(15)
        t.left(110)
        t.forward(15)
        t.left(70)
    t.end_fill()

def fp2(x,y):
    t.penup()
    t.goto(x,y)
    t.setheading(-55)
    t.pendown()
    t.begin_fill()
    t.color("red","red")
    for i in range(2):
        t.forward(50)
        t.left(110)
        t.forward(50)
        t.left(70)
    t.end_fill()


card(a[0],a[1])
number(d[0][0],d[0][1])
number(d[1][0],d[1][1])
fp1(d[2][0],d[2][1])
fp1(d[3][0],d[3][1])
fp2(d[4][0],d[4][1])
fp2(d[5][0],d[5][1])
fp2(d[6][0],d[6][1])
fp2(d[7][0],d[7][1])
fp2(d[8][0],d[8][1])
fp2(d[9][0],d[9][1])
fp2(d[10][0],d[10][1])

t.hideturtle()
