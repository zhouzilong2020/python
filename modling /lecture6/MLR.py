import numpy as np

class MLR:
    #  初始化，用户输入X，Y和是否需要截距
    def __init__(self, X, Y, intersect = False):
        # 用户输入不为array类型，进行转化
        if type(X) is np.array:
            self.X = X
        else: 
            try:
                self.X = np.array(X)
            except:
                print("please check the type of X!")
        if type(Y) is np.array:
            self.Y = Y
        else: 
            try:
                self.Y = np.array(Y)
            except:
                print("please check the type of Y!")
        self.intersect = intersect
        # 为X在左边添加一列全一列
        if self.intersect == True:
            col = self.X.shape[0]
            new_1 = np.ones((col, 1))
            self.X = np.c_[new_1, self.X]
        self.A = None
            
    # 给出一组新的值，返回预测值
    def predict(self, new_X):
        if self.A is None:
            self._fit()
        # 用户输入的的不是numpy的类型
        if not type(new_X) is np.array:
            try:
                new_X = np.array(new_X)
            except:
                print("please check the type of new_X!")
                return None
        # 用户输入的矩阵比较奇怪
        try:
            size = len(new_X)
            new_X = new_X.reshape(1, size)
        except:
            print("please cheeck the organization of the new_X!")
            return None
        # 对每一组值进行预报
        predict_Y = new_X*self.A[1] + self.A[0]
        return predict_Y

    # 按照(XTX)-1XTY,计算系数A
    def _fit(self):
        self.A = np.linalg.inv(self.X.T @ self.X) @ self.X.T @ self.Y

    # 获得系数 
    def getCoef(self):
        if self.A == None:
            self._fit()
        return self.A

def loadtxt(path):
    return np.loadtxt('{}'.format(path))