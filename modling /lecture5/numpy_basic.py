# numpy是基于C语言编写的，速度很快
import numpy as np
import numpy.random as npr
#  读进来的是一个矩阵！
data = np.loadtxt(r'/Users/zhouzilong/Desktop/python/modling /lecture5/刹车速度与距离.txt')

# 矩阵分片
# 二维分片
# matrix[行 begin:end:step, 列 begin:end:step]

# 取得第一列的全部元素
v = data[ : , 0]    
# 取得第二列的元素
d = data[ : , 1]

# 简单算术运算
# **对每一个元素进行乘方
# sum()求和
v2 = v**2
v3 = v**3
v4 = v**4

# A*B对应元素相乘
# 相当于求了个和
left = np.sum(d*v2-0.75*v3)

right = np.sum(v4)
k = left/right

# numpy支持对数组的计算，可以直接对一组数据进行计算，得到一个新矩阵