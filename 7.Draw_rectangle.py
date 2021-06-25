# Drawing Rectangle in an image
#If obj detected, draw rectangle: contains x,y

#SYNTAX:

import cv2
img=cv2.imread("1.jpg")

#cv2.rectangle(src,startpoint,endpoint,color,thickness)
cv2.rectangle(img, (200, 300), (200 + 100, 300 + 100), (0, 255, 0), 2)
#save image
cv2.imwrite("frame.jpg",img)
