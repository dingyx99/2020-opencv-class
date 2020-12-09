import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("Lena.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret1, th1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)
plt.imshow(th1, "gray")
plt.title("OTSU, thresold is "+str(ret1)), plt.xticks([]), plt.yticks([])
plt.show()
