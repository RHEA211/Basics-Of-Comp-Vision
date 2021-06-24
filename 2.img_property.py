#Image properties

import cv2
img= cv2.imread("1.jpg")

#get properties
print(img.shape)
#shows: 3means coloured


print(img.size)

#property/fprmat
print(img.dtype)
