from distutils.command.config import LANG_EXT
import cv2 as cv
import numpy as np

# Creates a blank image (dimensions and ammount of color channels)
blank = np.zeros((500,500, 3), dtype='uint8')
cv.imshow('Blank', blank)

# 1. Point the image a certain color

## Red
blank[:] = 0,0,255
cv.imshow('Red', blank)

## Green
blank[:] = 0,255,0
cv.imshow('Green', blank)

## Blue
blank[:] = 255,0,0
cv.imshow('Blue', blank)

# 2. Draw a rectangle

cv.rectangle(blank, (0,0), (250,250), (220, 120, 20), thickness=cv.FILLED)
cv.rectangle(blank, (blank.shape[0]//4, blank.shape[1]//4), (blank.shape[0]//2, blank.shape[1]//2), (0,0,255), thickness=cv.FILLED)
cv.imshow('Rectangle', blank)

# 3. Draw a Circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[1]//2), 40, (0,0,255), thickness=2)
cv.imshow('Blank', blank)

# 4. Draw a Line
cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[1]//2), (255,255,0), thickness=3)
cv.imshow('Blank', blank)

# 5. Write text
cv.putText(blank, 'Hello', (255,255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,255), thickness=2)
cv.imshow('Text', blank)

cv.waitKey(0)