import numpy as np
import tensorflow as tf
import tensorflow_hub as hub
import tensorflow_datasets as tfds
from tensorflow import keras

imdb = keras.datasets.imdb

# 仅仅保留最高频率的1w个单词
(train_data, train_labels), (test_data, test_labels) = imdb.load_data(num_words=10000)