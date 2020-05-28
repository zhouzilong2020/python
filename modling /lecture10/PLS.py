import numpy as np
from sklearn.cross_decomposition import PLSRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

class PLS_DA:
    def __init__(self, tt_ratio, n_components, scale):
        self.tt_ratio = tt_ratio
        self.n_components = n_components
        self.scale = scale
        self.pls = PLSRegression(n_components = n_components, scale = scale)
        self.color = ['r', 'c', 'y', 'm', 'k']
        self.type = ['o', 'o', ',', 'v', '<', '>']

    def fit(self, X, Y, flag = True):
        # 划分训练集合
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, Y, test_size=self.tt_ratio)
        self.pls.fit(self.X_train, self.y_train)

    # cls为分类标准
    def plotTrainTest(self, cls):
        T = self.pls.x_scores_
        # 为每一种分组画图
        for j, i in enumerate(cls):
            t = self.color[j]+self.type[j]
            plt.plot(T[self.y_train == i, 0], T[self.y_train == i, 1], t)
        
        aver = self.X_train.mean(axis = 0)
        self.X_test -= aver
        if self.scale:
            # ?
            pass

        # 预测的测试集的得分
        self.Tpred = None
        for i in range(self.n_components):
            t = self.X_test @ self.pls.x_weights_[ : , i]
            if self.Tpred is None:
                self.Tpred = t
            else:
                self.Tpred = np.c_[self.Tpred,t]
            self.X_test = self.X_test - np.outer(t, self.pls.x_loadings_[ : , i])
        # 画出预测图
        plt.scatter(self.Tpred[ :, 0], self.Tpred[ :, 1], c = self.y_test, edgecolors = 'black', s = 25)
        plt.show()

    def err(self):
        Ypred = self.pls.predict(self.X_test)
        errcnt = 0
        for predict, real in zip(Ypred, self.y_test):
            if predict*real < 0:
                errcnt += 1
                
        errRatio = errcnt / len(self.y_test) * 100
        return errRatio


# 归一化处理
def maxminnorm(array):
    # 获取每一列的最大最小值
    maxcols = array.max(axis=0)
    mincols = array.min(axis=0)

    data_rows = array.shape[0]
    data_cols = array.shape[1]
    # 生成一个空矩阵
    t = np.empty((data_rows,data_cols))
    for i in range(data_cols):
        t[ : , i] = (array[ : , i] - mincols[i]) / (maxcols[i] - mincols[i])
    return t


# 读取数据
X = np.loadtxt(r'/Users/zhouzilong/Desktop/python/modling /lecture10/wheat_X.txt')
y = np.loadtxt(r'/Users/zhouzilong/Desktop/python/modling /lecture10/wheat_y.txt')
# X中的个维度的数据量纲差异大，进行归一化处理
#X = maxminnorm(X)
pla_da = PLS_DA(.2, 2, False)# 训练 测试集比为8 ： 2, 取两个主成分， 不进行标准化
pla_da.fit(X, y) # 利用pla建模
r = pla_da.err()
print(f"error rate: {r:2.2}%")
pla_da.plotTrainTest([1, -1]) # 利用pla的到的得分矩阵进行降维聚类回归，并画出预测集的散点图