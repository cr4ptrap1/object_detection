import cv2
import numpy as np 

#image = cv2.imread('images/image.jpg')
#GaussianBlur = cv2.GaussianBlur(src=image, ksize=(5,5),sigmaX=0,sigmaY=0)

image = cv2.imread("images/allballs.jpg")
down_width = 600
down_height = 400
down_points = (down_width, down_height)
resized_down = cv2.resize(image, down_points,interpolation=cv2.INTER_LINEAR)

greyscaled = cv2.cvtColor(resized_down,cv2.COLOR_BGR2GRAY)
Guassian = cv2.adaptiveThreshold(greyscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)

cv2.imshow("Original", resized_down)
cv2.imshow("G blurred",Guassian )

cv2.waitKey(0)
cv2.destroyAllWindows()
