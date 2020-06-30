# -*- coding: utf-8 -*-
"""
Simple Thresholding 

@author: Christian Quintanar
"""

from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import cv2

img = Image.open("").convert('L')
threshold = 180
img = np.asarray(img)

thresh = np.zeros(img.shape)

height, width = img.shape
for y in range(height):
    for x in range(width):
        if(img[y,x]>=threshold):
            thresh[y,x] = 1
        
plt.subplot(131)
plt.title("Original")
plt.imshow(img, cmap="Greys_r")
plt.subplot(132)
plt.title("Thresholded Image")
plt.imshow(thresh, cmap="Greys_r")
plt.subplot(133)
plt.title("Histogram")
plt.hist(img.flatten(), bins=256, facecolor="green")
plt.axvline(threshold, color="black")
plt.show()
