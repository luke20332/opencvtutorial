# smooth image if lot of noise due to sensors or lighting.
# reduce noise by applying blurring.
# gaussian blur may not work

#need to define a kernel/window, which is overlayed on an image, a small section
# the window has a size - kernel size (rows x columns). 
# blur is applied to middle pixel based on surrounding pixels, the 8 surrounding ones.

import cv2 as cv

img = cv.imread("photos/capybara.jpg")
#cv.imshow("Capybara", img)

#averaging
# define kernel window, and pixel intensity of center = avg of surrounding ones.
# kernel is applied all across the image.
# cv.blur takes in image and a kernel size to compute the blur on.

# higher kernel = more blur


average = cv.blur(img, (3,3))
cv.imshow("avg blur", average)

# gaussian blur
# instead of average of surrounding pixels, each surrounding pixel is given a weight, and product of weights is the value of the center pixel
# less  blurring, but more of a natural bluee
# 3rd param is std deviation in the x direction.

gauss = cv.GaussianBlur(img, (3,3), 0)
cv.imshow("gauss", gauss)


#median blur
# similar to averaging, instead, we find the median of surrounding pixels
# better at reducing noise than gauss and avg
# less salt and pepper noise.
# good for reducing some of noise

#param isnt a tuple, it just takes an int - 3x3 or 7x7.
# looks more like a watercolor painting, smudged.
# not meant for high kernel sizes, only small noise reduction

#for equal kernel size, there is less blurring than gauss, 

median = cv.medianBlur(img, 3)
cv.imshow("median", median)


# bilateral blurring
# most effective, in advanced projects
# trad methods dont care about edges, here we retain edges.

#2nd param is the diameter of the pixel neighbourhood size
# 3rd is sigma colour - larger = more colors in neighbourhood to be considered
# sigma space = larger values = pixels further out affect it more. how much you want far pixels to affect it.

bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow("bi", bilateral)

# looks similar to original image, edges definitely still apparent
# larger params make it look like median blur - smudged image.


cv.waitKey(0)

