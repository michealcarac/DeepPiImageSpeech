# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 09:54:19 2019

@author: ocasciotti
"""
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.applications.vgg16 import VGG16
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.layers import Flatten, Dense, Dropout
from tensorflow.keras import Input
from tensorflow.keras.models import Model

tf.enable_eager_execution()

classes = ['none', 'one', 'ten']

datadir = os.getcwd() + '/dataset'
IMG_SHAPE = (480, 640)
batch_size = 1

image_gen = ImageDataGenerator(
                    rescale=1./255,
                    rotation_range=45,
                    horizontal_flip=False,
                    )

train_data_gen = image_gen.flow_from_directory(
                                                batch_size=batch_size,
                                                directory=datadir,
                                                shuffle=True,
                                                target_size=IMG_SHAPE,
                                                class_mode='sparse'
                                                )


load = False
train = True
if load:
    model = tf.keras.models.load_model('vgg16_model', compile=False)
    model.trainable = train
else:
    # load model and specify a new input shape for images
    new_input = Input(shape=(480, 640, 3))
    model = VGG16(include_top=False, input_tensor=new_input, classes=len(classes), weights='imagenet')
    model.trainable = False
    print(model.summary())
    last_layer = model.get_layer('block5_pool')
    last_output = last_layer.output

    x = Flatten()(last_output)
    x = Dense(128, activation='relu')(x)
    x = Dropout(0.5)(x)
    x = Dense(4, activation='softmax')(x)
    model = Model(model.input, x)

print(model.summary())

model.compile(optimizer="adam",
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

epochs = 1
tf.keras.models.save_model(model, os.getcwd() + '/vgg16_model', overwrite=True, include_optimizer=True, save_format=tf, signatures=None)
history = model.fit(train_data_gen, epochs=epochs)
tf.keras.models.save_model(model, os.getcwd() + '/vgg16_model', overwrite=True, include_optimizer=True, save_format=tf, signatures=None)
#
# converter = tf.lite.TFLiteConverter.from_keras_model(model)
# converter.optimizations = [tf.lite.Optimize.DEFAULT]
# tflite_model = converter.convert()
#
#
# # Save the model.
# with open('model.tflite', 'wb') as f:
#     f.write(tflite_model)

acc = history.history['accuracy']

loss = history.history['loss']

epochs_range = range(epochs)

plt.figure(figsize=(8, 8))
plt.subplot(1, 2, 1)
plt.plot(epochs_range, acc, label='Training Accuracy')
plt.legend(loc='lower right')
plt.title('Training and Validation Accuracy')

plt.subplot(1, 2, 2)
plt.plot(epochs_range, loss, label='Training Loss')
plt.legend(loc='upper right')
plt.title('Training and Validation Loss')
plt.show()

cap1 = cv2.VideoCapture(1)

picture = 1

while True:
    ret1, frame1 = cap1.read()
    cv2.imshow('frame1', frame1)

    key = cv2.waitKey(1) & 0xFF
    if ret1 and key == ord('p'):
        frame1 = np.expand_dims(frame1, axis=0)
        guess = np.argmax(model.predict(frame1))
        print(classes[guess])
        picture += 1
    elif key == ord('q'):
        cap1.release()
        cv2.destroyAllWindows()
        break
