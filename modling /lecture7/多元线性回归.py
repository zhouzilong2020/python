from MLR import *
X = loadtxt(r"/Users/zhouzilong/Desktop/python/modling /lecture7/X.txt")
Y = loadtxt(r"/Users/zhouzilong/Desktop/python/modling /lecture7/Y.txt")
mlr = MLR(X, Y, intersect = False)
mlr._fit()
print(mlr.Ftest(0.05))
print(mlr.A)
