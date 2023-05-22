# 开发时间：2023-05-17 10:30
# 开发人员：林坚洪
# encodeing "UTF-8"
import numpy as np
import ssl

# ssl._create_default_https_context = ssl._create_unverified_context

X = [[2, 0, -1.4],
     [2.2, 0.2, -1.5],
     [2.4, 0.1, -1],
     [1.9, 0, -1.2]]
print(np.array(X))

cov = np.cov(np.array(X).T)
print(cov)

w, v = np.linalg.eig(cov)
print('特征值：{0}\n 特征向量：{1}'.format(w, v))

arr1 = np.array(X)
arr2 = v.T
print(np.dot(arr1, arr2))

import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import fetch_olivetti_faces

faces = fetch_olivetti_faces()
X = faces.data
y = faces.target
print(X.shape)
