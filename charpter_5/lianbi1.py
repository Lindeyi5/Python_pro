# 开发时间：2023-04-26 10:49
# 开发人员：林坚洪
# encodeing "UTF-8"
import pandas as pd

data_dum = pd.read_csv('watermelon.csv')
# print(data_dum.head())

from sklearn.model_selection import train_test_split

X = data_dum.iloc[:, :-1]
y = data_dum.iloc[:, -1]
# print(X, y)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=False)
print(X_train.shape)
print(y_train.shape)
print(X_test.shape)
print(y_test.shape)


from sklearn.linear_model import LogisticRegression

lr = LogisticRegression(solver='liblinear')  # 建立模型
lr.fit(X_train, y_train)  # 用处理好的数据训练模型
print(lr)
print(lr.intercept_)
print(lr.coef_)

print('逻辑回归的准确率为：%.2f' % (lr.score(X_test, y_test) * 100))
from sklearn.metrics import classification_report

y_true, y_pred = y_test, lr.predict(X_test)
print(classification_report(y_true, y_pred))
