# 开发时间：2023-03-02 11:08
# 开发人员：林坚洪
# encodeing "UTF-8"
def secrity(m):
    m = int(m)
    g = m % 10
    s = int(m / 10) % 10
    b = int(m / 100) % 10
    w = int(m / 1000) % 10
    g = (g + 5) % 10
    s = (s + 5) % 10
    b = (b + 5) % 10
    w = (w + 5) % 10
    ss = g * 1000 + w + s * 100 + b * 10
    print(ss)


gg = input('请输入需要加密的电话号码')
secrity(gg)
# print(int(4567/10)%10)
