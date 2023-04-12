# 开发时间： 2022/7/25  11:01
# 开发人：林坚洪
try:
    a=int(input('请输入a'))
    b=int(input('请输入b'))
    c=a+b
    print(c)
except ValueError:
    print('搞笑吧你,老子不玩了')
