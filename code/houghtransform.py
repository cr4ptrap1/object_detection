import cv2
import numpy as np
import urllib.request

# IP camera url
url = 'http://192.168.137.118/800x600.jpg'


# Create a window to display the image stream
cv2.namedWindow('Stream Capture', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Stream Capture', 800, 600)

# Define lower and upper bounds for color thresholding
lower_red = np.array([0, 100, 100])
upper_red = np.array([10, 255, 255])

# Define the kernel for morphological operations
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))

while True:
    # Retrieve the image from the camera
    img_response = urllib.request.urlopen(url)
    img_array = np.array(bytearray(img_response.read()), dtype=np.uint8)
    img = cv2.imdecode(img_array, -1)

    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Apply color thresholding to isolate red objects
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_red, upper_red)

    # Perform morphological operations to remove noise and fill in gaps
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)

    # Find contours in the binary image
    contours, hierarchy = cv2.findContours(closing, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Loop through the contours to find the circular objects
    for contour in contours:
        area = cv2.contourArea(contour)
        perimeter = cv2.arcLength(contour, True)

        # Check if the contour is circular using circularity = 4pi(area/perimeter^2)
        if perimeter != 0:
            circularity = 4 * np.pi * area / perimeter**2
        else:
            circularity = 0

        # If the circularity is greater than a certain threshold, draw the circle
        if circularity > 0.6:
            (x, y), radius = cv2.minEnclosingCircle(contour)
            center = (int(x), int(y))
            radius = int(radius)
            cv2.circle(img, center, radius, (0, 255, 0), 2)

    # Display the image with detected circles
    cv2.imshow('Stream Capture', img)

    # Wait for 'q' key to be pressed to exit the program
    if cv2.waitKey(1) == ord('q'):
        break

# Release resources and close the window
cv2.destroyAllWindows()