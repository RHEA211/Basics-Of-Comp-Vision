# Read,Write, show img

import cv2
img=cv2.imread("1.jpg")

#to show img
cv2.imshow("First picture",img)

#save image
cv2.imwrite("Firstime.jpg",img)

#how much time show the image
cv2.waitKey(0)

#while closing , close everything
cv2.destroyAllWindows
