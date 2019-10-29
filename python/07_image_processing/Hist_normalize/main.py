import cv2
import numpy as np
import sys

if __name__=="__main__":
	I=cv2.imread(sys.argv[1],cv2.IMREAD_GRAYSCALE)
	Imax=np.max(I)
	Imin=np.min(I)

	Omin, Omax=0,255

	a= float(Omax-Omin)/(Imax-Imin)
	b=Omin - a*Imin

	O=a*I+b

	O=O.astype(np.uint8)

	cv2.imshow("I",I)
	cv2.imshow("O",O)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

