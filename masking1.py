import cv2
import numpy as np
cap=cv2.VideoCapture(0)

while(1):
    _,frame=cap.read()

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lower=np.array([110,50,50])
    upper=np.array([130,255,255])

    mask=cv2.inRange(gray,lower,upper)
    fina=cv2.bitwise_and(frame,frame,mask=mask)
    cv2.imshow('Frame Original',frame)
    cv2.imshow('GrayScale',gray)
    cv2.imshow('Mask',mask)
    cv2.imshow('final image',fina)
    k=cv2.waitKey(5) & 0xFF
    if k == 65:
        break
cv2.destroyAllWindows()
