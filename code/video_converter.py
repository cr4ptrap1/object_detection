import cv2 
#import numpy as np


#source video 
clip = cv2.VideoCapture("videos/hollowBall.mp4",)


if (clip.isOpened()==False):
    print ("error opening file")
else :

    fps = clip.get(5)
    frame_count = clip.get(7) 
    print ("Frame count : ",frame_count)

#set frame size and frames per second

frame_width = int(clip.get(3))
frame_height = int(clip.get(4))
frame_size = (frame_width,frame_height)
fps = 20;


#output file location name and type 
output = cv2.VideoWriter("videos/test_hollow.avi",cv2.VideoWriter_fourcc('M','J','P','G'),fps,frame_size,False)


#pull frames from file, convert and store in output file
while(clip.isOpened()):
    ret,frame = clip.read()
    if ret == True:
        flipped = cv2.flip(frame,0)
        greyscaled = cv2.cvtColor(flipped,cv2.COLOR_BGR2GRAY)
        Guassian = cv2.adaptiveThreshold(greyscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
        
        output.write(Guassian)
        #cv2.imshow("frame",Guassian)

        
        key = cv2.waitKey(20)
        
        if key == ord("q"):
            break 
    else:
        break


clip.release()
output.release()
cv2.destroyAllWindows()    




