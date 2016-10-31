import cv2
import numpy as np

img = cv2.imread('kigali.png', cv2.IMREAD_COLOR)

# Draw line on the image
cv2.line(img, (0, 0), (150, 150), (255, 150, 100), 15)


# Draw a rectangle
cv2.rectangle(img, (15, 25), (200, 150), (0, 255, 0), 5)


# Draw a circle
cv2.circle(img, (100, 78), 55, (0, 0, 255), -1)


# Draw a polygon
pts = np.array([[15, 5], [20, 30], [70, 20], [50, 10]], np.int32)
pts = pts.reshape((-1, 1, 2))
cv2.polylines(img, [pts], True, (0, 200, 200), 5)


# Write on the image
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'KCC!', (0, 130), font, 1, (210, 210,15), 5)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()