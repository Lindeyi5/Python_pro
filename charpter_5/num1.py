# 开发时间：2023-04-24 9:59
# 开发人员：林坚洪
# encodeing "UTF-8"

import warnings

warnings.filterwarnings('ignore')
import pandas as pd

data = pd.read_csv('input_data.csv')
print(data.head())

import matplotlib.pyplot as plt

X = data[["square_feet"]]
print(type(X), X)
y = data["price"]
print(type(y), y)

# fig, axes = plt.subplots(figsize=[5, 6])
# axes.scatter(X, y)
# plt.show()

from sklearn.linear_model import LinearRegression

linreg = LinearRegression()
model = linreg.fit(X, y)
print(model)
print()
print(linreg.intercept_)
print(linreg.coef_)
print(model.score(X, y))

plt.subplots(figsize=[6, 3])

plt.scatter(X, y, color='blue')
plt.plot(X, linreg.predict(X), color='red', linewidth=2)
# plt.show()

y_pred=linreg.predict([[700],[701],[800],[801]])
print(y_pred)
for i in y_pred:
    i=round(i,2)
    print(i)