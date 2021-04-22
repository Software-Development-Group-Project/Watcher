from keras.models import Sequential
from keras.layers import Activation, Flatten, Dropout, Conv2D, MaxPooling2D, Dense, BatchNormalization
from keras.callbacks import ModelCheckpoint
from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator
import numpy as np
import cv2
import os

cwd = os.getcwd()

model = Sequential()

model.add(Conv2D(32, (3, 3), input_shape=(64, 64, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(32, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Conv2D(32, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())

model.add(Dense(128, activation='relu'))
model.add(Dense(128, activation='relu'))
model.add(Dense(3, activation='softmax'))
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

train_data_gen = ImageDataGenerator(rescale=1./255, shear_range=0.2, zoom_range=0.2, horizontal_flip=True)

train_data_gen = ImageDataGenerator(rescale=1./255)

training_set = train_data_gen.flow_from_directory(os.path.join(cwd, "dataset\\training\\"), target_size=(64, 64), batch_size=32, class_mode='categorical')

testing_set = train_data_gen.flow_from_directory(os.path.join(cwd, "dataset\\testing\\"), target_size=(64, 64), batch_size=32, class_mode='categorical')

model.save(os.path.join(cwd, 'model\\face_recognition.h5'))  # or h5

model.fit_generator(training_set, steps_per_epoch=1200, epochs=15, validation_data=testing_set, validation_steps=300)

training_set.class_indices

{'nirahulan':0} # Add

