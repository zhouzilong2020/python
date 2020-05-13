weight = [7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
M = ['1' ,'0' ,'X' ,'9' ,'8' ,'7' ,'6' ,'5' ,'4' ,'3' ,'2']
N = int(input())
flag = False
for i in range(N):
    id = list(input())
    z = 0
    for k in range(17):
        try:
            int(id[k])
        except:
            print(''.join(id))
            flag = True
            break
        z = ( z + int(id[k]) * (weight[k]) )
    else :
        if M[z%11] != id[-1]:
            # 用前面的分隔符号来链接后面的！
            print(''.join(id))
            flag = True

if flag == False:
    print("All passed")


    
    
