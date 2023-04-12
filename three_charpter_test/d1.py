# 开发时间：2023-03-08 11:16
# 开发人员：林坚洪
# encodeing "UTF-8"
import numpy as np

ss = np.array(  # 定义数组矩阵
    [('X1', 'X2', 'X3'),
     (2, 0, -1.4),
     (2.2, 0.2, -1.5),
     (2.4, 0.1, -1),
     (1.9, 0, -1.2)
     ]
)
ss1 = np.array(  # 定义数组矩阵
    [
        (2, 0, -1.4),
        (2.2, 0.2, -1.5),
        (2.4, 0.1, -1),
        (1.9, 0, -1.2)
    ]
)
zz = ss1.T  # 转置
print('原矩阵:\n', ss1)
print('转置后原矩阵:\n', zz)
print('矩阵最大值:\n', ss1.max())
print('矩阵最小值:\n', ss1.min())
print('按行累计总和:\n', ss1.cumsum(axis=0))
print('按列累计总和:\n', ss1.cumsum(axis=1))
