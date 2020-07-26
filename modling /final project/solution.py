import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.datasets import load_digits
from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import classification_report

data = np.loadtxt("/Users/zhouzilong/Desktop/python/modling /final project/data.txt")
X = data[ : ,0 :4]
y = data[ : ,4 :7]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = .1)





# 建立神经网络模型
clf = MLPRegressor(hidden_layer_sizes=(1024, 2048, 2048, 1024,), alpha=1e-5,\
                    max_iter = 5000,\
                    random_state=1,\
                    verbose = True)
# 训练样本集
clf.fit(X_train, y_train)
# 得到预测集合
y_hat = clf.predict(X_test)

loss = y_hat - y_test
print(loss)
