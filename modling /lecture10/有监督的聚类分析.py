import numpy as np
A = np.loadtxt(r"wheat_X.txt")
B = np.loadtxt(r"wheat_Y.txt")




B[B==-1]=0
aver=A.mean(axis=0)
std=A.std(axis=0)
A=(A-aver)/std
allY=[]
for i in range(len(B)): # 转正交编码
    if (B[i]==1.0):
        oneY=[0,1]
    else:
        oneY=[1,0]  # -1
    allY.append(oneY)
Y=np.array(allY)
