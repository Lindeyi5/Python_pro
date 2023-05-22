# 开发时间：2023-04-27 11:03
# 开发人员：林坚洪
# encodeing "UTF-8"
# import warnings
#
# warnings.filterwarnings("ignore")
# dataSet = [[1, 3, 0, 1, 'no'],
#            [1, 3, 0, 2, 'no'],
#            [2, 3, 0, 1, 'yes'],
#            [3, 2, 0, 1, 'yes'],
#            [3, 1, 1, 1, 'yes'],
#            [3, 1, 1, 2, 'no'],
#            [2, 1, 1, 2, 'yes'],
#            [1, 2, 0, 1, 'no'],
#            [1, 1, 1, 1, 'yes'],
#            [3, 2, 1, 1, 'yes'],
#            [1, 2, 1, 2, 'yes'],
#            [2, 2, 0, 2, 'yes'],
#            [2, 3, 0, 1, 'yes'],
#            [3, 2, 0, 2, 'no']]
# print(dataSet)
# FeatureSet = []
# Label1 = ['age', 'salary', 'isStudent', 'credit', 'isBuy']
# Label = []
# for i in dataSet:
#     FeatureSet.append(i[:-1])
#     Label.append(i[-1])
# print(FeatureSet)
# print(Label)
#
# dataSet1 = [[1, 2, 3, 4, 'no'],
#             [5, 6, 7, 8, 'no'],
#             [9, 10, 11, 12, 'yes'],
#             [13, 14, 15, 16, 'yes']]
#
# print(dataSet1)
# print(dataSet1[1:])
#
# from sklearn.model_selection import train_test_split
#
# X_train, X_test, y_train, y_test = train_test_split(FeatureSet, Label, random_state=1)
# print(X_train)
# print(y_train)
# print('*' * 78)
#
# from sklearn.tree import DecisionTreeClassifier
#
# clf = DecisionTreeClassifier(random_state=1)
# # 默认的是基于 Gini 不纯度分类，基尼系数是一种评估数据集分割点优劣的成本函数
# clf = clf.fit(X_train, y_train)
# print(clf.feature_importances_)
# pre_labels = clf.predict(X_test)
# print(pre_labels)
# print('决策树的准确率为：%.2f' % (clf.score(X_test, y_test) * 100))
# from sklearn.metrics import classification_report
#
# print(classification_report(y_test, pre_labels))
#
# from sklearn.tree import export_graphviz
# from pydotplus import graph_from_dot_data
#
# features_4 = ['age', 'salary', 'isStudent', 'credit']
# dot_data = export_graphviz(clf, feature_names=features_4, filled=True, rounded=True)
# graph = graph_from_dot_data(dot_data)
# graph.write_png("tree_credit.png")
#
# import matplotlib.pyplot as plt
#
# img = plt.imread('tree_credit.png')
# fig = plt.figure(figsize=(9, 6))
# plt.imshow(img)
# plt.axis('off')
# plt.show()




import matplotlib.pyplot as plt

import warnings

warnings.filterwarnings("ignore")
import pandas as pd

data = pd.read_csv('bankloan.csv')
# print(data.head())
dataList = data.values.tolist()
# print(dataList)

FeatureSet = []
# '（age）、教育程度（ed）、雇员年限（employ）、居住年限（address）、收入（income）、收入
# 债务比（debtinc）、信用卡债务比（creddebt）、其它债务比（othdebt）、是否违约（default），'

Label1 = ['age','ed','employ','address','income','debtinc','creddebt','othdebt','default']
Label=[]
for i in dataList:
    FeatureSet.append(i[:-1])
    Label.append(i[-1])
# print(FeatureSet)
# print(Label)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(FeatureSet, Label, random_state=1,test_size=0.2)
# print(X_train)
# print(y_train)

from sklearn.tree import DecisionTreeClassifier

clf = DecisionTreeClassifier(criterion='gini',random_state=1,max_depth=6,min_samples_leaf=4)
# 默认的是基于 Gini 不纯度分类，基尼系数是一种评估数据集分割点优劣的成本函数
clf = clf.fit(X_train, y_train)
print(clf.feature_importances_)
pre_labels = clf.predict(X_test)
print(pre_labels)
print('决策树的训练集准确率为：%.2f' % (clf.score(X_train, y_train) * 100))
print('决策树的测试集准确率为：%.2f' % (clf.score(X_test, y_test) * 100))



# test=[]
# Xtrain,Xtest,Ytrain,Ytest=train_test_split(FeatureSet, Label,test_size=0.3)
# for i in range(10):
#     clf=DecisionTreeClassifier(criterion="gini"
#                                 ,random_state=30
#
#                                 ,max_depth=i+1
#                                # ,min_samples_leaf=10
#                                 #,min_samples_split=10
#     )
#     clf=clf.fit(Xtrain,Ytrain)
#     score=clf.score(Xtest,Ytest)
#     test.append(score)
# plt.plot(range(1,11),test,color="red",label="max_depth")
# plt.legend()
# plt.show()





from sklearn.metrics import classification_report

print(classification_report(y_test, pre_labels))

from sklearn.tree import export_graphviz
from pydotplus import graph_from_dot_data

features_4 = ['age','ed','employ','address','income','debtinc','creddebt','othdebt']
dot_data = export_graphviz(clf, feature_names=features_4, filled=True, rounded=True)
graph = graph_from_dot_data(dot_data)
graph.write_png("tree_credit.png")



img = plt.imread('tree_credit.png')

# fig = plt.figure(figsize=(9, 6))
# plt.imshow(img)
# plt.axis('off')
# plt.show()

from sklearn.tree import export_graphviz
from pydotplus import graph_from_dot_data


# for rows in data.iloc[:,:-1]:
#     print(data[rows])
#     for i in range(1,data.__len__()):
#     print(' '.join(data[rows]))
#     # for i in data:
#     #     print(data[rows])


# FeatureSet = []
# Label = []
# ajidajda=[]
# for i in data:
#     lisr = list(data[i])
#     # print(data[i])
#     ajidajda.append(i)
#     FeatureSet.append(data[i])
#     # Label.append(i[-1])
# print(FeatureSet)
# print(ajidajda)
# print(lisr)
# # print(Label)
