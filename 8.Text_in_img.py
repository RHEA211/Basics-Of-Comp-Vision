# Putting text in the image
#SYNTAX:

import cv2
img=cv2.imread("1.jpg")

#cv2.putText(src, text, position,font,fontSize,color,thickness)
text="WELCOME"


cv2.imwrite("textedimg.jpg",img)