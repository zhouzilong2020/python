import numpy as np
# delimiter = '' 列合理额之间的分割
# 求每一行
# np.sum(axis=1)
# 求每一列
# np.sum(axis=0)

x = np.loadtxt(r'/Users/zhouzilong/Desktop/python/modling /lecture6/wheat_X.txt')
mean = x.mean(axis=0)
print(mean)

# 两个维度分片
x[1:3, 1:3]

# 得到的是向量
x[:, 1]
# 得到的是二维矩阵
x[:, 1:2]

# 支持矩阵和向量进行操作，矩阵的每一列和每一行进行分别的操作

y = np.array([[1.1, 2.4], [2.7, 5.7]])
yhat = np.array([[1.3, 5.1], [2.6, 5.6]])
error = np.abs(y-yhat)/yhat
print(error)