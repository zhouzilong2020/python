N = int(input())
l = [[2,1]]
for i in range(N-1):
    l.append([sum(l[i]), l[i][0]])
for i, item in enumerate(l):
    l[i] = item[0]/item[1]
print(f"{sum(l):.2f}")
    
