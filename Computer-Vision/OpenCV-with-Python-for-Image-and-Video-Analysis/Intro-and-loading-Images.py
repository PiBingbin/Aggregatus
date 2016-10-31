import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('kigali.png', cv2.IMREAD_GRAYSCALE)
# Some other options are IMREAD_COLOR, IMREAD_UNCHANGED

# plt.imshow(img, cmap='gray', interpolation='bicubic')
# plt.show()

# Plot the image using cv
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the image
cv2.imwrite('kigali.jpg', img)
