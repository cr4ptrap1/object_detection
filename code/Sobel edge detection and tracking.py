import cv2
import numpy as np
import urllib.request

# IP camera url
url = 'http://192.168.137.189/cam-lo.jpg'



# create named window for output display
cv2.namedWindow('Output', cv2.WINDOW_NORMAL)

# set threshold values
low_threshold =50
high_threshold = 150

while True:

     # Read the current frame from the IP camera
    img_response = urllib.request.urlopen(url)
    img_np = np.array(bytearray(img_response.read()), dtype=np.uint8)
    img = cv2.imdecode(img_np, -1)


    # convert frame to grayscale
    grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # apply Gaussian blur
    blur = cv2.GaussianBlur(grey, (5, 5), 0)

    # apply Sobel edge detection
    sobel_x = cv2.Sobel(blur, cv2.CV_16S, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(blur, cv2.CV_16S, 0, 1, ksize=3)
    sobel_x = cv2.convertScaleAbs(sobel_x)
    sobel_y = cv2.convertScaleAbs(sobel_y)
    edges = cv2.addWeighted(sobel_x, 0.5, sobel_y, 0.5, 0)

    # convert edges to binary
    ret, binary = cv2.threshold(edges, low_threshold, high_threshold, cv2.THRESH_BINARY)

    # apply erosion to remove noise
    kernel = np.ones((5, 5), np.uint8)
    binary = cv2.erode(binary, kernel, iterations=1)

    # find contours
    contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # draw contours
    for cnt in contours:
        # calculate circularity of contour
        area = cv2.contourArea(cnt)
        perimeter = cv2.arcLength(cnt, True)
        circularity = 0
        if perimeter != 0:
            circularity = 4 * np.pi * area / perimeter**2
        if area > 1000 and circularity > 0.3:
            (x, y), radius = cv2.minEnclosingCircle(cnt)
            center = (int(x), int(y))
            radius = int(radius)
            img = cv2.circle(img, center, radius, (0, 255, 0), 2)

    # show output
    cv2.imshow('Output',binary)

    # exit condition
    if cv2.waitKey(1) == ord('q'):
        break

# release resources

cv2.destroyAllWindows()