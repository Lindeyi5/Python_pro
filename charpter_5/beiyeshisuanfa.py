# 开发时间：2023-05-10 10:13
# 开发人员：林坚洪
# encodeing "UTF-8"
import sklearn.datasets
import matplotlib.pyplot as plt
X, y = sklearn.datasets.make_moons(200,noise=0.20,random_state=0)
# print(X,y)
from sklearn.model_selection import train_test_split
train_X,test_X,train_y,test_y=train_test_split(X,y,test_size=0.2,random_state=1)
from sklearn.naive_bayes import GaussianNB
model=GaussianNB()
model.fit(train_X,train_y)
expected=test_y
predicted=model.predict(test_X)
print('byes的准确率为：%.2f'%(model.score(train_X,train_y)*100))
from sklearn import metrics
print(metrics.classification_report(expected, predicted))
print(metrics.confusion_matrix(expected, predicted))

print('-'*99)

from sklearn.datasets import load_iris
iris_dataset=load_iris()
X=iris_dataset.data
y=iris_dataset.target
from sklearn.model_selection import train_test_split
train_X,test_X,train_y,test_y=train_test_split(X,y,test_size=0.20,random_state=1)
from sklearn.naive_bayes import GaussianNB
model = GaussianNB()
model.fit(train_X, train_y)
expected = test_y
predicted = model.predict(test_X)
print('准确率为：%.2f'%(model.score(train_X, train_y) *100))
from sklearn import metrics
print(metrics.classification_report(expected, predicted))
print(metrics.confusion_matrix(expected, predicted))