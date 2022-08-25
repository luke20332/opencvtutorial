# split and merge colour channels
# color image is r,b,g colour channels merged together
# can split image into channels.

import cv2 as cv
import numpy as np

img = cv.imread("photos/capybara.jpg")

blank = np.zeros(img.shape[:2], dtype = 'uint8')

b, g, r = cv.split(img)
#split method splits into the 3 channels

#merging a colour, setting the others to black.
blue = cv.merge([b, blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank, blank, r])


cv.imshow("blue", blue)
cv.imshow("green", green)
cv.imshow("red", red)
#get the image in each of rbg.


# the images appear as greyscale, as it displays the distribution of pixel intensity for each colour channel
#blue channel has a dark capybara - low conc of blue in the capy
# green has a light grass, meaning there is a lot of green there.
# red is fairly dark, as brown is somewhat similar to red.




# printing shapes and dimensions of the image and the colours
print(img.shape)
#(627, 1200,3) = 3 colour channels, 600 is the height. 1200 is the width
print(b.shape) # no 3rd tuple, as it is 1.
print(g.shape)
print(r.shape)

# we can show each colour involved, reconstruc the image
# create a blank image, 




merged = cv.merge([b,g,r]) #returns original image
cv.imshow("merged image", merged)




cv.waitKey(0)


