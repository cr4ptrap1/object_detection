import cv2
import numpy as np
import urllib.request

# IP camera url
url = 'http://192.168.137.118/800x600.jpg'



# create named window for output display
cv2.namedWindow('Output', cv2.WINDOW_NORMAL)

# set threshold values
low_threshold = 0
high_threshold = 100

while True:
    imgResponse = urllib.request.urlopen(url)
    imgnp = np.array(bytearray(imgResponse.read()),dtype=np.uint8)
    img = cv2.imdecode(imgnp,-1)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    thresh = cv2.threshold(blur, 70, 255, cv2.THRESH_BINARY)
    sobelx = cv2.Sobel(thresh, cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(thresh, cv2.CV_64F, 0, 1, ksize=3)
    sobel = np.sqrt(sobelx ** 2 + sobely ** 2)

    cv2.imshow('stream capture', sobel)
    if cv2.waitKey(1) == 113:
        break


cv2.destroyAllWindows()