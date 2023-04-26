# 开发时间：2023-04-24 10:38
# 开发人员：林坚洪
# encodeing "UTF-8"
import pandas as pd

data = pd.read_csv('Advertising.csv')
print(data.head())

import matplotlib.pyplot as plt

# fig, axes = plt.subplots(1, 3, figsize=(12, 4))
# for n in range(3):
#     print(data.iloc[:, n + 1], data.iloc[:, 4])
#     axes[n].scatter(data.iloc[:, n + 1], data.iloc[:, 4])
# plt.show()

feature_cols = ['TV', 'Radio', 'Newspaper'] #指定特征列表
X = data[feature_cols] #提取特征列表数据
print(X.head())
y = data['Sales'] #等价 y = data.Sales
print(y.head())

from sklearn.model_selection import train_test_split
X_train,X_test, y_train, y_test = train_test_split(X, y, random_state=0)
# random_state 参数设定随机种子，以保证每次实验的一致性
print(X_train.shape)
print(y_train.shape)
print(X_test.shape)
print(y_test.shape)

from sklearn.linear_model import LinearRegression
linreg = LinearRegression()
model=linreg.fit(X_train, y_train)
print(model)
print(linreg.intercept_)
print(linreg.coef_)
print(model.score(X_train,y_train)) # 0.890307557756
y_pred = linreg.predict(X_test)
print(y_pred.round(2))

plt.plot(range(len(y_pred)),y_pred,'-',label="predict") #预测结果用实线表示
plt.plot(range(len(y_pred)),y_test,'--',label="test") #实际结果用虚线表示
plt.legend(loc="upper right") #显示图中的标签
plt.xlabel("the number of sales")
plt.ylabel('value of sales')
plt.show()