str1 = list(input())
d = {}
result = [0, ]
for i in str1:
    if i.upper() not in result and i.lower() not in result and i.isalpha():
        result.append(i)
        result[0]+=1
    if result[0] == 10:
        print(''.join(result[1:]))
        break
else:
    print("not found")
