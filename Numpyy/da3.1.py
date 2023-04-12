# 开发时间：2023-02-27 10:02
# 开发人员：林坚洪
# encodeing "UTF-8"
import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([(1.2, 32, 23), (21, 23, 4.4)])
arr3 = np.zeros((2, 3))
print(arr1)
print(arr2)
print(arr3)

arr4 = np.identity(3)
print(arr4)
arr5 = np.random.random(size=(2, 3))
print(arr5)
arr6 = np.arange(5, 20, 3)
print(arr6)
arr7 = np.linspace(1, 2, 5)
print(arr7)
print(arr2.shape)
print(arr1.shape)
print(arr2.ndim)
print(arr2.size)
print(arr2.dtype.name)
print(arr1.dtype.name)
print(type(arr2))
print(type(arr1))
print(arr1.ndim)




def f(x, y):
    return 10 * x + y


arr8 = np.fromfunction(f, (4, 3), dtype=int)
print(arr8)
print(arr8[1:3, :-1])
print(arr8[1:3, 0:-1])

print(arr8[:-2, 0:4])
print(arr8[:, 1:])
b = np.arange(12).reshape(3, 4)
print(b)
arr9 = np.array([[2, 3], [1, 4]])
arr10 = np.array([[1, 2], [3, 4]])
print(arr9, '\n' * 2, arr10)
print(arr9 - arr10)
print(arr9 * arr10)
print(np.dot(arr9, arr10))
print(arr9.T)
print(np.linalg.inv(arr10))
print(arr10.sum())
print(arr10.max())
print(arr10.cumsum(axis=0))
print(np.exp(arr10))
print(np.sin(arr10))
print(np.sqrt(arr10))
print(np.add(arr9, arr10))
print(np.vstack((arr9, arr10)))
print(np.hstack((arr9, arr10)))
print(np.hsplit(np.hstack((arr9, arr10)),2))
print(np.vsplit(np.vstack((arr9, arr10)),2))



##print('练习3,4')
##xx = np.array([[2, 0, -1.4], [2.2, 0.2, -1.5], [2.4, 0.1, -1], [1.9, 0, -1.2]])
##print(xx)
##print(xx.T)
##print(np.linalg.inv(xx))
##print(xx.max())
##print(xx.min())
##print(xx.cumsum(axis=0))
##print(xx.cumsum(axis=1))

a1=np.array([1,1,2])
print(a1.ndim)
a1=np.array([[[1,1,1],[1,2,3],[1,1,1],[1,2,3]],[[1,1,1],[1,2,3],[1,1,1],[1,2,3]]])
print(a1.ndim)
#arr99=np.array([(1.2,32,33,23),(21,23,4.4)],[(1.2,32,33,23),(21,23,4.4)])
#print(arr99.ndim)