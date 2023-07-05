import cv2
import numpy as np
import matplotlib.pyplot as plt



image = cv2.imread("woods.jpg", 0)

# A
plt.figure(figsize=(10, 10), constrained_layout=False)

fourier_transformed_image = np.fft.fft2(image)

shifted_transformed_image = np.fft.fftshift(fourier_transformed_image)

plt.subplot(1,3,1), plt.imshow(image,'gray'), plt.title("1-Original Image")
plt.subplot(1,3,2), plt.imshow(np.abs(shifted_transformed_image,),'gray'), plt.title("1-Fourier")
plt.subplot(1,3,3), plt.imshow(np.angle(shifted_transformed_image),'gray'), plt.title("1-Phase")
plt.show()

# B
plt.figure(figsize=(10, 10), constrained_layout=False)

plt.subplot(1,3,1), plt.imshow(image,'gray'), plt.title("2-Original Image")
plt.subplot(1,3,2), plt.imshow(np.abs(shifted_transformed_image),'gray'), plt.title("2-Fourier")
plt.subplot(1,3,3), plt.imshow(np.log(np.abs(shifted_transformed_image)+1),'gray'), plt.title("2-Fourier After Log")

plt.show()


# C
plt.figure(figsize=(10, 10), constrained_layout=False)

inversed_fourier_image = np.fft.ifft2(shifted_transformed_image)

plt.subplot(1,3,1), plt.imshow(image,'gray'), plt.title("3-Original Image")
plt.subplot(1,3,2), plt.imshow(np.log(np.abs(shifted_transformed_image + 1)),'gray'), plt.title("3-Fourier")
plt.subplot(1,3,3), plt.imshow(np.abs(inversed_fourier_image),'gray'), plt.title("3-Inverse Fourier")

plt.show()
