import numpy as np
import cv2
from numpy.lib.function_base import copy

red = (0,0,255)
canvas = np.zeros((200,240,3), "uint8")
origimg = cv2.imread("lena.bmp")

cv2.rectangle(canvas, (30,30), (70,70), red, -1)
cv2.imwrite("pres4picsave.bmp", canvas)

copyimg = origimg.copy()
cv2.imwrite("lenacopy.bmp",copyimg)