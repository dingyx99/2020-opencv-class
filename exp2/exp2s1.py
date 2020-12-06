import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("lena.bmp",0)
dft = cv2.dft(np.float32(img), cv2.DFT_COMPLEX_INPUT)
dft_shift = np.fft.fftshift(dft)
magnitude_spectrum = 20 * np.log(cv2.magnitude(dft_shift[:,:,0], dft_shift[:,:,1]))

plt.subplot(121), plt.imshow(img, 'gray')
plt.title('Original Image', plt.xticks([]), plt.yticks([]))
plt.subplot(122), plt.imshow(magnitude_spectrum, 'gray')
plt.title('DFT', plt.xticks([]), plt.yticks([]))
plt.show()