import cv2
import numpy as np
import sys

global image,drawing,topLeft,botRight
drawning = 0
mode = True
topLeft=[-1,-1]
botRight=[-1,-1]

def mouse_click(event, x, y, flags, param):
	global drawing, topLeft, botRight
	if event == cv2.EVENT_LBUTTONDOWN:
		drawing =1 
		topLeft[0]=x
		topLeft[1]=y
		botRight[0]=-1
		botRight[1]=-1
	elif event == cv2.EVENT_MOUSEMOVE:
		if drawning ==1:
			botRight[0]=x
			botRight[1]=y
	elif event == cv2.EVENT_LBUTTONUP:
		botRight[0]=x
		botRight[1]=y
		drawing =2
		imgROI=img[topLeft[1]:botRight[1], topLeft[0]:botRight[0]]
		cv2.destroyWindow('ROI')
		cv2.imshow('ROI',imgROI)
		cv2.waitKey(1)

def main():
	cv2.imshow("image",img)
	cv2.namedWindow('image')
	cv2.setMouseCallback('image',mouse_click)
	while(1):
		img2=img.copy()
		if botRight[0]!=-1 & botRight[1]!= -1:
			cv2.rectangle(img2,tuple(topLeft),tuple(botRight),(0,255,0),2)
			cv2.imshow('image',img2)

		k=cv2.waitKey(1)&0xff
		if(k==27):
			break
	cv2.destroyAllWindows()


if len(sys.argv)>1:
	img=cv2.imread(sys.argv[1])
	main()
else:
	print("Usage: python3 mouse_ROI.py imageFile")
