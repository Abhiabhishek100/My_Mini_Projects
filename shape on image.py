import cv2 as cv
import numpy as np
k=np.zeros((600,600,3),np.uint8)

k[:]=255,255,0
cv.line(k,(0,0),(600,600),(0,0,255),3)
cv.rectangle(k,(0,0),(250,350),(0,200,100),cv.FILLED)#/any width like(9,123.7,5)
cv.circle(k,(400,300),50,(0,255,255),3)
cv.putText(k,"Surru",(350,200),cv.FONT_HERSHEY_SIMPLEX,1,(255,0,255),2)
cv.imshow("k",k)
cv.waitKey(0)