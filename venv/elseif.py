# 开发时间： 2022/7/13  17:55
# 开发人：林坚洪
'''score=int(input('请输入查询成绩'))
if score>=90 and score<=100:
    print('A级')
elif score>=80 and score<90:
    print('B级')
elif 70 <= score < 80:
    print('C级')
else:print('成绩无效')'''
score=int(input('请输入查询成绩'))
money=input('你有钱吗?y/n')
if  score>=90:
    if money is 'y':
       print('你是好好学生')
    else:
       print('你是好学生')
else:
    if money is 'y':
       print('你是学生')
    else:
       print('你是坏坏学生')