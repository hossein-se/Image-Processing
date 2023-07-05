import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

image1 = cv.imread('Clear.jpg')
noisy_img = cv.imread('Degraded.jpg')
cleaned_img = cv.medianBlur(noisy_img, 3)

sub_image = cv.subtract(image1, noisy_img)
mse_1 = cv.mean(sub_image ** 2)[0]
sub_image_clear  = cv.subtract(image1, cleaned_img)
mse_2 = cv.mean(sub_image_clear  ** 2)[0]

print("MSE_1: ", round(mse_1,3))
print("MSE_2: ", round(mse_2,3))

cv.imshow('original_img.jpg', image1)
cv.imshow('noisy_img.jpg', noisy_img)
cv.imshow('remove_salt_and_pepper_image.jpg', cleaned_img)

cv.imwrite('original_img.jpg',image1)
cv.imwrite('noisy_img.jpg',noisy_img)
cv.imwrite('remove_salt_and_pepper_image.jpg',cleaned_img)

cv.waitKey(0)
cv.destroyAllWindows()