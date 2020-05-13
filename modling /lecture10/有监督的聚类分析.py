import numpy as np
import matplotlib.pyplot as plt
X = np.loadtxt(r"wheat_X.txt")
y = np.loadtxt(r"wheat_Y.txt")
# B[B==-1]=0
aver=X.mean(axis=0)
std=X.std(axis=0)
X=(X-aver)/std
allY=[]
for i in range(len(y)): # 转正交编码
    if (y[i]==1.0):
        oneY=[0,1]
    else:
        oneY=[1,0]  # -1
    allY.append(oneY)
Y=np.array(allY)


from PCR import PCR
pcr = PCR(X, Y)
pcr.confirmPCs()
pcr.fit(8)
T = pcr.T
P = pcr.P


Yhat = pcr.predict(X)
exp = np.exp(Yhat)
sumExp = np.sum(exp, axis=1, keepdims=True)
softmax = exp / sumExp  
Ypred=np.argmax(softmax,axis=1)

y[y==1.0] = 0
y[y==-1] = 1

err = y-Ypred
err = err[err!=0]
errRate = len(err)/len(y)*100
# print(errRate)


# 深度可视化
x_min = T[:, 0].min() - .5
x_max = T[:, 0].max() + .5
y_min = T[:, 1].min() - .5
y_max = T[:, 1].max() + .5
h = .2
xx, yy = np.meshgrid( np.array(x_min, x_max, h), np.array(y_min, y_max, h) )

t0 = xx.flatten()
t1 = yy.flatten()
Tmoni = np.c_[t0, t1]

Xmoni = Tmoni @ P[: , 0:2].T
Yhat = pcr.predict(Xmoni)
# print(softmax)

