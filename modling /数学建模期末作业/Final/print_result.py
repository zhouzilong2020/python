import numpy as np
import numpy.random as rnp

import pylab as pyl

class Print():
    def __init__(self, canvas, recs = None, pos = None):
        self.width = canvas[0]
        self.height = canvas[1]
        self.recs = recs
        self.pos = pos
        self.cnt = 0
        self.ax = pyl.gca()

    def print(self,path):
        pass

    
    def plot(self, recs, pos , fill = False):
        self.ax.cla()
        self.recs = recs
        self.pos = pos
        for i in range(len(self.recs)):
            x = self.pos[i].x
            y = self.pos[i].y
            tem = pyl.Rectangle((x, y), self.recs[i].width, self.recs[i].height, color=colors[self.recs[i].color], fill = fill)  
            self.ax.add_patch(tem)
        pyl.axis('on')
        pyl.xlim(0, self.width)
        pyl.ylim(0, self.height)  
        pyl.savefig(f'./result_image/{self.cnt}({self.width}x{self.height})')#保存图片
        self.cnt+=1

class Rectangle:
    def __init__(self, w, h, area, profit, color):
        self.width = w
        self.height = h
        self.area = area
        self.profit = profit
        self.color = color

    def revole(self):
        self.width ,self.height = self.height, self.width

class Pos:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return self.x, self.y

class Schedule:
    # 工厂函数模式，每一个Schedule对应于一个画布
    def __init__(self, canvas, reval, recs, demand):
        # recs是有标准属性的，可以直接用种类得到长宽
        # rec[0] = 长 , rec[1] = 宽, rec[2]=面积， rec[3]=售价 
        self.recs = []
        self.recs_R = []
        for i, rec in enumerate(recs):
            self.recs.append(Rectangle(rec[0], rec[1], rec[2], rec[3], i))
            self.recs_R.append(Rectangle(rec[1], rec[0], rec[2], rec[3], i))

        # 打印
        self.printer = Print(canvas)
        # 画布的长宽
        self.width = canvas[0]
        self.height = canvas[1]
        # 画布成本
        self.cost = canvas[2]
        # 回收价值
        self.reval = reval
        # levels记录了某一个水平线的高度，和左下角位置
        self.level_set = set()
        self.level_set.add(0)
        self.levels = [[0, 0]]
        # 记录每一个排入的长方形坐标组合
        self.pos = []
        # 需求量的累计编号
        self.demand = demand.copy()
        for i in range(1, len(demand)):
            self.demand[i] += self.demand[i-1]

        # 用来存放rec的顺序
        self.type = []

    def printCanvas(self):
        self.printer.plot(self.type, self.pos)


    # 返回第i个需求序列的矩形类型
    def getType(self, num):
        if num < 0:
            flag = 1
        else:
            flag = 0
        num = abs(num)
        for i in range(len(self.demand)):
            if num < self.demand[i]:
                if flag:
                    return self.recs_R[i]
                else:
                    return self.recs[i]
    
    
    def setNewRecs(self, order):
        del self.pos
        self.pos = []
        del self.levels
        self.levels = [[0,0]]
        self.order = order
        self.type.clear()
        self.level_set.clear()
        self.level_set.add(0)

    # 检测是否能在某一地方放入矩形
    def isPutable(self, x, y, rec):
        if 0 <= x <= self.width and 0 <=  x+rec.width <= self.width:
            if 0 <= y <= self.height and 0 <= y+rec.height <= self.height:
                if len(self.pos) == 0:
                    return True
                for p in self.pos:
                    if x < p.x < x + rec.width and y < p.y < y + rec.height:
                        return False
                return True
        return False

    # 在x，y的位置放置一个rectangle
    def putRectangle(self, x, y, rec):
        self.pos.append(Pos(x, y))
        if y + rec.height not in self.level_set:
            self.level_set.add(y + rec.height)
            self.levels.append([y + rec.height, x])
        self.type.append(rec)

    # 返回某一水平线上的宽度和左下角坐标
    def getWidth(self, x, level):
        l = x
        r = self.width
        for i in range(len(self.pos)):
            x1 = self.pos[i].x
            y1 = self.pos[i].y
            x2 = x1 + self.type[i].width
            y2 = y1 + self.type[i].height
            if y1 < level < y2:
                if r > x1 > l:
                    r = x1
                if x1 == l:
                    return 0
        return r - l

    def run1(self):
        i = 0
        while len(self.levels) != 0 and i < len(self.order):
            # 对所有高度进行排序，获得当前最低的level, 左下角坐标，和可用宽度
            self.levels.sort(key = lambda o:o[0])

            for j in range(len(self.levels)):
                level_x = self.levels[j]
                min_level = level_x[0]
                x = level_x[1]
                W = self.getWidth(x ,min_level)
                rec = self.getType(self.order[i])

                if self.isPutable(x, min_level, rec) and W >= rec.width:
                    self.putRectangle(x, min_level, rec)
                    self.levels[j][1] += rec.width
                    i+=1
                    break
            else:
                break
        if i != len(self.order):
            self.success = False
            self.pos.clear()
        else:
            self.success = True


    def run(self):
        i = 0
        while len(self.levels) != 0 and i < len(self.order):
            # 对所有高度进行排序，获得当前最低的level, 左下角坐标，和可用宽度
            self.levels.sort(key = lambda o:o[0])
            level_x = self.levels[0]
            min_level = level_x[0]
            x = level_x[1]
            W = self.getWidth(x ,min_level)

            rec = self.getType(self.order[i])

            if self.isPutable(x, min_level, rec) and W >= rec.width:
                self.putRectangle(x, min_level, rec)
                self.levels[0][1] += rec.width
                i+=1
            else:
                optimal = -1
                for j in range(i+1 , len(self.order)):
                    tem = self.getType(self.order[j])
                    if self.isPutable(x, min_level, tem) and W >= tem.width:
                        if optimal == -1:
                            optimal = j
                        else: 
                            if self.getType(self.order[optimal]).height < tem.height:
                                optimal = j

                # 成功找到了这样的矩形
                if optimal != -1:
                    # 将这个矩形并填入序列
                    tem = self.getType(self.order[optimal])
                    self.putRectangle(x, min_level, tem )
                    self.levels[0][1] += tem.width
                    # 交换位置
                    self.order[i], self.order[optimal] = self.order[optimal], self.order[i]
                    i+=1

                else:
                    # 如果找不到，则删除当前中的最低水平线，下一次循环中则变更为第二矮的水平线
                    self.levels.remove(level_x)
                    self.level_set.remove(min_level)
        
        if i != len(self.order):
            self.success = False
            self.pos.clear()
        else:
            self.success = True

    def evalFun(self, order):
        value = 0
        tem1 = self.pos.copy()
        tem2 = self.recs.copy()
        self.setNewRecs(order)
        # 进行排序 --->得到一组坐标值 和一组rec的顺序
        # 撒大是大！！！！！！！！！！！！！！！！！！1
        self.run1()

        if self.success:
            used = 0
            for rec in self.type:
                value += rec.profit
                used += rec.area
            # 回收
            recycle = ((self.width*self.height)/1000000 - used) * self.reval
            # 总收益
            value = value + recycle - self.cost
            del tem1
            del tem2
            return value
        else: 
            self.pos = tem1
            self.recs = tem2
            return -999

    def isSuccess(self):
        return self.success

    def getPos(self):
        return self.pos

    def getRecs(self):
        return self.type

