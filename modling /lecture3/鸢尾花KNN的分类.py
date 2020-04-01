# # # 鸢尾花的KNN预测模式

# typy1待预测值[4.9, 3.1]
type1 = [[5.1, 3.5 ],  [4.9, 3. ],  [4.7, 3.2], [4.6, 3.1], [5. , 3.6], [5.4, 3.9],
       [4.6, 3.4], [5. , 3.4 ], [4.4, 2.9] ]
# typy2待预测值[5.7, 2.8]
type2 = [[5.5, 2.6 ],  [6.1, 3. ],  [5.8, 2.6], [5. , 2.3], [5.6, 2.7],
       [5.7, 3. ],  [5.7, 2.9],  [6.2, 2.9], [5.1, 2.5]]
sign1 = [-1, -1, -1, -1, -1, -1, -1, -1, -1]
sign2 = [1, 1, 1, 1, 1, 1, 1, 1, 1]

from KNN import Point, KNN

sample = KNN(type1+type2, sign1+sign2)
# 有待分类的数据集
unknown = [Point([4.9, 3.1]), Point([5.7, 2.8])]
sample.classify(unknown, 7)
for item in unknown:
    item.getType()

# 程序执行：
# the type of [4.9, 3.1] is 1
# the type of [5.7, 2.8] is -1
