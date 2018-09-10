#Lets organize Everything

# First start with the packages
import cv2
import numpy as np
from matplotlib import pyplot as plt
from pyimagesearch.shapedetector import ShapeDetector
import argparse
import imutils

imagePath = 'highQuality.png'
img = cv2. imread(imagePath,1)
# now we have edge detection via canny edge detection algorithm
edges = cv2.Canny(img,400,1100)

#show the new images
plt.imshow(edges)
plt.title('edgeDetection'), plt.xticks([]), plt.yticks([]) #hide the ticks

#plt.show()

#now we have the edge image stored.
#resize the image and then calculate the ratio factor
resized = imutils.resize(edges, width=300)
cv2.imshow("resized",resized)
ratio = edges.shape[0] / float(resized.shape[0])


# convert the resized image to grayscale, blur it slightly,
# and threshold it
blurred = cv2.GaussianBlur(resized, (5, 5), 0)
#cv2.imshow("blurred",blurred)
thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]
#cv2.imshow("Threshold",thresh)
cv2.imshow("original", img)

#find coutours:
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE)

cnts = cnts[0] if imutils.is_cv2() else cnts[1]
sd = ShapeDetector()
selected_Contours = []

# loop over the countours to select only desired contours
for c in cnts:
    peri = cv2.arcLength(c,True)
    approx = cv2.approxPolyDP(c,0.05*peri,True)
    
    if len(approx) >= 4:
            selected_Contours.append(c)


#drawing selected contours
for c in selected_Contours:
    # compute the center of the contour, then detect the name of the
    # shape using only the contour
    M = cv2.moments(c)
    cX = int((M["m10"] / M["m00"]) * ratio)
    cY = int((M["m01"] / M["m00"]) * ratio)
    shape = sd.detect(c)
    # multiply the contour (x, y)-coordinates by the resize ratio,
    # then draw the contours and the name of the shape on the image
    c = c.astype("float")
    c *= ratio
    c = c.astype("int")
    cv2.drawContours(edges, [c], -1, (240,248,255), 2)
    cv2.putText(edges, shape, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX,
        0.5, (255, 255, 255), 2)

    # show the output image
    cv2.imshow("Image", edges)
    cv2.waitKey(0)
