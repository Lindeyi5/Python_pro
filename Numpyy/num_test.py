# 开发时间：2023-02-27 11:27
# 开发人员：林坚洪
# encodeing "UTF-8"
import numpy as np


def fun(i, j):
    return (i + 1) * (j + 1)


dd = np.fromfunction(fun, (9, 9))
print(dd)
