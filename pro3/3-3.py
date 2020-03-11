str1 = list(input())
m, n = input().split()
for i in range(str1.__len__()-1, -1, -1):
    if(str1[i] == m or str1[i] == n):
        print(f"{i} {str1[i]}")