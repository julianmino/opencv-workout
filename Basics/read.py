from tkinter import Frame
from tokenize import Comment
import cv2 as cv

# READING AN IMAGE

img = cv.imread('../Supporting Files/Photos/cat.jpeg')

cv.imshow('Cat', img)

cv.waitKey(0) ## Waits for a key to be pressed.

# READING A VIDEO

# It can take an integer or a video file path 
# as an argument (0 --> integrated webcam)
capture = cv.VideoCapture('../Supporting Files/Videos/marathon.mp4')

## Reading a video is like reading each frame,
## so we have to loop until the end of the video.

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'): # 2nd clause means if letter 'd' is pressed
        break

capture.release()
cv.destroyAllWindows()