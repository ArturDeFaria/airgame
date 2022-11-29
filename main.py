import numpy as np
import cv2 as cv

cap1 = cv.VideoCapture(0)
#cap2 = cv.VideoCapture(1)
i=0
while True:
    
    ret1, frame1 = cap1.read()
   #ret2, frame2 = cap2.read()
    
    cv.imshow('frame', frame1)
    if cv.waitKey(0) or i>=5000 : break
    i +=1
    print (i)

cap1.release()
cv.destroyAllWindows()