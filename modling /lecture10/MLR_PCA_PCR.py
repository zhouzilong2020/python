import numpy as np
from scipy.stats import f

# 多元线性回归
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
        if len(self.A) == 0:
            self._fit()
        return self.A

    # F检验，alpha为显著性水平，一般默认为0.05
    def Ftest(self, alpha = 0.05):
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

# SVD分解--->PCA分解
class PCA:
    def __init__(self, X):
        self.X = X
    
    def SVDdecompose(self):
        # SVD分解
        B = np.linalg.svd(self.X, full_matrices=False)
        self.lamda = B[1]
        # 进行PCA分解
        self.P = B[2].T
        self.T = B[0]*B[1]
        # 前一组分和后一组分的比例-->用以寻找突越点
        compare = [self.lamda[i]/self.lamda[i+1] for i in range(len(self.lamda) - 1) ]
        # 累计百分比，可以说占用累计百分比的信息量
        cum = self.lamda.cumsum()/self.lamda.sum() * 100
        return np.array(compare), cum

    # 取出前k个组分，进行降维
    def PCAdecompose(self, k):
        T = self.T[: , :k]
        P = self.P[: , :k]
        return T, P

class PCR:
    def __init__(self,X,Y):
        self.X=X
        self.Y=Y
        self.pca = None

    # 对X进行SVD分解，返回分解后的矩阵，可以使用compare，和cum来确定独立分组数目
    def confirmPCs(self):
        self.pca=PCA(self.X)
        compare,cum=self.pca.SVDdecompose()
        return compare,cum

    # PCs为独立分组数
    def fit(self,PCs):
        # 如果在进行主成分回归时没有先进行主成分分解，则进行主成分分解
        if self.pca == None:
            self.confirmPCs()

        T, P = self.pca.PCAdecompose(PCs)
        self.P = P
        self.T = T
        # 使用降维后的空间来做多元线性回归
        self.mlr = MLR(T, self.Y, False)
        self.mlr.fit()
        # 得到转换后的空间的一组系数矩阵
        self.A=self.mlr.getCoef()

    # 使用在新空间下进行预测，
    def predict(self,Tnew):
        T = np.dot(Tnew,self.P)
        ans = self.mlr.predict(T)
        return ans
        
    # 进行fisher检验
    def fTest(self,arfa):
        return self.mlr.Ftest(arfa)

def example():
    
    data = np.loadtxt(r'data.txt')
    S = data[ : , :-1]
    C = data[ : , -1:]
    pcr = PCR(S, C)

    print("秩分析", pcr.confirmPCs())

    k = int(input("输入独立组分数:"))
    pcr.fit(k)
    Snew = S
    C_predict = pcr.predict(Snew)
    err = np.abs(C- C_predict).sum(axis = 0)/ C.sum(axis = 0) *100
    print(err)
    F = pcr.fTest(0.05)
    print(F)

