# Drawing Rectangle in an image
#If obj detected, draw rectangle: contains x,y

#SYNTAX:

import cv2
img=cv2.imread("1.jpg")

#cv2.rectangle(src,startpoint,endpoint,color,thickness)

#save image
cv2.imwrite("frame.jpg",img)