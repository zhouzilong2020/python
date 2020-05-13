import numpy as np
import matplotlib.pyplot as plt

# 取点
x = np.linspace(0, 5, 10)
y = x ** 2

# 一行，两列，的第一个图
plt.subplot(1,2,1)
plt.plot(x, y, 'r--')

# 一行，两列，的第二个图
plt.subplot(1,2,2)
plt.plot(y, x, 'g*-')
plt.show()

