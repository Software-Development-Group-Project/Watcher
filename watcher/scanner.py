# import the necessary packages
import os
import cv2
import sqlite3
import logging
import threading
import numpy as np
import face_recognition
from datetime import datetime
from mail_server import MailServer
import tensorflow as tf
from tensorflow.keras.models import load_model

# importing cascades xml, face mask model and face recog model
face_cascade = cv2.CascadeClassifier('./assets/models/haarcascade_frontalface_default.xml')
# importing face mask detection custom CNN model
face_mask_detect_model = load_model('./assets/models/face_mask.h5')

# dict that used show label based on model prediction
status = {0: 'MASK', 1: 'NO MASK'}

#  --------------------------------------- Uncomment after updating the member database -----------------------------------------------

# cursor = self.member_connection.cursor()
# query = "SELECT name, email, imageLocation FROM Members ORDER BY name ASC"
# cursor.execute(query)
# results =  cursor.fetchall()

# mails = [result[1] for result in results]
# count = [0 for result in results]
# mailed_time = [datetime.now() for result in results]
# detected_time = [datetime.now() for result in results]
# known_face_encodings = [
#     face_recognition.face_encodings(face_recognition.load_image_file(result[5])) for result in results
# ]
# known_face_names = [result[0] for result in results]

#  --------------------------------------- Uncomment after updating the member database -----------------------------------------------

#  ------------------------------------------- Delete after updating the member database ---------------------------------------------

# Given an image, return the 128-dimension face encoding for each face in the image.
nirahulan_image = face_recognition.load_image_file("./assets/faces/nirahulan.jpg")
nirahulan_face_encoding = face_recognition.face_encodings(nirahulan_image)[0]

jenoshanan_image = face_recognition.load_image_file("./assets/faces/jenoshanan.jpg")
jenoshanan_face_encoding = face_recognition.face_encodings(jenoshanan_image)[0]

vithushigan_image = face_recognition.load_image_file("./assets/faces/vithushigan.jpg")
vithushigan_face_encoding = face_recognition.face_encodings(vithushigan_image)[0]

ashwinth_image = face_recognition.load_image_file("./assets/faces/ashwinth.jpg")
ashwinth_face_encoding = face_recognition.face_encodings(ashwinth_image)[0]

known_face_encodings = [
    nirahulan_face_encoding,
    jenoshanan_face_encoding,
    vithushigan_face_encoding,
    ashwinth_face_encoding
]

known_face_names = [
    "Nirahulan",
    "Jenoshanan",
    "Vithushigan",
    "Ashwinth",
]

#  ------------------------------------------- Delete after updating the member database ---------------------------------------------

class Scanner:

    def __init__(self):
        self.mail_server = MailServer()  # creating instance of mail server
        self.video = cv2.VideoCapture(0)  # connecting to the webcam using opencv
        self.face_locations = []
        self.face_encodings = []
        self.face_names = []
        self.process_this_frame = True

    def __del__(self):
        self.video.release()  # video connection will be released when the instance of Scanner class garbage collected

    # returning frames
    def get_frame(self):
        ret, frame = self.video.read()  # reading the frames from source and returning boolean (to denote success) and captured frame        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # converting the frame to gray because face mask detection model doesn't require RGB frame
        face = face_cascade.detectMultiScale(gray, 1.3, 5)  # searching for faces using the cascade classifier

        for (x, y, w, h) in face:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)  # showing red rectangle over the detected face
            resized = cv2.resize(gray, (100, 100))  # resizing the detected face (part of the frame) to 100x100
            normalized = resized / 255.0  # Optimization. so values for input layer will be 0-1
            reshaped = np.reshape(normalized, (1, 100, 100, 1))  # reshaping the numpy array (part of the frame)
            result = face_mask_detect_model.predict(reshaped)  # passing the reshaped numpy array to the model and storing the probablity of class array
            state = np.argmax(result, axis=1)[0]  # geting the index of the class which have the highest probablity

            if state == 1:  # if the user without mask detected
                cv2.putText(frame, status[state], (x, (y - 10)), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)  # showing test "NO MASK" over the detected face
                small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25) # Resize frame of video to 1/4 size for faster face recognition processing
                rgb_small_frame = small_frame[:, :, ::-1] # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)

                # Only process every other frame of video to save time
                if self.process_this_frame:
                    # Find all the faces and face encodings in the current frame of video
                    self.face_locations = face_recognition.face_locations(rgb_small_frame)
                    self.face_encodings = face_recognition.face_encodings(rgb_small_frame, self.face_locations)

                    self.face_names = []
                    for face_encoding in self.face_encodings:
                        # See if the face is a match for the known face(s)
                        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                        name = "Unknown"

                        # use the known face with the smallest distance to the new face
                        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                        best_match_index = np.argmin(face_distances)
                        if matches[best_match_index]:
                            name = known_face_names[best_match_index]

#  --------------------------------------- Uncomment after updating the database -----------------------------------------------

                            # self.send_alert(name, mails[best_match_index])

#  --------------------------------------- Uncomment after updating the database -----------------------------------------------


                        self.face_names.append(name)


                self.process_this_frame = not self.process_this_frame

                # Display the results
                for (top, right, bottom, left), name in zip(self.face_locations, self.face_names):
                    # Scale back up face locations since the frame we detected in was scaled to 1/4 size
                    top *= 4
                    right *= 4
                    bottom *= 4
                    left *= 4

                    # Draw a box around the face
                    cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

                    # Draw a label with a name below the face
                    cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
                    font = cv2.FONT_HERSHEY_DUPLEX
                    cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
                
        ret, jpeg = cv2.imencode('.jpg', frame)  # encoding np.arry to jpg image
        return jpeg.tobytes()  # returing the jpg images as bytes

#  ----------------------------------------- Email function currently unavialable ----------------------------------------------

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
