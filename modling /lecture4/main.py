from file import getData
from KNN import Point, KNN

# 从文件中读取数据
dataSet = getData("lecture 4/山-变色鸢尾花瓣.txt")
typeSet = getData("lecture 4/山-变色鸢尾花瓣分类.txt")

# 点1、3取自样本集一，点2、4取自样本点集二
unknown = [Point([4.9, 3.1]), Point([5.7, 2.8]), Point([4.7, 3.2]), Point([5.8, 2.6])]

# 使用样本建立KNN数据集
sample = KNN(dataSet, typeSet)
# 设置未知集合
sample.setUnknown(unknown)
# 按照7个最近样本点进行KNN预测
sample.classify(7)
# 输出预测
sample.getAnswer()

# 输出结果如下：：
# (4.9, 3.1) is predicted as type -1
# (5.7, 2.8) is predicted as type 1
# (4.7, 3.2) is predicted as type -1
# (5.8, 2.6) is predicted as type 1