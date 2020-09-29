import cv2
import matplotlib.pyplot as plot
import numpy as np

#define banana hsv range
lower_banana = np.array([24,43,46])
upper_banana = np.array([30,255,255])

#define orange hsv range
lower_orange = np.array([16,43,46])
upper_orange = np.array([20,255,255])

#define purple brussel hsv range
lower_purple = np.array([120,43,46])
upper_purple = np.array([173,255,255])

#define tomato hsv range
lower_tomato1 = np.array([0,43,46])
upper_tomato1 = np.array([10,255,255])
lower_tomato2 = np.array([175,43,46])
upper_tomato2 = np.array([180,255,255])

#define lemon hsv range
lower_lemon = np.array([30,43,46])
upper_lemon = np.array([77,255,255])

img=cv2.imread('pic/fruit.png')
img=cv2.resize(img, (640,480), interpolation=cv2.INTER_AREA)
img_HSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
b,g,r = cv2.split(img)
img=cv2.merge([r,g,b])

def color_mask(img,img_HSV, HSV_lower,HSV_upper):
    mask = cv2.inRange(img_HSV, HSV_lower, HSV_upper)
    result_image = cv2.bitwise_and(img, img, mask=mask)
    return result_image

def plot_fig(fig,sub_num, img, text):
    ax= fig.add_subplot(sub_num)
    ax.title.set_text(text)
    plot.imshow(img)

img_lemon = color_mask(img, img_HSV, lower_lemon, upper_lemon)
img_tomato1 = color_mask(img, img_HSV, lower_tomato1, upper_tomato1)
img_tomato2 = color_mask(img, img_HSV, lower_tomato2, upper_tomato2)
img_tomato = cv2.bitwise_or(img_tomato1, img_tomato2)
img_orange = color_mask(img, img_HSV, lower_orange, upper_orange)
img_purple = color_mask(img, img_HSV, lower_purple, upper_purple)
img_banana = color_mask(img, img_HSV, lower_banana, upper_banana)


fig=plot.figure()
plot_fig(fig, 231, img, 'Original')
plot_fig(fig, 232, img_banana, 'Banana')
plot_fig(fig, 233, img_tomato, 'Tomato')
plot_fig(fig, 234, img_orange, 'Orange')
plot_fig(fig, 235, img_lemon,  'Lemon')
plot_fig(fig, 236, img_purple, 'Purple')

plot.show()
plot.close()
