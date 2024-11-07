#BMI转换器 加强版（模块化）

#模块部分
def get_bmi():
    height=float(input('请输入你的身高:(m)'))
    weight=float(input('请输入你的体重:(kg)'))
    bmi=(weight/(height*height))
    return bmi   #把该程序块的结果带回到主程序去用
def jud(x):
    if(x<18):
        print('你有点瘦了，不要挑食，记得多吃点哦！')
    elif(x<=24):
        print('我嘞个完美身材，继续保持哦！')
    elif(x<=28):
        print('微胖，要注意饮食哦！')
    else:
        print('你有亿点胖了，一定要管住嘴，迈开腿，小心三高哦！')
#主程序部分
an=''
while(an==''):
    result=get_bmi()
    print('您的BMI为%.2f'%result)
    jud(result)
    an=input('once again?\n')
