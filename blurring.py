import cv2
img=cv2.imread('dhruvi.jpg')
cv2.imshow('Original',img)
##median blur
mb=cv2.medianBlur(img,5)
cv2.imshow('median_blur',mb)
##bilateral blur
bb=cv2.bilateralFilter(img,9,75,75)
cv2.imshow('bilateral',bb)
##gaussian blur

gb=cv2.GaussianBlur(img,(5,5),0)
cv2.imshow('gaussian_blur',gb)
