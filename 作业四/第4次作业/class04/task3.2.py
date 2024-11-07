#用t代替turtle实现简化
import turtle as t
t.speed(0)
#用模块法绘图更方便
#定义国旗面
def flag(x,y):
    t.setheading(0)
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.begin_fill()
    t.color('red','red')
    t.forward(350)
    t.left(90)
    t.forward(250)
    t.left(90)
    t.forward(350)
    t.left(90)
    t.forward(250)
    t.left(90)
    t.end_fill()
#定义五角星
def star(x,y,z,L):
    t.setheading(z)
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.begin_fill()
    t.color("gold","gold")
    t.forward(L)
    t.right(144)
    t.forward(L)
    t.right(144)
    t.forward(L)
    t.right(144)
    t.forward(L)
    t.right(144)
    t.forward(L)
    t.end_fill()
#定义中国标准国旗
def china_flag(x0,y0,x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,x5,y5,z5):
    flag(x0,y0)
    star(x1,y1,z1,80)
    star(x2,y2,z2,30)
    star(x3,y3,z3,30)
    star(x4,y4,z4,30)
    star(x5,y5,z5,30)
#主程序
china_flag(-300,-60,-270,130,0,-180,150,30,-170,130,0,-175,100,-10,-185,70,-30)
china_flag(60,-60,90,130,0,180,150,30,190,130,0,185,100,-10,175,70,-30)
china_flag(-300,-320,-270,-130,0,-180,-110,30,-170,-130,0,-175,-160,-10,-185,-190,-30)
china_flag(60,-320,90,-130,0,180,-110,30,190,-130,0,185,-160,-10,175,-190,-30)
t.hideturtle()


















    
