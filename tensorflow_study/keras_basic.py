import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layer


# Define Sequential model with 3 layers
model = keras.Sequential(
    [
        # 这里的2是两个参数？
        layers.Dense(2, activation="relu", name="layer1"),
        layers.Dense(3, activation="relu", name="layer2"),
        layers.Dense(4, name="layer3"),
    ]
)

# 此外，还可以通过model.add(layer) 来添加层次
# pop 函数也可以删除一个层次，行为类似于stack
# Call model on a test input
x = tf.ones((3, 3))
y = model(x)