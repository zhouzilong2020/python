import numpy as np
from PCA import PCA
from MLR import MLR

class PCR:
    def __init__(self,X,Y):
        self.X=X
        self.Y=Y

    # 对X进行SVD分解，返回分解后的矩阵，可以使用compare，和cum来确定独立分组数目
    def confirmPCs(self):
        self.pca=PCA(self.X)
        compare,cum=self.pca.SVDdecompose()
        return compare,cum

    # PCs为独立分组数
    def fit(self,PCs):
        T,P=self.pca.PCAdecompose(PCs)
        self.P = P
        self.T = T
        self.mlr=MLR(T,self.Y,False)
        self.mlr.fit()
        self.A=self.mlr.getCoef()

    def predict(self,Xnew):
        T=np.dot(Xnew,self.P)
        ans=self.mlr.predict(T)
        return ans
        
    def fTest(self,arfa):
        return self.mlr.Ftest(arfa)


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

