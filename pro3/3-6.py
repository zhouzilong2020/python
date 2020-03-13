# 本题要求统计一个整型序列中出现次数最多的整数及其出现次数。
# 输入格式：
# 输入在一行中给出序列中整数个数N（0<N≤1000），以及N个整数。数字间以空格分隔。
# 输出格式：
# 在一行中输出出现次数最多的整数及其出现次数，数字间以空格分隔。题目保证这样的数字是唯一的。
# 输入样例：
# 10 3 2 -1 5 3 4 3 0 3 2
# 输出样例：
# 3 4
N, *num = input().split()
d = {}
max_cnt = 0
max_num = 0
for i in num:
    if i in d:
        d[i] +=1
    else :
        d[i] = 1
    if d[i] > max_cnt:
        max_cnt = d[i]
        max_num = i
print(f"{max_num} {max_cnt}")



