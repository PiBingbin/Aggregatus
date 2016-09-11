import cv2
import numpy as np
import os


"""a byte is an integer ranging from 0 to 255. a pixel is represented
by one byte per channel"""

# Make an array of 120,000 random bytes

randomByteArray = bytearray(os.urandom(120000))

flatNumpyArray = np.array(randomByteArray)

# Convert the array to make a 400*300 grayscale image
grayImage = flatNumpyArray.reshape(300, 400)
cv2.imwrite('RandomGray.png', grayImage)


# Convert the array to make a 400*100 color image
bgrImage = flatNumpyArray.reshape(100, 400, 3)
cv2.imwrite('RandomColor.png', bgrImage)