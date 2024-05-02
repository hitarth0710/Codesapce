#!/usr/bin/env python
# coding: utf-8

# # Handwritten digits recognition (using Convolutional Neural Network)

# > - 🤖 See [full list of Machine Learning Experiments](https://github.com/trekhleb/machine-learning-experiments) on **GitHub**<br/><br/>
# > - ▶️ **Interactive Demo**: [try this model and other machine learning experiments in action](https://trekhleb.github.io/machine-learning-experiments/)

# ## Experiment overview

# In this experiment we will build a [Convolutional Neural Network](https://en.wikipedia.org/wiki/Convolutional_neural_network) (CNN) model using [Tensorflow](https://www.tensorflow.org/) to recognize handwritten digits.
# 
# A **convolutional neural network** (CNN, or ConvNet) is a Deep Learning algorithm which can take in an input image, assign importance (learnable weights and biases) to various aspects/objects in the image and be able to differentiate one from the other.
# 
# ![digits_recognition_cnn.png](../../demos/src/images/digits_recognition_cnn.png)

# ## Import dependencies
# 
# - [tensorflow](https://www.tensorflow.org/) - for developing and training ML models.
# - [matplotlib](https://matplotlib.org/) - for plotting the data.
# - [seaborn](https://seaborn.pydata.org/index.html) - for plotting confusion matrix.
# - [numpy](https://numpy.org/) - for linear algebra operations.
# - [pandas](https://pandas.pydata.org/) - for displaying training/test data in a table.
# - [math](https://docs.python.org/3/library/math.html) - for calculating square roots etc.
# - [datetime](https://docs.python.org/3.8/library/datetime.html) - for generating a logs folder names.

# In[1]:


# Selecting Tensorflow version v2 (the command is relevant for Colab only).
get_ipython().run_line_magic('tensorflow_version', '2.x')


# In[4]:


import tensorflow as tf
import matplotlib.pyplot as plt
import seaborn as sn
import numpy as np
import pandas as pd
import math
import datetime
import platform

print('Python version:', platform.python_version())
print('Tensorflow version:', tf.__version__)


# ## Configuring Tensorboard
# 
# We will use [Tensorboard](https://www.tensorflow.org/tensorboard) to debug the model later.

# In[5]:


# Load the TensorBoard notebook extension.
# %reload_ext tensorboard
get_ipython().run_line_magic('load_ext', 'tensorboard')


# In[6]:


# Clear any logs from previous runs.
get_ipython().system('rm -rf ./.logs/')


# ## Load the data
# 
# The **training** dataset consists of 60000 28x28px images of hand-written digits from `0` to `9`.
# 
# The **test** dataset consists of 10000 28x28px images.

# In[7]:


mnist_dataset = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist_dataset.load_data()


# In[8]:


print('x_train:', x_train.shape)
print('y_train:', y_train.shape)
print('x_test:', x_test.shape)
print('y_test:', y_test.shape)


# In[9]:


# Save image parameters to the constants that we will use later for data re-shaping and for model traning.
(_, IMAGE_WIDTH, IMAGE_HEIGHT) = x_train.shape
IMAGE_CHANNELS = 1

print('IMAGE_WIDTH:', IMAGE_WIDTH);
print('IMAGE_HEIGHT:', IMAGE_HEIGHT);
print('IMAGE_CHANNELS:', IMAGE_CHANNELS);


# ## Explore the data
# 
# Here is how each image in the dataset looks like. It is a 28x28 matrix of integers (from `0` to `255`). Each integer represents a color of a pixel.

# In[10]:


pd.DataFrame(x_train[0])


# This matrix of numbers may be drawn as follows: 

# In[13]:


plt.imshow(x_train[0], cmap=plt.cm.binary)
plt.show()


# Let's print some more training examples to get the feeling of how the digits were written.

# In[14]:


