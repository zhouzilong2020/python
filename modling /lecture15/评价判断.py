import numpy as np

def formFeature(lines, featureWords):  # 根据评语，获得转换矩阵
    feature=np.zeros((len(lines),len(featureWords)))  #矩阵大小为：用户评价条数*特征词数
    for i in range(feature.shape[0]):
        for j in range(feature.shape[1]):
            feature[i,j]=lines[i].count(featureWords[j])
    return feature

featureWords=['赞','差','太差','帅','起球','不好','货真价实','上当','骗子']  #特征词
f = open(r'网站用户评价.txt','r')  # 读用户评价
lines = f.readlines()
debate = []
ans = np.zeros((len(lines)))  #用户结论
for i in range(len(lines)):
    oneLine = lines[i]
    info = oneLine.split()  #对一行进行分割
    debate.append(info[0]) #用户评价语
    ans[i] = float(info[1])  #评价分类
feature = formFeature(debate,featureWords)  #获得矩阵


from sklearn.naive_bayes import GaussianNB
bayes = GaussianNB()
model=bayes.fit(feature, ans) #建模
newDebate=["店家骗子走了我的心"]  #新的两条评价
feature1 = formFeature(newDebate,featureWords)
pred = model.predict(feature1)  #预测
print(newDebate)
print(pred)
