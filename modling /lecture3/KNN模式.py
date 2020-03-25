from math import sqrt
class Point:
    def __init__(sefl, coor, classid):
        self.coor = coor
        self.classid = classid
        
    def dis(self, another):
        dist = 0
        for x1, x2 in zip(self.coor, another.coor):
            dist += (x1-x2)**2
        self.dist = sqrt(dist)
        

p1=Point([1,0.4],1);p2=Point([0.8,0.8],1);p3=Point([0.5,0.2],1)  # 1类
p4=Point([2,1.4],-1);p5=Point([1.8,1.8],-1);p6=Point([1.5,1.2],-1) # 2类
lp=[p1,p2,p3,p4,p5,p6];    #形成列表

px = Point([0.2, 1.7], 0)
for p in lp:
    p.dis(px)

lp.sort(key=lambda o: o.dist)
for i in range(5):
    ans+=lp[i].classid/lp[i].d
