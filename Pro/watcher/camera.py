# import the necessary packages
from keras.models import load_model
import cv2
import numpy as np

# importing cascades xml
face_cascade = cv2.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')
model = load_model('cascades/model-017.model')
labels_dict={0:'MASK',1:'NO MASK'}
color_dict={0:(0,255,0),1:(0,0,255)}

class Camera:

    def __init__(self):
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        self.video.release()

    def get_frame(self):
        # --- Earlier version ----
        ret, img = self.video.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)        

        for (x, y, w, h) in faces:
            # cv2.rectangle(img, (x, y), (x + w, x + h), (255, 0, 0), 2)
            face_img=gray[y:y+w,x:x+w]
            resized=cv2.resize(face_img,(100,100))
            normalized=resized/255.0
            reshaped=np.reshape(normalized,(1,100,100,1))
            result=model.predict(reshaped)

            label=np.argmax(result,axis=1)[0]
        
            cv2.rectangle(img,(x,y),(x+w,y+h),color_dict[label],2)
            cv2.rectangle(img,(x,y-40),(x+w,y),color_dict[label],-1)
            cv2.putText(img, labels_dict[label], (x, y-10),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,255),2)
            
        ret, jpeg = cv2.imencode('.jpg', img)
        return jpeg.tobytes()