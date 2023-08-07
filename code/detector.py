import cv2 
import numpy as np

image = cv2.imread('images/image.jpg')

if image is None:
    print ('could not read image')

kernel1 = np.array([[0,0,0],
                    [0,1,0],
                    [0,0,0]])

identity = cv2.filter2D(src=image, ddepth=-1, kernel=kernel1)

#cv2.imshow("original", image)
cv2.imshow("identity", identity)

#cv2.waitKey()
#cv2.imwrite("identity", identity)
#cv2.destroyAllWindows()

#kernals for blurring. 5x5 and 10x10 arrays of 1's, normalised 
kernel2 = np.ones((5,5), np.float32)/25
img = cv2.filter2D(src=image, ddepth=-1,kernel=kernel2)
kernel3 = np.ones((10,10),np.float32)/100
img2 = cv2.filter2D(src=image, ddepth=-1,kernel=kernel3)

#blur shortcut

img_blur = cv2.blur(src=image,ksize=(5,5))
cv2.imshow("blur shortcut",img_blur)

cv2.imshow('original', image)
cv2.imshow("kernel blur", img)
cv2.imshow("kernal big", img2)


cv2.waitKey()
#cv2.imwrite('blur_kernal', img)
cv2.destroyAllWindows()



