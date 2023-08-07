import cv2
import numpy as np
import urllib.request

# set up the camera url
url = 'http://192.168.137.189/cam-mid.jpg'

# set up the robot url and commands
#robot_url = 'http://192.168.137.50/robot_control'
#forward_command = {'command': 'forward', 'duration': 1000}  # move for 1 second
#left_command = {'command': 'left', 'duration': 1000}
#right_command = {'command': 'right', 'duration': 1000}
#stop_command = {'command': 'stop'}  # stop moving

# set up the window to display the camera stream
cv2.namedWindow('Stream Capture', cv2.WINDOW_AUTOSIZE)

while True:
    # get the current image from the camera
    img_response = urllib.request.urlopen(url)
    img_np = np.array(bytearray(img_response.read()), dtype=np.uint8)
    img = cv2.imdecode(img_np, -1)

    # convert the image to greyscale
    grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # apply a Gaussian blur to the image to reduce noise
    blurred = cv2.GaussianBlur(grey, (5, 5), 0)

    # apply a binary threshold to the image to isolate the ball
    thresholded = cv2.threshold(blurred, 100, 128, cv2.THRESH_BINARY)

    # perform erosion and dilation to reduce noise and fill in gaps
    kernel = np.ones((5, 5), np.uint8)
    eroded = cv2.erode(thresholded, kernel, iterations=2)
    dilated = cv2.dilate(eroded, kernel, iterations=2)

    # find the contours in the thresholded image
    contours, _ = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # initialize variables for the largest contour
    largest_area = 50
    largest_contour = None

    # loop over the contours and find the largest one that is likely to be the ball
    for contour in contours:
        area = cv2.contourArea(contour)
        perimeter = cv2.arcLength(contour, True)
        circularity = 4 * np.pi * area / perimeter**2

        if area > 1000 and circularity > 0.5:
            if area > largest_area:
                largest_area = area
                largest_contour = contour

    # if we found a contour, draw a circle around it and move the robot
    if largest_contour is not None:
        (x, y), radius = cv2.minEnclosingCircle(largest_contour)
        center = (int(x), int(y))
        radius = int(radius)
        img = cv2.circle(img, center, radius, (0, 255, 0), 2)
        cv2.imshow('Stream Capture', thresholded)

    # Check if ball is on the left or right of the frame
        #if x < img.shape[1] / 2:
                #urllib.request.urlopen(robot_url, data=bytes(str(left_command), encoding='utf8'))
        #else:
                #urllib.request.urlopen(robot_url, data=bytes(str(right_command), encoding='utf8'))
            
    # Check if ball is on the top or bottom of the frame
        #if y < img.shape[0] / 2:
                #urllib.request.urlopen(robot_url, data=bytes(str(forward_command), encoding='utf8'))
        #else:
                #urllib.request.urlopen(robot_url, data=bytes(str(stop_command), encoding='utf8'))

        



    # wait for a keypress and check if it's the escape key to exit the loop
    if cv2.waitKey(1) == 27:
        break

# clean up
cv2.destroyAllWindows()
