import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def split(im):  # im为去除背景后的整个图像
    assert im.mode == '1'
    w, h = im.size
    xs = [0, 31, 65, 91, 122, 150, 182, 211,242, 271,  w]
    ys = [0, 47, 93, 137, 185,232, h]
    for i, x in enumerate(xs):
        if i + 1 >= len(xs):
            break
        for j, y in enumerate(ys):
            if j + 1 >= len(ys):
                break
            box = (x, y, xs[i + 1], ys[j + 1])  # 一个字符所在图像的位置
            t = im.crop(box).copy()  # 将字符挖出来
            t.save("/Users/zhouzilong/Desktop/python/modling /lecture13/digit/" + str((i + 1) % 10) + "_" + str(j) + ".bmp")

def to_32_32(im, ii, jj):
    im = im.convert("L")
    w, h = im.size  # 校图像的宽、高
    xrow = []
    ycol = []
    for i in range(w):
        for j in range(h):
            pixel = im.getpixel((i, j))  # 返回某一点的像素值
            if (pixel < 1):
                xrow.append(i)
                ycol.append(j)
    xLength = max(xrow) - min(xrow) + 1
    yLength = max(ycol) - min(ycol) + 1  # 得到字符的长度宽度
    box = (min(xrow), min(ycol), max(xrow) + 1, max(ycol) + 1)
    t = im.crop(box).copy()  # 从当前的图像中返回一个矩形区域的拷贝。变量box是一个四元组，定义了左、上、右和下的像素坐标
    xStart = (32 - xLength) // 2
    yStart = (32 - yLength) // 2  # 居中
    bg = Image.new('RGB', (32, 32), 'white')
    bg.paste(t, (xStart, yStart))  # 将一张图粘贴到另一张图像上




im=Image.open(r"/Users/zhouzilong/Desktop/python/modling /lecture13/numbers.jpeg").convert('L')
img = np.array(im)

# 灰度256级模式,调整二值分割
plt.figure("hist")
arr=img.flatten()
n, bins, patches = plt.hist(arr, bins=256, density =1, facecolor='green', alpha=0.75)  
# plt.show()

im = im.point(lambda x: 255 if x > 142 else 0) #大于阈值，取白色，否则像素值置0，黑色
# im.show()

# 切割数字
xs = [0, 31]
ys = [0, 47]
box=(xs[0],ys[0],xs[1],ys[1])
t = im.crop(box).copy()
t.show()

#
