# rescale is done to prevent computational strain
from configparser import Interpolation
import cv2 as cv



#img = cv.imread('photos/cat.jpg')
#cv.imshow("Cat", img)

# if a value is already set in func declaration, that is the default value
# for image, video and live video

def rescaleFrame(frame, scale = 0.75):
  width = int(frame.shape[1] * scale) #frame.shape is a attribute of the frame, the width = 1, height = 0
  height = int(frame.shape[0] * scale)

  dimensions = (width, height)
  # dimensions is a tuple of the new width and height of the image

  return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)
  # return a resized image, based on the original frame, to the new dimensions, and interpolate as INTER_AREA

img = cv.imread('photos/cat.jpg') #img is the large image of the cat
cv.imshow("cat resized", rescaleFrame(img, 0.1)) # we show a resized version of img, using rescaleFrame

#live video only (webcam)
def changeRes(width, height):
  capture.set(3,width)
  capture.set(4, height)
  # 3 and 4 are properties of the capture class, 3 = wdith, 4 = height.
  # 10 is the brightness of the image







# same code from read.py, but we are going to resize the frames from the video
capture = cv.VideoCapture('videos/hdcorn.mp4')
#capture = cv.VideoCapture(0)  for a live video 

while True:
  isTrue, frame = capture.read()  

  frame_resized = rescaleFrame(frame, 0.2)

  cv.imshow('Video', frame)
  cv.imshow('Video Resized', frame_resized)
  # putting these in the same while loop means that the videos play simultaneously, overlayed upon one other in the order which they are called, (resized one is on top of the larger one)


  if cv.waitKey(20) & 0xff==ord('d'): 
    break


capture.release() # release the capture, freeing the memory
cv.destroyAllWindows() 


cv.waitKey(0)

