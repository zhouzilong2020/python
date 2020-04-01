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
    if(len(lines[0].split()) > 1):
        for line in lines:
            line = list(map(float, line.split()))
            data.append(line)
    else:
        for line in lines:
            line = float(line)
            data.append(line)
    return data
