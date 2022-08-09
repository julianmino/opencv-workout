import cv2 as cv

## Functions

def rescaleFrame(frame, scale=0.75):
    # Images, videos & live video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes(capture: cv.VideoCapture, width, height):
    # Only live videos
    capture.set(3, width) 
    capture.set(4, height)

## Main

### IMAGE RESIZING

img = cv.imread('../Supporting Files/Photos/cat.jpeg')
cv.imshow('Cat', img)
cv.waitKey(0)

img_resized = rescaleFrame(img)
cv.imshow('Cat Rescaled', img_resized)
cv.waitKey(0)

### VIDEO RESIZING

captureVideo = cv.VideoCapture('../Supporting Files/Videos/marathon.mp4')

while True:
    isTrue, frame = captureVideo.read()
    cv.imshow('Video', rescaleFrame(frame))

    if cv.waitKey(20) & 0xFF==ord('d'): # 2nd clause means if letter 'd' is pressed
        break

captureVideo.release()

### LIVE VIDEO RESIZING

captureLive = cv.VideoCapture(0)

changeRes(captureLive, 600, 400) # Here we change the resolution

while True:
    isTrue, frame = captureLive.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'): # 2nd clause means if letter 'd' is pressed
        break

captureLive.release()
cv.destroyAllWindows()