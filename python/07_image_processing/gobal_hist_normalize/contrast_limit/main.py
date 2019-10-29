import cv2
import numpy as np
import sys

if __name__ =="__main__":
	if len(sys.argv)>1:
		src = cv2.imread(sys.argv[1],cv2.IMREAD_GRAYSCALE)
	else:
		print("Usge: python3 CLAHE.py imageFile")
	clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
	dst = clahe.apply(src)

	cv2.imshow("src", src)
	cv2.imshow("dst", dst)

	cv2.waitKey(0)
	cv2.destroyAllWindows()
