import cv2
import numpy as np
import matplotlib.pyplot as plt
import math




def distance_calculator(x1, y1, x2, y2):


    distance = math.sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))

    return distance


def high_pass_filter(image, radius, center_x, center_y):


    filtered_image = []

    image_height = len(image)
    image_width = len(image[0])

    for row_counter in range(image_height):
        row = []
        for pixel_counter in range(image_width):

            distance = distance_calculator(center_x, center_y, pixel_counter, row_counter)

            if distance < radius:
                row.append(0)
            else:
                row.append(image[row_counter][pixel_counter])

        filtered_image.append(row)

    return filtered_image


def man_picture_fit_filter(image):


    filtered_image = []

    image_height = len(image)
    image_width = len(image[0])

    center_x = int(image_width / 2)
    center_y = int(image_height / 2)

    x1 = center_x - 0.25
    x2 = center_x + 0.25
    y1 = 0
    y2 = center_y - 10
    x3 = center_x - 0.25
    y3 = center_y + 10
    x4 = center_x + 0.25
    y4 = image_height

    for row_counter in range(image_height):
        row = []
        for pixel_counter in range(image_width):

            if (pixel_counter >= x1) and (pixel_counter <= x2) and (row_counter >= y1) and (row_counter <= y2):
                row.append(0)
            elif (pixel_counter >= x3) and (pixel_counter <= x4) and (row_counter >= y3) and (row_counter <= y4):
                row.append(0)
            else:
                row.append(image[row_counter][pixel_counter])

        filtered_image.append(row)

    return filtered_image





image = cv2.imread("man.png", 0)

fourier_transformed_image = np.fft.fft2(image)

shifted_transformed_image = np.fft.fftshift(fourier_transformed_image)

filtered_image = high_pass_filter(shifted_transformed_image, 5, 120, 16)
filtered_image = high_pass_filter(filtered_image, 5, 120, 41)
filtered_image = high_pass_filter(filtered_image, 5, 120, 100)
filtered_image = high_pass_filter(filtered_image, 5, 120, 302)
filtered_image = high_pass_filter(filtered_image, 5, 120, 278)
filtered_image = high_pass_filter(filtered_image, 5, 120, 218)


plt.figure(figsize=(10, 10), constrained_layout=False)
plt.subplot(1, 2, 1), plt.imshow(np.log(1 + np.abs(shifted_transformed_image)), 'gray'), plt.title(
    "image  frequency Domain")
plt.subplot(1, 2, 2), plt.imshow(np.log(1 + np.abs(filtered_image)), 'gray'), plt.title("Filters")
plt.show()

plt.figure(figsize=(10, 10), constrained_layout=False)
plt.subplot(1, 1, 1), plt.imshow(np.abs(np.fft.ifft2(filtered_image)), 'gray'), plt.title("image  after filtering")
plt.show()



