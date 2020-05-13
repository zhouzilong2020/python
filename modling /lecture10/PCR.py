import numpy as np
from PCA import PCA
from MLR import MLR

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


# data = np.loadtxt(r'data.txt')
# S = data[ : , :-1]
# C = data[ : , -1:]
# pcr = PCR(S, C)

# print("秩分析", pcr.confirmPCs())

# k = int(input("输入独立组分数:"))
# pcr.fit(k)
# Snew = S
# C_predict = pcr.predict(Snew)
# err = np.abs(C- C_predict).sum(axis = 0)/ C.sum(axis = 0) *100
# print(err)
# F = pcr.fTest(0.05)
# print(F)

