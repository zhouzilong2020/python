def f(x):
    global fibonacci
    if x <= len(fibonacci):
        return fibonacci[x-1]
    else:
        for i in range(len(fibonacci), x):
            fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
        return fibonacci[x-1]

fibonacci = [1,1]
N = int(input())
if N < 1 or N >46:
    print("Invalid.")
elif N ==1:
    print(f"{1:11}")
else:
    f(N)
    for i, item in enumerate(fibonacci):
        print(f"{item:11}", end='')
        if i%5 == 4:
            print()
    if N%5!=0:
        print()
