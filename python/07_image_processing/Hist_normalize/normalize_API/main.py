import cv2
import sys

if __name__ == '__main__':
	if len(sys.argv)>1 :
		src = cv2.imread(sys.argv[1],cv2.IMREAD_ANYCOLOR)
	else:
		print ("Usge: python3 normailze.py imageFile")
	dst = cv2.normalize(src,None,255,0,cv2.NORM_MINMAX,cv2.CV_8U)

	cv2.imshow("src",src)
	cv2.imshow("dst",dst)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
