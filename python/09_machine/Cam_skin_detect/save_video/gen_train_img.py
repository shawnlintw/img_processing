import numpy as np
import cv2
import os


for i in range(10):
	cap=cv2.VideoCapture("gesture_video/m{}.mov".format(i))
	frame_cnt=0
	img_cnt=500
	while(cap.isOpened()):
		ret,frame = cap.read()
		if ret ==None:
			break
		if frame is None:
			break
		cv2.imshow('test',frame)
		img_name = 'gesture_video/m'+ str(i)+'/'+str(i)+'_{}.png'.format(img_cnt)
		
		if frame_cnt ==0:
			cv2.imwrite(img_name,frame)
			img_cnt+=1
		frame_cnt +=1
		if frame_cnt >=5:
			frame_cnt=0
		if cv2.waitKey(1) & 0xff ==ord('q'):
			break
	cap.release()
	cv2.destroyAllWindows()
