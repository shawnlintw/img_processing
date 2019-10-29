import cv2
import numpy as np
import sys

if __name__=="__main__":
	I = cv2.imread(sys.argv[1],cv2.IMREAD_GRAYSCALE)
	fI=I/float(255)

	gamma = 0.5

	O=np.power(fI,gamma)


	cv2.imshow("I",I)
	cv2.imshow("O",O.astype('uint8')*255)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
