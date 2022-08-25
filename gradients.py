# gradients and edge dections
# gradients present in an image, like an edge, but not the same
# same in programming context

# canny edge detector is a complex one, but there are others.

import cv2 as cv
import numpy as np

img = cv.imread("photos/capybara.jpg")

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow("g", gray)


#Laplace
# laplacian finds the laplacian of an image. gradients of the gray image - add 2nd derivs of the sobel operator
# src img
# ddepth, here it is CV_64F, depth of the result image
# then convert to an np array

lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))

cv.imshow("LAplace", lap)

#looks like a pencil shading of the image.
# edges are present, but other details are smudged

#transition from black to white and vv, it is a positive or negative slope
# pixel values cannot be negative, so we find the absolute value of the image, then convert to uint8, image specific datatype.


# Sobel gradient magnitude representation
#finds grad in x and y directions

sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)

#cv.imshow('Sobel X', sobelx)
#cv.imshow('Sobel Y', sobely)

# x direction shows a lot of vertical lines, as it looks for the gradient in the x direction, meaning that horizontal lines are seen easily, vv.

# find the combined edge detected image by combining x and y

combined_sobel = cv.bitwise_or(sobelx, sobely)
cv.imshow("combined" ,combined_sobel)

# can see that the sobel edge detector is different to the laplacian one, due to them being different algorithms

canny = cv.Canny(gray, 150, 175)
cv.imshow("canny", canny)

# canny is very advanced, and uses sobel at one point
# canny is like a line drawing, but sobel is fairly blurry.
# sobel is used in more complex scenarios.

cv.waitKey(0)