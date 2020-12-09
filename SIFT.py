import cv2
import numpy as np
img=cv2.imread('dhruvi.jpg')
cv2.imshow('Original',img)

(rows,cols)=img.shape[:2]
print(rows)
print (cols)
##Rotation
M=cv2.getRotationMatrix2D((100,100),45,1)
changed=cv2.warpAffine(img,M,(cols,rows))
cv2.imshow('rotated',changed)

##translate
Pos=np.float32([[0,1,0],[5,5,10]])
translated=cv2.warpAffine(img,Pos,(cols,rows))
cv2.imshow('translated',translated)
