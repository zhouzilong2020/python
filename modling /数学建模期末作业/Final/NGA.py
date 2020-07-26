import numpy as np
import numpy.random as npr
import algorithm as al

class Individual:
    _n=0
    eval=0.0
    chr=None
    
    def __init__(self,n, sequence = False):
        self._n=n
        # 排列的先后顺序
        self.chr=npr.random(n)
        change_8_9 = np.zeros(n, np.int)
        if sequence:
            self.chr.sort()
            dirc = np.zeros(n, np.int)
        else:
            # 旋转方向 0不旋转 1旋转90度
            dirc = npr.randint(0, 2, n)

        self.chr = np.c_[self.chr, dirc, change_8_9]
        # 按照第一列的随机数进行排序，返回的是一个行索引！！！！
        # self.order = self.chr[:,0].argsort() 
        # self.sort()
    
    # 按照随机数和旋转方向生成编号顺序
    # 正编号代表不旋转，副编号代表旋转
    def sort(self):
        self.order = self.chr[:,0].argsort()
        for i in range(len(self.chr)):
            if self.chr[i][1] == 1:
                self.order[i] = -self.order[i]
            if self.chr[i][2] == 1 and 772 <= self.order[i] < 913:
                self.order[i] *= 10
                
    def crossover(self,another):
        startPos = npr.randint(self._n) # 交叉的起始位置
        if startPos+1 == self._n:
            endpos = startPos+1
        else:
            endpos = npr.randint(startPos+1, self._n) # 交叉结束位点
        
        son1 = Individual(self._n)
        son2 = Individual(self._n)

        # 交叉前的基因全部保留
        son1.chr[0:startPos]=self.chr[0:startPos]
        son2.chr[0:startPos]=another.chr[0:startPos]
        # 交叉段基因
        son1.chr[startPos:endpos]=another.chr[startPos:endpos]
        son2.chr[startPos:endpos]=self.chr[startPos:endpos]
        # 交叉点后的基因全部保留
        son1.chr[endpos:]=self.chr[endpos:]
        son2.chr[endpos:]=another.chr[endpos:]

        son1.sort()
        son2.sort()
        return son1,son2

    # 交换变异
    def crossMutation(self, rate):
        son = Individual(self._n)
        son.chr=self.chr.copy()

        tot = int(self._n * rate)
        for i in range(tot):
            p1 = npr.randint(self._n) # 交换位置1
            p2 = npr.randint(self._n) # 交换的位置2
            while p1 == p2:
                p2 = npr.randint(self._n)
            son.chr[p1], son.chr[p2] = son.chr[p2], son.chr[p1]
        son.sort()
        return son
    
    # 旋转变异
    # 采用多点旋转的方式
    def whirlMutation(self, rate):
        son = Individual(self._n)
        son.chr=self.chr.copy()
        tot = int(self._n * rate)
        for a in range(tot):
            p = npr.randint(self._n) # 旋转的起始位置
            if son.chr[p][1] == 1:
                son.chr[p][1] = 0
            else:
                son.chr[p][1] = 1
        son.order = self.order.copy()
        # son.sort()
        return son
    
    def from9To8Mutation(self, rate):
        son = Individual(self._n)
        son.chr=self.chr.copy()
        tot = int(self._n * rate)

        for a in range(tot):
            p = npr.randint(self._n) # 变换8---9的起始位置
            if son.chr[p][2] == 1:
                son.chr[p][2] = 0
            else:
                son.chr[p][2] = 1
        son.sort()
        return son

    def mutation(self,learnRate):
        son = Individual(self._n)
        son.chr=self.chr.copy()
        mutationPos =npr.randint(self._n) #变异的位置

        #产生一个-0.5-0.5之间的随机小数
        temp = npr.random()-0.5
        son.chr[mutationPos] += learnRate * temp
        return son
        
