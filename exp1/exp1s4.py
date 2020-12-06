import cv2
import numpy as np

img = cv2.imread("Fruits.jpg")
cv2.imshow("Original", img)

img_median_blur = cv2.medianBlur(img, 5)
font = cv2.FONT_HERSHEY_COMPLEX
cv2.imshow("Median Blur", img_median_blur)

img_blur = cv2.blur(img, (5,5))
cv2.imshow("Blur", img_blur)

cv2.waitKey(0)
cv2.destroyAllWindows()