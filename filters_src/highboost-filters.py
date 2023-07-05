import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


#read image
img1 = cv.imread('bell.jpg',cv.IMREAD_COLOR)
img2 = cv.imread('blur.jpg',cv.IMREAD_COLOR)
img2 = cv.resize(img2, (300, 300))

#gaussian
gauss = cv.GaussianBlur(img2, (7,7), 0)


#gmask
gmask = cv.subtract(img2,gauss)

#highboost filtering
k=14
img_unsharp = cv.addWeighted(img2, 1, gmask, k, 0)

#show results
cv.imshow('image_orginal',img2)
cv.imshow('image_gauss',gauss)
cv.imshow('image_mask',gmask)
cv.imshow('imag_final',img_unsharp)

#save results
cv.imwrite('image_orginal.jpg', img2)
cv.imwrite('image_gauss.jpg', gauss)
cv.imwrite('image_mask.jpg', gmask)
cv.imwrite('imag_final.jpg', img_unsharp)



cv.waitKey(0)
cv.destroyAllWindows()