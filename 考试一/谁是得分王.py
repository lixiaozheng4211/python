print("==============成绩录入===============")
n1=input("姓名1：")
cj1=input("成绩1：")
n2=input("姓名2：")
cj2=input("成绩2：")
n3=input("姓名3：")
cj3=input("成绩3：")
n4=input("姓名4：")
cj4=input("成绩4：")

print("本小组的成绩录入如下：")
print("序号    姓名     成绩")
print( "1","     ",n1,"     ",cj1)
print( "2","     ",n2,"     ",cj2)
print( "3","     ",n3,"     ",cj3)
print( "4","     ",n4,"     ",cj4)

a=n1,cj1
b=n2,cj2
c=n3,cj3
d=n4,cj4
if max(cj1,cj2,cj3,cj4)==cj1:
    print("本次考试成绩最高的是",a)
elif max(cj1,cj2,cj3,cj4)==cj2:
    print("本次考试成绩最高的是",b)
elif max(cj1,cj2,cj3,cj4)==cj3:
    print("本次考试成绩最高的是",c)
else:
    print("本次考试成绩最高的是",d)
    
