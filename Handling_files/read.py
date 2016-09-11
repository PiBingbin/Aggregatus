import cv2

image = cv2.imread('MyPic.png')
cv2.imwrite('MyPic.jpg', image)

"""By default, imread() returns an image in BGR color format, even if the file uses 
a grayscale format. BGR represents the same color space as RGB but the byte order is reversed"""

grayImage = cv2.imread('MyPic.png', cv2.CV_LOAD_IMAGE_GRAYSCALE)
cv2.imwrite('MyPicGray.png', grayImage)
