N = int(input())

if N == 0:
    print(f"{1:.8f}")
else:
    l = [1]
    for i in range(2, N+1):
        l.append(i*l[i-2])
    r = [1/i for i in l]
    print(f"{sum(r)+1:.8f}")
