# 开发时间：2023-04-24 11:33
# 开发人员：林坚洪
# encodeing "UTF-8"
# 数据列分别代表 age,salary,isStudent,credit,isBuy
import warnings

warnings.filterwarnings("ignore")
dataSet = [[1, 3, 0, 1, 'no'],
           [1, 3, 0, 2, 'no'],
           [2, 3, 0, 1, 'yes'],
           [3, 2, 0, 1, 'yes'],
           [3, 1, 1, 1, 'yes'],
           [3, 1, 1, 2, 'no'],
           [2, 1, 1, 2, 'yes'],
           [1, 2, 0, 1, 'no'],
           [1, 1, 1, 1, 'yes'],
           [3, 2, 1, 1, 'yes'],
           [1, 2, 1, 2, 'yes'],
           [2, 2, 0, 2, 'yes'],
           [2, 3, 0, 1, 'yes'],
           [3, 2, 0, 2, 'no']]
print(dataSet)
FeatureSet = []
Label1 = ['age', 'salary', 'isStudent', 'credit', 'isBuy']
Label = []
for i in dataSet:
    FeatureSet.append(i[:-1])
    Label.append(i[-1])
print(FeatureSet)
print(Label)

dataSet1 = [[1, 2, 3, 4, 'no'],
            [5, 6, 7, 8, 'no'],
            [9, 10, 11, 12, 'yes'],
            [13, 14, 15, 16, 'yes']]

print(dataSet1)
print(dataSet1[1:])

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(FeatureSet, Label, random_state=1)
print(X_train)
print(y_train)
print('*' * 78)

from sklearn.tree import DecisionTreeClassifier

clf = DecisionTreeClassifier(random_state=1)
# 默认的是基于 Gini 不纯度分类，基尼系数是一种评估数据集分割点优劣的成本函数
clf = clf.fit(X_train, y_train)
print(clf.feature_importances_)
pre_labels = clf.predict(X_test)
print(pre_labels)
print('决策树的准确率为：%.2f' % (clf.score(X_test, y_test) * 100))
from sklearn.metrics import classification_report

print(classification_report(y_test, pre_labels))

from sklearn.tree import export_graphviz
from pydotplus import graph_from_dot_data

features_4 = ['age', 'salary', 'isStudent', 'credit']
dot_data = export_graphviz(clf, feature_names=features_4, filled=True, rounded=True)
graph = graph_from_dot_data(dot_data)
graph.write_png("tree_credit.png")

import matplotlib.pyplot as plt

img = plt.imread('tree_credit.png')
fig = plt.figure(figsize=(9, 6))
plt.imshow(img)
plt.axis('off')
plt.show()
