import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier

X = np.loadtxt(r"/Users/zhouzilong/Desktop/python/modling /lecture12/1x1.txt")
y = np.loadtxt(r"/Users/zhouzilong/Desktop/python/modling /lecture12/1y1.txt")

from pylab import *
Xtrain, Xtest, Ytrain, Ytest = train_test_split(X, y, test_size = 0.1)
Xmax = Xtrain.max(axis = 0)
Xmin = Xtrain.min(axis = 0)


Xtrain = (Xtrain - Xmin) / (Xmax - Xmin)
Xtest = (Xtest - Xmin) / (Xmax - Xmin)
X = (X - Xmin) / (Xmax - Xmin)

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

# alpha正则化系数，防止过拟合
clf=MLPClassifier( hidden_layer_sizes=(100,), alpha=1e-5,\
                    max_iter = 5000,\
                    random_state=1,\
                    verbose = False)  # 很多参数
clf.fit(Xtrain, Ylable)
Yhat = clf.predict(Xtest)
Ypredict = Yhat.argmax(axis = 1)
print(Ypredict)
print(Ytest)
from sklearn.metrics import classification_report
print(classification_report(Ytest, Ypredict))

# score = clf.score(Xtest, Ylable)  #预测得分，准确率
# yhat=clf.predict(Xtest)  # 预测值
prob=clf.predict_proba(Xtest) # 预测概率


x_min = X[:, 0].min() - .5
x_max = X[:, 0].max() + .5
y_min = X[:, 1].min() - .5
y_max = X[:, 1].max() + .5
h = .2  
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
from matplotlib import pyplot as plt
from matplotlib.colors import ListedColormap
cm = plt.cm.Accent
cm_bright = ListedColormap(['#FF0000', '#0000FF'])

Z = clf.predict_proba(np.c_[xx.ravel(), yy.ravel()]) [:, 1] 
# 选择第一类的概率输出
# 制作概率的等高线图
Z = Z.reshape(xx.shape)

CS = plt.contour(xx,yy, Z, 4, colors='k',)              
plt.clabel(CS, fontsize=12, inline=1)
# 画训练集点
plt.scatter(Xtrain[:, 0], Xtrain[:, 1], c=Ytrain, cmap=cm_bright, edgecolors='black', s=25)
# 画测试集点 
plt.scatter(Xtest[:, 0], Xtest[:, 1], c=Ytest, cmap=cm_bright, alpha=0.3, edgecolors='black', s=25)

# plt.xlim(xx.min(), xx.max())
# plt.ylim(yy.min(), yy.max())

plt.show()
