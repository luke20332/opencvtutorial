# binarisation of an image
# convert to a binary image, 0 = black or 255 white
# take image, and a value - threshold, compare each pixel value to the threshold
# if less, it is set to 0, black
# if more, set to 255 - white.
# creaet a binary image from an original one

import cv2 as cv

img = cv.imread("photos/capybara.jpg")
#cv.imshow("original", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('Gray', gray)



#simple thresholding
#cv threshold takes in a grayscale image, the threshold value and a max value, in this case 255
# type of threhsolding is binary
# if below, sets to 0, as is expected in binary images
# thresh is the binarised image
# threshold is the 100 value, that we had passed in.


threshold, thresh = cv.threshold(gray, 100, 255, cv.THRESH_BINARY)
#cv.imshow(" simple thresholded", thresh)

#playing with the values changes which pixels are white or black,
# higher values = less will be white, a lot darker of an image

# inverse threshold
# if less than 150, set to 255
# if greater than, set to 0
# the opposite of the original image.




threshold, thresh_inverse = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
#cv.imshow(" simple thresholded inverse", thresh_inverse)


#Adaptive thresholding 
# downside of simple, is specifying a threshold value
# wont work in advanced cases
# let computer find the optimal value of the threshold value

# 2nd param is max value
# adaptive method we choose is mean of a neighbourhood of pixels - Ad thresh mean c
# just the method we use to find the threshold value

# thresh binary - as per before, we want a binary image


#blocksize (11), what opencv uses to find the mean value. smaller is more accurate

# c value is an int subbed from mean to finetune the thresholder. can be 0 or int. higher the value the less features can be made out
 

adaptive_thresh = cv.adaptiveThreshold(gray, 255,cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 23,11)
cv.imshow("adaptive", adaptive_thresh)

# the threshold value depends on where the window used to find the threshold is, it can vary amon the entire image.

# adaptive gaussian adds a weight to each pixel value, and computes the mean across pixels
# mean is better in this case, but can be different based on the scenario



cv.waitKey(0)
