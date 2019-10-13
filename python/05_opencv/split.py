import cv2
import numpy as np


img=cv2.imread("../img/clouds.jpg",1)
(b,g,r)=cv2.split(img)

cv2.imshow("img",img)
cv2.imshow("Blue channel",b)
cv2.imshow("Green channel",g)
cv2.imshow("Red channel",r)
cv2.waitKey(0)
cv2.destroyAllWindows()
