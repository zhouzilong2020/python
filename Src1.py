import time

mySum = 0
bg = time.clock()
for i in range(1, 100000):
    mySum = 0
    for i in range(1 ,100):
        mySum = mySum+i
dur1 = time.clock() - bg
print(f"Running time for iteration:{dur1}")

bg = time.clock()
for i in range(1, 100000):
    mySum = sum([int(number) for number in range(1, 100)])
dur2 = time.clock() - bg
print(f"Running time for 列表解析式:{dur2}")
