# 开发时间：2023-03-10 20:49
# 开发人员：林坚洪
# encodeing "UTF-8"
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
st = pd.read_excel('student.xlsx')
name_obj = []
for i in range(st.shape[1]):
    name_obj.append(st[st.columns[i]].values.T.tolist())  # 将每一列提取出来放入列表中
    print(name_obj[i])
fig = plt.figure(figsize=(10, 7))
ax = [0 for x in range(0, st.shape[1]-1)]
color=['lightblue','skyblue','deepskyblue','b']
for i in range(len(ax)):  # i=0,1,2,3
    ax[i] = fig.add_subplot(2, 2, (i + 1))
    ax[i].title.set_text(st.columns[i + 1])
    ax[i].set_xlabel('姓名')
    ax[i].set_ylabel('分数')
    plt.bar(name_obj[0], name_obj[i + 1], width=0.5, color=color[i])
    plt.ylim(40, 100)
fig.tight_layout()
plt.show()
