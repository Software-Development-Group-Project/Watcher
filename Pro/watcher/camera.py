# import the necessary packages
import os
import cv2
import numpy as np
import tensorflow as tf
import logging
from keras.models import load_model
from PIL import Image
from time import sleep

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
tf.autograph.set_verbosity(0)
logging.getLogger("tensorflow").setLevel(logging.ERROR)

# importing cascades xml
face_cascade = cv2.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')
face_mask_detect_model = load_model('cascades/model-017.model')
face_recog_model = load_model('cascades/face_recognition.h5')

labels_dict = {0: 'MASK', 1: 'NO MASK'}
color_dict = {0: (0, 255, 0), 1: (0, 0, 255)}
classes={0:"jenoshanan", 1:'nirahulan', 2:'thuwarakan', 3:'vithu'} 

class Camera:

    def __init__(self):
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        self.video.release()

    def get_frame(self):
        
        ret, img = self.video.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        face = face_cascade.detectMultiScale(gray, 1.3, 5)
        
        for (x, y, w, h) in face:
            
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            resized = cv2.resize(gray, (100, 100))
            normalized = resized / 255.0
            reshaped = np.reshape(normalized, (1, 100, 100, 1))
            result = face_mask_detect_model.predict(reshaped)
            label = np.argmax(result, axis=1)[0]

            if(label == 1):
        
                face_img = img[y:y+h, x:x+w]
        
                if type(face_img) is np.ndarray:

                    resized_face_img = cv2.resize(face_img, (64, 64))
                    resized_int_face_img = Image.fromarray(resized_face_img, 'RGB')
                    img_array = np.array(resized_int_face_img)
                    img_array = np.expand_dims(img_array, axis=0)
                    pred = face_recog_model.predict(img_array)
                    label = classes[pred.argmax()]
        
                cv2.putText(img, str(label), (x, y), cv2.FONT_HERSHEY_SIMPLEX, .7, (0, 255, 0), 2)

            # cv2.rectangle(img, (x, y), (x + w, y + h), color_dict[label], 2)
            # # cv2.rectangle(img, (x, y - 40), (x + w, y), color_dict[label], -1)
            # cv2.putText(img, labels_dict[label], (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)        
            
        ret, jpeg = cv2.imencode('.jpg', img)
        return jpeg.tobytes()
