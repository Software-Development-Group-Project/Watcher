# import the necessary packages
import os
import cv2
import numpy as np
import tensorflow as tf
import logging
from keras.models import load_model
from PIL import Image
from datetime import datetime
from mail_server import MailServer
import threading
import multiprocessing

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
tf.autograph.set_verbosity(0)
logging.getLogger("tensorflow").setLevel(logging.ERROR)

# importing cascades xml
face_cascade = cv2.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')
face_mask_detect_model = load_model('cascades/model-017.model')
face_recog_model = load_model('cascades/face_recognition.h5')

status = {0: 'MASK', 1: 'NO MASK'}
users = {0: "jenoshanan", 1: 'nirahulan', 2: 'thuwarakan', 3: 'vithu'}
mails = {0: "jenoshanan.2019695@iit.ac.lk", 1: "nirahulan.20191022@iit.ac.lk", 2: "thuwarakan123@gmail.com",
         3: "vithushigan.20191148@iit.ac.lk"}
count = {0: 0, 1: 0, 2: 0, 3: 0}
mailed_time = {0: datetime.now(), 1: datetime.now(), 2: datetime.now(), 3: datetime.now()}
detected_time = {0: datetime.now(), 1: datetime.now(), 2: datetime.now(), 3: datetime.now()}


class Scanner:

    def __init__(self):
        self.video = cv2.VideoCapture(0)
        self.video.set(cv2.CAP_PROP_FPS, 100)

        self.mail_server = MailServer()

    def __del__(self):
        self.video.release()

    def get_frame(self):
        ret, img = self.video.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        face = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in face:

            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

            resized = cv2.resize(gray, (100, 100))
            normalized = resized / 255.0
            reshaped = np.reshape(normalized, (1, 100, 100, 1))
            result = face_mask_detect_model.predict(reshaped)
            state = np.argmax(result, axis=1)[0]

            if state == 1:

                cv2.putText(img, status[state], (x, (y - 10)), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

                face_img = img[y:y + h, x:x + w]

                if type(face_img) is np.ndarray:

                    resized_face_img = cv2.resize(face_img, (64, 64))
                    resized_int_face_img = Image.fromarray(resized_face_img, 'RGB')
                    img_array = np.array(resized_int_face_img)
                    img_array = np.expand_dims(img_array, axis=0)
                    pred = face_recog_model.predict(img_array)
                    id = pred.argmax()
                    name = users[id]
                    to = mails[id]
                    detected_time[id] = datetime.now()

                    self.send_alert(id, name, to)

                cv2.putText(img, str(name).upper() + " - " + str(pred[0][id]), (x, (y + h + 22)), cv2.FONT_HERSHEY_SIMPLEX, .7, (255, 255, 255), 2)

        ret, jpeg = cv2.imencode('.jpg', img)
        return jpeg.tobytes()

    def create_alert_thread(self, name, to):
        mail_thread = threading.Thread(target=self.mail_server.create_mail, args=(name, to))
        mail_thread.start()

    def send_alert(self, id, name, to):
        difference = detected_time[id] - mailed_time[id]
        difference_in_sec = difference.total_seconds()
        minutes = divmod(difference_in_sec, 60)[0]

        if count[id] == 0:
            self.create_alert_thread(name, to)
            mailed_time[id] = datetime.now()
            count[id] += 1

        elif count[id] >= 0 and minutes >= 10:
            self.create_alert_thread(name, to)
            mailed_time[id] = datetime.now()