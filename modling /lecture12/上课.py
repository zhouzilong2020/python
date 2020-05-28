import numpy as np
from sklearn.model_selection import train_test_split
X = np.loadtxt(r"/Users/zhouzilong/Desktop/python/modling /lecture12/1x0.txt")
y = np.loadtxt(r"/Users/zhouzilong/Desktop/python/modling /lecture12/1y0.txt")

from pylab import *
plot(X[y==1,0],X[y==1,1],'b^')
plot(X[y!=1,0],X[y!=1,1],'ro')

Xtrain, Xtest, Ytrain, Ytest = train_test_split(X, y, test_size = 0.1)
Xmax = Xtrain.max(axis = 0)
Xmin = Xtrain.min(axis = 0)
Xtrain = (Xtrain - Xmin) / (Xmax - Xmin)

# 对y进行正交互化处理
Ylable = []
for i in range(len(Ytrain)):
    one = [0, 0]
    if Ytrain[i] == 0:
        one[0] = 1
    else:
        one[1] = 1
    Ylable.append(one)
Ylable = np.array(Ylable)

from NeuralNetwork import NeuralNetwork
        
nn = NeuralNetwork(layers = [Xtrain.shape[-1], 10, Ylable.shape[-1]])
nn.fit(Xtrain, Ylable)

Xtest = (Xtest - Xmin) / (Xmax - Xmin)
Yhat = nn.predict(Xtest)

# 分类结果
from sklearn.metrics import classification_report
print(classification_report(Ytest, Yhat))
