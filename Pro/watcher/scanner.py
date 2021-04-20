# import the necessary packages
import os
import cv2
import sqlite3
import logging
import threading
import numpy as np
from PIL import Image
from datetime import datetime
from mail_server import MailServer

# to stop warnings tensorflow cuda driver
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
logging.getLogger("tensorflow").setLevel(logging.ERROR)
logging.getLogger('tensorflow').setLevel(logging.FATAL)

import tensorflow as tf
from tensorflow.keras.models import load_model

# to stop warnings tensorflow cuda driver
tf.autograph.set_verbosity(3)
tf.get_logger().setLevel(logging.ERROR)

# importing cascades xml, face mask model and face recog model
face_cascade = cv2.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')
face_mask_detect_model = load_model('cascades/model-017.model')
face_recog_model = load_model('cascades/face_recognition.h5')

# connecting to the database and retreiving members
connection = sqlite3.connect('members.db')
cursor = connection.cursor()  # creating cursor instance for db to execute sql statement
query = "SELECT name, email FROM Members ORDER BY name ASC"  # face recognition model classes are ordered by members name
cursor.execute(query)
results = cursor.fetchall()

# using the database to retrieve their names and mail
mails = [result[1] for result in results]  # storing mails in array
users = [result[0] for result in results]  # storing user names in array

# used to send email
# count dictionary used to identify whether to send email imdietly or not
# if the user detected without mask for the first time then mail will be send to the user and admin
# after the first alert mail, mail will be send to the user and admin in 10 min break
# this is helpfull for frames
count = [0 for result in results]
mailed_time = [datetime.now() for result in results]
detected_time = [datetime.now() for result in results]

# closing the connection with database
connection.close()

# dict that used show label based on model prediction
status = {0: 'MASK', 1: 'NO MASK'}


class Scanner:

    def __init__(self):
        self.video = cv2.VideoCapture(0)  # connecting to the webcam using opencv
        self.video.set(cv2.CAP_PROP_FPS, 100)  # setting the frames
        self.mail_server = MailServer()  # creating instance of mail server

    def __del__(self):
        self.video.release()  # video connection will be released when the instance of Scanner class garbage collected

    # returning frames
    def get_frame(self):
        ret, img = self.video.read()  # reading the frames from source and returning boolean (to denote success) and captured frame
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # converting the frame to gray because face mask detection model doesn't require RGB frame
        face = face_cascade.detectMultiScale(gray, 1.3, 5)  # searching for faces using the cascade classifier

        for (x, y, w, h) in face:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)  # showing red rectangle over the detected face
            resized = cv2.resize(gray, (100, 100))  # resizing the detected face (part of the frame) to 100x100
            normalized = resized / 255.0  # Optimization. so values for input layer will be 0-1
            reshaped = np.reshape(normalized, (1, 100, 100, 1))  # reshaping the numpy array (part of the frame)
            result = face_mask_detect_model.predict(reshaped)  # passing the reshaped numpy array to the model and storing the probablity of class array
            state = np.argmax(result, axis=1)[0]  # geting the index of the class which have the highest probablity

            if state == 1:  # if the user without mask detected
                cv2.putText(img, status[state], (x, (y - 10)), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)  # showing test "NO MASK" over the detected face
                face_img = img[y:y + h, x:x + w]  # croping the images/frame to detected face and storing in the variable

                if type(face_img) is np.ndarray:  # if the face_img is an numpy array
                    resized_face_img = cv2.resize(face_img, (64, 64))  # resizing the image to 64x64
                    resized_int_face_img = Image.fromarray(resized_face_img, 'RGB')  # converting float values in numpy array to int values (0-255)
                    img_array = np.array(resized_int_face_img)  # converting the image to numpy array
                    img_array = np.expand_dims(img_array, axis=0)  # converting three demnsional array to sigle demensional
                    pred = face_recog_model.predict(img_array)  # passing the reshaped numpy array to the model and storing the probablity of class array
                    id = pred.argmax()  # getting the index of the class which have the highest probablity
                    name = users[id]  # getting the predicted user's name
                    to = mails[id]  # getting the predicted user's mail
                    detected_time[id] = datetime.now()  # updating the predicted time
                    self.send_alert(id, name, to)  # calling the send_alert method which will send alert mail

                cv2.putText(img, str(name).upper() + " - " + str(pred[0][id]), (x, (y + h + 22)),
                            cv2.FONT_HERSHEY_SIMPLEX, .7, (255, 255, 255), 2)  # showing the detected user's name over the face

        ret, jpeg = cv2.imencode('.jpg', img)  # encoding np.arry to jpg image
        return jpeg.tobytes()  # returing the jpg images as bytes

    # using thread to send email which will be help full to show video with less lag
    def create_alert_thread(self, name, to):
        mail_thread = threading.Thread(target=self.mail_server.create_mail, args=(name, to))  # creating thread
        mail_thread.start()  # starting thread

    # sending alert to detected user and admin
    def send_alert(self, id, name, to):
        difference = detected_time[id] - mailed_time[id]  # finding the difference between lastly detected time and lastly mailed time
        difference_in_sec = difference.total_seconds()  # converting datatime obj to seconds
        minutes = divmod(difference_in_sec, 60)[0]  # converting sec to min

        # if user/member detected for the first time then send the mail immediatly
        if count[id] == 0:
            self.create_alert_thread(name, to)
            mailed_time[id] = datetime.now()  # updating the lastly mailed time for the specific member
            count[id] += 1  # increasing count id for the specific member

        # if mail already sent before and difference between detected time and mailed time is 10 then sending the next mail
        elif count[id] >= 0 and minutes >= 10:
            self.create_alert_thread(name, to)
            mailed_time[id] = datetime.now()  # updating the mailed time for the spcific user
