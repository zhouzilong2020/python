N = int(input())
if N == 0:
    print("0.00000000")
elif N ==1:
    print("1.00000000")
else:
    l = [1]
    for i in range(2, N):
        l.append(i*l[i-2])
    print(l)
    r = [1/i for i in l]
    print(f"{sum(r)+1:.8f}")