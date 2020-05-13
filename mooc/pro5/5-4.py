ball = set({6,7,8,9,10})
line = list(map(int, input().split(',')))
for i in line:
    if i in ball:
        ball.remove(i)  
for i,num in enumerate(ball):
    if i+1 == len(ball):
        print(num)
    else:
         print(num, end=' ')
