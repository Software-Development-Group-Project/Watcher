from time import sleep
import cv2, os
cwd = os.getcwd()

def face_dataset_creater(username, path, numberOfImages):    
    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    detector = cv2.CascadeClassifier(os.path.join(cwd, "cascades/haarcascade_frontalface_default.xml"))
    sampleNum = 0

    while True:
        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = detector.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            sampleNum += 1
            if(os.path.exists(path)) is False:
                os.mkdir(path)    
            cv2.imwrite(os.path.join(path, username+"."+str(sampleNum)+".jpg"), img[y:y+h, x:x+w])
        cv2.putText(img, ("Image No  : "+str(sampleNum)), (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
        cv2.putText(img, ("Image More: "+str(numberOfImages-sampleNum)), (20, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
        cv2.imshow('dataset', img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        elif cv2.waitKey(1) & 0xFF == ord('w'):
            sleep(20)
        elif sampleNum > numberOfImages:
            break

    cam.release()
    cv2.destroyAllWindows()


username = str(input("Enter user name? [use simple letter] "))

print("\n* Take images in different ligtings condition \n* Press w to wait for 10 seconds [Program become not responding for a while]\n* Press q to stop the program\n")

path = os.path.join(cwd, "testing\\"+username)
face_dataset_creater(username, path, 11000)

path = os.path.join(cwd, "training\\"+username)
face_dataset_creater(username, path, 4000)