str1 = list(input().lstrip())
c = input().strip()
result = []
for i in str1:
    if i != c.lower() and i != c.upper() and i != c:
        result.append(i)
# 将result由list转化为一个串
result = ''.join(result)
# 将result先用split() 切片，注意，其中的多个空格将被认为是一个分隔符
# 再用单个空格符链接
result = ' '.join(result.split())
print(f"result: {result}")