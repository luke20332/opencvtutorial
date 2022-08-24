import cv2 as cv
import numpy as np

img = cv.imread('photos/finger.jpg')

cv.imshow("original", img)

#translation
# shift along x and y axis
# need a translation func
# x and y is amount of pixels to be translated by
# need to make a translation matrix first, which is a numpy matrix
# type is a float, take in a lsit of 2 lsits, [[],[]]


def translate (img, x, y):
  transMat = np.float32([[1,0,x],[0,1,y]]) #
  dimensions = (img.shape[1], img.shape[0]) # 1 is width, 0 is height
  return cv.warpAffine(img, transMat, dimensions)
  # warpAffine translates the image based on the translation matrix


# -x --> translate to the left
# -y --> shift up
# +x --> translate right
# +y --> shift down

"""
translated = translate(img, 50, 50)
cv.imshow("translated", translated)
"""

# rotation
# can specify any rotation point, default is centre

def rotate(img, angle, rotPoint=None):
  (height, width) = img.shape[:2] # set the height and width as the 2 last values

  if rotPoint is None:
    rotPoint = (width//2, height//2) # if not defined, it is the centre

  #params are rotation point, the angle of rotation and scale 
  rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0) # like translation
  dimensions = (width, height) # dimensions are assigned as the same as before

  return cv.warpAffine(img, rotMat, dimensions)

"""
rotated = rotate(img, 45) # in degrees from the positive x axis
cv.imshow("rot", rotated)

rotated1 = rotate(rotated, 45)
cv.imshow("fduf", rotated1)
"""

# can then rotate the rotated image.
# however, since it uses the most recent image, some of it will be cut off, introducing some black triangles
# somewhat skewed image


#resizing
"""
resized = cv.resize(img, (1920,1080), interpolation=cv.INTER_CUBIC)
cv.imshow("resize", resized)
"""

#flipping
# takes in a flip code, can be 0, 1, -1
# 0 is a vertical flip, over x axis - reflect over x axis
# 1 is a horizontal over y axis
# -1 is both

flip = cv.flip(img, 0)
cv.imshow("Flip", flip)


# cropping

cropped = img[100:200, 150:200]
cv.imshow("CRopped", cropped)

cv.waitKey(0)

