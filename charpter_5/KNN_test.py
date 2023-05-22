# 开发时间：2023-05-06 10:10
# 开发人员：林坚洪
# encodeing "UTF-8"
import sklearn.datasets
import matplotlib.pyplot as plt
X, y = sklearn.datasets.make_moons(200, noise=0.20,random_state=0)
# print(X,y)
plt.scatter(X[:,0], X[:,1], s=40, c=y) #s 设置点的大小，c 设置颜色
plt.show()
print('*'*89)
from sklearn import preprocessing
normalized_X = preprocessing.normalize(X)
print(normalized_X[:5])

from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier(n_estimators=100)
clf.fit(X,y)
print(clf.feature_importances_)

from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier( n_neighbors=15)
model.fit(X, y)
from sklearn import metrics
from sklearn.metrics import classification_report
y_true, y_pred = y, model.predict(X)
print(classification_report(y_true, y_pred))
print(metrics.confusion_matrix(y_true, y_pred))
# import sklearn.datasets
# import matplotlib.pyplot as plt
# X, y = sklearn.datasets.make_moons(200, noise=0.20,random_state=0)
# # print(X,y)
# from sklearn.model_selection import train_test_split
# X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=0)
# from sklearn import metrics
# from sklearn.svm import SVC
# model = SVC(gamma='auto')
# model.fit(X_train, y_train)
# print('SVC 的准确率为：%.2f'%(model.score(X_train, y_train) *100))
# expected = y_test
# predicted = model.predict(X_test)
# # summarize the fit of the model
# print(metrics.classification_report(expected, predicted))
# print(metrics.confusion_matrix(expected, predicted))