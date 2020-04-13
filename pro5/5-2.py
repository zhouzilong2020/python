cnt = 0
weight = 0
N = int(input())
for i in range(N):
    newline = eval(input())
    # 这里是遍历的key
    for j in newline:
        for k in newline[j]:
            cnt+=1
            weight+=newline[j][k]
        # weight+=
print(f"{N} {cnt} {weight}")