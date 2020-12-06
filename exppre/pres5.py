import numpy as np
import cv2

red = (0,0,255)
canvas = np.zeros((200,240,3), "uint8")

cv2.rectangle(canvas, (30,30), (70,70), red, -1)
cv2.imshow("Canvas", canvas)

cv2.waitKey(0)
cv2.destroyAllWindows()