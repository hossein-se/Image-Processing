
import cv2
import numpy as np

# A
img = cv2.imread('car.jpg')

img = cv2.resize(img, (800, 600))

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_red = np.array([0,0,0])
upper_red = np.array([255, 255, 255])
mask1 = cv2.inRange(hsv, lower_red, upper_red)

mask = mask1
kernel = np.ones((2,2),np.float32)/50
filtered_mask = cv2.filter2D(mask,-1,kernel)

red_object = cv2.bitwise_and(img, img, mask=filtered_mask)

red_object_hsv = cv2.cvtColor(red_object, cv2.COLOR_BGR2HSV)
red_object_hsv[:,:,0] += 65
red_object_rgb = cv2.cvtColor(red_object_hsv, cv2.COLOR_HSV2BGR)

cv2.imwrite('final1.jpg', red_object_rgb)
cv2.imshow('final1', red_object_rgb)


# B
mask = mask1
kernel = np.ones((2,2),np.float32)/50
filtered_mask = cv2.filter2D(mask,-1,kernel)

red_object = cv2.bitwise_and(img, img, mask=filtered_mask)

destination_img = cv2.imread('land.jpg')
destination_img = cv2.resize(destination_img, (800, 600))

rows, cols, channels = red_object.shape

res = destination_img[0:rows, 0:cols]
final2 = cv2.addWeighted(res, 0.7, red_object, 0.5, 0)
destination_img[0:rows, 0:cols] = final2

cv2.imshow('final2', destination_img)
cv2.imwrite("final2.jpg", destination_img)




# C
img2 = cv2.imread('ju.jpg')
img2 = cv2.resize(img2  , (640 , 740))


hsv = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)


lower_y = np.array([0, 0, 0])
upper_y = np.array([255, 255, 255])
mask_yellow1 = cv2.inRange(hsv, lower_y, upper_y)

y_mask = mask_yellow1

kernel = np.ones((2,2),np.float32)/50
yfiltered_mask = cv2.filter2D(y_mask,-1,kernel)

y_object = cv2.bitwise_and(img2,img2,mask=yfiltered_mask)

y_object_hsv = cv2.cvtColor(y_object, cv2.COLOR_BGR2HSV)
y_object_hsv[:,:,0] += 65
y_object_rgb = cv2.cvtColor(y_object_hsv, cv2.COLOR_HSV2BGR)

cv2.imwrite('final3.jpg', y_object_rgb)
cv2.imshow('final3', y_object_rgb)

cv2.waitKey(0)
cv2.destroyAllWindows()

