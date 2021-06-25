# Putting text in the image
#SYNTAX:

import cv2
img=cv2.imread("1.jpg")

#cv2.putText(src, text, position,font,fontSize,color,thickness)
text="WELCOME"

cv2.putText(img,text , (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
cv2.imwrite("textedimg.jpg",img)
