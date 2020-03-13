N = int(input())
str_set = []
max_len = 0
pos = 0
for i in range(N):
    str_set.append(input())
    if len(str_set[i]) > max_len:
        max_len = len(str_set[i])
        pos = i
print(f"The longest is: {str_set[pos]}")

