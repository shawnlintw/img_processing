import cv2
import numpy as np
#import matplotlib.pyplot as plt

global img
global point1,point2,point3,point4
global click_times
global pts1,pts2
pts1=[]
pts2=[]
global x1,x2,y1,y2
#global x1,x2,y1,y2
def on_mouse(event, x, y, flag, param):
	global img, point, point2, click_times,pts1,pts2,x1,x2,y1,y2
	img2 = img.copy()

	if event ==cv2.EVENT_LBUTTONDOWN:
		point = (x,y)
		click_times= click_times+1
		if click_times <=4 :
			pts1.append(list(point))
			print(pts1)
		elif click_times >4 & click_times <=8:
			if click_times ==5:
				x1=x
				y1=y
			if click_times ==7:
				x2=x
				y2=y
			pts2.append(list(point))
			print(pts2)
		cv2.circle(img2,point,10, (0,255,0), 5)
		cv2.imshow('image', img2)

		if click_times>=8 :
			rows=pts2[2][0]-pts2[0][0];
			cols=pts2[2][1]-pts2[0][0];
			print(rows)
			print(cols)
			pts1 = np.float32(pts1)
			pts2 = np.float32(pts2)

			M=cv2.getPerspectiveTransform(pts1,pts2)
			res = cv2.warpPerspective(img,M,(rows,cols))
			cv2.imshow('result',res)
	
	elif event == cv2.EVENT_MOUSEMOVE and (flag & cv2.EVENT_FLAG_LBUTTON):
		pass
	elif event == cv2.EVENT_LBUTTONUP:
		pass


def main():
	global img
	global click_times
	click_times=0
	img=cv2.imread('../../img/left02.jpg')
	cv2.namedWindow('image')
	cv2.setMouseCallback('image', on_mouse)
	cv2.imshow('image', img)
	cv2.waitKey(0)

if __name__ == '__main__':
	main()
