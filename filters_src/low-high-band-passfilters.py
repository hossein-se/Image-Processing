import cv2
import numpy as np
import matplotlib.pyplot as plt
import math





def distance_calculator(x1, y1, x2, y2):


    distance = math.sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))

    return distance


def low_pass_filter(image, radius):


    filtered_image = []

    image_height = len(image)
    image_width = len(image[0])

    center_x = int(image_width / 2)
    center_y = int(image_height / 2)

    for row_counter in range(image_height):
        row = []
        for pixel_counter in range(image_width):

            distance = distance_calculator(center_x, center_y, pixel_counter, row_counter)

            if distance > radius:
                row.append(0)
            else:
                row.append(image[row_counter][pixel_counter])

        filtered_image.append(row)

    return filtered_image


def high_pass_filter(image, radius):


    filtered_image = []

    image_height = len(image)
    image_width = len(image[0])


    center_x = int(image_width / 2)
    center_y = int(image_height / 2)

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


def band_pass_filter(image, inner_radius, outer_radius):


    high_pass_image = high_pass_filter(image, inner_radius)
    low_pass_image = low_pass_filter(high_pass_image, outer_radius)
    filtered_image = low_pass_image

    return filtered_image




image = cv2.imread("peacock-feather.jpg", 0)

fourier_transformed_image = np.fft.fft2(image)

shifted_transformed_image = np.fft.fftshift(fourier_transformed_image)


plt.figure(figsize=(10, 10), constrained_layout=False)

low_pass_image_10 = low_pass_filter(shifted_transformed_image, 10)
low_pass_image_50 = low_pass_filter(shifted_transformed_image, 50)
low_pass_image_100 = low_pass_filter(shifted_transformed_image, 100)
low_pass_image_250 = low_pass_filter(shifted_transformed_image, 250)

plt.subplot(1, 5, 1), plt.imshow(image, 'gray'), plt.title("Original Image")
plt.subplot(1, 5, 2), plt.imshow(np.abs(np.fft.ifft2(low_pass_image_10)), 'gray'), plt.title("L-R = 10")
plt.subplot(1, 5, 3), plt.imshow(np.abs(np.fft.ifft2(low_pass_image_50)), 'gray'), plt.title("L-R = 50")
plt.subplot(1, 5, 4), plt.imshow(np.abs(np.fft.ifft2(low_pass_image_100)), 'gray'), plt.title("L-R = 100")
plt.subplot(1, 5, 5), plt.imshow(np.abs(np.fft.ifft2(low_pass_image_250)), 'gray'), plt.title("L-R = 250")
plt.show()


plt.figure(figsize=(10, 10), constrained_layout=False)

high_pass_image_10 = high_pass_filter(shifted_transformed_image, 10)
high_pass_image_50 = high_pass_filter(shifted_transformed_image, 50)
high_pass_image_100 = high_pass_filter(shifted_transformed_image, 100)
high_pass_image_250 = high_pass_filter(shifted_transformed_image, 250)

plt.subplot(1, 5, 1), plt.imshow(image, 'gray'), plt.title("Original Image")
plt.subplot(1, 5, 2), plt.imshow(np.abs(np.fft.ifft2(high_pass_image_10)), 'gray'), plt.title("H-R = 10")
plt.subplot(1, 5, 3), plt.imshow(np.abs(np.fft.ifft2(high_pass_image_50)), 'gray'), plt.title("H-R = 50")
plt.subplot(1, 5, 4), plt.imshow(np.abs(np.fft.ifft2(high_pass_image_100)), 'gray'), plt.title("H-R = 100")
plt.subplot(1, 5, 5), plt.imshow(np.abs(np.fft.ifft2(high_pass_image_250)), 'gray'), plt.title("H-R = 250")
plt.show()


plt.figure(figsize=(10, 10), constrained_layout=False)

band_pass_image = band_pass_filter(shifted_transformed_image, 35, 70)

plt.subplot(1, 2, 1), plt.imshow(image, 'gray'), plt.title("Original Image")
plt.subplot(1, 2, 2), plt.imshow(np.abs(np.fft.ifft2(band_pass_image)), 'gray'), plt.title("B-R = (35,70)")
plt.show()

