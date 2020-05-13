num = list(input())
tem = num[0]
num[0] = num[2]
num[2] = tem
# tem记录第一个有效数字的位置
tem = 0
# 只需要判断前两个数字即可
for i in range(2):
    if num[tem] == '0':
        tem+=1
print(''.join(num[tem : ]))