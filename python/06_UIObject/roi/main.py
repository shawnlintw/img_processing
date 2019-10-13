import cv2

global img
global point1,point2

def on_mouse(event, x, y, flag, param):
	global img, point1, point2
	img2 = img.copy()
	if event ==cv2.EVENT_LBUTTONDOWN:
		point1 =(x,y)
		cv2.circle(img2,point1,10, (0,255,0), 5)
		cv2.imshow('image', img2)
	elif event == cv2.EVENT_MOUSEMOVE and (flag & cv2.EVENT_FLAG_LBUTTON):
		cv2.rectangle(img2, point1, (x,y), (255,0,0), 5)
		cv2.imshow('image', img2)
	elif event == cv2.EVENT_LBUTTONUP:
		point2 = (x,y)
		cv2.rectangle(img2, point1, point2, (0,0,255),5)
		cv2.imshow('image', img2)

def main():
	global img
	img=cv2.imread('../../img/lean.jpg')
	cv2.namedWindow('image')
	cv2.setMouseCallback('image', on_mouse)
	cv2.imshow('image', img)
	cv2.waitKey(0)

if __name__ == '__main__':
	main()
