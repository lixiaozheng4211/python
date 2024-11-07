#BMI转换器 普通版
print('你好，欢迎使用BMI转换器')
an=''
#-------循环控制语句
while(an==''):
    height=float(input('请输入你的身高:(m)'))
    weight=float(input('请输入你的体重:(kg)'))
    bmi=(weight/(height*height))
    #---------------------------------散装显示法(%),.2f表示小数点保留两位
    print('你的身高为%.2f,体重为%.2f,您的BMI为%.2f'%(height,weight,bmi))
    if(bmi<18):
        print('你有点瘦了，不要挑食，记得多吃点哦！')
    elif(bmi<=24):
        print('我嘞个完美身材，继续保持哦！')
    elif(bmi<=28):
        print('微胖，要注意饮食哦！')
    else:
        print('你有亿点胖了，一定要管住嘴，迈开腿，小心三高哦！')
    an=input('once again?(回车继续)')
