import cv2
img=cv2.imread('dhruvi.jpg')
##cv2.imshow('original',img)
import matplotlib.pyplot as plt
import numpy as np

##Erosion(blur) & Dilation (smooth)

gray=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
strel=np.ones((5,5),np.uint8)
img1=cv2.erode(img,strel)

cv2.imshow('Eroded',img1)
img2=cv2.dilate(img,strel)
##cv2.imshow('Dilated',img2)
lower=np.array([40,40,40])
upper=np.array([70,255,255])

mask=cv2.inRange(gray,lower,upper)
mask=cv2.bitwise_and(img,img,mask=mask)

##cv2.imshow('gray',mask)
images=[img,img1, img2,mask]
titles=['A','B','C','D']
for i in range(4):
    plt.subplot(2,2,i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])
    
plt.show()
