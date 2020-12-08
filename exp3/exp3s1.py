import cv2
import numpy as np
import matplotlib.pyplot as plt
import Morphology as mor

img_dilate = cv2.imread("1.png").astype(np.float32)
img_erode = cv2.imread("2.png").astype(np.float32)

gray_dilate = mor.BGR2GRAY(img_dilate)
gray_erode = mor.BGR2GRAY(img_erode)

otsu_dilate = mor.otsu_binarization(gray_dilate)
otsu_erode = mor.otsu_binarization(gray_erode)

result_dilate = mor.Dilate(otsu_dilate)
result_erode = mor.Erode(otsu_erode)

cv2.imshow("Before Dilate", img_dilate)
cv2.imshow("After Dilate", result_dilate)
cv2.imshow("Before Erode", img_erode)
cv2.imshow("After Erode", result_erode)

cv2.waitKey(0)
cv2.destroyAllWindows()