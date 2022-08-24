import cv2 as cv

img = cv.imread('photos/finger.jpg')
cv.imshow('original image', img)

# this image rn is a 3 channel, rgb image.

# Conversion into greyscale, show intensity distribution instead of colours
# cvtColor converts inverts the colour of the image, in this case from color (BGR channel) to grayscale

"""
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grey', gray)
"""

# 2 - Blurring an image
# remove noise, extra elements we dont want to have, due to lighting, or camera, etc
#using a gaussian image
# params are src image, a kernel size: a 2x2 tuple window size opencv uses to comptute the gaussian blur on the image. As in DDCS, the kernel is a smaller tuple overlayed on the original to create a blur. spatial filtering using 2d convolution
# kernel size has to be odd number, to have a central pixel. Higer kernel = more blur

# then a border


blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
#cv.imshow("blurred", blur)



#3. Edge cascade
# trying to find the edges in the image
# many to choose, using the canny one here which is popular
# a multi stage algorithm blurring, gradient computation, etc

#2 threshold values.

# quite a detailed image, with info we may potentially not need, so we can pass the blurred image instead to reduce some of the edge details. far less edges will be shown. more of a sillouette



canny = cv.Canny(blur, 125, 175)
cv.imshow("canny", canny)


# 4. Dilate in image using a structuring element.
# element is the canny edges we have found
# take in an image or the element (canny image), kernel size, and iterations, in this case just one

# essentially makes the edge lines found a lot thicker
# can erode dilated image to restore original structuring element

dilated = cv.dilate(canny, (7,7), iterations = 3 )
cv.imshow("dilate", dilated)

#5. Eroding
# attempts to undo the dilation, not perfect but does 'sharpen' the image in a sense


eroded = cv.erode(dilated, (7,7), iterations = 3)
cv.imshow("eroded", eroded)

#resize and crop an image
# already done resizing, using the cv.resize func

# 2nd param is the final resolution, the size of the final image
# cv interpolation occurs naturally, useful if shrinking the iamge inter_area, or default
# inter_linear if enlarging
# inter_cubic if enlarging - slower but high quality.

"""
resized = cv.resize(img, (750,100), interpolation= cv.INTER_CUBIC)
cv.imshow("resize", resized)
"""

# cropping
# images are arrays, can do array slicing, select portion based on pixel values
# so pixels in between 50 and 200 pixels int he y axis
# pixels between 200 and 400 in the x axis are shown



crop = img[50:200, 200:400]
cv.imshow("cropped", crop)



cv.waitKey(0)
