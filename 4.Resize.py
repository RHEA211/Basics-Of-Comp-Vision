import cv2
import imutils

#img and code should be in same directory
img=cv2.imread("1.jpg")

resizeImg=imutils.resize(img,width=20,height=20)
cv2.imwrite("Resizedimg.jpg",resizeImg)

#resized img has been saved in same directory
