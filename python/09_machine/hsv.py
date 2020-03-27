import cv2
import numpy as np

cap=cv2.VideoCapture(0)
cv2.namedWindow('image')

High_H=179
Low_H=0

High_S=255
Low_S=0

High_V=255
Low_V=0

width=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)+0.5)
height=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)+0.5)
fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
out=cv2.VideoWriter('output.mov',fourcc,20.0,(width,height))

def nothing(x):
	pass

cv2.createTrackbar('Low_H','image',0,179,nothing)
cv2.createTrackbar('High_H','image',179,179,nothing)

cv2.createTrackbar('Low_S','image',0,255,nothing)
cv2.createTrackbar('High_S','image',255,255,nothing)

cv2.createTrackbar('Low_V','image',0,255,nothing)
cv2.createTrackbar('High_V','image',255,255,nothing)

while(cap.isOpened()):
	ret,frame = cap.read()
	
	vlowH=cv2.getTrackbarPos('Low_H','image')
	vhighH=cv2.getTrackbarPos('High_H','image')
	vlowS=cv2.getTrackbarPos('Low_S','image')
	vhighS=cv2.getTrackbarPos('High_S','image')
	vlowV=cv2.getTrackbarPos('Low_V','image')
	vhighV=cv2.getTrackbarPos('High_V','image')
	
	hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
	lower_hsv= np.array([vlowH, vlowS, vlowV])
	high_hsv = np.array([vhighH, vhighS, vhighV])
	mask = cv2.inRange(hsv, lower_hsv, high_hsv)
	frame= cv2.bitwise_and(frame, frame, mask=mask)
	cv2.imshow('image',frame)
	out.write(frame)
	k=cv2.waitKey(5)&0xff
	if k==27:
		break

print("LOW H:",vlowH,"S: ",vlowS, "V: ",vlowV,"\n")
print("High H:", vhighH,"S:",vhighS ,"V: ",vhighV,"\n")
out.release()
cap.release()
cv2.destroyAllWindows()
