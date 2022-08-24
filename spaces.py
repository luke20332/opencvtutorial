#switching between colour spaces in opencv
# a space of colours - representing an array of pixel colors - rgb, grayscale, hsv, lab, etc

import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('photos/capybara.jpg')
cv.imshow("original", img)

#bgr to grayscale, essentially show pixel intensity
# color is bgr, to grayscale

"""
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)
"""

# BGR to HSV (hue, saturation, value)
# how humans see color


hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV_FULL)
#cv.imshow("HSV", hsv)

#BGR TO LAB
# kinda like a washed down hsv


lab = cv.cvtColor(img, cv.COLOR_BGR2Lab)
#cv.imshow("LAB", lab)


#opencv uses bgr, but others use rbg. so we will get color inversion if we attempt to load an image from opencv into another module which uses rgb

#plt.imshow(img)
#plt.show()

#images are different bgr image, but matplotlib displays as rgb. ie ref and blue are other way round.

# BGR to RGB

"""
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)# representing bgr image as rgb
cv.imshow("H", rgb) # cv assumes its bgr, but its rgb, so colours have been inverted.


plt.imshow(rgb) # plt reads rgb as rgb, so its in colornig
plt.show()
"""

# now we can reverse, convert all to bgr, except grayscale to hsv, need to do bgr in between them.

#hsv to bgr

hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
#cv.imshow("hsv to bgr", hsv_bgr)

lab_bgr = cv.cvtColor(lab, cv.COLOR_Lab2BGR)
#cv.imshow("lab to bgr", lab_bgr)



cv.waitKey(0)