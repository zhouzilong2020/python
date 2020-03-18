# a = [1, 2, 3]
# b = a
# # a,b指向一个东西
# a += [3, 4]
# # a被赋予了一个新的地址
# a = a+[1, 3]

# 综合来看：
#     append()不会改变内存地址，这是list的一个方法
#     +=也不会
#     而+则返回了一个新的地址

#######九宫格优化问题
# 不断交换，如果两行、两列、对角线的绝对值之差的和减小了，则保留交换
# ***list[start:end:step]一种遍历方法

import math
from random import randint
# loss函数判断是否有优化
def loss(A):
    row1 = sum(A[:3])
    row2 = sum(A[3:6])
    row3 = sum(A[6:])
    col1 = sum(A[::3])
    col2 = sum(A[1::3])
    col3 = sum(A[2::3])
    diag1 = sum(A[0::4])
    diag2 = sum(A[6:0:-2])
    s = abs(row1-row2)+abs(row2-row3)
    s+= abs(col1-col2)+abs(col2-col3)
    s+= abs(diag1-diag2)
    return s

def print9(A):
    for i in range(9):
        if i%3 ==0:
            print()
        print(A[i], end=' ')
    print()

# 并不是循环次数越多越好，可能陷入一个局部最优解，从而阻止了最优解的发生
for i in range(100):
    B = list(range(1, 10))
    b_eval = 100000
    A = B.copy()
    for j in range(100):
        # 得到移动
        p1, p2= randint(0,8), randint(0,8)
        A[p1], A[p2] =  A[p2], A[p1]
        a_eval = loss(A)

        if a_eval < b_eval:
            # 更新棋盘和估值
            B = A
            b_eval = a_eval
        elif b_eval == 0:
            # 得到最优
            break
        else:
            # 如果估值更差，取消移动
            A[p1], A[p2] =  A[p2], A[p1]
    if b_eval == 0:
        print("！！！get answer！！！")
        break

print9(B)
