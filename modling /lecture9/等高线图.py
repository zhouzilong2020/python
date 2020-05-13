import matplotlib.pyplot as plt
import numpy as np
n=200
x = np.linspace(-10.0, 10.0, n);y = np.linspace(-10.0, 10.0, n)
s1=2*np.exp(-((x+1)/(3))**2)  
#生成一条高斯曲线 ,高斯峰公式  s=A*exp(-((x-w)/sigma)**2)
s2=2*np.exp(-((y+2)/(3))**2) 
Z1=np.outer(s1,s2)  # 向量外积，生成第一个高斯山包
w1=2*np.exp(-((x-2)/4)**2);w2=2*np.exp(-((y-1)/4)**2)
Z2=np.outer(w1,w2)  # 生成第二个高斯山包
X, Y = np.meshgrid(x, y)
Z=100*(Z2-Z1)

# X,Y,Z需要时plotsurface类型
CS = plt.contour(X, Y, Z, 10) # 制作等高线，横砍10刀
plt.clabel(CS, inline=True, fontsize=10) #inline控制画标签，移除标签下的线
plt.title('Simplest default with labels')
plt.show()
