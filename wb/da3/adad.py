# 开发时间：2023-03-06 21:38
# 开发人员：林坚洪
# encodeing "UTF-8"
from pylab import *

n = 1024
X = np.random.normal(0,1,n)
Y = np.random.normal(0,1,n)

scatter(X,Y)
show()