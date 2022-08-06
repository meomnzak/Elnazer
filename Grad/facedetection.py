import cv2


face_cascade = cv2.CascadeClassifier(
    'cascades/haarcascade_profileface.xml')

faceCascade2 = cv2.CascadeClassifier(
    'cascades/haarcascade_frontalface_default.xml')

camera = cv2.VideoCapture(0)
while (cv2.waitKey(1) == -1):
    success, frame = camera.read()
    if success:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faceFront = faceCascade2.detectMultiScale(
            gray, 1.3, 5, minSize=(30, 30))
        facesL = face_cascade.detectMultiScale(
            gray, 1.3, 5, minSize=(30, 30))
        # 1 code to flip horizontaly
        flipped = cv2.flip(gray , 1)
        facesR = face_cascade.detectMultiScale(flipped , 1.3  , 5 ,  minSize=(30, 30)  )
        for (x, y, w, h) in faceFront:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            roi_gray = gray[y:y+h, x:x+w]
        for (x, y, w, h) in facesL:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
            roi_gray = gray[y:y+h, x:x+w]
            """
        for (x, y, w, h) in facesR: 
            cv2.rectangle(frame, (x+10,y), ((x+w+50), y+h), (0, 0, 255), 2)
            roi_gray = gray[y:y+h, x:x+w]
            """
        cv2.imshow('Face Detection', frame)
        key = cv2.waitKey(1)
        if key == 27:
            break
camera.release()
cv2.destroyAllWindows() 