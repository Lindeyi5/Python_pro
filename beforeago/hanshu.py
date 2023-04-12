# 开发时间： 2022/7/24  10:55
# 开发人：林坚洪
'''
def cald(a, b,c):
    d = a * b -c
    return d

ss = cald(1,2,3)
print(ss)
ssd=cald(b=1,c=2,a=3)
print(ssd)



#函数内存变化
def fun(a1,a2):
    print('a1',a1)
    print('a2', a2)
    a1=100
    a2.append(10)
    print('a1', a1)
    print('a2', a2)

n1=11
n2=[22,33,44]
fun(n1,n2)

print('n1', n1)
print('n2', n2)



# 函数返回值
def fun(list):
    odd = []
    even = []
    for i in list:
        if i % 2 == 0:
            odd.append(i)
        else:
            even.append(i)
    return odd, even


a1 = [37, 34, 2, 5, 26, 4, 22, 456, 345, 232]
fun(a1)
print(fun(a1))


#字典和元祖
def fun(*args):
    print(args)
fun(100,200,333,344)

def fun1(**args):
    print(args)
fun1(a=100,b=200,c=333,d=344)

#局部变量和全局变量
def fun(a,b,c):
    global ff
    ff=100
    print(a,b,c)
listt=[233,455,44]
fun(*listt)
print(ff)

def fun(n):
    if n==1:
        return n
    else:
        s=n*fun(n-1)
        return s

s=fun(6)
print(s)'''

'''失败品
print(1,1,2,3,5,8)
def fun(i):
    a=[i]
    if i<0:
        print('输出错误')
    elif i<3:
        a[0]=1
        a[1]=1
        return a
    elif 3<=i:
        if i<3:
          a[0] = 1
          a[1] = 1
        else:
          a[i]=a[i-1]+a[i-2]
    return a

ff=int(input('请输入数列个数'))
print(fun(ff))'''


def fun(i):
    if i == 1:
        s = 1
    elif i == 2:
        s = 2
    else:
        s = fun(i - 1) + fun(i - 2)
    return s

i = int(input('请输入数列个数'))

for i in range(1, i):
    print([fun(i)], end='')
print()
print(1, 1, 2, 3, 5, 8)
