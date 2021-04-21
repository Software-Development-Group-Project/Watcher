import cv2

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cwd = os.getcwd()
detector = cv2.CascadeClassifier(os.path.join(cwd, "cascades/haarcascade_frontalface_default.xml"))
sampleNum = 0

while True:
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        sampleNum += 1
        cv2.imwrite(os.path.join(cwd, "dataset\\testing\\nirahulan"+"."+str(sampleNum)+".jpg"), img[y:y+h, x:x+w])
        #cv2.imwrite(os.path.join(cwd, "dataset\\training\\nirahulan"+"."+str(sampleNum)+".jpg"), img[y:y+h, x:x+w])
        cv2.imshow('dataset'+str(sampleNum), img)

    if cv2.waitKey(100) & 0xFF == ord('q'):
        break
    elif sampleNum > 100:
        break

cam.release()
cv2.destroyAllWindows()