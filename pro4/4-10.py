from math import sqrt
x, y = tuple(map(int, input().split()))
x, y = (y, x) if x < y else (x, y)
x1,y1 = x,y
mod = x1%y1
while mod != 0:
    x1 = y1
    y1 = mod
    mod = x1%y1
mod = y1

# primeNum=[]
# for i in range(2, int(sqrt(x))):
#     for j in range(2, int(sqrt(i))):
#         if i%j == 0:
#             break
#     else:
#         primeNum.append(i)

factor1 ={f'{mod}':1}
factor2 ={f'{mod}':1}
while x != 1:
 
print(f"{mod}", end=' ')
