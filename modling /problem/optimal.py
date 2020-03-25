from math import sin, pi
from random import random, randint

# 估计sin（x）在0-pi上的最大值，x为给定起始点，N为循环次数
def optimal_sin(x = 0, N = 1000):
    y = sin(x)
    for i in range(N):
        dx = random()
        if randint(0,1):
            dx = -dx
        new_x = x+dx
        new_y = sin(new_x)
        if y < new_y and  0 <= new_x <= pi:
            y = new_y
            x = new_x
    return y
        
print(f"{optimal_sin(0, 1000):0.8f}")