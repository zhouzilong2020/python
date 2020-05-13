A, B = map(int,input().split())
cnt = 0
Sum = 0
for i in range(A, B+1):
    cnt += 1
    Sum += i
    print(f"{i:5}", end='')
    if cnt % 5 == 0:
        print()
else:
    if cnt % 5 != 0:
        print()
    print(f"Sum = {Sum}")