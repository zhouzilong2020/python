import numpy as np
from sklearn.cross_decomposition import PLSRegression
from sklearn import datasets

iris=datasets.load_iris() # 从数据库获得数据
data=iris.data #获得自变量数据
target=iris.target  # 获得样本的分类信息

# 选择两类
x=data[target!=2]
y=target[target!=2]
y[y==0]=-1

# 分割训练集
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=.2)

pls = PLSRegression(n_components=2, scale=False)
pls.fit(X_train, y_train)
T=pls.x_scores_

# 对训练集合聚类画图
import matplotlib.pyplot as plt
plt.plot(T[y_train!=1,0],T[y_train!=1,1],'yo')
plt.plot(T[y_train==1,0],T[y_train==1,1],'ro')

# 转换预报集，首先减去训练集的方差
aver= X_train.mean(axis = 0)
X_test -= aver

# 测试集合的得分
Tpred=None
for i in range(2):
    t = X_test.dot(pls.x_weights_[ : , i])
    if Tpred is None:
        Tpred = t
    else:
        Tpred = np.c_[Tpred,t]
    X_test = X_test-np.outer(t, pls.x_loadings_[ : , i])

# 画出测试集合的预测图
plt.scatter(Tpred[:, 0], Tpred[:, 1], c = y_test,  edgecolors = 'black', s = 25)
plt.show()

