import cv2
import numpy as np
img=cv2.imread('dhruvi.jpg')
cv2.imshow('Original',img)

##Edge detection
edges=cv2.Canny(img,50,100)
cv2.imshow('a',edges)
