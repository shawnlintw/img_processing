# -*- coding: utf-8 -*-
import cv2
import sys

if __name__=="__main__":
	if len(sys.argv)>1:
		image=cv2.imread(sys.argv[1])
	else:
		print("Usage: python load_img.py imageFile")

cv2.imshow("image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()

