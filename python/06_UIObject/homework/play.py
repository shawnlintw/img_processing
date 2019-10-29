import numpy as np
import cv2

cap=cv2.VideoCapture("output.mov")

while(cap.isOpened()):
	ret,frame=cap.read()
	
	if(ret==None):
		break
	cv2.imshow('frame',frame)
	#cv2.waitKey(33)
	if cv2.waitKey(1)&0xff==ord('q'):
		break
cap.release()
cv2.destroyAllWindows()
