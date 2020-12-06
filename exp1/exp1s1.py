import cv2
import numpy as np
import matplotlib.pyplot as plt

def calcGrayHist(I):
    h,w =I.shape[:2]
    grayHist = np.zeros([256], np.uint64)
    for i in range(h):
        for j in range(w):
            grayHist[I[i][j]] += 1
    return grayHist

img = cv2.imread("lena.bmp",0)
grayHist = calcGrayHist(img)
x = np.arange(256)
plt.plot(x, grayHist, 'r', linewidth=2, c='black')
plt.xlabel("Gray Label")
plt.ylabel("Number of Pixels")
plt.show()