import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("Lena.jpg", 0)

ret, th = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
cv2.imshow("Original", img)
cv2.imshow("Threshold", th)

cv2.waitKey(0)
cv2.destroyAllWindows()