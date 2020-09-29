# include the HSV and YCrCb 

import cv2
import numpy as np
import math

cap= cv2.VideoCapture(0)
cv2.namedWindow('image')

while(cap.isOpened()):
	ret,frame=cap.read()
	frame = cv2.flip(frame,1)
	
	frame = cv2.resize(frame, (640,360))
	
	#frame = cv2.equalizeHist(frame)

	frame_HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	HSV_mask = cv2.inRange(frame_HSV, (0,15,0),(17,170,255))
	HSV_mask = cv2.morphologyEx(HSV_mask, cv2.MORPH_OPEN, np.ones((5,5), np.uint8))
	HSV_result = cv2.bitwise_not(HSV_mask)


	frame_YCrCb = cv2.cvtColor(frame, cv2.COLOR_BGR2YCrCb)

	YCrCb_mask = cv2.inRange(frame_YCrCb,(0,135,85),(255,180,135))
	YCrCb_mask = cv2.morphologyEx(YCrCb_mask, cv2.MORPH_OPEN, np.ones((5,5), np.uint8))
	YCrCb_result = cv2.bitwise_not(YCrCb_mask)

	global_mask = cv2.bitwise_and(YCrCb_mask, HSV_mask)
	global_mask = cv2.medianBlur(global_mask,3)
	global_mask = cv2.morphologyEx(global_mask, cv2.MORPH_OPEN, np.ones((4,4),np.uint8))
	#global_mask = cv2.morphologyEx(global_mask, cv2.MORPH_CLOSE, np.ones((6,6), np.uint8))
	global_result = cv2.bitwise_not(global_mask)
	#kernel = np.ones((3,3),np.uint8)
	
	#roi=frame[700:1150, 100:550]

	#cv2.rectangle(frame, (700,100),(1150,550), (255,0,0),4)

	cv2.imshow('image',frame)
	cv2.imshow('HSV', HSV_result)
	cv2.imshow('YCrCb', YCrCb_result)
	cv2.imshow('Result', global_result)
	k=cv2.waitKey(5)&0xff
	if k==27:
		break

cap.release()
cv2.destroyAllWindows()
