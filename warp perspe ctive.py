import cv2 as cv
import numpy as np
img=cv.imread("3d.jpg")
# width,height= 400,400
width,height= 1000,1000
pts1 = np.float32([[99,56],[105,200],[150,160],[145,89]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv.getPerspectiveTransform(pts1,pts2)
out = cv.warpPerspective(img,matrix,(width,height))
cv.imshow("out",out)
print(img.shape)
cv.waitKey(0)