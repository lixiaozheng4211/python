p='y'
while(p=='y'):
    total_scores=int(input('请输入你这学期必选的科目总数：'))
    a=0;a_score=0;a_grade=0;total_grades=0
    while a<total_scores:
        a+=1
        name=input('请输入课程名字：')
        score=float(input('请输入必选科目的学分：'))
        grade=float(input('请输入你得到的成绩：'))
        jd=float(input('必选科目的绩点：'))
        total_grades+=score*jd
        a_score+=score;a_grade+=grade

    ave_grade=total_grades/a_score
    print('你的总学分是：'+str(a_score)+';你的平均绩点是:'+str(ave_grade))
    p=input('once again???(y/n)')
