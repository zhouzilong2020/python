from sklearn import datasets
import numpy as np
import matplotlib.pyplot as plt
# 鸢尾花的散点图

# 汉字编码格式改变：
import matplotlib as mpl
# 负号显示
plt.rcParams['axes.unicode_minus'] = False
# 汉字显示
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = [u'SimHei']



iris=datasets.load_iris()
X=iris.data #获得自变量数据
y=iris.target  # 获得样本的分类信息

cls1 = y==0
cls2 = y==1
cls3 = y==2

# 组分一的各个数据
X1 = X[cls1]
# 组分二的各个数据
X2 = X[cls2]
# 组分三的各个数据
X3 = X[cls3]

d1 = 0
d2 = 1
plt.scatter(X1[:,d1] ,X1[:,d2] ,s=20, c='b',marker='o', label = '类型1')
plt.scatter(X2[:,d1] ,X2[:,d2] ,s=20, c='y',marker='v', label = '类型2')
plt.scatter(X3[:,d1] ,X3[:,d2] ,s=20, c='r',marker='+', label = '类型3')

# plt.plot(X1[:,0] ,X1[:,1], 'ro')
# 使用plot画散点图，r为颜色，o为点样
plt.legend(loc = 'upper left')

plt.show()
