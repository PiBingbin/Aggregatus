import cv2
import numpy as np

img1 = cv2.imread('hand.png')
img2 = cv2.imread('loc.png')
img3 = cv2.imread('bright.png')
#
# add = img2 + img3
# weighted = cv2.addWeighted(img2, 0.6, img3, 0.4, 0)
# cv2.imshow('add', add)
# cv2.imshow('weighted', weighted)

rows, cols, channels = img2.shape
roi = img1[0:rows, 0:cols]

# Create a mask of img 2
img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# Apply the threshold
ret, mask = cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY_INV)

mask_inv = cv2.bitwise_not(mask)

img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
img2_fg = cv2.bitwise_and(img2, img2, mask=mask)

dst = cv2.add(img1_bg, img2_fg)
img1[0:rows, 0:cols] = dst


cv2.imshow('mask_inv', mask_inv)
cv2.imshow('res', img1)
cv2.imshow('dst', dst)
cv2.imshow('img1_bg', img1_bg)
cv2.imshow('img2_fg', img2_fg)

cv2.waitKey(0)
cv2.destroyAllWindows()
