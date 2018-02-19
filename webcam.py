import numpy as np
import cv2


cascade = cv2.CascadeClassifier('lbpcascade_frontalface_improved.xml')

video = cv2.VideoCapture(0)
while(True):
    ret, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces_default = cascade.detectMultiScale(gray, 1.3, 4)
    for (x,y,w,h) in faces_default:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        cv2.putText(frame,str(x)+", "+str(y),(x,y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 1, cv2.LINE_AA)
    cv2.imshow('frame',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()