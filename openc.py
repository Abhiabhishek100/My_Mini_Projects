import cv2 as cv
import numpy as np
# k=cv.imread("boss.jpg")
# cv.imshow("output",k)
# cv.waitKey(0)
# # To read  image
# cap=cv.VideoCapture("boss hiphop.mp4")
# while True:
#     success, img=cap.read()
#     cv.imshow("video",img)
#     if cv.waitKey(100) & 0xFF == ord('q'):
#         break
# img=cv.imread("boss1.jpg")
# gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow("gray",gray)
# blur= cv.GaussianBlur(gray,(25,25),0)
# cv.imshow("blur",blur)
# Canny= cv.Canny(img,100,100)
# cv.imshow("canny",Canny)
# kernel=np.ones((5,5),np.uint8)
# dialation=cv.dilate(Canny,kernel,iterations=1)
# cv.imshow("dialated",dialation)
# erode=cv.erode(dialation,kernel,iterations=1)
# cv.imshow("eroded",erode)
# conversion of image as many filters
img=cv.imread("boss1.jpg");
imgresize=cv.resize(img,(300,200))
print(img.shape,imgresize.shape)
cv.imshow("image",imgresize)
imgcropped=img[0:200,200:500]
cv.imshow("cropped",imgcropped)
cv.waitKey(0) # to read video
