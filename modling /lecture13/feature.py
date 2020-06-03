from PIL import Image
import numpy as np
def featureExtract(im):
    im = im.convert("1")
    y = np.array([0, 1])
    features = []  # 将32*32的小图像分割成256个2*2的范围，统计每个2*2的小方框中，像素值为0的个数，由此将每个字符表达为256个数字组成的向量
    for j in range(16):
        x = np.array([0, 1])
        for i in range(16):
            box = (x[0], y[0], x[1] + 1, y[1] + 1)  # 2*2小区间，开区间
            t = im.crop(box).copy()
            count = 0.0
            for ii in range(2):
                for jj in range(2):
                    pixel = t.getpixel((ii, jj))
                    if (pixel < 1):
                        count += 1.0
            features.append(count)
            x = x + 2  # np.array+2整个矩阵向右平移
        y = y + 2
    return features


