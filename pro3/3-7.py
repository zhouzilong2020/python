# 本题要求编写程序，找出给定的n个数中的最大值及其对应的最小下标（下标从0开始）。
# 输入格式:
# 输入在第一行中给出一个正整数n（1<n≤10）。第二行输入n个整数，用空格分开。
# 输出格式:
# 在一行中输出最大值及最大值的最小下标，中间用一个空格分开。
# 输入样例:
# 6
# 2 8 10 1 9 10
# 输出样例:
# 10 2
N = int(input())
num = list(input().split())
# 初始化为第一个数字，以防止负数
max_num = int(num[0])
pos = {}
for i in range(N):
    num[i] = int(num[i])
    if num[i] not in pos:
        pos[ num[i] ] = i
    if num[i]  > max_num:
        max_num = num[i]
print(f"{max_num} {pos[max_num]}")

