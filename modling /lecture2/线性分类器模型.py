
# # # 分类器线性模型
 def loss(x, y, a, b):
     tem=[]
     for sample, sign in zip(x,y):
         one =[sample[i]*a[i] for i in range(len(sample))]
         t = (sum(one) + b)*y
         tem.append(t)
     s = 0
     for t in tem:
         if t < 0:
             s += -t
     return s, tem

 def linearSensor():
     a = [1,1]
     b = 1
     r = 0.1
     X
     Y
     s, tem = loss(X,Y,a,b)
     for i in range(1000):
         if tem[i] < 0:
             a[0] += r*Y[i]*X[i][0]
             a[1] += r*Y[i]*X[i][1]
             b += r*Y[i]



