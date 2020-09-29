import sys
import numpy as np
import cv2
import matplotlib.pyplot as plt

def calcGrayHist(image):
	rows,cols=image.shape

	grayHist=np.zeros([256],np.uint64)
	for r in range(rows):
		for c in range(cols):
			grayHist[image[r][c]]+=1
	return grayHist

if __name__ =="__main__":
	if len(sys.argv)>1:
		image = cv2.imread(sys.argv[1], cv2.IMREAD_GRAYSCALE)
	else:
		print("Usage: python3 main.py imageFile")
		exit()
	grayHist = calcGrayHist(image)
	
	x_range = range(256)
	plt.plot(x_range, grayHist,'r', linewidth =2 ,c='black')

	y_maxValue= np.max(grayHist)
	plt.axis([0,255,0,y_maxValue])

	plt.xlabel('gray Level')
	plt.ylabel('number of pixels')
	plt.show()



