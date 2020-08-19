import tensorflow_datasets as tfds
# import tensorflow as tf
import matplotlib.pyplot as plt

def plot_graphs(history, metric):
  plt.plot(history.history[metric])
  plt.plot(history.history['val_'+metric], '')
  plt.xlabel("Epochs")
  plt.ylabel(metric)
  plt.legend([metric, 'val_'+metric])
  plt.show()

dataset, info = tfds.load('imdb_reviews', with_info=True, as_supervised=True, download=False)
train_dataset, test_dataset = dataset['train'], dataset['test']
encoder = info.features['text'].encoder
print('Vocabulary size: {}'.format(encoder.vocab_size))
print(tfds.__path__)
# (train_data, validation_data, test_data) = tfds.load(
#     name="imdb_reviews",
#     split=('train[:60%]', 'train[60%:]', 'test'),
#     as_supervised=True)

