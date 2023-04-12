# 开发时间：2023-02-22 10:57
# 开发人员：林坚洪
# encodeing "UTF-8"
def fun2(a,b,c):
    print(a,b,c)
fun2(1,2,3)
fun2(a=1,c=3,b=2)
fun2(1,c=3,b=2)
fun2(a=3,b=2,c=4)

def fun3(str1,*num):
    print(str1,num)
fun3('numbers',1,2,3,4,5)

def fun4(a,*num,**numm):
    print(a,num,numm)
fun4('dadas',2,3,4,5,b=3,c=77)

