import turtle as t
t.speed(0)
def card():
    t.penup()
    t.goto(-225,-150)
    t.pendown()
    t.begin_fill()
    t.color("black","blue")
    for i in range(2):
        t.forward(450)
        t.left(90)
        t.forward(300)
        t.left(90)
    t.end_fill()

def word(x,y,m,n,h):
    t.penup()
    t.goto(x,y)#-35,0
    t.pendown()
    t.begin_fill()
    t.color("#FFD74F")
    t.write(m,font=("Comic",n,h))
    t.end_fill()

card()
word(-215,110,'长江大学',20,"normal")
word(-38,0,'李沁春',36,"bold")
word(-100,50,'2024编程实验室',24,"normal")
word(-80,-30,"QQ：2469402957",20,"normal")
word(-130,-100,"喜欢打篮球乒乓球",26,"normal")
t.hideturtle()
