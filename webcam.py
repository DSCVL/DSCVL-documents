import numpy as np
import cv2
 

video = cv2.VideoCapture(0)

ret, frame = video.read()
height = np.size(frame, 0)
width = np.size(frame, 1)

x = width/2
y = height/2
while(True):
	ret, frame = video.read()
	frame[y:x, y:x] = (0,255,0)
	cv2.imshow('frame', frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

video.release()
cv2.destroyAllWindows()