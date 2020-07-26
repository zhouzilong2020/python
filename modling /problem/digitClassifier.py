import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.datasets import load_digits
from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report

digits = load_digits()
X = digits.data
y = digits.target
# 归一化处理
scaler = MinMaxScaler(feature_range=(0,1))
scaler.fit(X)

# 正交化处理
label_y = LabelBinarizer().fit_transform(y)
X_train, X_test, y_train, y_test = train_test_split(X, label_y, test_size = .1)
# 建立神经网络模型
clf = MLPClassifier(hidden_layer_sizes=(100,), alpha=1e-5,\
                    max_iter = 5000,\
                    random_state=1,\
                    verbose = True)
# 训练样本集
clf.fit(X_train, y_train)
# 得到预测集合
y_hat = clf.predict(X_test)
# 预报结果
print(classification_report(y_test, y_hat,zero_division=False))