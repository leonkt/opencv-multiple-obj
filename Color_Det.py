import numpy as np
import cv2

lower = np.array([33,80,40])
upper = np.array([102,255,255])
cam = cv2.VideoCapture(0)


while True:
	returned, img = cam.read()
	img = cv2.resize(img, (340, 220))
	imgV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
	

	cv2.imshow("Camera", img)
	cv2.imshow("Masked General", mask)
	cv2.imshow("Masked Close", maskClose)	
	cv2.imshow("Open", maskOpen)
	cv2.waitKey(10)

