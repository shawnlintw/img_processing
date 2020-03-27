import cv2
import numpy as np
import math

cap= cv2.VideoCapture(0)
cv2.namedWindow('image')

while(cap.isOpened()):
	ret,frame=cap.read()
	frame = cv2.flip(frame,1)
	kernel = np.ones((3,3),np.uint8)
	
	roi=frame[700:1150, 100:550]

	cv2.rectangle(frame, (700,100),(1150,550), (255,0,0),4)


	cv2.imshow('image',frame)
	k=cv2.waitKey(5)&0xff
	if k==27:
		break

cap.release()
cv2.destroyAllWindows()
