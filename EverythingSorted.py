#Lets organize Everything

# First start with the packages
import cv2
import numpy as np
from matplotlib import pyplot as plt
from pyimagesearch.shapedetector import ShapeDetector
import argparse
import imutils
from skimage.morphology import erosion, dilation, opening, closing, white_tophat
from skimage.morphology import disk, square
from skimage.restoration import (denoise_tv_chambolle, denoise_bilateral,
                                 denoise_wavelet, estimate_sigma)

imagePath = 'highQuality.png'
imagePath2 = 'test1.png'
imagePath3 = 'test2.png'
img = cv2. imread(imagePath,1)
enlarged = imutils.resize(img,width=1000)
# now we have edge detection via canny edge detection algorithm
edges = cv2.Canny(img,400,1200)

# Now lets try to use close operator to see if we can patch all the holes
selem = disk(2)
closed = closing(edges,selem)

#now we have the edge image and closed 
#resize the image and then calculate the ratio factor
resized = imutils.resize(closed, width=1000)
cv2.imshow("resized",resized)
ratio = edges.shape[0] / float(resized.shape[0])


# convert the resized image to grayscale, blur it slightly,
# and threshold it
blurred = cv2.GaussianBlur(resized, (5, 5), 0)


# do a errosion to remove some of the small blobs
erroded = erosion(blurred, square(4))
#erroded = denoise_bilateral(erroded,multichannel=False)
cv2.imshow("erroded", erroded)


#find coutours:
cnts = cv2.findContours(erroded.copy(), cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE)

cnts = cnts[0] if imutils.is_cv2() else cnts[1]
sd = ShapeDetector()
selected_Contours = []


#defining a function
# takes in the sides and the perimeter of the contour. Expect regular shape, compare area and perimeter ratio to see if the shape is the desired one.
# If close enough to ideal ratio, keep this countour
# may or may not be needed. s
    
def shapeVerification (contour) :
    perimeter = cv2.arcLength(contour,True)
    area = cv2.contourArea(contour)
    sides = len(countour)

    if sides == 4:
        # for rectangles, the aspect ratio is important. Get rid of thin lines
        x,y,w,h = cv.boundingRect(cnt)
        aspect_ratio = float(w)/h
        if aspect_ratio < 0.6 :
            return False
        else :
            return True 
    elif ( sides == 5 or sides(countour) == 6 ):
        # for pentagon compute area of a regular pentagon
        ideal_area = perimeter**2 / (4*math.tan( math.pi / sides) )
        area_Ratio = ideal_area / area
        if (area_Ratio <= 1.2 and area_Ratio >= 0.8 ) :
            return True
        else :
            return False
    elif (sides > 6) :
        ideal_area = perimeter **2 / (math.pi * 4)
        if (area_Ratio <= 1.2 and area_Ratio >= 0.8 ) :
            return True
        else :
            return False
    else :
        return False

# loop over the countours to select only desired contours
for c in cnts:
    peri = cv2.arcLength(c,True)
    approx = cv2.approxPolyDP(c,0.02*peri,True)
    if len(approx) >= 4 :
        selected_Contours.append(approx)


#drawing selected contours
for c in selected_Contours:
    # compute the center of the contour, then detect the name of the
    # shape using only the contour
    M = cv2.moments(c)
    #cX = int((M["m10"] / M["m00"]) * ratio)
    cX = int((M["m10"] / M["m00"]))
    cY = int((M["m01"] / M["m00"]))
    shape = sd.detect(c)
    # multiply the contour (x, y)-coordinates by the resize ratio,
    # then draw the contours and the name of the shape on the image
    c = c.astype("float")
    #c *= ratio
    c = c.astype("int")
    cv2.drawContours(enlarged, [c], -1, (240,248,255), 2)
    cv2.putText(enlarged, shape, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX,
        0.5, (255, 255, 255), 2)

    # show the output image
    cv2.imshow("Image", enlarged)
    cv2.waitKey(0)
