from math import sqrt
class KNN:

    # 初始化数据集和分类集
    def __init__(self, dataset, idset):
        self.dataset = dataset
        self.idset = idset

    # 使用knn的分类方法，鉴别给入points的类别
    def classify(self, points):
        totalDist = 0
        for point in points:
            for coor, id in zip(self.dataset, self.idset):
                tem = 0
                for x1, x2 in zip(coor, point.coor):
                    tem += (x1-x2)**2
                totalDist += tem/id
            # 为该数据点设置预测分类
            if totalDist > 0:
                point.setId(1)
            else:
                point.setId(-1)

class Point:
    # 初始化数据点
    def __init__(self, coor, classid = 0):
        self.coor = coor
        self.classid = classid
    # 设置分类集
    def setId(self, classid):
        self.classid = classid
    # 打印分类集
    def getType(self):
        if self.classid == 0:
            print(f"please use KNN to predict first")
        else:
            print(f"the type of {self.coor} is {self.classid}")