numbers_to_display = 25
num_cells = math.ceil(math.sqrt(numbers_to_display))
plt.figure(figsize=(10,10))
for i in range(numbers_to_display):
    plt.subplot(num_cells, num_cells, i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(x_train[i], cmap=plt.cm.binary)
    plt.xlabel(y_train[i])
plt.show()


# ## Reshaping the data
# 
# In order to use convolution layers we need to reshape our data and add a color channel to it. As you've noticed currently every digit has a shape of `(28, 28)` which means that it is a 28x28 matrix of color values form `0` to `255`. We need to reshape it to `(28, 28, 1)` shape so that each pixel potentially may have multiple channels (like Red, Green and Blue).

# In[15]:


x_train_with_chanels = x_train.reshape(
    x_train.shape[0],
    IMAGE_WIDTH,
    IMAGE_HEIGHT,
    IMAGE_CHANNELS
)

x_test_with_chanels = x_test.reshape(
    x_test.shape[0],
    IMAGE_WIDTH,
    IMAGE_HEIGHT,
    IMAGE_CHANNELS
)


# In[16]:


print('x_train_with_chanels:', x_train_with_chanels.shape)
print('x_test_with_chanels:', x_test_with_chanels.shape)


# ## Normalize the data
# 
# Here we're just trying to move from values range of `[0...255]` to `[0...1]`.

# In[17]:


x_train_normalized = x_train_with_chanels / 255
x_test_normalized = x_test_with_chanels / 255


# In[18]:


# Let's check just one row from the 0th image to see color chanel values after normalization.
x_train_normalized[0][18]


# ## Build the model
# 
# We will use [Sequential](https://www.tensorflow.org/api_docs/python/tf/keras/Sequential?version=stable) Keras model.
# 
# Then we will have two pairs of [Convolution2D](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Conv2D?version=stable) and [MaxPooling2D](https://www.tensorflow.org/api_docs/python/tf/keras/layers/MaxPool2D?version=stable) layers. The MaxPooling layer acts as a sort of downsampling using max values in a region instead of averaging.
# 
# After that we will use [Flatten](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Flatten?version=stable) layer to convert multidimensional parameters to vector.
# 
# The las layer will be a [Dense](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Dense?version=stable) layer with `10` [Softmax](https://www.tensorflow.org/api_docs/python/tf/keras/activations/softmax?version=stable) outputs. The output represents the network guess. The 0-th output represents a probability that the input digit is `0`, the 1-st output represents a probability that the input digit is `1` and so on...
# 

# In[19]:


model = tf.keras.models.Sequential()

model.add(tf.keras.layers.Convolution2D(
    input_shape=(IMAGE_WIDTH, IMAGE_HEIGHT, IMAGE_CHANNELS),
    kernel_size=5,
    filters=8,
    strides=1,
    activation=tf.keras.activations.relu,
    kernel_initializer=tf.keras.initializers.VarianceScaling()
))

model.add(tf.keras.layers.MaxPooling2D(
    pool_size=(2, 2),
    strides=(2, 2)
))

model.add(tf.keras.layers.Convolution2D(
    kernel_size=5,
    filters=16,
    strides=1,
    activation=tf.keras.activations.relu,
    kernel_initializer=tf.keras.initializers.VarianceScaling()
))

model.add(tf.keras.layers.MaxPooling2D(
    pool_size=(2, 2),
    strides=(2, 2)
))

model.add(tf.keras.layers.Flatten())

model.add(tf.keras.layers.Dense(
    units=128,
    activation=tf.keras.activations.relu
));

model.add(tf.keras.layers.Dropout(0.2))

model.add(tf.keras.layers.Dense(
    units=10,
    activation=tf.keras.activations.softmax,
    kernel_initializer=tf.keras.initializers.VarianceScaling()
))


# Here is our model summary so far.

# In[20]:


model.summary()


# In order to plot the model the `graphviz` should be installed. For Mac OS it may be installed using `brew` like `brew install graphviz`.

# In[21]:


tf.keras.utils.plot_model(
    model,
    show_shapes=True,
    show_layer_names=True,
)


# ## Compile the model

# In[22]:


adam_optimizer = tf.keras.optimizers.Adam(learning_rate=0.001)

model.compile(
    optimizer=adam_optimizer,
    loss=tf.keras.losses.sparse_categorical_crossentropy,
    metrics=['accuracy']
)


# ## Train the model

# In[23]:


log_dir=".logs/fit/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=log_dir, histogram_freq=1)

training_history = model.fit(
    x_train_normalized,
    y_train,
    epochs=10,
    validation_data=(x_test_normalized, y_test),
    callbacks=[tensorboard_callback]
)


# Let's see how the loss function was changing during the training. We expect it to get smaller and smaller on every next epoch.

# In[24]:


plt.xlabel('Epoch Number')
plt.ylabel('Loss')
plt.plot(training_history.history['loss'], label='training set')
plt.plot(training_history.history['val_loss'], label='test set')
plt.legend()


# In[25]:


plt.xlabel('Epoch Number')
plt.ylabel('Accuracy')
plt.plot(training_history.history['accuracy'], label='training set')
plt.plot(training_history.history['val_accuracy'], label='test set')
plt.legend()


# ## Evaluate model accuracy
# 
# We need to compare the accuracy of our model on **training** set and on **test** set. We expect our model to perform similarly on both sets. If the performance on a test set will be poor comparing to a training set it would be an indicator for us that the model is overfitted and we have a "high variance" issue.

# ### Training set accuracy

# In[26]:


get_ipython().run_cell_magic('capture', '', 'train_loss, train_accuracy = model.evaluate(x_train_normalized, y_train)\n')


# In[27]:


print('Training loss: ', train_loss)
print('Training accuracy: ', train_accuracy)


# ### Test set accuracy

# In[28]:


get_ipython().run_cell_magic('capture', '', 'validation_loss, validation_accuracy = model.evaluate(x_test_normalized, y_test)\n')


# In[29]:


print('Validation loss: ', validation_loss)
print('Validation accuracy: ', validation_accuracy)


# ## Save the model
# 
# We will save the entire model to a `HDF5` file. The `.h5` extension of the file indicates that the model shuold be saved in Keras format as HDF5 file. To use this model on the front-end we will convert it (later in this notebook) to Javascript understandable format (`tfjs_layers_model` with .json and .bin files) using [tensorflowjs_converter](https://www.tensorflow.org/js/tutorials/conversion/import_saved_model) as it is specified in the [main README](https://github.com/trekhleb/machine-learning-experiments).

# In[30]:


model_name = 'digits_recognition_cnn.h5'
model.save(model_name, save_format='h5')


# In[31]:


loaded_model = tf.keras.models.load_model(model_name)


# ## Use the model (do predictions)
# 
# To use the model that we've just trained for digits recognition we need to call `predict()` method.

# In[32]:


predictions_one_hot = loaded_model.predict([x_test_normalized])


# In[33]:


print('predictions_one_hot:', predictions_one_hot.shape)


# Each prediction consists of 10 probabilities (one for each number from `0` to `9`). We need to pick the digit with the highest probability since this would be a digit that our model most confident with.

# In[34]:


# Predictions in form of one-hot vectors (arrays of probabilities).
pd.DataFrame(predictions_one_hot)


# In[35]:


# Let's extract predictions with highest probabilites and detect what digits have been actually recognized.
predictions = np.argmax(predictions_one_hot, axis=1)
pd.DataFrame(predictions)


# So our model is predicting that the first example from the test set is `7`.

# In[37]:


print(predictions[0])


# Let's print the first image from a test set to see if model's prediction is correct.

# In[38]:


plt.imshow(x_test_normalized[0].reshape((IMAGE_WIDTH, IMAGE_HEIGHT)), cmap=plt.cm.binary)
plt.show()


# We see that our model made a correct prediction and it successfully recognized digit `7`. Let's print some more test examples and correspondent predictions to see how model performs and where it does mistakes.

# In[39]:


numbers_to_display = 196
num_cells = math.ceil(math.sqrt(numbers_to_display))
plt.figure(figsize=(15, 15))

for plot_index in range(numbers_to_display):    
    predicted_label = predictions[plot_index]
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    color_map = 'Greens' if predicted_label == y_test[plot_index] else 'Reds'
    plt.subplot(num_cells, num_cells, plot_index + 1)
    plt.imshow(x_test_normalized[plot_index].reshape((IMAGE_WIDTH, IMAGE_HEIGHT)), cmap=color_map)
    plt.xlabel(predicted_label)

plt.subplots_adjust(hspace=1, wspace=0.5)
plt.show()


# ## Plotting a confusion matrix
# 
# [Confusion matrix](https://en.wikipedia.org/wiki/Confusion_matrix) shows what numbers are recognized well by the model and what numbers the model usually confuses to recognize correctly. You may see that the model performs really well but sometimes (28 times out of 10000) it may confuse number `5` with `3` or number `2` with `3`.

# In[40]:


confusion_matrix = tf.math.confusion_matrix(y_test, predictions)
f, ax = plt.subplots(figsize=(9, 7))
sn.heatmap(
    confusion_matrix,
    annot=True,
    linewidths=.5,
    fmt="d",
    square=True,
    ax=ax
)
plt.show()


# ## Debugging the model with TensorBoard
# 
# [TensorBoard](https://www.tensorflow.org/tensorboard) is a tool for providing the measurements and visualizations needed during the machine learning workflow. It enables tracking experiment metrics like loss and accuracy, visualizing the model graph, projecting embeddings to a lower dimensional space, and much more.

# In[41]:


get_ipython().run_line_magic('tensorboard', '--logdir .logs/fit')


# ## Converting the model to web-format
# 
# To use this model on the web we need to convert it into the format that will be understandable by [tensorflowjs](https://www.tensorflow.org/js). To do so we may use [tfjs-converter](https://github.com/tensorflow/tfjs/tree/master/tfjs-converter) as following:
# 
# ```
# tensorflowjs_converter --input_format keras \
#   ./experiments/digits_recognition_cnn/digits_recognition_cnn.h5 \
#   ./demos/public/models/digits_recognition_cnn
# ```
# 
# You find this experiment in the [Demo app](https://trekhleb.github.io/machine-learning-experiments) and play around with it right in you browser to see how the model performs in real life.
