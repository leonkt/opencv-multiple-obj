import numpy as np
import cv2

lower = np.array([33,80,40])
upper = np.array([102,255,255])
cam = cv2.VideoCapture(0)


while True:
	returned, img = cam.read()
	img = cv2.resize(img, (340, 220))
	imgV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
	mask = cv2.inRange(imgV, lower, upper)
	kernelO = np.ones((5,5))
	kernelC = np.ones((20,20))

	maskOpen = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernelO)
	maskClose = cv2.morphologyEx(maskOpen, cv2.MORPH_CLOSE, kernelC)

	i2, contours, h = cv.findContours(maskClose.copy(), cv.CV_RETR_EXTERNAL, CV_CHAIN_APPROX_SIMPLE)
	cv2.drawContours(img, contours, -1, (255,0,0), 3)
	for i in range(len(contours)):
		x,y,w,h = cv2.boundingRect(conts[i])

	cv2.imshow("Camera", img)
	cv2.imshow("Masked General", mask)
	cv2.imshow("Masked Close", maskClose)	
	cv2.imshow("Open", maskOpen)
	cv2.waitKey(10)

