import socket
import struct
import pickle
import time
import cv2
import sys
import numpy as np
import urllib.request


IP = socket.gethostbyname(socket.gethostname())
PORT = 20000
BUFFER_SIZE = 4096

tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
url = "http://192.168.0.221/image/jpeg"
camera = cv2.VideoCapture(0)

sent_frames = 0
tcp_client.connect((IP, PORT))


while True:
    img_resp = urllib.request.urlopen(url)
    imgnp = np.array(bytearray(img_resp.read()),dtype=np.uint8)
    frame = cv2.imdecode(imgnp,-1)

    cv2.imshow("video feed", frame)
    key = cv2.waitKey(5)
    if key == ord("q"):
        break
        
