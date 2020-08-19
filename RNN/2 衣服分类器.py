import tensorflow as tf 
from tensorflow import keras

import numpy as np
import matplotlib.pyplot as plt

fashion_mnist = keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
# 将灰度值转化到0-1的范围内
train_images = train_images / 255.0
test_images = test_images / 255.0

# 搭建模型
model = keras.Sequential([
    # 输入层，一个28*28的矩阵，flatten将其转化为一个一维数组
    keras.layers.Flatten(input_shape=(28, 28)),
    # 隐藏层，激活函数为relu
    keras.layers.Dense(128, activation='relu'),
    # 输出层次
    keras.layers.Dense(10)
])

# 使用的是稀疏分类下的交叉熵
model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])
model.fit(train_images, train_labels, epochs=20)
test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)

# 将结果softmax，输出概率预测概率
probability_model = tf.keras.Sequential([model, 
                                         tf.keras.layers.Softmax()])
print('\nTest accuracy:', test_acc)