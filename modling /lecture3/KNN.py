from math import sqrt
class KNN:
    unknown = []
    answer = []

    # 初始化数据集和分类集
    def __init__(self, dataset, idset):
        self.dataset = dataset
        self.idset = idset

    # 使用knn的分类方法，以k个最近的样本点对未知points进行预测
    def classify(self, points, k):
        for point in points:
            dis_list = []
            for coor, id in zip(self.dataset, self.idset):
                tem = 0
                # 这里的dis需要先保存列表，后面根据最近的几个点来进行加权操作！！
                for x1, x2 in zip(coor, point.coor):
                    tem += (x1-x2)**2
                # dis_list保存待预测点和所有已知样本点的距离和已知样本点的id
                dis_list.append([sqrt(tem), id])
            
            # 对dis_list表中按照距离排序
            dis_list = sorted(dis_list, key=lambda x:x[0])
            predict_value = 0
            for i in range(k):
                # 于待测点越近权重应该分配越大
                predict_value += dis_list[i][1]/dis_list[i][0]
            # 为该数据点设置预测分类
            if predict_value > 0:
                KNN.answer.append(1)
                point.setId(1)
            else:
                KNN.answer.append(-1)
                point.setId(-1)

    def setUnknown(self, l):
        KNN.unknown.append(l)
    
    


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

