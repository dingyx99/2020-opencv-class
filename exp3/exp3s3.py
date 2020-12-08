import cv2
import numpy as np
import matplotlib.pyplot as plt
import Morphology as mor

img = cv2.imread("1.png").astype(np.float32)
gray = mor.BGR2GRAY(img)
otsu = mor.otsu_binarization(gray)

result = mor.Opening(otsu, 1)
result = mor.Closing(result, 1)

cv2.imshow("Original", img)
cv2.imshow("Processed", result)

cv2.waitKey(0)
cv2.destroyAllWindows()