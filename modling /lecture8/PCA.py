import numpy as np
from MLR import MLR

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

# class PCR:
#     def __init__(self):
#         pass

def main():
    S = np.loadtxt(r'S.txt').T
    y = np.loadtxt(r'C.txt').T

    pca = PCA(S)
    print(pca.SVDdecompose())
    k = int(input())
    T, P = pca.PCAdecompose(k)
    print("得分\n" ,T)


    mlr = MLR(T, y, intersect = False)
    mlr.fit()
    # Xnew要先转换到新空间去！
    Xnew = S
    Tnew = Xnew @ P

    Chat = mlr.predict(Tnew)
    err = np.abs((y - Chat)).sum(axis=0) /y.sum(axis=0)  *100
    print(err)



