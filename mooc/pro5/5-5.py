line = input().split()
char = input()
cnt = 0
for i in line:
    if i == char:
        cnt += 1
print(cnt)