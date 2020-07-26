import numpy as np
from sklearn.datasets import load_digits
digits = load_digits()
X = digits.data
y = digits.target

# 进行成交交化处理
from keras.utils import to_categorical
y = to_categorical(y)

# 对数据进行样本集、测试集划分
from sklearn.model_selection import train_test_split
Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, test_size=.1) 


# 建立神经网络模型
from keras.models import Sequential
model = Sequential()
from keras.layers import Dense
# 输入层
model.add(Dense(units = 256, activation = 'relu', input_dim=X.shape[1]))
# 输出层
model.add(Dense(units = 10, activation = 'softmax'))
model.compile(loss = 'categorical_crossentropy', optimizer='AdaDelta', metrics = ['accuracy'])

# 进行回归
model.fit(Xtrain, ytrain, epochs=100, batch_size=5)
loss_and_metrics = model.evaluate(X, y, batch_size=10)
# 进行预测
classes = model.predict(Xtest, batch_size=5)
predict = np.argmax(classes,axis=1)  

# 结果进行判断分析
from sklearn.metrics import classification_report
ytrue=np.argmax(ytest,axis=1)
err=ytrue-predict
print(classification_report(ytrue,predict))
