# 开发时间：2023-03-15 9:15
# 开发人员：林坚洪
# encodeing "UTF-8"
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
st = pd.read_excel('student.xlsx')
fig = plt.figure(figsize=(10, 6))
ax1=['skyblue',]
print(st.shape)
print(st.shape[0])
print(st.shape[1])
print(st.columns[1])
# for i in range(st.shape[1]):
#     print(st.columns[i])
#     print(st[st.columns[i]])
#     print(i)
    # ax1[i] = fig.add_subplot(2, 2, 1)
    # plt.bar(1,2)
#plt.show()