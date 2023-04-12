# 开发时间：2023-03-15 16:42
# 开发人员：林坚洪
# encodeing "UTF-8"
# 开发时间：2023-03-10 20:49
# 开发人员：林坚洪
# encodeing "UTF-8"
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
st = pd.read_excel('student.xlsx')

name = st['姓名'].values.T.tolist()
yw = st['语文'].values.T.tolist()
sx = st['数学'].values.T.tolist()
yy = st['英语'].values.T.tolist()
zz = st['政治'].values.T.tolist()
x = name
fig = plt.figure(figsize=(10, 7))
ax1 = fig.add_subplot(2, 2, 1)
ax1.title.set_text('语文')
plt.ylim(40, 100)
plt.bar(x, yw, width=0.5, color='skyblue')
ax2 = fig.add_subplot(2, 2, 2)
ax2.title.set_text('数学')
plt.ylim(40, 100)
plt.bar(x, sx, width=0.5, color='b')
ax3 = fig.add_subplot(2, 2, 3)
ax3.title.set_text('英语')
plt.ylim(40, 100)
plt.bar(x, yy, width=0.5, color='deepskyblue')
ax4 = fig.add_subplot(2, 2, 4)
ax4.title.set_text('政治')
plt.ylim(40, 100)
plt.bar(x, zz, width=0.5)



ax1.set_xlabel('姓名')
ax2.set_xlabel('姓名')
ax3.set_xlabel('姓名')
ax4.set_xlabel('姓名')
ax1.set_ylabel('分数')
ax2.set_ylabel('分数')
ax3.set_ylabel('分数')
ax4.set_ylabel('分数')
fig.tight_layout()
# plt.show()

# print(st)
# fig, ax = plt.subplots(1,4, figsize= (12,8))
# for i in range(st.shape[1]):
#     ax[i] = st.iloc[:, i:(i+1)]
#     ax[1].bar(ax[i+1], ax[0], width=0.5)
#
#     plt.show()


fig, axes = plt.subplots(3, 3)
axes_list = []
for i in range(axes.shape[0]):
    for j in range(axes.shape[1]):
        axes_list.append(axes[i, j])

for ax in axes_list:
    ax.plot([1, 2, 3])
plt.show()