import numpy as np
import cv2
from rplidar import RPLidar
import array 
import glob
from math import sqrt, pow

 

	# function video capture and return a frame
inputvideo = cv2.VideoCapture(0)

point = ( 0,0)
color_mouse =(10, 200, 20)
line_width = 4
radius = 20 
count = 0

 

# function to click on the video with a mouse
def click_mouse( event, x, y, flags, param):

	global point, pressed, dist
	if event == cv2.EVENT_LBUTTONDOWN:
		print("pressed", x, y)
		point = (x,y)
		var = x^2 + y^2
		dist = sqrt(var)
		print("distance", dist)
# mouse actions over the video 
cv2.namedWindow("videocaptured")
cv2.setMouseCallback("videocaptured", click_mouse)


while True:

	ret, image = inputvideo.read()
	cv2.circle(image, point, radius, color_mouse, line_width)
	cv2.imshow("videocaptured", image)

	#if dist != 0:
	cv2.imwrite("frame%d.png" % count, image)
	count += 1

	if  cv2.waitKey(1) & 0xFF == ord('q'):
		break




inputvideo.release()
cv2.destroyAllWindows()