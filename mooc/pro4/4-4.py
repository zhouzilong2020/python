from math import sqrt
def isPrime(x):
    if x == 2 or x == 3:
        return True
    # 任何一个大于六的素数一定在六的倍数的两边
    if x%6 != 1  and x%6 != 5: 
        return False 
    p = int(sqrt(x))
    # 虽然在6的倍数两边，也可能是5或者7的倍数
    for i in range(5, p+1, 6):
        if x%i == 0 or x%(i+2) == 0:
            return False
    return True


even = int(input())
for i in range(2, even):
    if isPrime(i) and isPrime(even-i):
        print(f"{even} = {i} + {even-i}")
        break
