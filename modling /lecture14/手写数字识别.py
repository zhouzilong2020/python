import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from ImageDigit import ImageDigit
# 导入训练数字
img = Image.open(r"/Users/zhouzilong/Desktop/python/modling /lecture14/numbers.jpeg")
i_d = ImageDigit(img)
# 背景阈值
i_d.convert_to_bw(142)
digits = i_d.split()
i_d.to_32_32(r"/Users/zhouzilong/Desktop/python/modling /lecture14/train")
# 提取训练集合特称
X_train, y_train = i_d.featureExtract()


# 导入测试数字
img = Image.open(r"/Users/zhouzilong/Desktop/python/modling /lecture14/test_digit.png")
i_d = ImageDigit(img)
# 背景阈值
i_d.convert_to_bw(200)
digits = i_d.split()
i_d.to_32_32(r"/Users/zhouzilong/Desktop/python/modling /lecture14/test")
# 提取测试集合特征
X_test, y_test = i_d.featureExtract()


from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report
from keras.models import Sequential
# 利用keras建模
model = Sequential()
from keras.layers import Dense
model.add(Dense(units = 512, activation = 'relu', input_dim=256))
model.add(Dense(units = 10, activation = 'softmax'))
model.compile(loss = 'categorical_crossentropy', optimizer='AdaDelta', metrics = ['accuracy'])

model.fit(X_train, y_train, epochs=100, batch_size=5)
loss_and_metrics = model.evaluate(X_test, y_test, batch_size=10)

classes = model.predict(X_test, batch_size=5)
predict = np.argmax(classes,axis=1)  
# 找每行最大元素位置，根据正交编码，最大值位置就是类
ytrue=np.argmax(y_test,axis=1)
print(classification_report(ytrue,predict))