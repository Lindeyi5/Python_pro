# 开发时间：2023-03-08 22:45
# 开发人员：林坚洪
# encodeing "UTF-8"
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

s = pd.read_csv('titanic.csv')
print('查看数据缺失值', s.isnull().sum())
print('显示数据前5行', s.head().to_string())
print('显示数据行数和列数', s.shape)
print('-' * 88)
print('计算基本的统计数据', s.describe(include='all').to_string())
print('生存比例', s.value_counts('survived', normalize=True))
print('-' * 88)
print('年龄最大前5位', s.sort_values(by='age', ascending=False).head().to_string())
# print(s['sex'].isnull())
# print(s['age'].isnull())
cframe = s[s.age.notnull()]  # 过滤掉年龄为空的数据
print('计算过滤后基本的统计数据', cframe.describe(include='all').to_string())
print('计算过滤后平均年龄', round(cframe['age'].mean(), 2))
print('-' * 88)

# 未过滤数据时计算船舱等级对应的平均票价
Class_of_cabin = ['1st', '2nd', '3rd']  # 列表：存放船舱等级
key_value = {}  # 字典：存放船舱等级key以及对应的平均票价value
# 对每一类船舱进行循环
for this_class in Class_of_cabin:
    pclass_all = s[s["pclass"] == this_class]  # 遍历所有舱的船客的信息
    pclass_fares = pclass_all["fare"]  # 再从每次取得的信息中，返回fare(票价)这列的数据
    average_fares = pclass_fares.mean()  # 求平均票价
    key_value[this_class] = round(average_fares, 2)  # 将平均票价value赋值给对应的船舱等级key

print("每类船舱对应的平均票价 = ", key_value)
# aggfunc：聚合函数， pivot_table后新dataframe的值都会通过aggfunc进行运算。
# 在pivot_table会将多重值调用aggfunc函数后放在相应的位置上。
passenger_fare = cframe.pivot_table(index="pclass", values="fare", aggfunc=np.mean)  # 通过添加参数进行计数或求和
print(passenger_fare)
print('-' * 88)
print('每类船舱对应的平均存活率')
passenger_survival = cframe.pivot_table(index="pclass", values="survived", aggfunc=np.mean)  # 通过添加参数进行计数或求和
print(passenger_survival)
print('求每类船舱对应的平均年龄')
passenger_age = cframe.pivot_table(index="pclass", values="age", aggfunc=np.mean)
print(passenger_age)
print('-' * 88)

print('计算成年人和儿童死亡率')


def age_label(row):
    age = row["age"]
    if pd.isnull(age):
        return "unknown"
    elif age < 18:
        return "minor"
    else:
        return "adult"


# apply作用在一行或者是一列上的函数。对矩阵或数组进行计算，一行或一列地运行
age_labels = cframe.apply(age_label, axis=1)
print(age_labels)
s['age_labels'] = age_labels
age_group_survival = s.pivot_table(index="age_labels", values="survived")
print(age_group_survival)

plt.rcParams['axes.unicode_minus'] = False  # 处理无法显示中文的问题
plt.rcParams['font.sans-serif'] = ['SimHei']

fig = plt.figure(1, figsize=(8, 8))
ax1 = fig.add_subplot()
label = ['遇难人员', '存活人员']
color = ['pink', 'deepskyblue']
explode = 0.05, 0.05  # 扇区间隔

# patches 绘制饼图每一块的对象
# texts 文本的列表
# autotexts 百分比的文本列表
patches, label_text, p_text = ax1.pie(s.value_counts('survived', normalize=True),
                                      labels=label, colors=color,
                                      startangle=90,  # 从哪个角度开始
                                      autopct='%.2f%%',  # 保留小数
                                      explode=explode,  # 设置扇区间隔
                                      shadow=True)
for t in label_text:
    t.set_size(20)
for t in p_text:
    t.set_size(30)
ax1.set_title('全体成员的生存情况', fontsize=20)
plt.show()

fig = plt.figure(figsize=(10, 6))

plt.subplot2grid((1, 2), (0, 0))
plt.bar(label, cframe.survived.value_counts(), width=.5)
plt.title("获救情况")
plt.ylabel("人数")

plt.subplot2grid((1, 2), (0, 1))
cframe.pclass.value_counts().plot(kind="bar")
plt.ylabel("人数")
plt.title("不同船舱等级人员分布")
plt.show()

fig = plt.figure(figsize=(10, 6))
plt.subplot2grid((1, 2), (0, 0))
plt.scatter(cframe.survived, cframe.age)
plt.ylabel("年龄")
plt.grid(axis='y')
plt.title("按年龄看获救情况")

plt.subplot2grid((1, 2), (0, 1))
cframe.embarked.value_counts().plot(kind='bar')
plt.title("各登船口岸上船人数")
plt.ylabel("人数")
plt.show()

fig = plt.figure(figsize=(10, 6))
plt.subplot2grid((1, 2), (0, 0), colspan=2)
cframe.age[cframe.pclass == '1st'].plot(kind='kde')  # 密度图 KDE,
cframe.age[cframe.pclass == '2nd'].plot(kind='kde')
cframe.age[cframe.pclass == '3rd'].plot(kind='kde')
plt.xlabel("年龄")
plt.ylabel("密度")
plt.xlim(0, 90)
plt.title("各等级的乘客年龄分布")
plt.legend(('1等舱', '2等舱', '3等舱'), loc='best')
plt.show()
