# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D 
# fig = plt.figure() 
# ax = Axes3D(fig)

# plot_trisurf（以小三角形构成曲面单元）
# plot_surface（以菱形构成曲面单元）
# 两者需要的数据类型不一样
# trisurf: 使用x,y,z是等长的1D array，x,y,z对应的元素，组成维空间的一个点。
# surface 使用的是np.meshgrid产生的数据,都是二维矩阵

# X = [0, 1, 2, 1.5]
# Y = [0, 4, 4, 1]
# Z = [0, 2, 0, 0]
# # XYZ每一个对应坐标，使用trisur
# ax.plot_trisurf(X, Y, Z)
# plt.show()

import numpy as np
n=200
x = np.linspace(-10.0, 10.0, n)
y = np.linspace(-10.0, 10.0, n)
s1=2*np.exp(-((x+1)/(3))**2)  
#生成一条高斯曲线 ,高斯峰公式  s=A*exp(-((x-w)/sigma)**2)
s2=2*np.exp(-((y+2)/(3))**2) 
Z1=np.outer(s1,s2)  # 向量外积，生成第一个高斯山包
w1=2*np.exp(-((x-2)/4)**2)
w2=2*np.exp(-((y-1)/4)**2)
Z2=np.outer(w1,w2)  # 生成第二个高斯山包
X, Y = np.meshgrid(x, y)
Z=100*(Z2-Z1)

from mpl_toolkits.mplot3d import Axes3D
# cm color_map
from matplotlib import cm
import matplotlib.pyplot as plt
fig = plt.figure()
ax = Axes3D(fig)
ax.plot_surface(X, Y, Z,cmap=cm.jet)
plt.show() # 画3d曲面


