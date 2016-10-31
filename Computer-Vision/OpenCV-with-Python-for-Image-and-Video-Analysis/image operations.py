import cv2
import numpy as np

img = cv2.imread('kigali.png', cv2.IMREAD_COLOR)

img[55, 55] = [255, 255, 255]
px = img[55, 55]

img[100:150, 100:150] = [255, 255, 255]

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()