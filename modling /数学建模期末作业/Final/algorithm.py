import numpy as np
import numpy.random as rnp
# import print as p

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



    # 返回第i个需求序列的矩形类型
    def getType(self, num):
        if num < 0:
            flag = 1
        else:
            flag = 0
        if abs(num) > 1211:
            if flag:
                return self.recs_R[7]
            else:
                return self.recs[7]

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


# def main():
#     # 各个板子的长、宽、成本
#     canvas3 = [(2500,2500, 10) ,(2000,2000,6.5), (1800,1800,4.8) ,(1500,1500,4)]
#     canvas5 = [(2500,2500, 13) ,(2000,2000, 8.45), (1800,1800, 6.24) ,(1500,15005.2)]
#     # 回收价值
#     reval = 1.4
#     # 三层纸箱的设计 长 宽 面积 售价
#     layer_3 = np.loadtxt(r'/Users/zhouzilong/Desktop/tongjimcm2020/PROC/3layer.txt')
#     layer_3 = layer_3.tolist()

#     demand_3 = np.loadtxt(r'/Users/zhouzilong/Desktop/tongjimcm2020/PROC/demand3.txt')
#     demand_3 = demand_3.tolist()

#     type2500_2500 = Schedule(canvas3[0],reval = reval, recs = layer_3, demand = demand_3)

#     for i in range(0,1):
#         # # 生成一个待排的箱子序列
#         # order = [1,1000, 1210, -34, 410, 650,650,650,650,650,650,650,650,650,650,650,650]
#         # # 650,650,650]
#         # # 评估这个序列
#         # value = type2500_2500.evalFun(order)
#         P = p.Print(canvas3[0][0],canvas3[0][1])
#         # # 如果成功拍下则打印
#         # if type2500_2500.isSuccess():
            
#         #     print(f'type{i} success revenue:{value:.2}')
#         #     pos = type2500_2500.getPos()
#         #     recs = type2500_2500.getRecs()
#         #     P.plot(recs, pos, False)

#         # 生成一个待排的箱子序列
#         order = [650,650,650,650,650,650,650,650,650,650,650,650,650,650,650,650, 650,650,650,650,650,650,650,650,650]
#         # 650,650,650]
#         # 评估这个序列
#         value = type2500_2500.evalFun(order)

#         # 如果成功拍下则打印
#         if type2500_2500.isSuccess():
#             print(f'type{i} success revenue:{value:.2}')
#             pos = type2500_2500.getPos()
#             recs = type2500_2500.getRecs()
#             P.plot(recs, pos, False)
    

if __name__ == "__main__":
    main()


# rec = [Rectangle(30, 40),Rectangle(40, 50), Rectangle(40, 20)]
# S = Schedule(rec, 100, 100)
# pos = S.getPos()
# pl = p.Print(100, 100, rec, pos)
# pl.plot()
