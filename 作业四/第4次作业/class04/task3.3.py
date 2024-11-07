#用t代替turtle简便一些
import turtle as t
import time
t1=t.Turtle()
t2=t.Turtle()
#定义旗杆
def qigan():
    t2.penup()
    t2.goto(-300,-1000)
    t2.pendown()
    t2.setheading(180)
    t2.begin_fill()
    t2.forward(10)
    t2.right(90)
    t2.forward(2000)
    t2.right(90)
    t2.forward(10)
    t2.right(90)
    t2.forward(2000)
    t2.end_fill()
#定义国旗面
def jx(x,y):
    t1.setheading(0)
    t1.speed(0)
    t1.penup()
    t1.goto(x,y)
    t1.pendown()
    t1.color("red")
    t1.begin_fill()
    #循环结构，括号里表示循环次数
    for i in range(2):
        t1.forward(450)
        t1.left(90)
        t1.forward(300)
        t1.left(90)
    t1.end_fill()
#定义五角星
def star(x,y,L,an):
    t1.penup()
    t1.goto(x,288+y)
    t1.pendown()
    t1.setheading(an)
    t1.color("gold")
    t1.begin_fill()
    #循环结构，括号里表示循环次数
    for _ in range(5):
        t1.forward(L)
        t1.right(144)
    t1.end_fill()
def main(x,y):
    jx(x,y)
    star(-270,-50+y,120,0)
    star(-140,-30+y,35,40)
    star(-100,-50+y,35,20)
    star(-100,-90+y,35,0)
    star(-140,-130+y,35,45)
    t1.hideturtle()
i=0
while(i<=30):
    t1.clear()
    time.sleep(0.1)
    t1.speed(0)
    t2.speed(0)
    t.tracer(0)
    qigan()
    t.tracer(1)
    t.tracer(0)
    main(-310+11,-300+i*10)
    t.tracer(10,1)
    t1.hideturtle()
    i=i+1
