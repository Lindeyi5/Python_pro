# 开发时间：2023-03-01 11:33
# 开发人员：林坚洪
# encodeing "UTF-8"
def fib(n):
    f1 = [1, 1]
    for i in range(2, n):
        x = f1[i - 1] + f1[i - 2]
        f1.append(x)
    return f1[n - 1]


print(fib(10))
