import cv2

# importing cascades xml
face_cascade = cv2.CascadeClassifier('cascades\haarcascade_frontalface_default.xml')


class Camera:

    def __init__(self):
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        self.video.release()

    def get_frame(self):
        ret, img = self.video.read()
        img = cv2.resize(img, (600,400))
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, x + h), (255, 0, 0), 2)
        ret, jpeg = cv2.imencode('.jpg', img)
        return jpeg.tobytes()
