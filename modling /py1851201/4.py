from sklearn import datasets
import numpy as np
import matplotlib.pyplot as plt

# 导入数据
data = np.loadtxt(r'./datatest.txt')
# 原始数据的折线图
plt.plot(data[:,0] ,data[:,1], 'b-', label='orig')

# 峰值位置图
plt.plot([24,24] ,[0,2], 'r-', label='12->24.0')
plt.plot([170,170] ,[0,2], 'r-', label='85->170.0')
plt.plot([312,312] ,[0,2], 'r-', label='156->312.0')

# 设置图例位置
plt.legend(loc = 'upper left')
plt.show()
