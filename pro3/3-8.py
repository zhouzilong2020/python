str1 = list(input())
N = len(str1)
for i in range(N//2):
    tem = str1[i]
    str1[i] = str1[N-1-i]
    str1[N-1-i] = tem
print(''.join(str1))