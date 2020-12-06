import cv2
import numpy as np

img = cv2.imread("lena.bmp",1)
cv2.imshow("Source", img)

(b, g, r) = cv2.split(img)
bH = cv2.equalizeHist(b)
gH = cv2.equalizeHist(g)
rH = cv2.equalizeHist(r)

result = cv2.merge((bH, gH, rH))
cv2.imshow("Destination", result)

cv2.waitKey(0)
cv2.destroyAllWindows()