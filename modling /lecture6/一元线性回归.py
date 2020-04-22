import numpy as np

data = np.loadtxt(r"/Users/zhouzilong/Desktop/python/modling /lecture6/data.txt")
x = data[: , 0:]
y = data[: , 1:]
ones = np.ones(len(x))
# 左边加一

X = np.c_[ones, x]

Xt = X.T
X_1 = (Xt*X).linalg.
