# 开发时间：2023-03-06 11:35
# 开发人员：林坚洪
# encodeing "UTF-8"
# 绘制出不同种类鸢尾花花萼和花瓣长度（SpealLength）和宽度（Spealwidth）的散点图
# 和箱线图（boxplot）。数据从机器学习包中导入。
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
iris_dataset = load_iris()
iris = pd.DataFrame(iris_dataset.data, columns=
['SpealLength', 'Spealwidth', 'Petalwidth', 'PetalLength'])
print(iris)

fig, axes = plt.subplots(1, 2, figsize=(12, 6))

a = iris['SpealLength']
b = iris['Spealwidth']
c = iris['Petalwidth']
d = iris['PetalLength']
axes[0].scatter(a, b, c='red')
axes[1].scatter(d, c, c='blue')

axes[0].set_xlabel("鸢尾花花萼长度")
axes[0].set_ylabel("鸢尾花花萼宽度")
axes[0].title.set_text("不同种类鸢尾花花萼长度和宽度散点图")
axes[1].set_xlabel("鸢尾花花瓣长度")
axes[1].set_ylabel("鸢尾花花瓣宽度")
axes[1].title.set_text("不同种类鸢尾花花瓣长度和宽度散点图")

plt.show()

plt.figure(figsize=(12, 7))
plt.grid(True)
plt.boxplot(iris,
            labels=list(['SpealLength', 'Spealwidth', 'Petalwidth', 'PetalLength']),  # 为箱线图添加标签，类似于图例的作用
            sym="g+",  # 异常点形状
            showmeans=True  # 是否显示均值
            )
plt.show()

