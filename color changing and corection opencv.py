import cv2
import numpy as np
def empty(a):
    pass
path="lambo.jpeg"

cv2.namedWindow("trackbars")
cv2.resizeWindow("trackbars",640,240)
cv2.createTrackbar("hue min","trackbars",4,179,empty)
cv2.createTrackbar("hue max","trackbars",179,179,empty)
cv2.createTrackbar("sat min","trackbars",80,255,empty)
cv2.createTrackbar("sat max","trackbars",255,255,empty)
cv2.createTrackbar("val min","trackbars",63,255,empty)
cv2.createTrackbar("val max","trackbars",255,255,empty)
while True:
    imr = cv2.imread(path)
    down = (800, 400)
    img = cv2.resize(imr, down, interpolation=cv2.INTER_LINEAR)
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    hmin=cv2.getTrackbarPos("hue min", "trackbars")
    hmax=cv2.getTrackbarPos("hue max", "trackbars")
    smin=cv2.getTrackbarPos("sat min", "trackbars")
    smax=cv2.getTrackbarPos("sat max", "trackbars")
    vmin=cv2.getTrackbarPos("val min", "trackbars")
    vmax=cv2.getTrackbarPos("val max", "trackbars")
    print(hmin,hmax,smin,smax,vmin,vmax)
    upper=np.array([hmax,smax,vmax])
    lower=np.array([hmin,smin,vmin])
    mask=cv2.inRange(imgHSV,lower,upper)
    result= cv2.bitwise_and(img,img,mask=mask)

    cv2.imshow("ori", img);
    # cv2.imshow("hsv", imgHSV)
    cv2.imshow("mask",mask)
    cv2.imshow("result",result)
    cv2.waitKey(1)

