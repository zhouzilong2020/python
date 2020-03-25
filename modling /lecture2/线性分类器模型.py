
# # # 分类器线性模型
type1 = [[5.1, 3.5 ],  [4.9, 3. ],  [4.7, 3.2], [4.6, 3.1], [5. , 3.6], [5.4, 3.9],
       [4.6, 3.4], [5. , 3.4 ], [4.4, 2.9], [4.9, 3.1]]
type2 = [[5.5, 2.6 ],  [6.1, 3. ],  [5.8, 2.6], [5. , 2.3], [5.6, 2.7],
       [5.7, 3. ],  [5.7, 2.9],  [6.2, 2.9], [5.1, 2.5],  [5.7, 2.8]]
sign1 = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
sign2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]


def loss(x, y, a, b):
    tem=[]
    for sample, sign in zip(x,y):
        # 求出每一个样本在当前系数下的评估
        one = [sample[i]*a[i] for i in range(len(sample))]
        # 评估的系数乘上其真实分类指标
        t = (sum(one) + b)*sign
        # tem存贮所有的评估数值
        tem.append(t)
    # s记录所有的偏离数值
    s = 0
    for t in tem:
        # 如果评估数值为负则说明判断错误，记录损失中
        if t < 0:
            s += -t
    return s, tem

# 给予初始的学习速率进行线性分类,这里每一次返回当前学习速率的学习次数
def linearSensor(r):
    # 给予初始值
    a, b = [1,1], 1
    # 给予学习速率
    # r = 0.1
    # 初始化样本
    X = type1+type2
    Y = sign1+sign2
    for i in range(100):
        # 进行评估，得到当前损失
        s, tem = loss(X,Y,a,b)
        for j in range(len(tem)):
            # 对于每一次误判，进行梯度下降学习
            if tem[j] < 0:
                a[0] += r*Y[j]*X[j][0]
                a[1] += r*Y[j]*X[j][1]
                b += r*Y[j]
        else: print(f"after {i:2} study, ther current model is {a[0]:.03f}x1+{a[1]:.03f}x2+{b:.03f} = 0, the loss is {s:.2f}")
        # 误判损失为零，说明当前学习完成
        if s == 0:
                print("model studey completed!")
                return i
                break
    else: return 999
        
#  在一定的处置情况下选择最优的学习速率
def optimalR():
    r = [1/i for i in range(1, 1000)]
    optimal = 0
    cnt = 100000
    for i in r:
        if cnt > linearSensor(i):
            optimal = i
            cnt = linearSensor(i)
    return optimal


def showPlot(x, y, a, b):
    xvalue=[x[i][0] for i in range(len(x))]

    xmin=min(xvalue)
    xmax=max(xvalue)
    xp=[xmin,xmax]
    yp=[-a[0]/a[1]*xmin-b/a[1],-a[0]/a[1]*xmax-b/a[1]]
    cls1x=[x[i][0] for i in range(len(x)) if y[i]==-1]
    cls2x=[x[i][0] for i in range(len(x)) if y[i]==1]
    cls1y=[x[i][1] for i in range(len(x)) if y[i]==-1]
    cls2y=[x[i][1] for i in range(len(x)) if y[i]==1]
    plot(cls1x,cls1y,'b^')
    plot(cls2x,cls2y,'r^')
    plot(xp,yp)
    show()


# optimalRate = optimalR()
optimalRate = 0.0315
linearSensor(optimalRate)
