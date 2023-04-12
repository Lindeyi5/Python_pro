# 开发时间：2023-02-22 10:57
# 开发人员：林坚洪
# encodeing "UTF-8"
def fun():
    print('hello,wprld!')


fun()


def hello(name):
    print('hellow!\t' + name)


hello('Tom')


def maxmin(a, b):
    if a > b:
        return a, b
    else:
        return b, a


big, small = maxmin(10, 20)
print(maxmin(1, 2))
print(big, small)
print(small, big)
print('-' * 88)

from math import log


def mf(base):
    return lambda x: log(x, base)


mm = mf(3)
print(mm(9))
print(log(9, 3))
