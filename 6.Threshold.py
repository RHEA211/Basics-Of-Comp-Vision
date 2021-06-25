#Thresholding
#Before applying thresholding , our img should be gray scale

import cv2
img=cv2.imread("1.jpg")
grayIMG=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#THRESHOLD IMG

#threshold img= cv2.threshold(sourceimg,threshold,maxvalueforThreshold,binary,type)

thresImg=cv2.threshold(grayIMG,120,255,cv2.THRESH_BINARY)[1]
cv2.imwrite("thresholdImg.jpg",thresImg)
#This saves the threshold img in the same folder
