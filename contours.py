# Contour Detection
# conoturs are the boundaries of an object. line or curve joining points of an object
# not the same as edges, useful in object recognition

import cv2 as cv
import numpy as np


img = cv.imread("photos/capybara.jpg")
cv.imshow("Original", img)

blank = np.zeros(img.shape, dtype= 'uint8') #blank image of same dimensions as the original capybara image
cv.imshow("Blank", blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
cv.imshow("BLUR", blur)

canny = cv.Canny(blur, 125, 175)
cv.imshow("canny edges", canny)
# passing in blur gives less edges, only the main ones as we have a less detailed image
# using img gives more edges, as the canny edge detector is able to pick up more.


#find contours using the findContours method
# looks at the structuring element, returns 2 values
#takes in the edges (canny image), the mode: cv.RETR_TREE(hierarchichal contours), cv.RETR_LIST(all contours)
# method is contour approx method, here it is none

# contours is a list of all coords of the images
# hierarchies are the hierarchical rep of the contours, ie rectangle with a square with a circle - rep that opencv used to find the contours

#RETR_LIST is the mode where the findContours find and returns the list
# RETR_EXTERNAL - external contours only
# RETR_TREE = all hierarchical contours

# contour approximation method - how to approx the contours
# here we just return all, using none - every single coord
# chain_approx_simple compresses all contours into ones that make the most sense
# ie a line is turned into 2 end points of it.


# instead of a canny edge detector, we can do thresholding
# threshold value and max value, 
# it will attempt to binarise the image, if a pixels intensity is below 125 - set to 0
# then the type is a binarisation of the image


ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow("THRESH", thresh)
#far less contours in the thresholded image


contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contours found!')

# length of list is the amount of contours in the image
# f {var} used to format a variable, and method applied to it


#changing to simple hasnt changed it - no compression
# one way we can work around is to blur the gray scale image before we find the canny edges
# reduced by 59 times


# we can visualise contours by drawing over the image
# cv. drawcontours takes in an image to draw over, a list of all contours, contour index = how many contours in the iamge (-1), color, thickness
cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow("contours drawn", blank)

# notthe same as the canny image, as the find contours method didnt use canny to detect, it used a smoother image

# if we change it to canny, then it should be the same, just one is in red.
# contours are the curves that join points along boundaries, so they are like edges


# use canny, then find contours, 
# after that threshold(thresh), and find contours.
# simple thresholding has disadvanges



cv.waitKey(0)

