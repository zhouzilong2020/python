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
        if len(self.A) == 0:
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

class PCA:
    def __init__(self, X):
        self.X = X
    
    def SVDdecompose(self):
        B = np.linalg.svd(self.X, full_matrices=False)
        self.lamda = B[1]
        self.P = B[2].T
        self.T = B[0]*B[1]
        compare = [self.lamda[i]/self.lamda[i+1] for i in range(len(self.lamda) - 1) ]
        # 累计百分比，可以说占用累计百分比的信息量
        cum = self.lamda.cumsum()/self.lamda.sum() * 100
        return np.array(compare), cum

    def PCAdecompose(self, k):
        T = self.T[: , :k]
        P = self.P[: , :k]
        return T, P

class PCR:
    def __init__(self,X,Y):
        self.X=X
        self.Y=Y

    def confirmPCs(self):
        self.pca=PCA(self.X)
        compare,cum=self.pca.SVDdecompose()
        return compare,cum

    def fit(self,PCs):
        T,P=self.pca.PCAdecompose(PCs)
        self.P=P
        self.mlr=MLR(T,self.Y,False)
        self.mlr.fit()
        self.A=self.mlr.getCoef()

    def predict(self,Xnew):
        T=np.dot(Xnew,self.P)
        ans=self.mlr.predict(T)
        return ans
        
    def fTest(self,arfa):
        return self.mlr.Ftest(arfa)

def main():
    data = np.loadtxt(r'data.txt')
    X = data[ : , :-1]
    Y = data[ : , -1:]
    pcr = PCR(X, Y)
    print("秩分析", pcr.confirmPCs())
    k = int(input("输入独立组分数:"))
    pcr.fit(k)
    Xnew = X
    Y_predict = pcr.predict(Xnew)
    err = np.abs(Y- Y_predict).sum(axis = 0)/ Y.sum(axis = 0) *100
    print(err)
    F = pcr.fTest(0.05)
    print(F)

if __name__ == '__main__':
    main()