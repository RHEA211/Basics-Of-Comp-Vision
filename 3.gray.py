#Gray Scale

import cv2

img=cv2.imread("1.jpg")

#convert to grey scale
grayimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#save gray img
cv2.imwrite("GrayIMG.jpg",grayimg)

#show both img
cv2.imshow("Original",img)
cv2.imshow("GrayIMG",grayimg)

cv2.waitkey(0)
cv2.destroyAllWindows()
