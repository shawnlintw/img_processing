import cv2
import numpy as np

#mouse callback function
def mouse_click(event,x,y,flags,param):
	#print("event:",event )
	if event == cv2.EVENT_LBUTTONDOWN:
		print("Left Button Down")


img=np.zeros((512,512,3),np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',mouse_click)
while(1):
	cv2.imshow('image',img)
	k=cv2.waitKey(1)&0xff
	if(k==27):
		break
cv2.destroyAllWindows()
