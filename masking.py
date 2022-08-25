# using bitwise operations, we can maks
# focus on certain parts of image to focus on, ie people, focus on faces
# remove unwanted parts



import cv2 as cv
import numpy as np


img = cv.imread("photos/capybara.jpg")
cv.imshow("original", img)

# important that mask shape is the same as the shape of the original image. dimensions identical

blank = np.zeros(img.shape[:2], dtype = 'uint8')

circlemask = cv.circle(blank.copy(), (img.shape[1]//2 - 125, img.shape[0]//2 - 145), 100, 255, -1)

rectmask = cv.rectangle(blank, (img.shape[1]//2 - 125, img.shape[0]//2 - 145), (img.shape[1] // 2, img.shape[0] // 2), 255, -1)
#cv.imshow("mask", rectmask)

rectangle = cv.rectangle(blank.copy(), (30,30),(370,370), 255, -1)

weird_shape = cv.bitwise_and(circlemask, rectangle)
cv.imshow("weird", weird_shape)


# mask is just a circle over a blank screen.

# to mask an image, we take the original image, and it with itself, and use mask = the mask we just made to produce a mask over the image.



masked = cv.bitwise_and(img,img, mask = weird_shape)
cv.imshow("masked image", masked)




cv.waitKey(0)
