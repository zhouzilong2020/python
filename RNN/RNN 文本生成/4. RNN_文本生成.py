import tensorflow as tf

import numpy as np
import os
import time

## 
# 初始化处理数据
##
path_to_file = tf.keras.utils.get_file('shakespeare.txt', 'https://storage.googleapis.com/download.tensorflow.org/data/shakespeare.txt')
# 读取并为 py2 compat 解码
text = open(path_to_file, 'rb').read().decode(encoding='utf-8')

# 需要筛选出非重复的字符集
vocab = sorted(set(text))

# 创建从非重复字符到索引的映射
# 一个字符对应一个编码：你-->1 好-->2

# char2idx是一个字典，汉字是key，数字编码是value
char2idx = {u:i for i, u in enumerate(vocab)}
# idx2char是数组。ind2char[2]就是2编码的汉字
idx2char = np.array(vocab)

# 将文本全部转化为数字编码
text_as_int = np.array([char2idx[c] for c in text])

##
# RNN开始：对于每一个时间步骤进行预测下一个字符
##

# 设定每个输入句子长度的最大值
seq_length = 100
examples_per_epoch = len(text)//seq_length

# 创建训练样本 / 目标
# 该函数吧文本响亮转换为字符索引流
char_dataset = tf.data.Dataset.from_tensor_slices(text_as_int)

# batch方法将吧单个字符转换为需要的长度序列
sequences = char_dataset.batch(seq_length+1, drop_remainder=True)


# 建立一个每次向后移一个位置的映射
def split_input_target(chunk):
    input_text = chunk[:-1]
    target_text = chunk[1:]
    return input_text, target_text

dataset = sequences.map(split_input_target)
##
# 创建训练批次
##
# 批大小
BATCH_SIZE = 64

# 设定缓冲区大小，以重新排列数据集
# （TF 数据被设计为可以处理可能是无限的序列，
# 所以它不会试图在内存中重新排列整个序列。相反，
# 它维持一个缓冲区，在缓冲区重新排列元素。） 
BUFFER_SIZE = 10000

dataset = dataset.shuffle(BUFFER_SIZE).batch(BATCH_SIZE, drop_remainder=True)

##
# 建立模型
##
# 词集的长度
vocab_size = len(vocab)
# 嵌入的维度
embedding_dim = 256
# RNN 的单元数量
rnn_units = 1024

def build_model(vocab_size, embedding_dim, rnn_units, batch_size):
    model = tf.keras.Sequential([
        tf.keras.layers.Embedding(vocab_size, embedding_dim,
                              batch_input_shape=[batch_size, None]),
        tf.keras.layers.GRU(rnn_units,
                        return_sequences=True,
                        stateful=True,
                        recurrent_initializer='glorot_uniform'),
        tf.keras.layers.Dense(vocab_size)
    ])
    return model

model = build_model(
  vocab_size = len(vocab),
  embedding_dim=embedding_dim,
  rnn_units=rnn_units,
  batch_size=BATCH_SIZE)



# 定义损失函数
def loss(labels, logits):
  return tf.keras.losses.sparse_categorical_crossentropy(labels, logits, from_logits=True)

# 编译模型
model.compile(optimizer='adam', loss=loss)


## 配置检查点：检查中间过程的行为
# 检查点保存至的目录
checkpoint_dir = './training_checkpoints'
# 检查点的文件名
checkpoint_prefix = os.path.join(checkpoint_dir, "ckpt_{epoch}")
checkpoint_callback=tf.keras.callbacks.ModelCheckpoint(
    filepath=checkpoint_prefix,
    save_weights_only=True)

# 训练次数
EPOCHS=5

# 训练模型
history = model.fit(dataset, epochs = EPOCHS, callbacks=[checkpoint_callback])

# 生成文本
def generate_text(model, start_string):
  # 评估步骤（用学习过的模型生成文本）

  # 要生成的字符个数
  num_generate = 1000

  # 将起始字符串转换为数字（向量化）
  input_eval = [char2idx[s] for s in start_string]
  input_eval = tf.expand_dims(input_eval, 0)

  # 空字符串用于存储结果
  text_generated = []

  # 低温度会生成更可预测的文本
  # 较高温度会生成更令人惊讶的文本
  # 可以通过试验以找到最好的设定
  temperature = 1.0

  # 这里批大小为 1
  model.reset_states()
  for i in range(num_generate):
      predictions = model(input_eval)
      # 删除批次的维度
      predictions = tf.squeeze(predictions, 0)

      # 用分类分布预测模型返回的字符
      predictions = predictions / temperature
      predicted_id = tf.random.categorical(predictions, num_samples=1)[-1,0].numpy()

      # 把预测字符和前面的隐藏状态一起传递给模型作为下一个输入
      input_eval = tf.expand_dims([predicted_id], 0)

      text_generated.append(idx2char[predicted_id])

  return (start_string + ''.join(text_generated))

print(generate_text(model, start_string=u"ROMEO: "))