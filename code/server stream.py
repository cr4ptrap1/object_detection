import numpy as np
import urllib.request
import cv2
import time as t 


#url for webserver followed by the image size and file type.
url = 'http://192.168.137.50:81/stream'

cv2.namedWindow('stream capture',cv2.WINDOW_AUTOSIZE)


prev_frame_time = 1
new_frame_time = 0
#loop fetches new image from webserver, adds the data to an array and applies the processing techneque. 
while True:
    
    imgResponse = urllib.request.urlopen(url + ".jpeg") 
    imgnp = np.array(bytearray(imgResponse.read()),dtype=np.uint8)
    img = cv2.imdecode(imgnp,-1)
    greyscaled = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    Guassian = cv2.adaptiveThreshold(greyscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
   
    img_blur = cv2.blur(src=Guassian,ksize=(5,5))
    
    edges = cv2.Canny(image=img_blur, threshold1=100, threshold2=200)


    fps = 1/(new_frame_time-prev_frame_time)
    prev_frame_time = new_frame_time
    fps = int(fps)
    fps = str(fps)
    cv2.putText(fps, (7, 70), 3, (100, 255, 0), 3, cv2.LINE_AA)
    
    
    cv2.imshow('stream captured' ,edges)
    if cv2.waitKey(1) == 113:
        break


cv2.destroyAllWindows

### testing ##
#greyscaled = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#Guassian = cv2.adaptiveThreshold(greyscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
#sobelx = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5) # Sobel Edge Detection on the X axis
#sobely = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5) # Sobel Edge Detection on the Y axis
#sobelxy = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5) # Combined X and Y Sobel Edge Detection