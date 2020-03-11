import math
import itertools 
height = list(map(int, input().split())) #map返回一个迭代器，使用list函数将起转化为列表
sum = 0
cunt = 0
for i in height:
    sum += i
    cunt+=1
average = sum/cunt
for j in height:
    if j > average:
        print(f"{j}", end= ' ')