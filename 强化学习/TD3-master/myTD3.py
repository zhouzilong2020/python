from keras.models import Sequential
from keras.layers import Dense
import numpy as np
import tensorflow as tf
from tensorflow import keras


class Actor():
    def __init__(self, state_dim, action_dim, max_action):
        # 搭建神经网络模型
        self.model = Model()
        super(Actor, self).__init__()
        self.layer1 = Linear(input_dim = state_dim, units = 256, activation = "relu")
        self.layer2 = Linear(256, 256)
        self.layer3 = Linear(256, action_dim)

        self.max_action = max_action

    def call(self, state):
        pass
# model = Sequential()
# 3 增加网络层
# model.add(Dense(units=5, activation='relu',input_dim=2)) 
# #输入层需要input_dim参数，较特殊, units则是指input的下一层
# model.add(Dense(units=2, activation= 'softmax'))  # ，输出2节点
# 4 编译模型
# model.compile(loss='categorical_crossentropy', optimizer='sgd', metrics=['accuracy'])
# 5 训练和预报
# model.fit(Xtrain, ytrain, epochs=100, batch_size=5)
# classes = model.predict(Xtest, batch_size=5)
