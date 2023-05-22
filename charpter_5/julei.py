# 开发时间：2023-05-10 10:32
# 开发人员：林坚洪
# encodeing "UTF-8"
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs

X, y = make_blobs(n_samples=1000, n_features=2,
                  centers=[[-1, -1], [0, 0], [1, 1], [2, 2]],
                  cluster_std=[0.1, 0.1, 0.1, 0.1],
                  random_state=9)
plt.scatter(X[:, 0], X[:, 1], marker='o')
plt.show()
print(X)

from sklearn.cluster import KMeans

y_pred = KMeans(n_clusters=2, random_state=9, n_init=2).fit_predict(X)
plt.scatter(X[:, 0], X[:, 1], c=y_pred)
plt.show()
from sklearn import metrics
print(metrics.calinski_harabasz_score(X, y_pred))  # 3116.17067633

y_pred = KMeans(n_clusters=3, random_state=9, n_init=2).fit_predict(X)
plt.scatter(X[:, 0], X[:, 1], c=y_pred)
plt.show()
print(metrics.calinski_harabasz_score(X, y_pred))  # 2931.6250302

y_pred = KMeans(n_clusters=4, random_state=9, n_init=2).fit_predict(X)
plt.scatter(X[:, 0], X[:, 1], c=y_pred)
plt.show()
print(metrics.calinski_harabasz_score(X, y_pred))

y_pred = KMeans(n_clusters=5, random_state=9, n_init=2).fit_predict(X)
plt.scatter(X[:, 0], X[:, 1], c=y_pred)
plt.show()
print(metrics.calinski_harabasz_score(X, y_pred))  # 5924.05061348

y_pred = KMeans(n_clusters=9, random_state=9, n_init=2).fit_predict(X)
plt.scatter(X[:, 0], X[:, 1], c=y_pred)
plt.show()
print(metrics.calinski_harabasz_score(X, y_pred))  # 5924.05061348

SSE = []  # 存放每次结果的误差平方和
for k in range(1, 10):
    estimator = KMeans(n_clusters=k, n_init=2)  # 构造聚类器
    estimator.fit(X)
    SSE.append(estimator.inertia_)
x = range(1, 10)
plt.xlabel('k')
plt.ylabel('SSE')
plt.plot(x, SSE, 'o-')
plt.show()
