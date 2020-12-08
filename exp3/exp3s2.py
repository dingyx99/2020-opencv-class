import cv2
import numpy as np
import matplotlib.pyplot as plt
import Morphology as mor

img = cv2.imread("lena.bmp").astype(np.float32)
gray = mor.BGR2GRAY(img)
otsu = mor.otsu_binarization(gray)

result_open = mor.Opening(otsu)
result_close = mor.Closing(otsu)

cv2.imshow("Original", gray)
cv2.imshow("After Opening", result_open)
cv2.imshow("After Closing", result_close)

cv2.waitKey(0)
cv2.destroyAllWindows()
