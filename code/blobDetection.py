import cv2
import numpy as np


im = cv2.imread("images/image.jpg", cv2.IMREAD_GRAYSCALE)


params = cv2.SimpleBlobDetector_Params()

params.minThreshold = 10;
params.maxThreshold = 200;

params.filterByArea = True
params.minArea = 1500

params.filterByCircularity = True
params.minCircularity = 0.1

params.filterByConvexity = True
params.minConvexity = 0.87

params.filterByInertia = True
params.minInertiaRatio = 0.01

ver = (cv2.__version__).split('.')
if int(ver[0]) < 3 :
    detector = cv2.SimpleBlobDetector(params)
else :
    detector = cv2.SimpleBlobDetector_create(params)
    
        