import numpy as np
import matplotlib.pyplot as plt

# range()必须整数区间，整数步长
# np.arange()可以小数步长
# np.linspace(左区间，右区间——包含，份数，endpoint=False——包不包含右区间)

x = np.arange(-np.pi, np.pi, 0.1)
y = np.sin(x)
plt.plot(x,y,color = 'b', ls = ':', lw = '2', label='sin')
# ls:线的种类'-' '-.' ':'
# lw:线宽度
# color:颜色... 
# lable:曲线的名字
plt.legend(loc = 'upper left')
# legend: lable放置的位置

# 画网格线 
plt.grid(True)


x1, x2, y1, y2 = -3, 3, -1, 1
# 设置坐标轴的范围
plt.xlim(x1, x2)
plt.ylim(y1, y2)

# 坐标轴的标签
# 图的标签
plt.xlabel('x_label')
plt.title('title')

# 画饼图：
# plt.pie(data, explode=[0, 0, 1])
# 表示第i个饼被拖出来

# 散点图
# s是大小，c颜色，marker是点的类型
# marker可以选择：
plt.scatter(x, y, s=20, c='b', marker='4')

# numpy：数据过滤
# Y = X[ [1, 2, 3] ]
# Y取得X的第1，2，3行数
#
X=np.random.standard_normal((10,5)).round(3)
# 取列
rows=[0,4,8]
Y=X[rows]
#取行
cols=[1,4]
Z=X[:,cols]
# 此外，也可以用[True, False, True ... ]来对应X的十行，来得到过滤
rows1=[True,False,True,True, False, False, False, False, False, False]
X1=X[rows1]

# 汉字编码格式改变：
import matplotlib as mpl
# 负号显示
mpl.rcParams['axes.unicode_minus'] = False
# 汉子显示
mpl.rcParams['font.family'] = 'sans-serif'
mpl.rcParams['font.sans-serif'] = [u'SimHei']

# 指定图大小和分辨率
# 800x600，每英寸100个点
fig, axes = plt.subplots(figsize=(8,6),dpi=100)


# x = np.linspace(0, 5, 10)
# y = x ** 2
# fig, axes = plt.subplots(figsize=(8,6),dpi=100)
# axes.plot(x, y, 'r')
# axes.set_xlabel('x')
# axes.set_ylabel('y')
# axes.set_title('title')
# plt.show()
