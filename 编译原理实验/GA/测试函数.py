import numpy as np

n = 200
x = np.linspace(-5.0, 5.0, n)
y = np.linspace(-5.0, 5.0, n)
X, Y = np.meshgrid(x, y)

x_y = np.power(X, 2) + np.power(Y, 2)

Z1 = np.power(np.sin(np.power(x_y, 0.5)), 2) - 0.5
Z2 = np.power((1 + 0.001 * x_y), 2)
Z = 0.5 - Z1 / Z2
from mpl_toolkits.mplot3d import Axes3D
# cm color_map
from matplotlib import cm
import matplotlib.pyplot as plt
from matplotlib.ticker import LinearLocator, FormatStrFormatter

fig = plt.figure()
ax = Axes3D(fig)

ax.plot_surface(X, Y, Z, cmap=cm.jet)

ax.set_xlabel(u'x')
ax.set_ylabel(u'y')
ax.set_zlabel(u'f(x,y)')
plt.show()  # 画3d曲面
plt.savefig(fig)