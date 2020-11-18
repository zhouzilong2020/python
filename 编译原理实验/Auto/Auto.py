import numpy as np
import numpy.random as npr
import matplotlib.pyplot as plt
from queue import Queue


class Auto:
    l_road = 150
    v_max = 4
    p = 0.1
    p_c = 0.5
    carCnt = 5
    maxT = 200

    cars = None

    def __init__(self, l_road=150, v_max=4, p=0.2, p_c=0.5, carCnt=5, maxT=200):
        self.l_road = l_road
        self.v_max = v_max
        self.p = p
        self.p_c = p_c
        self.carCnt = carCnt
        self.maxT = maxT
        self.cars = np.array([-1 for i in range(l_road)])
        plt.xlabel("road")
        plt.ylabel("time")

        # 初始化汽车位置以及汽车速度
        for i in range(carCnt):
            self.cars[npr.randint(self.l_road)] = 2

    def run(self):
        for i in range(self.maxT):
            self.draw(i)
            # 新车开进来
            if self.cars[0] == -1 and npr.randint(10) < self.p_c * 10:
                self.cars[0] = 2
            self.stimulate()
        plt.show()

    def draw(self, t):
        pos = np.where(self.cars != -1)[0]
        y = np.array([t for i in range(len(pos))])
        plt.scatter(pos, y, s=20, c='b', marker='4')

    def stimulate(self):
        pos = np.where(self.cars != -1)[0]
        for i in range(0, len(pos) - 1):
            speed = self.cars[pos[i]]
            # 与下一辆车的距离
            d = pos[i + 1] - pos[i] - 1

            # 加速规则
            speed = min(speed + 1, self.v_max)
            # 减速规则
            speed = min(speed, d)
            # 随机减速规则
            if npr.randint(10) < self.p * 10:
                speed = max(speed - 1, 0)

            # 更新当前车的位置
            self.cars[pos[i]] = -1
            if pos[i] + speed < self.l_road:
                self.cars[pos[i] + speed] = speed
        # 最后一辆车
        speed = self.cars[pos[-1]]
        self.cars[pos[-1]] = -1
        if pos[-1] + speed < self.l_road:
            self.cars[pos[-1] + speed] = speed


auto = Auto(l_road=100, maxT=150, p=0.5, carCnt=16)
auto.run()
