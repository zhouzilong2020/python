import numpy as np
from sklearn.naive_bayes import GaussianNB
data = np.loadtxt(r"/Users/zhouzilong/Desktop/python/modling /lecture15/genderData.txt")
x = data[:, : -1]
y = data[:, -1]

x_new = np.array([[6,130,8],[7,200,13]])
bayes = GaussianNB()
model=bayes.fit(x, y)  #x是特征，y是分类
pred = model.predict(x_new)
print(pred)
