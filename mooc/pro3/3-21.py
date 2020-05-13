str1 = list(input())
result = []
for i in str1:
    if i.isupper() and i not in result:
        result.append(i)
if len(result) == 0:
    print("Not Found")
else:
    print(''.join(result))