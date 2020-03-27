import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('pichand.jpg')

color = ('b','g','r')
for i, col in enumerate (color):
	histr = cv2.calcHist([img],[i],None,[255],[0,250])
	plt.plot(histr,color=col)
	plt.xlim([0,256])


'''
imgYCC = cv2.cvtColor(img,cv2.COLOR_BGR2YCR_CB)
colorYCC = ('b','g','r')
for i, col in enumerate (color):
	histraa = cv2.calcHist([imgYCC],[i],None,[255],[0,255])
	plt.plot(histraa,color=col)
	plt.xlim([0,256])
'''

plt.show()

