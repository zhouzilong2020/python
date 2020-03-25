# 二分法取中间的值m
# 比较f(a), f(b), f(m)的符号
# 用m取代同号
# 当a，b足够小的时候可以认为结束
from math import *
def equation(a,b,c):
    delta = b*b-4*a*c
    if delta>=0:
        root1=(-b+sqrt (delta))/(2*a)
        root2=(-b-sqrt (delta))/(2*a)
        return [root1,root2]
    else:
        return [ ]
    
ans = equation(24,-600,471)

# 遗传优化算法可以根据执行的次数来动态的调节学习速率
