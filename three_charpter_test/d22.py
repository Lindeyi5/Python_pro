# 开发时间：2023-03-13 11:19
# 开发人员：林坚洪
# encodeing "UTF-8"
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

# 船舱等级一共有3种，计算每一种船舱等级对应的平均票价
passenger_classes = ['1st', '2nd', '3rd']  # 列表：存放船舱等级
fares_by_class = {}  # 字典：存放船舱等级key以及对应的平均票价value
# 对每一类船舱进行循环
for this_class in passenger_classes:
    # 当this_class = 1时，返回的是所有一等舱的船客的信息
    # 当this_class = 2、3时，同理
    pclass_rows = s[s["pclass"] == this_class]
    # 再从每次取得的信息中，返回“Fare”(票价)这列的数据
    pclass_fares = pclass_rows["fare"]
    # .mean()：求平均票价
    fare_for_class = pclass_fares.mean()
    # 将平均票价value赋值给对应的船舱等级key
    fares_by_class[this_class] = fare_for_class

print("每类船舱对应的平均票价 = ", fares_by_class)
print('-' * 88)
print('每类船舱对应的平均存活率')
passenger_survical = cframe.pivot_table(index="pclass", values="survived", aggfunc=np.mean)#通过添加参数进行计数或求和
print(passenger_survical)
print('求每类船舱对应的平均年龄')
passenger_age = cframe.pivot_table(index="pclass", values="age", aggfunc=np.mean)
print(passenger_age)
print('-' * 88)
print('计算成年人和儿童死亡率')


def generate_age_label(row):
    age = row["age"]
    if pd.isnull(age):
        return "unknown"
    elif age < 18:
        return "minor"
    else:
        return "adult"


age_labels = cframe.apply(generate_age_label, axis=1)
print(age_labels)
s['age_labels'] = age_labels
age_group_survival = s.pivot_table(index="age_labels", values="survived")
print(age_group_survival)

plt.rcParams['axes.unicode_minus'] = False  # 处理无法显示中文的问题
plt.rcParams['font.sans-serif'] = ['SimHei']

fig = plt.figure(1, figsize=(6, 6))
ax1 = fig.add_subplot(1, 1, 1)
label = ['遇难', '存活']
color = ['#C23531', '#F5DEB3']
explode = 0.05, 0.05  # 扇区间隔

patches, l_text, p_text = ax1.pie(s.value_counts('survived', normalize=True), labels=label, colors=color, startangle=90,
                                  autopct='%1.0f%%',
                                  explode=explode, shadow=True)
for t in l_text:
    t.set_size(20)
for t in p_text:
    t.set_size(20)
ax1.set_title('全体成员的生存情况', fontsize=20)
plt.show()

fig = plt.figure(figsize=(15, 10))
fig.set(alpha=0.3)  # 设定图表颜色alpha参数(透明度)

plt.subplot2grid((2, 3), (0, 0))
cframe.survived.value_counts().plot(kind='bar')
plt.title("获救情况 (1为获救)")
plt.ylabel("人数")

plt.subplot2grid((2, 3), (0, 1))
cframe.pclass.value_counts().plot(kind="bar")
plt.ylabel("人数")
plt.title("乘客等级分布")

plt.subplot2grid((2, 3), (0, 2))
plt.scatter(cframe.survived, cframe.age)
plt.ylabel("年龄")
plt.grid( which='major', axis='y')
plt.title("按年龄看获救分布 (1为获救)")

plt.subplot2grid((2, 3), (1, 0), colspan=2)
cframe.age[cframe.pclass == '1st'].plot(kind='kde')
cframe.age[cframe.pclass == '2nd'].plot(kind='kde')
cframe.age[cframe.pclass == '3rd'].plot(kind='kde')
plt.xlabel("年龄")
plt.ylabel("密度")
plt.xlim(0, 90)
plt.title("各等级的乘客年龄分布")
plt.legend(('头等舱', '2等舱', '3等舱'), loc='best')

plt.subplot2grid((2, 3), (1, 2))
cframe.embarked.value_counts().plot(kind='bar')
plt.title("各登船口岸上船人数")
plt.ylabel("人数")
plt.show()