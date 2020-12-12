import cv2,numpy,os,sys
haar_file='haarcascade_face.xml'
##dst='E:\datasets'
##sub='dhruvi'
##path=os.path.join(dst,sub)
##if os.path.isdir(path):
##    os.mkdir(path)
path='C:\\Users\\dhruvi\\Desktop\\face_recognition\\'

(width,height)=(130,20)
face=cv2.CascadeClassifier(haar_file)
img=cv2.imread('dhruvi.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces=face.detectMultiScale(gray,1.3,3)
for (x,y,w,h)in faces:
    cv2.rectangle(img,(x,y),(x+w,h+y),(0,0,255),2)
    fac=gray[y:y+h,x:x+w]
    final_face=cv2.resize(fac,(width,height))
    cv2.imwrite('%s / abc .png' %(path),final_face)

cv2.imshow('OpenCV',img)
    
    
