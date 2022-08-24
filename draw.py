import cv2 as cv
import numpy as np

# a blank image is a matrix of 0's (500x500), number of colour channels (3) and is of the type uint8 - the datatype of an image


blank = np.zeros((500,500,3), dtype = 'uint8')

"""
img = cv.imread('photos/capybara.jpg')
cv.imshow('cat', img)

cv.imshow('blank', blank)
"""

# 1. Painting the image a certain colour

"""
blank[:] = 30,55,100
cv.imshow('Random colour', blank)
"""

# 2. Colouring a certain portion
"""
blank[200:300, 300:400] = 0,0,255
cv.imshow("Range", blank)
"""
# 3. Draw a rectangle, using the cv.rectangle method
# this takes the params: image, start pixel(top left), end pixel(bottom right), colour and thickness
# thickness = cv.FILLED will fill the area instead, or -1.


"""
cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness=-1)
cv.imshow('Rectangle', blank)
"""

# 3.5 making a square, with dimensions being half of the original image

"""
cv.rectangle(blank,(0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness = -1)
cv.imshow("REctangle", blank) 
"""

# 4. Drawing a circle
# params are image, centre pixel, radius, colour, thickness

"""
cv.circle(blank, (250,250), 40, (0,0,255), thickness = -1)
cv.imshow('circle', blank)
"""

# 5 . Drawing a line
# params are image, beginning, end of line and colour of line

"""
cv.line(blank, (100,250), (300, 400), (255,255,255), thickness = 5 )
cv.imshow("line", blank)
"""

# 6 text on an image
# params are image, text, origin of text(x,y of base) , fontFace, scale of text, color, thicknees
cv.putText(blank, "hello my name is jason", (0,255), cv.FONT_HERSHEY_COMPLEX, 1.0, (255,255,255), thickness = 2)
cv.imshow("text", blank)






cv.waitKey(0)


#draw on standalone images, or a blank image to work with