# 颜色池，共计12中颜色
colors = np.matrix([ 
(255, 0, 0),
(0, 255, 0) ,
(0, 0, 255),
(79,129,189) ,
(192,80,77) ,
(155,187,89) ,
(128,100,162),
(75,172,198) ,
(151, 151, 151) ,
(36,169, 225),
(91, 74, 66) ,
(130, 57, 53) ])
colors = (colors / 255).tolist()

# 各个板子的长、宽、成本
canvas3 = [(2500,2500, 10) ,(2000,2000,6.5), (1800,1800,4.8) ,(1500,1500,4)]
canvas5 = [(2500,2500, 13) ,(2000,2000, 8.45), (1800,1800, 6.24) ,(1500,1500,5.2)]
# 回收价值
reval = 1.4
# 三层纸箱的设计 长 宽 面积 售价
layer_3 = np.loadtxt(r'./3layer.txt').tolist()
# 三层纸箱的需求
demand_3 = np.loadtxt(r'./demand3.txt').tolist()
# 不同纸板进行规划
type_2500 = Schedule(canvas3[0], reval, layer_3, demand_3)
type_2000 = Schedule(canvas3[1], reval, layer_3, demand_3)
type_1800 = Schedule(canvas3[2], reval, layer_3, demand_3)
type_1500 = Schedule(canvas3[3], reval, layer_3, demand_3)
demand_3_num = int(np.sum(demand_3))

# 得到规划好的数据
# 如果需要重新跑，则清修改路径
order = np.loadtxt(r'./result/3/result_170---500.txt')

def f(order):
    # 分别代表四个类型的底板
    global type_2500,type_2000,type_1800,type_1500,demand_3_num
    i = 0
    order = order.tolist()
    p = [[0, 0, type_2500], [0, 0, type_2000], [0, 0, type_1800], [0, 0, type_1500]]
    value = 0

    while  i < demand_3_num-1:
        p[0][:2] = getValue(order[ i: ], p[0][2].evalFun)
        p[1][:2] = getValue(order[ i: ], p[1][2].evalFun)
        p[2][:2] = getValue(order[ i: ], p[2][2].evalFun)
        p[3][:2] = getValue(order[ i: ], p[3][2].evalFun)
        p.sort(key = lambda o:o[0])
        i += p[-1][1]
        value += p[-1][0]
#        画图
        p[-1][2].printCanvas()
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

def main():
    global order
    a = f(order)
    print(a)
    
    
if __name__ == '__main__':
    main()