class NGA:
    population=[]
    dimension=1
    bestPos=worstPos=0
    mutationProb=10
    crossoverProb=90
    maxIterTime=1000
    evalFunc=None
    arfa =1
    popu=2


    def __init__(self,popu, dimension,crossoverProb,mutationProb,maxIterTime,evalFunc):
        # 初始化种群
        for i in range(popu):
            if i == 0:
                oneInd=Individual(dimension, True)
            else:
                oneInd=Individual(dimension, False)
            oneInd.sort()
            oneInd.eval=evalFunc(oneInd.order)
            self.population.append(oneInd)
        
        # 交叉概率
        self.crossoverProb=crossoverProb
        # 变异概率
        self.mutationProb=mutationProb
        # 最大迭代次数
        self.maxIterTime=maxIterTime
        # 评估函数
        self.evalFunc=evalFunc
        # 种群数量
        self.popu=popu
        # 维度、基因的数量
        self.dimension=dimension

    #找最好、最坏个体位置
    def findBestWorst(self):
        self.population.sort(key=lambda o:o.eval)
        self.bestPos=self.popu-1
        self.worstPos=0
        
    #交叉操作 
    def crossover(self):
        # 找到两个亲代染色体
        fatherPos=npr.randint(0,self.popu)
        motherPos=npr.randint(0,self.popu)
        while motherPos == fatherPos:
            motherPos = npr.randint(0,self.popu)
        father = self.population[fatherPos]
        mother = self.population[motherPos]

        # 生成两个子代
        son1,son2=father.crossover(mother)
        # 为子代评估
        son1.eval = self.evalFunc(son1.order)
        son2.eval = self.evalFunc(son2.order)
        
        # 如果子代中比原始种群中的最差样本更好，则保留，否则舍去
        self.findBestWorst()
        if son1.eval > self.population[self.worstPos].eval:
            self.population[self.worstPos] = son1
        self.findBestWorst()
        if son2.eval > self.population[self.worstPos].eval:
            self.population[self.worstPos] = son2
            
    # 变异操作
    def mutation(self):
        # 找到一个有待变异的个体
        father = self.population[npr.randint(self.popu)]
        # 生成变异个体
        son=father.mutation()
        # 如果子代中比原始种群中的最差样本更好，则保留，否则舍去
        son.eval = self.evalFunc(son.order)
        self.findBestWorst()
        if son.eval > self.population[self.worstPos].eval:
            self.population[self.worstPos] = son

    def mutation1(self,rate):
        # 找到一个有待变异的个体
        father = self.population[npr.randint(self.popu)]
        # 生成变异个体
        son=father.crossMutation(rate)
        # 如果子代中比原始种群中的最差样本更好，则保留，否则舍去
        son.eval = self.evalFunc(son.order)
        self.findBestWorst()
        if son.eval > self.population[self.worstPos].eval:
            self.population[self.worstPos] = son

    def mutation2(self,rate):
        # 找到一个有待变异的个体
        father = self.population[npr.randint(self.popu)]
        # 生成变异个体
        son=father.whirlMutation(rate)
        # 如果子代中比原始种群中的最差样本更好，则保留，否则舍去
        son.eval = self.evalFunc(son.order)
        self.findBestWorst()
        if son.eval > self.population[self.worstPos].eval:
            self.population[self.worstPos] = son
    
    def mutation3(self,rate):
        # 找到一个有待变异的个体
        father = self.population[npr.randint(self.popu)]
        # 生成变异个体
        son=father.from9To8Mutation(rate)
        # 如果子代中比原始种群中的最差样本更好，则保留，否则舍去
        son.eval = self.evalFunc(son.order)
        self.findBestWorst()
        if son.eval > self.population[self.worstPos].eval:
            self.population[self.worstPos] = son
            
    def solve(self):
        shrinkTimes = self.maxIterTime / 10 
        # 将总迭代代数分成10份 逐次降低学习速率！
        oneFold = shrinkTimes # 每份中包含的次数
        i = 0
        while i < self.maxIterTime:
            print(i,"---",self.maxIterTime)
            if i == shrinkTimes:
                self.arfa =self.arfa / 2.0
                #经过一份代数的迭代后，将收敛参数arfa缩小为原来的1/2，以控制mutation的变异大小
                shrinkTimes += oneFold  #下一份到达的位置
            for  j in range(self.crossoverProb):
                self.crossover()
            for  j in range(self.mutationProb[0]):
                self.mutation1(self.arfa)
            for  j in range(self.mutationProb[1]):
                self.mutation2(self.arfa)
            for j in range(self.mutationProb[2]):
                self.mutation3(self.arfa)
            print("func value:",self.population[self.bestPos].eval)
            i=i+1
            self.outPut(f'result_{i}---{self.maxIterTime}.txt')
            
    def getAnswer(self):
        self.findBestWorst()
        best = self.population[self.bestPos]
        diec = best.chr
        order = best.order.copy()
        for i in range(best._n):
            if diec[i][1] == 1:
                order[i] = -order[i]
        return self.population[self.bestPos].order.tolist()
    
    def outPut(self, path):
        result = self.getAnswer()
        f = open(f'result/{path}', mode = 'w')
        for i in result:
            f.writelines(f'{i}\n')
        f.close()


def f(order):
    # 分别代表四个类型的底板
    global type_2500,type_2000,type_1800,type_1500,demand_3_num
    i = 0
    order = order.tolist()
    p = [[0, 0, type_2500], [0, 0, type_2000], [0, 0, type_1800], [0, 0, type_1500]]
    value = 0

    while  i < demand_3_num-1:
        p[0][:2] = getValue(order[ i: ], type_2500.evalFun)
        p[1][:2] = getValue(order[ i: ], type_2000.evalFun)
        p[2][:2] = getValue(order[ i: ], type_1800.evalFun)
        p[3][:2] = getValue(order[ i: ], type_1500.evalFun)
        p.sort(key = lambda o:o[0])
        i += p[-1][1]
        value += p[-1][0]
        # p[-1][2].printCanvas()
    return value

def getValue(order, evalFun):
    j = 1
    v1 = evalFun(order[ : 1])
    while j < len(order):
        v2 = evalFun(order[ : j+1])
        if v2 > v1:
            j += 1
            v1 = v2
        else:
            return [v1, j]
    return [v1, j]
        


# 各个板子的长、宽、成本
canvas3 = [(2500,2500, 10) ,(2000,2000,6.5), (1800,1800,4.8) ,(1500,1500,4)]
canvas5 = [(2500,2500, 13) ,(2000,2000, 8.45), (1800,1800, 6.24) ,(1500,15005.2)]
# 回收价值
reval = 1.4
# 三层纸箱的设计 长 宽 面积 售价
layer_3 = np.loadtxt(r'./3layer.txt').tolist()
# 三层纸箱的需求
demand_3 = np.loadtxt(r'./demand3.txt').tolist()
# 不同纸板进行规划
type_2500 = al.Schedule(canvas3[0], reval, layer_3, demand_3)
type_2000 = al.Schedule(canvas3[1], reval, layer_3, demand_3)
type_1800 = al.Schedule(canvas3[2], reval, layer_3, demand_3)
type_1500 = al.Schedule(canvas3[3], reval, layer_3, demand_3)
demand_3_num = int(np.sum(demand_3))


def main():
    maxIterTime = 2
    # popu, dimension,  crossoverProb mutationProb, maxIterTime,evalFunc
    # 这里的变异分为三种变异，故以一个数组表示，最终每一次的变异、交叉次数即为输入的次数
    nga = NGA(10, demand_3_num, 1, [2,2,5], maxIterTime, f)
    nga.solve()
   
    
if __name__ == "__main__":
    main()
