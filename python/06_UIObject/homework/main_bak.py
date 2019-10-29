import cv2
import numpy as np

cap=cv2.VideoCapture(0)
cv2.namedWindow('image')

High_H=180
Low_H=0

High_S=255
Low_S=0

High_V=255
Low_V=0


def nothing(x):
	pass

cv2.createTrackbar('Low_H','image',0,180,nothing)
cv2.createTrackbar('High_H','image',0,180,nothing)
cv2.createTrackbar('Low_S','image',0,255,nothing)
cv2.createTrackbar('High_S','image',0,255,nothing)
cv2.createTrackbar('Low_V','image',0,255,nothing)
cv2.createTrackbar('High_V','image',0,255,nothing)

while(1):
	ret,frame = cap.read()
	
	vlowH=cv2.getTrackbarPos('Low_H','image')
	vhighH=cv2.getTrackbarPos('High_H','image')
	vlowS=cv2.getTrackbarPos('Low_S','image')
	vhighS=cv2.getTrackbarPos('High_S','image')
	vlowV=cv2.getTrackbarPos('LOW_V','image')
	vhighV=cv2.getTrackbarPos('High_V','image')
	
	hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
	lower_hsv= np.array([vlowH, vlowS, vlowV])
	high_hsv = np.array([vhighH, vhighS, vhighV])
	mask = cv2.inRange(hsv, lower_hsv, high_hsv)
	frame= cv2.bitwise_and(frame, frame, mask=mask)
	cv2.imshow('image',frame)
	k=cv2.waitKey(5)&0xff
	if k==27:
		break
cv2.destroyAllWindows()
