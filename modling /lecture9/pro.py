import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib as mpl
import numpy as np

z = np.loadtxt(r"mix_2.txt")

# 取矩阵的行、列
size = z.shape
# 建立网格点
y = np.arange(0, size[0], 1)
x = np.arange(0, size[1], 1)
x, y = np.meshgrid(x, y)

# 绘制三维图
fig = plt.figure();
ax = Axes3D(fig)
ax.set_xlabel(u'time')
ax.set_ylabel(u'wavelength')
ax.set_zlabel(u'peak')
ax.plot_surface(x, y, z, cmap=plt.cm.hot)
plt.show()

# 绘制等高线图
fig, axes = plt.subplots(figsize=(8, 6), dpi=100)
# X,Y,Z需要时plotsurface类型
CS = plt.contour(x, y, z, 10)  # 制作等高线，横砍10刀
plt.clabel(CS, inline=True, fontsize=10)  # inline控制画标签，移除标签下的线
plt.title('Contour map for mix_2')
plt.show()
