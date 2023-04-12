# 开发时间：2023-03-06 11:35
# 开发人员：林坚洪
# encodeing "UTF-8"
# 绘制出不同种类鸢尾花花萼和花瓣长度（SpealLength）和宽度（Spealwidth）的散点图
# 和箱线图（boxplot）。数据从机器学习包中导入。
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
iris_dataset = load_iris()
iris = pd.DataFrame(iris_dataset.data, columns=
['SpealLength', 'Spealwidth', 'Petalwidth', 'PetalLength'])
#print(iris)
x=np.linspace(0,149,150)
fig,axes=plt.subplots(figsize=(12,6))
# axes[iris].scatter(iris.iloc[:, 1], iris.iloc[:, 2])
# plt.show()
a=iris['SpealLength']
b=iris['Spealwidth']
c=iris['Petalwidth']
d=iris['PetalLength']
plt.scatter(x,a,c='red')
plt.scatter(x,b,c='blue')
plt.scatter(x,c,c='pink')
plt.scatter(x,d,c='yellow')
# plt.scatter(a,c,c='blue')
# plt.scatter(a,d,c='green')
plt.show()