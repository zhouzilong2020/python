# 根据预测公式和实际数据比对，让在某一参数下预测值和真值最小，则参数最好
# 重要的是如何评估模型

# 遗传算法！
# 生成很多组参数k1,k2,k3, 就可以生成了一个模型
# 1.遗传    在整个数据库（种群），随机挑两个个体，进行数据交叉融合（基因重组）
# 2.变异    挑一个个体，随便变化一个小数（变异）
# 如果以上两个方法使得评估模型变小了（比原来的种群的最差的个体好），则取代值
# ！！总是通过优胜劣汰的方式使得种群个数保持不变
# 这样不断迭代，则重构种群，最后的到进化种群

import numpy as np
import numpy.random as npr

data = np.loadtxt(r'/Users/zhouzilong/Desktop/python/modling /lecture5/黑枸杞溶出.txt')
t = data[:, 0]
A = data[:, 1]

class Individual:
    # 生成一个n个基因（n个维度的变量），遗传算法的个体
    def __init__(self, n):
        self.error = 999999
        self.chromosome = npr.random(n)

    def predict(self):
        global t, A
        # 解包
        a, k1, k2 = self.chromosome
        # 计算公式
        # 这里是对于每一组参数，对所有数据来进行评估
        # 这里的predict也是一个一个矩阵！
        predict = a*k1*(np.exp(-k1*t)-np.exp(-k2*t))/(k2-k1)
        error = np.sum(np.abs(A-predict))
        self.eva = error

id1 = Individual(3)
id1.predict()
print(id1.eva)

# 如何找到群体最优解？
# 1.迭代次数限制
# 种群数量，变异概率
class NGA:
    def __init__(self, popu, dimension, crossoverProb, mutationProb, maxlterTime, evalFunc):
        s




# 环境值从小到大排序
# self.population.sort(key = lambda x:x.ecal)