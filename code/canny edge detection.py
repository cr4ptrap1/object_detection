import cv2
import numpy as np
import urllib.request

url = 'http://192.168.137.118/800x600.jpg'

cv2.namedWindow('stream capture',cv2.WINDOW_AUTOSIZE)

# Define the lower and upper thresholds for binary thresholding
lower_thresh = 50
upper_thresh = 255

while True:
    # Read the image from the URL
    imgResponse = urllib.request.urlopen(url)
    imgnp = np.array(bytearray(imgResponse.read()),dtype=np.uint8)
    img = cv2.imdecode(imgnp,-1)

    # Convert the image to grayscale
    grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to the grayscale image
    blur = cv2.GaussianBlur(grey, (5, 5), 0)

    # Apply Canny edge detection to the blurred grayscale image
    edges = cv2.Canny(blur, 50, 150)

    # Apply binary thresholding to the edge image
    binary = cv2.threshold(edges, lower_thresh, upper_thresh, cv2.THRESH_BINARY)

    # Show the binary image
    cv2.imshow('Binary Image', binary)

    if cv2.waitKey(1) == 113:
        break

cv2.destroyAllWindows()