import cv2



src = cv2.imread("images/allballs.jpg", cv2.IMREAD_GRAYSCALE);


th,dst = cv2.threshold(src,0,255,cv2.THRESH_BINARY);
cv2.imwrite("images/threshold_example.jpg",dst);

th,dst = cv2.threshold(src, 0,128,cv2.THRESH_BINARY);
cv2.imwrite("images/threshold_binary_MAX.jpg", dst);

th,dst = cv2.threshold(src,127,255,cv2.THRESH_BINARY_INV);
cv2.imwrite("images/threshold_binary_INV.jpg",dst);

th,dst = cv2.threshold(src,127,255,cv2.THRESH_TRUNC);
cv2.imwrite("images/threshold_TRUNC.jpg",dst);

th,dst = cv2.threshold(src,127,255,cv2.THRESH_TOZERO);
cv2.imwrite("images/threshold_TOZERO.jpg",dst);

th,dst = cv2.threshold(src,127,255,cv2.THRESH_TOZERO_INV);
cv2.imwrite("images/threshold_TOZEROINV.jpg",dst);



