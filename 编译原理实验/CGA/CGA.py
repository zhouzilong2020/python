import numpy as np
import numpy.random as npr


class Cell:
    _n = 0
    digits = None
    value = 0

    def __init__(self, n):
        if n % 2 == 0:
            self._n = n
        else:
            self._n = n + 1
        self.digits = npr.randint(0, 10, self._n)

    def duplicate(self, father1, father2, bg, ed):
        self.digits[:bg] = father1.digits[:bg]
        self.digits[bg:ed] = father2.digits[bg:ed]
        self.digits[ed:] = father1.digits[ed:]

    def crossover(self, rhs):
        # 交叉起始位置
        bg = int(npr.randint(self._n))
        # 交叉长度
        len = int(npr.randint(self._n) + 1)
        # 交叉终止位置
        ed = bg + len

        son1 = Cell(self._n)
        son2 = Cell(self._n)

        # 复制染色体
        son1.duplicate(self, rhs, bg, ed)
        son2.duplicate(rhs, self, bg, ed)

        return son1, son2

    def mutation(self):
        son = Cell(self._n)
        son.digits = self.digits.copy()
        pos = npr.randint(self._n)
        son.digits[pos] = npr.randint(0, 10)
        return son


class Species1:
    cells = []
    evalFunc = None
    digit_num = 0
    bestPos = 0
    worstPos = 0
    population = 0
    _mP = 10
    _cP = 90
    _t = 100

    def __init__(self, population, digit_num, mP, cP, t, evalFunc):
        self.population = population
        self.digit_num = digit_num
        self._cP = cP
        self._mP = mP
        self._t = t
        self.evalFunc = evalFunc

        for i in range(population):
            cell = Cell(digit_num)
            cell.eval = evalFunc(cell.digits)
            self.cells.append(cell)

    def reset(self):
        self.cells.clear()
        for i in range(self.population):
            cell = Cell(self.digit_num)
            cell.eval = self.evalFunc(cell.digits)
            self.cells.append(cell)

    # 找最好的个体位置
    def findBestWorst(self):
        self.cells.sort(key=lambda o: o.eval)
        self.bestPos = 0
        self.worstPos = self.population - 1

    def getBestNeighborPos(self, i):
        pos = []
        if i - 10 >= 0:
            pos.append(i - 10)
        if i + 10 < self.population:
            pos.append(i + 10)
        if (i - 1) % 10 == i % 10 and i - 1 >= 0:
            pos.append(i - 10)
        if (i + 1) % 10 == i % 10 and i + 1 < self.population:
            pos.append(i + 10)
        best = self.cells[pos[0]]
        for p in pos:
            if best.eval > self.cells[p].eval:
                best = self.cells[p]
        return best

    def crossover(self):
        father_pos = npr.randint(0, self.population)
        father = self.cells[father_pos]
        # 这里是向上下左右中最好的那一个学习
        mother = self.getBestNeighborPos(father_pos)

        son1, son2 = father.crossover(mother)

        son1.eval = self.evalFunc(son1.digits)  # ;// 评估第一个子代
        son2.eval = self.evalFunc(son2.digits)
        self.findBestWorst()

        if son1.eval < self.cells[self.worstPos].eval:
            self.cells[self.worstPos] = son1

        self.findBestWorst()
        if son2.eval < self.cells[self.worstPos].eval:
            self.cells[self.worstPos] = son2

    def mutation(self):
        father = self.cells[npr.randint(self.population)]
        son = father.mutation()
        son.eval = self.evalFunc(son.digits)

        self.findBestWorst()
        if son.eval < self.cells[self.worstPos].eval:
            self.cells[self.worstPos] = son

    def getAvg(self):
        avg = 0
        for cell in self.cells:
            avg += cell.eval
        return avg / self.population

    def solve(self):
        i = 0
        avg = []
        while i < self._t:
            # print(i, "---", self._t)
            for j in range(self._cP):
                self.crossover()
            for j in range(self._cP):
                self.mutation()
            # print(f"avg:{self.getAvg()}")
            # print("func value:", self.cells[self.bestPos].eval)
            i = i + 1
            avg.append(self.getAvg())

    def getBest(self):
        self.findBestWorst()
        return self.cells[0].eval


def func(digits):
    half = int(len(digits) / 2)
    x = 0
    y = 0
    for i, digit in enumerate(digits[:half]):
        x += digit * np.power(0.1, i)
    for i, digit in enumerate(digits[half:]):
        y += digit * np.power(0.1, i)
    x_y = np.power(x, 2) + np.power(y, 2)
    z1 = np.power(np.sin(np.power(x_y, 0.5)), 2) - 0.5
    z2 = np.power((1 + 0.001 * x_y), 2)
    return -(0.5 - z1 / z2)


cnt = 0
CGA = Species1(400, 4, 50, 50, 100, func)
CGA.solve()
