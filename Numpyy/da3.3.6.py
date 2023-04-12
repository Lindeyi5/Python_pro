# 开发时间：2023-03-08 10:20
# 开发人员：林坚洪
# encodeing "UTF-8"
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
fig=plt.figure(figsize=(12,6))
x=range(5)
y=[2,2,5,2,4]
s=['数量1','数量2','数量3','数量4','数量5']
ax1 = fig.add_subplot(2,2,1)
plt.bar(x, y, width=0.5)
plt.xticks(x, s, rotation=0)
ax2 = fig.add_subplot(2,2,2)
plt.bar(range(4), [3, 4,2,3], width=0.3)
plt.xticks(x, s, rotation=0)
ax3 = fig.add_subplot(2,2,3)
plt.bar(range(4), [3, 4,2,3], width=0.3)
plt.xticks(x, s, rotation=90)
ax4 = fig.add_subplot(2,2,4)
plt.bar(range(4), [3, 4,2,3], width=0.3)
plt.xticks(x, s, rotation=90)
plt.show()