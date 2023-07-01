import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


#read image
img1 = cv.imread('bell.jpg',cv.IMREAD_COLOR)
img2 = cv.imread('blur.jpg',cv.IMREAD_COLOR)
img2 = cv.resize(img2, (300, 300))

#gaussian
gauss = cv.GaussianBlur(img2, (7,7), 0)



cv.waitKey(0)
cv.destroyAllWindows()