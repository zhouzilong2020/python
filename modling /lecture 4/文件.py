# PDB库

# f=open("filen_ame", 'mode')
# 不存在为写打开时，会自动创建

# f.readline()  一次读一行
# f.readlines() 一次全部读完，形成一个字符串列表
# for line in f: 直接将文件handler当成一个列表
# r"..." 中间的字符串全部作为raw material 不做任何转义字符使用

# 输入filename，返回该文件内包含的数据，以矩阵的方式实现
def getData(filename):
    f = open(f"{filename}", 'r')
    lines = f.readlines()
    data = []
    for line in lines:
        # split()可以将两个字符串中间的任意空格、制表符全部清除、作为分隔符号分割
        line = line.split()
        line = list(map(float, line))
        data.append(line)
    return data

dataSet = getData('lecture 4/山-变色鸢尾花瓣.txt')
typeSet = getData('lecture 4/山-变色鸢尾花瓣分类.txt')
typeSet = list(map(lambda x:x.extend(x), typeSet))
print(dataSet)
print(typeSet)