from math import sqrt

def getMeNprime(N, prime):
    if N == 1:
        return [2]
    
    pos = int(sqrt(N))
    checklist = getMeNprime(pos, prime[:pos+1])
    # 可以优化复制结果的范围
    for i in range(len(checklist)):     
        prime[i] = checklist[i]

    for i in prime[pos : ]:
        for j in checklist:
            if j != 0 and i%j == 0 and i!=j:
                prime[prime.index(i)] = 0
                break
    return prime

M, N = map(int, input().split())
num = [i for i in range(2, N+1)]
if len(num) > 0:
    prime = set(getMeNprime(N+1, num))
    result = []
    for i in range(M, N+1):
        if i in prime:
            result.append(i)
    print(f"{len(result)} {sum(result)}")
else:
    print("0 0")