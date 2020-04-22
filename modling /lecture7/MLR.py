import numpy as np
from scipy.stats import f
class MLR:
    #  初始化，用户输入X，Y和是否需要截距
    def __init__(self, X, Y, intersect = False):
        # 判断数据是否是一维的
        if len(X.shape) == 1:
            self.X = Y.reshape(-1, 1)
        else:
            self.X = X
        # 判断数据是否是一维的
        if len(Y.shape) == 1:
            self.Y = Y.reshape(-1, 1)
        else:
            self.Y = Y
        self.intersect = intersect
        self.A = None
            
    # 给出一组新的值，返回预测值
    def predict(self, new_X):
        if self.A is None:
            self.fit()
        # 如果方程中存在常数项,则为new_X矩阵左边添加一列全1
        if self.intersect:
            col = new_X.shape[0]
            new_1 = np.ones((col, 1))
            new_X = np.c_[new_1, new_X]
        predict_Y =  new_X @ self.A
        return predict_Y

    # 按照(XTX)-1XTY,计算系数A
    def fit(self):
        # 如果存在常数项，为X在左边添加一列全一列
        if self.intersect:
            col = self.X.shape[0]
            new_1 = np.ones((col, 1))
            X = np.c_[new_1, self.X]
        else :
            X = self.X
        self.A = np.linalg.inv(X.T @ X) @ X.T @ self.Y

    # 获得系数 
    def getCoef(self):
        if self.A == None:
            self._fit()
        return self.A

    # F检验
    def Ftest(self, alpha):
        global f
        n = len(self.X)
        Y_predict = self.predict(self.X)

        # 按照列计算,Y矩阵中可能含有多个函数
        Qe = ((self.Y - Y_predict)**2).sum( axis=0 )
        Y_avg = self.Y.mean( axis = 0)
        U = ((Y_predict - Y_avg)**2).sum( axis = 0 )

        # 得到x变量的个数
        k = self.X.shape[1]
        # F分布的预测值
        F_predict = (U/k) / (Qe/(n-k-1))
        F_theory = f.isf(alpha, 1, n-k-1)

        ans = []
        for f in F_predict:
            ans.append([f, F_theory, f > F_theory])
        return ans


data = np.loadtxt(r"data.txt")
# Y为GDP（产出）
Y = data[ : , 1]
# X中第一列为就业人数（L），第二列为财力投入（K）
X = data[ : , 2: ]
# 根据道格拉斯生产关系函数进行变形，求自然对数
Y = np.log(Y)
X = np.log(X)
# 进行多元线性回归并进行检测
mlr = MLR(X, Y, intersect = True)
mlr.fit()
print(mlr.Ftest(0.05))
# 得到系数
coe = mlr.A
print(f"A = {np.exp(coe[0])}, alpha = {coe[1]}, beta = {coe[2]}")
