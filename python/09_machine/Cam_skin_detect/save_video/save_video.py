

import cv2
import numpy as np
import math

cam = cv2.VideoCapture(0)

cv2.namedWindow("test")

img_counter =0

width = int (500)
height = int (400)

fourcc= cv2.VideoWriter_fourcc('m','p','4','v')
out= cv2.VideoWriter('output.mov',fourcc,10.0,(width,height))

def Skin_detect(img):

	frame_HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
	HSV_mask = cv2.inRange(frame_HSV, (0,15,0),(150,255,255))
	HSV_mask = cv2.morphologyEx(HSV_mask, cv2.MORPH_OPEN, np.ones((10,10), np.uint8))

	frame_YCrCb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
	YCrCb_mask = cv2.inRange(frame_YCrCb,(0,135,85),(255,190,135))
	YCrCb_mask = cv2.morphologyEx(YCrCb_mask, cv2.MORPH_OPEN, np.ones((10,10), np.uint8))

	global_mask = cv2.bitwise_and(YCrCb_mask, HSV_mask)
	global_mask = cv2.medianBlur(global_mask,3)
	global_mask = cv2.morphologyEx(global_mask, cv2.MORPH_OPEN, np.ones((4,4),np.uint8))
	global_color = cv2.bitwise_and(img, img, mask = global_mask)

	gray = cv2.cvtColor(global_color,cv2.COLOR_BGR2GRAY)
	gray = cv2.equalizeHist(gray)
	return gray

record =0

while True:

	ret, frame = cam.read()
	frame = cv2.flip(frame,1)
	kernel = np.ones((3,3),np.uint8)
	roi = frame[100:500, 700:1200]

	cv2.rectangle(frame, (700,100),(1200,500),(0,0,0),4)
	cv2.imshow("test",frame)
	gray=Skin_detect(roi)
	cv2.imshow("ROI", gray)
	if not ret:
		break
	k = cv2.waitKey(1)
	
	if record ==1:
		out.write(roi)

	if k%256 == 27:
		break
	elif k%256 ==32:
		record=1
out.release()
cam.release()
cv2.destroyAllWindows()

