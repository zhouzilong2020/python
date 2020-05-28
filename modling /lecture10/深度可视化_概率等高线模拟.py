import matplotlib.pyplot as plt
import numpy as np
from MLR_PCA_PCR import PCR
# 读取数据
X = np.loadtxt(r'wheat_X.txt')
y = np.loadtxt(r'wheat_y.txt')
# -—————————————————————————聚类分析—————————————————————
# 将X中的各个维度的数据标准化
av = X.mean(axis=0)
std = X.std(axis=0)
X = (X-av)/std
# 将Y进行二维正交化
allY = []
for i in y:
    if i == 1.0:
        allY.append([1,0])
    else:
        allY.append([0,1])
Y = np.array(allY)

# 确定主成分
pcr=PCR(X,Y)
pcr.confirmPCs()
pcr.fit(8)


T=pcr.T
P=pcr.P
d1=0
d2=1
# 进行数据筛选，在T和y中，选取T中对应行y取1的数据的第d1列
plt.scatter(T[y==1,d1],T[y==1,d2],c='b',marker='o',label='good')
plt.scatter(T[y==-1,d1],T[y==-1,d2],c='r',marker='v',label='bad')
# 画图的图例的摆放位置
plt.legend(loc='upper left')
# -————————————————————————————————————————————————————


#——————————————————————————概率等高线图——————————————————
x_min = T[:, 0].min() - .5
x_max = T[:, 0].max() + .5
y_min = T[:, 1].min() - .5
y_max = T[:, 1].max() + .5
h = .2 
# 生成采样点的矩阵，这里的采样点的取数值是在降维后的空间的坐标
xx, yy = np.meshgrid(np.arange(x_min, x_max, h),  np.arange(y_min, y_max, h))
# 将xx和yy扁平化
t0=xx.flatten()
t1=yy.flatten()
# 得到一组采样点的模拟值
Tmoni=np.c_[t0,t1]
# 转化为原来的空间坐标
Xmoni=Tmoni @ P[:,0:2].T

# 使用生成的采样值，获得原空间下的预报值
Yhat=pcr.predict(Xmoni)
# 生成softMax值
exp=np.exp(Yhat)
sumExp = exp.sum(axis = 1, keepdims = True)
softmax = exp / sumExp
# 使用第一类的概率进行输出
Z = softmax [:, 0]
# 制作概率的等高线图
Z = Z.reshape(xx.shape)
CS = plt.contour(xx,yy, Z, 10, colors='k',)      
plt.clabel(CS, fontsize=9, inline=1)
plt.show()