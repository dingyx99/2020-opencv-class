import cv2
import numpy as np

img = cv2.imread("Fruits.jpg")
cv2.imshow("Original", img)

img_Gaussian_blur = cv2.GaussianBlur(img, (7,7),0)
cv2.imshow("Gaussian Blur", img_Gaussian_blur)

cv2.waitKey(0)
cv2.destroyAllWindows()