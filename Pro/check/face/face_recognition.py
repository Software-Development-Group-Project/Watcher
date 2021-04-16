import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

import tensorflow as tf
tf.autograph.set_verbosity(0)

import logging
logging.getLogger("tensorflow").setLevel(logging.ERROR)

import cv2
from keras.models import load_model
import numpy as np
from PIL import Image

cwd = os.getcwd()
model = load_model(os.path.join(cwd, 'model\\face_recognition.h5'))
face_cascade = cv2.CascadeClassifier(os.path.join(cwd, "cascades\haarcascade_frontalface_default.xml"))
# classes={0:"jenoshanan", 1:'nirahulan', 2:'thuwarakan', 3:'unknown', 4:'vithu'} 
classes={0:"jenoshanan", 1:'nirahulan', 2:'thuwarakan', 3:'vithu'} 

cam = cv2.VideoCapture(0)
while True:
    ret, frame = cam.read()
    faces = face_cascade.detectMultiScale(frame, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        face = frame[y:y+h, x:x+w]
        if type(face) is np.ndarray:
            face = cv2.resize(face, (64, 64))
            img = Image.fromarray(face, 'RGB')
            img_array = np.array(img)
            img_array = np.expand_dims(img_array, axis=0)
            pred = model.predict(img_array)
            label = classes[pred.argmax()]
        cv2.putText(frame, str(label), (x, y), cv2.FONT_HERSHEY_SIMPLEX, .7, (0, 255, 0), 2)
    cv2.imshow('frame', frame)
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
