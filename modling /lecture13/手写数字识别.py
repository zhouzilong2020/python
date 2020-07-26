import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from ImageDigit import ImageDigit
# 导入训练数字
img = Image.open(r"/Users/zhouzilong/Desktop/python/modling /lecture13/numbers.jpeg")
i_d = ImageDigit(img)
# 背景阈值
i_d.convert_to_bw(142)
digits = i_d.split()
i_d.to_32_32(r"/Users/zhouzilong/Desktop/python/modling /lecture13/train")
# 提取训练集合特称
X, y = i_d.featureExtract()


# 导入测试数字
img = Image.open(r"/Users/zhouzilong/Desktop/python/modling /lecture13/test_digit.png")
i_d = ImageDigit(img)
# 背景阈值
i_d.convert_to_bw(200)
digits = i_d.split()
i_d.to_32_32(r"/Users/zhouzilong/Desktop/python/modling /lecture13/test")
# 提取测试集合特征
X_test, y_test = i_d.featureExtract()


from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report

# 建立神经网络模型
clf = MLPClassifier(hidden_layer_sizes=(256, 128, 64,), alpha=1e-6,\
                    max_iter = 5000,\
                    random_state=1,\
                    verbose = True)
# 训练样本集
clf.fit(X, y)
# 得到预测集合
y_hat = clf.predict(X_test)
# 预报结果
print(classification_report(y_test, y_hat,zero_division=False))