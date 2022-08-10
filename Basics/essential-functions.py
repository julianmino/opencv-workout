import cv2 as cv

img = cv.imread('../Supporting Files/Photos/cat.jpeg')

cv.imshow('Cat', img)

# CONVERTING TO GRAYSCALE

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# BLUR

blur = cv.GaussianBlur(img, (5, 5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# EDGE CASCADE

canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny', canny)

# DILATING THE IMAGE
dilated = cv.dilate(canny, (3,3), iterations=1)
cv.imshow('Dilated', dilated)

# ERODING
eroded = cv.erode(dilated, (3,3), iterations=1)
cv.imshow('Eroded', eroded)

# RESIZE

resized = cv.resize(img, (500,500), interpolation=cv.INTER_AREA)
cv.imshow('Resixed', resized)

# CROPPING
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)
cv.waitKey(0)