import cv2
import numpy as np

def nothing(x):
	pass
imgBGR=np.zeros((100,512,3),np.uint8)
imgHSV=np.zeros((100,512,3),np.uint8)
cv2.namedWindow('image')

cv2.createTrackbar('H','image', 0,180,nothing)
cv2.createTrackbar('S','image', 0,255,nothing)
cv2.createTrackbar('V','image', 0,255,nothing)

switch='0: OFF\n 1: ON'
cv2.createTrackbar(switch,'image', 0,1,nothing)

while(1):
	cv2.imshow('image',imgBGR)
	k=cv2.waitKey(1)&0xff
	if k==27:
		break
	H = cv2.getTrackbarPos('H','image')
	S = cv2.getTrackbarPos('S','image')
	V = cv2.getTrackbarPos('V','image')
	s = cv2.getTrackbarPos(switch,'image')

	if s==0:
		imgHSV[:]=0
	else:
		imgHSV[:]=[H,S,V]
		imgBGR=cv2.cvtColor(imgHSV,cv2.COLOR_HSV2BGR)

cv2.destroyAllWindows() 
