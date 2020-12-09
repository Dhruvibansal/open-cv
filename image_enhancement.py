import cv2
img=cv2.imread('dhruvi.jpg')
import matplotlib.pyplot as plt

###Image Resize######
reduced=cv2.resize(img,(0,0),fx=0.5,fy=0.5)
bigger_image=cv2.resize(img,(1368,840),interpolation=cv2.INTER_AREA)

##interpolation (quality maintain krta hai)
##INTER_AREA
##INTER_CUBIC
##INTER_LINEAR

interpolated_image=cv2.resize(img,(200,200),interpolation=cv2.INTER_LINEAR)

## individual show of images
##a=cv2.imshow('Original Image',img)
##b=cv2.imshow('Half Image',reduced)
##c=cv2.imshow('Large', bigger_image)
##d=cv2.imshow('Interpolated',interpolated_image)

titles=['A','B','C','D']
images=[img,reduced,bigger_image,interpolated_image]
for i in range(4):
    plt.subplot(2,2,i+1)
##  cv2.imshow(titles[i],images[i])
    plt.title(titles[i])
    plt.imshow(images[i])
plt.show()

