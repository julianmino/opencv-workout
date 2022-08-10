import cv2 as cv
import numpy as np

# Variables

videoCapture = cv.VideoCapture(1)
prevCircle = None

# Functions

def squareDifference(x1,y1,x2,y2): 
    return (x1-x2)**2 + (y1-y2)**2

# Parameters

kSize = 17
                                    ## Param1 --> [each frame read from videoCapture]
houghMethod = cv.HOUGH_GRADIENT     ## Param2 --> Hough method
dp = 1.2                            ## Param3 --> dp (the larger, the more likely two circles close to each other will be merged)
minDistBetweenCircles = 200         ## Param4 --> minDist, (if our scenario won't have many circles to detect, it's better for this number to be high)
sensitivity = 70                    ## Param6 --> param1 (circle detection sensitivity)
accuracy = 40                       ## Param7 --> param2 (circle detection accuracy. Refers to the number of edges needed to declare the shape as a circle)
minRadius = 10                      ## Param8 --> minRadius (minimum radius to be detected)
maxRadius = 30                      ## Param9 --> maxRadius (maximum radiues to be detected)

centerPointColor = (255,0,0)
circumferenceCircleColor = (0,0,255)
# Main

while True:
    isTrue, frame = videoCapture.read()
    if not isTrue: 
        break

    # Convert the frame to grayscale to remove image noise
    grayFrame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY) # First step
    # Gaussian Blur requires a kernelSize, which is the 
    # window size that will be evaluated to blur
    blurFrame = cv.GaussianBlur(grayFrame, (kSize,kSize), 0) # Second step

    # Use of Hough Transform (returns a list of circles)
    circles = cv.HoughCircles(
        blurFrame, 
        houghMethod, 
        dp, 
        minDistBetweenCircles, 
        param1=sensitivity, 
        param2=accuracy, 
        minRadius=minRadius, 
        maxRadius=maxRadius)

    if circles is not None:
        # Parse circles list into numpy list
        circles = np.uint16(np.around(circles))
        # Find the best possible circle
        chosen = None
        for i in circles[0,:]:
            if chosen is None:
                chosen = i
            if prevCircle is not None:
                if squareDifference(chosen[0], chosen[1], prevCircle[0], prevCircle[1]) <= squareDifference(i[0], i[1], prevCircle[0], prevCircle[1]):
                    chosen = i
        # Draw a circle to represent the center of the circumference
        cv.circle(frame, (chosen[0], chosen[1]), 1, centerPointColor, 8)
        # Draw a circle around the circumference
        cv.circle(frame, (chosen[0], chosen[1]), chosen[2], circumferenceCircleColor, 3)
        prevCircle = chosen
    
    cv.imshow('Circle Detector', frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

videoCapture.release()
cv.destroyAllWindows()