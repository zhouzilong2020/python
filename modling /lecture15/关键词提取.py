import jieba
from collections import Counter
f = open(r'/Users/zhouzilong/Desktop/python/modling /lecture15/网站用户评价.txt','r')
lines = f.readlines()
debate=[]

for i in range(len(lines)):
    oneLine = lines[i]
    info = oneLine.split()
    debate.append(info[0]) # 取评价语
al = jieba.lcut(''.join(debate),cut_all=True) # 用户所有的评价词

al = [elem for elem in al if elem !=''] #过滤掉空格

al = dict(Counter(al)) # 形成词典，即每个词出现的频率
res = list(reversed(sorted(al.items() , key=lambda x:x[1]))) # 从大到小排序
res = list(filter(lambda x: x[1] > 2,res)) # 过滤掉出现次数小于3的词
for i in res:
    print(i)
