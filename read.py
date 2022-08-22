import cv2 as cv

#read in images through imread
#store read image as a local var, img, which is a matrix of pixels representing the image

img = cv.imread('photos/capybara.jpg')

cv.imshow('Capybara', img)
# cv.imshow shows the image as a new window

cv.waitKey(0)
#waits for a delay for a key to be pressed, if 0 = infinite.


# reading in videos
# instead of path, integers 0,1,2,3 are used for your webcam and other connected cameras


capture = cv.VideoCapture('videos/corn.mp4')
#capture var is an instance of the VideoCapture class.


# use a while loop and read the video frame by frame
#capture.read reads in the video frame by frame and returns frame, and a bool if frame was read or not

while True:
  isTrue, frame = capture.read() # convert the image frame by frame
  cv.imshow('Video', frame) #show each frame


  if cv.waitKey(20) & 0xff==ord('d'): # after 20 seconds and another condition - if d is pressed, then break
    break


capture.release() # release the capture, freeing the memory
cv.destroyAllWindows() # close all windows


# x button doesnt kill, need to use d

# -215 assertion error occurs when opencv isnt able to find a media file to display to the user. This can either be due to a wrong path given by the user or if the video finishes and runs out of 'frames' to display to the user.

