# 开发时间：2023-05-08 10:55
# 开发人员：林坚洪
# encodeing "UTF-8"
import sklearn.datasets
import matplotlib.pyplot as plt

X, y = sklearn.datasets.make_moons(200, noise=0.20, random_state=0)
print(X, y)
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)
# from sklearn.linear_model import LogisticRegression
#
# clf = LogisticRegression(solver='lbfgs')  # 建立 LR 模型
# clf.fit(X_train, y_train)
# print('逻辑回归的准确率为：%.2f' % (clf.score(X_train, y_train) * 100))
# from sklearn.metrics import classification_report
#
# y_true, y_pred = y_test, clf.predict(X_test)
# print(classification_report(y_true, y_pred))


from sklearn.neural_network import MLPClassifier # MLP（Multi-layer Perceptron）
clf = MLPClassifier(solver='lbfgs',hidden_layer_sizes=(3), random_state=0)
'''
batch参数用来指定mini-batch sgd优化器的样本批量大小，默认值为200(如样本数低于200，则为样本数)。

max_iter用来指定神经网络的最大迭代次数，默认值为200。

random_state用来指定随机种子，用来控制模型初始权重的随机性。如果给定特定值，重新跑模型的时候，可以得出同样的结果。

tol参数用于指定优化器的忍耐度。当损失函数的值的变化小于了忍耐度，便认为训练结束，从而停止训练。默认值为1e-4。

momentum参数用于指定随机梯度下降优化器的动量，其值介于0到1之间。该参数仅在优化器为sgd的情形下有效。

activation用来指定激活函数。

activation = identity，使用f(x) = x的激活函数
activation = logistic，使用f(x) = 1 / (1 + exp(-x))的激活函数，又名sigmoid激活函数。
activation = tanh，使用双曲正切激活函数。
activation = relu，使用整流线性单元激活函数。（默认值）
solver用来指定优化器。

solver = lbfgs,使用拟牛顿法作为优化器。
solver = sgd,使用随机梯度下降优化器。
solver = adam，使用adam优化器。（默认值）
learning_rate参数用来指定学习率的模式。

learning_rate = constant，即使用常数作为学习率。用learning_rate_init参数来设置其值。(默认值)
learning_rate = invscaling，使用一种逐渐自动下降的学习率。在训练的第t步，学习率会变为learning_rate_init / pow(t, power_t)。其中power_t可以手动设定，其默认值为0.5。
learning_rate = adaptive，使用自适应的学习率，当误差函数变化很小时，就会降低学习率。
learning_rate_init 用来指定学习率，默认值为0.001。

hidden_layer_sizes用于指定网络架构，输入形式为元组，元组长度表示架构的层数，元组第i个数表示第i层的神经元个数。例如hidden_layer_sizes = “512-512-64”表示该多层感知机会用三个隐藏层，神经元数量分别为512，512，64。
默认值为100，表示只用一个100个神经元的隐藏层。

power_t。该参数仅当learning_rate = invscaling时有效，其作用见learning_rate参数下invscaling取值时的说明。默认值为0.5。
'''
clf.fit(X_train, y_train)
print('神经网络的准确率为：%.2f'%(clf.score(X_train, y_train) *100))
from sklearn.metrics import classification_report
y_true, y_pred = y_test, clf.predict(X_test)
print(classification_report(y_true, y_pred))
from sklearn import metrics
print(metrics.confusion_matrix(y_true, y_pred))

print(clf.get_params())

param_grid = {'hidden_layer_sizes':[3,5,10,12,15]}
import pandas as pd
from sklearn.model_selection import train_test_split, KFold, GridSearchCV
kf = KFold(n_splits=3, shuffle=True, random_state=123)
gs= GridSearchCV(clf, param_grid, cv = kf, return_train_score=True)
gs.fit(X, y)
cv_results = pd.DataFrame(gs.cv_results_)
#print(cv_results)
print(gs.best_estimator_)

clf=gs.best_estimator_
clf.fit(X_train, y_train)
print('神经网络的准确率为：%.2f'%(clf.score(X_train, y_train) *100))
from sklearn.metrics import classification_report
y_true, y_pred = y_test, clf.predict(X_test)
print(classification_report(y_true, y_pred))


from sklearn import metrics
print(metrics.confusion_matrix(y_true, y_pred))
X1=[[1.445,0.344]]
print(clf.predict(X1)) #[1]
import sklearn.datasets
X, y = sklearn.datasets.make_moons(200, noise=0.20,random_state=0)
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=0)
from sklearn import linear_model, metrics
from sklearn.neural_network import BernoulliRBM
rbm=BernoulliRBM(
n_components=3,learning_rate=0.1,batch_size=10, n_iter=10, random_state=9)
rbm.fit(X, y)
from sklearn.metrics import classification_report
y_true, y_pred = y, rbm.predict(X)
print(classification_report(y_true, y_pred))
from sklearn import linear_model, metrics
from sklearn.neural_network import BernoulliRBM
from sklearn.pipeline import Pipeline
logistic = linear_model.LogisticRegression(solver='lbfgs',max_iter=3000)
rbm = BernoulliRBM(random_state=0, verbose=True)
classifier = Pipeline(steps=[('rbm', rbm), ('logistic', logistic)])
rbm.learning_rate = 0.08
rbm.n_iter = 50
# n_components 值越大，性能越好，但计算量也越大
rbm.n_components = 200
logistic.C =50000
classifier.fit(X_train, y_train)
print('BP 神经网络的准确率为：%.2f'%(classifier.score(X_train, y_train) *100))
print("Logistic regression using RBM features:\n%s\n" %
(metrics.classification_report(y_test,classifier.predict(X_test))))
print(metrics.confusion_matrix(y_test, classifier.predict(X_test)))