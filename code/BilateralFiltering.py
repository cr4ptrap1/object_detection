import cv2 
import numpy as np 

image = cv2.imread("images/image.jpg")

bilateral_filter = cv2.bilateralFilter(src=image, d=9,sigmaColor=75,sigmaSpace=75)

cv2.imshow("original", image)
cv2.imshow("bilateral filter",bilateral_filter)

cv2.waitKey(0)
cv2.destroyAllWindows()

