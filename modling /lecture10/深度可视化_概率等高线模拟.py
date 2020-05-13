import matplotlib.pyplot as plt
import numpy as np
X=np.loadtxt(r'wheat_X.txt')
av=X.mean(axis=0)
std=X.std(axis=0)
X=(X-av)/std
y=np.loadtxt(r'wheat_y.txt')
allY=[]
for i in y:
    if i==1.0:
        allY.append([1,0])
    else:
        allY.append([0,1])
Y=np.array(allY)
from PCR import PCR
pcr=PCR(X,Y)
pcr.confirmPCs()
pcr.fit(8)
T=pcr.T
P=pcr.P
f1=0
f2=1
plt.scatter(T[y==1,f1],T[y==1,f2],c='b',marker='o',label='good')
plt.scatter(T[y==-1,f1],T[y==-1,f2],c='r',marker='v',label='bad')
plt.legend(loc='upper left')


x_min = T[:, 0].min() - .5
x_max = T[:, 0].max() + .5
y_min = T[:, 1].min() - .5
y_max = T[:, 1].max() + .5
h = .2  
xx, yy = np.meshgrid(np.arange(x_min, x_max, h),  np.arange(y_min, y_max, h))
t0=xx.flatten()
t1=yy.flatten()
Tmoni=np.c_[t0,t1]
Xmoni=Tmoni @ P[:,0:2].T


Yhat=pcr.predict(Xmoni)
exp=np.exp(Yhat)
sumExp=exp.sum(axis=1,keepdims=True)
#sumExp = np.sum(exp, axis=1, keepdims=True)
softmax = exp / sumExp
Z = softmax [:, 0]  #选择第一类的概率输出
# 制作概率的等高线图
Z = Z.reshape(xx.shape)
CS = plt.contour(xx,yy, Z, 10, colors='k',) # 负值将用虚线显示             
plt.clabel(CS, fontsize=9, inline=1)
plt.show()