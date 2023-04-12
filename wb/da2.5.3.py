# 开发时间：2023-02-16 10:06
# 开发人员：林坚洪
# encodeing "UTF-8"
for a in ['e','f','g']:
    print(a)
for a in "string":
    print(a,end=" ")
for a in range(2,10):
    print(a,end=" ")



for n in range(2,10):
    for x in range(2,n):
        if n%x==0:
            print(n,'equals',x,'*',n/x)
            break
    else:
        print(n,"是一个质数")