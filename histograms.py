#visualise distributions of pixel intensities in an image.
# color or grayscale, can see distribution of intensities with a plot or graph

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("photos/capybara.jpg")

blank = np.zeros(img.shape[:2], dtype='uint8')


"""
gray  =cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)
"""

mask = cv.circle(blank, (img.shape[1] // 2, img.shape[0]//2), 100, 255, -1)
# the mask we are using on the original iamge

#masked is the image once it has been masked.
masked = cv.bitwise_and(img, img,mask=mask) # when doing bitwise and, we get the same image twice, applying a mask of a circle overtop
cv.imshow("the mask", masked)

# when radius of circle is 100, the histogram is similar to the original image
# when i put it to 10, then the histogram is a lot different as it predominantly takes up the eye


#greyscale histograms
# need a list, so pass a singular list of image
# 2nd param is # channels = index of channel we want a histogram for, grayscale, so use lsit, pass 0
# then mask - no mask needed so non
# histSize = number of bins we want as a list
# range = range of pixel values 0 to 256

"""
grayhist = cv.calcHist([gray], [0], mask, [256],[0,256])

plt.figure()
plt.title('grayscale histogram')
plt.xlabel('Bins') # the intervals of pixel intensities
plt.ylabel('# of pixels')
plt.plot(grayhist)
plt.xlim([0,256])
plt.show()
"""

# for the capybara image, there is a peak at around 171, so there are 12000 pixels that have an intensity of 171.

# peak around 120 to 200

# for the finger image, there is a small blip around 20, which is the darks of the image
# Massive peak at the end, which is the whites of the image (text box at top);

# can compute a histogram after a mask has been applies




#color histogram
# the histogram of the original image
# plot for blue, red and green channels
# blue peaks at 100, red at 170, green at 185
# can see dist of pixel intensities of different colors


plt.figure()
plt.title('color histogram')
plt.xlabel('Bins') # the intervals of pixel intensities
plt.ylabel('# of pixels')

colors = ('b','g','r') #tuple of colors, set to each of bgr.
for i,col in enumerate(colors): # for each value in the tuple colors
  hist = cv.calcHist([img], [i], mask, [256],[0,256]) # compute over image, channels is i, no mask, histsize = 256, range is 0 to 256.
  plt.plot(hist, color = col) # plot the histogram on the plot, color is right color
  plt.xlim([0,256]) # limits of the graph are 0 to 256 on the x axis



# when using the masked image, blue and green peak early, red later on, as the image of the capybara is brown, which is similar to red.

#analyse dist of pixel intensities, gray or color.
# advances projects, analyse image, equalise it to reduce any peaking


plt.show()

cv.waitKey(0)