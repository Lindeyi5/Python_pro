# 开发时间：2023-05-22 10:08
# 开发人员：林坚洪
# encodeing "UTF-8"
import pandas as pd

data = pd.read_csv('sales.csv', encoding='utf-8')
print(data.head(5))
print(data.describe(include='all'))
print(data.shape)

import matplotlib.pyplot as plt

plt.hist(data['mj'].dropna(), bins=60)  # bins 制定直方图中条形的个数
# plt.show()

plt.boxplot(data['mj'].dropna())
# plt.show()

X = data[['qy', 'fx', 'mj', 'jg']]
y = data['lb']
from sklearn.model_selection import train_test_split

train_X, test_X, train_y, test_y = train_test_split(X, y, test_size=0.2, random_state=1)
print(train_X.shape, train_y.shape)
print(test_X.shape, test_y.shape)

mj_train_na = pd.isnull(train_X['mj'])
mj_test_na = pd.isnull(test_X['mj'])
print(mj_train_na)
print(mj_test_na)

train_X = train_X.values
test_X = test_X.values
train_X_copy = train_X.copy()

from sklearn.impute import SimpleImputer

imp = SimpleImputer(strategy='mean')

imp.fit(train_X[:, [2]])
train_X[:, [2]] = imp.transform(train_X[:, [2]])
print(train_X[:])
test_X[:, [2]] = imp.transform(test_X[:, [2]])

from sklearn.preprocessing import LabelEncoder

print(train_X[:5, 0])
print(train_X[:5, 1])

le_qy = LabelEncoder()
le_qy.fit(train_X[:, 0])
train_X[:, 0] = le_qy.transform(train_X[:, 0])
le_fx = LabelEncoder()
le_fx.fit(train_X[:, 1])
train_X[:, 1] = le_fx.transform(train_X[:, 1])
print(train_X[:5])

qy = train_X[:, 0]
fx = train_X[:, 1]
mj = train_X[:, 2]
jg = train_X[:, 3]
lb = train_y
fig, axes = plt.subplots(1, 4, figsize=[12, 3])
axes[0].scatter(qy, lb)
axes[1].scatter(fx, lb)
axes[2].scatter(mj, lb)
axes[3].scatter(jg, lb)
# plt.show()
