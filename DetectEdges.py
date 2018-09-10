#Going to load a simple image

    #from PIL import Image, ImageFilter

    #image = Image.open('rulerTestImage.jpeg')
    #image.show()



import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('highQuality.png',11)
edges = cv2.Canny(img,400,1000)
cv2.imshow('originalDefault',img)

plt.subplot(121),plt.imshow(img)
plt.title('Original Image'), plt.xticks([]), plt.yticks([]) #hides the ticks
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()
