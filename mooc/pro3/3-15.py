str1 = list(input())
result = []
for i in str1:
    if i not in result:
        result.append(i)
result.sort()
print(''.join(result))