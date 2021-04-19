# import the necessary packages
import os
import cv2
import numpy as np
import tensorflow as tf
import logging
import smtplib
from email.message import EmailMessage
from keras.models import load_model
from PIL import Image
from time import sleep
from datetime import datetime

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
mail={0:"jenoshanan.2019695@iit.ac.lk", 1:"nirahulan.20191022@iit.ac.lk", 2:"thuwarakan123@gmail.com", 3:"vithushigan.20191148@iit.ac.lk"}
# count={0:0, 1:0, 2:0, 3:0}
mailed_time={0:datetime.now(), 1:datetime.now(), 2:datetime.now(), 3:datetime.now()}
detected_time={0:datetime.now(), 1:datetime.now(), 2:datetime.now(), 3:datetime.now()}

def send_email(subject, message, to):
        msg = EmailMessage()
        msg.set_content(message)
        msg['subject'] = subject
        msg['to'] = to

        user = "watchera2019@gmail.com"
        msg['from'] = user
        password = "jsexodmjokkpcebg"

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(user, password)
        server.send_message(msg)

        server.quit()    

def create_mail(name, to):
        admin = "thuwarakan123@gmail.com"
        heading = " Watcher (alert) "
        message ="{}, put your mask immediately" .format(name)
        adminMessage = "{} is not wearing a mask, please check" .format(name)
        send_email(heading, message, to)
        send_email(heading, adminMessage, admin)

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
                    key = pred.argmax()
                    label = classes[key]
                    to = mail[key]
                    detected_time[key] = datetime.now()

                cv2.putText(img, str(label), (x, y), cv2.FONT_HERSHEY_SIMPLEX, .7, (0, 255, 0), 2)
                
                # count[key] = count[key] + 1
                # count[key] == 1 or count[key] % 200 == 0 
                
                difference = detected_time[key] - mailed_time[key]
                difference_in_sec = difference.total_seconds()
                minutes = divmod(difference_in_sec, 60)[0]
                
                print("min - " + str(minutes))

                if(minutes>=5):
                    create_mail(label, to)                
                    mailed_time[key] = datetime.now()
                

            # cv2.rectangle(img, (x, y), (x + w, y + h), color_dict[label], 2)
            # cv2.rectangle(img, (x, y - 40), (x + w, y), color_dict[label], -1)
            # cv2.putText(img, labels_dict[label], (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)        
            
        ret, jpeg = cv2.imencode('.jpg', img)
        return jpeg.tobytes()
