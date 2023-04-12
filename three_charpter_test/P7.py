'''
encoding = 'utf-8'
author:ljk
date:2023-03-08 11:08
'''
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data.csv')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
# print(data.head())
x1 = data.iloc[0, 1:]
x2 = data.iloc[1, 1:]
x3 = data.iloc[2, 1:]
x4 = data.iloc[3, 1:]
x5 = data.iloc[4, 1:]

print(x1)
y = range(5)
s = ['a', 'b', 'c', 'd', 'e']
fig, ax = plt.subplots(1, 5, figsize= (12,8))
#
ax[0].bar(y, x1, width = 0.5)
ax[0].set_xticks(y, s)
ax[0].set_title('图一')

ax[1].bar(y, x2 , width = 0.5)
ax[1].set_xticks(y, s)
ax[1].set_title('图二')

ax[2].bar(y, x3 , width = 0.5)
ax[2].set_xticks(y, s)
ax[2].set_title('图三')

ax[3].bar(y, x4 , width = 0.5)
ax[3].set_xticks(y, s)
ax[3].set_title('图四')

ax[4].bar(y, x5 , width = 0.5)
ax[4].set_xticks(y, s)
ax[4].set_title('图五')

plt.show()