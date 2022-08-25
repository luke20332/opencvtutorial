# AND OR XOR NOT
# used in image processing and masks
# 0 off, 1 = on




from cmath import rect
import cv2 as cv
import numpy as np

img = cv.imread("photos/capybara.jpg")
img1 = cv.imread("photos/finger.jpg")

blank = np.zeros((400,400), dtype='uint8') # blank image, binary

# create a rectangle in opencv, image is a copy of the blank, with 
# starting point 30 pixels from true zero, and end also 30
# colour is just an int as its a binary image, 255 being white
# thickness = -1 fill image


rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1 )

circle = cv.circle(blank.copy(), (200,200), 200, 255, -1)


#cv.imshow("rect", rectangle)
#cv.imshow("circle", circle)

# AND
# cv.bitwise_and is a function used to find the bitwise and of 2 images

bitwiseand = cv.bitwise_and(rectangle, circle)
#cv.imshow("bit and", bitwiseand)
# kind of a mixture of both images.
# placed on top and returned intersection of the images.
# only gives area common to both, as is nature of AND.

# OR

bitwiseor = cv.bitwise_or(rectangle, circle)
#cv.imshow("or", bitwiseor)
# returns all area - common and not common, but at least one.


# XOR
# return the non intersecting regions - only the single layered regions

bitxor = cv.bitwise_xor(rectangle, circle)
cv.imshow("xor", bitxor)

# NOT
# inverts the binary color - 1 -> 0, 0->1


bitnot = cv.bitwise_not(rectangle)
cv.imshow("not", bitnot)

cv.waitKey(0)