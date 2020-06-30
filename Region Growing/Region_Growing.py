# -*- coding: utf-8 -*-
"""
Region Growing

1.- Chose a pixel
2.- Set mean to pixel intensity
3.- Consider each neighbor of pixel
    1.- If neighbor intensity - mean > threshold
    2.- Append neighbor pixel to region
        1.- Update region mean and restart

@author: Christian Quintanar
"""

import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import cv2

img = Image.open("").convert('L')
img = np.asarray(img)

thresh = np.zeros(img.shape)
seed_x, seed_y = (200, 393)
mean = (float)(img[seed_y, seed_x])
sumT = (float)(img[seed_y, seed_x])
threshold = 40
region = np.zeros(img.shape)
checked = np.zeros(img.shape)
region[seed_y, seed_x] = 1

queue = []
queue.append([seed_y,seed_x])
count=1

neighbors = np.array([[-1,0],[0,1],[1,0],[0,-1],[-1,-1],[1,-1],[1,1],[-1,1]])

while queue != []:
    pixel = queue.pop(0)
    for neighbor in neighbors:
        coord = pixel+neighbor
        if(coord[0]>=0 and coord[1]>=0 and coord[0]<img.shape[0] and coord[1]<img.shape[1]):
            if(checked[coord[0], coord[1]]==0):
                if(abs(img[coord[0], coord[1]]-mean)<threshold):
                    region[coord[0], coord[1]] = 1
                    queue.append([coord[0], coord[1]])
                    count+=1
                    sumT+=img[coord[0], coord[1]]
                    mean=sumT/count
                checked[coord[0], coord[1]]=1

height, width = img.shape
for y in range(height):
    for x in range(width):
        if(region[y,x]==1):
            thresh[y,x] = img[y,x]

plt.subplot(131)
plt.title("Original")
plt.imshow(img, cmap="Greys_r")
plt.subplot(132)
plt.title("ROI")
plt.imshow(region, cmap="Greys_r")
plt.subplot(133)
plt.title("Crop")
plt.imshow(thresh, cmap="Greys_r", vmin=0, vmax=255)
plt.show()
