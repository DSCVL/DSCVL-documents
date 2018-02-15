import numpy as np
import cv2

# Capture frame
video = cv2.VideoCapture(0)

ret, frame = video.read()
height = np.size(frame, 0)
width = np.size(frame, 1)

# Define x and y position to place dot
x = width/2
y = height/2
while(True):
	ret, frame = video.read()
	frame[y:x, y:x] = (0,255,0) # mark x y position with green box
	cv2.imshow('frame', frame)	# overlay on frame
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# Clean exit
video.release()
cv2.destroyAllWindows()