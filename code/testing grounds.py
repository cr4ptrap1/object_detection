import numpy as np
import urllib.request
import cv2





url = 'http://192.168.137.86/800x600.jpg'

cv2.namedWindow('stream capture',cv2.WINDOW_AUTOSIZE)
lower_red = np.array([0, 100, 100])
upper_red = np.array([10, 255, 255])

while True:
    
    imgResponse = urllib.request.urlopen(url)
    imgnp = np.array(bytearray(imgResponse.read()),dtype=np.uint8)
    img = cv2.imdecode(imgnp,-1)
    greyscaled = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    filter = cv2.GaussianBlur(greyscaled, (5,5), 1)
    edges = cv2.Canny(filter, 100, 200)
    

    


    cv2.imshow('stream captured',edges)
    if cv2.waitKey(1) == 113:
        break
    cv2.destroyAllWindows
