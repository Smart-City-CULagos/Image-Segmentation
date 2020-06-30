# -*- coding: utf-8 -*-
"""
Otsu's method

1.- Compute histogram and probabilities of each level
2.- Setup initial w and u
3.- Step through all posible thresholds t=1, ... maximun intensity level
    1.- Update w and u
    2.- Compute sigma squared
4.- Desired threshold corresponds to maximum sigma squared

@author: Christian Quintanar
"""

from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import cv2

img = Image.open("").convert('L')
img = np.asarray(img)

histogram = np.zeros(256, dtype="uint32")
sequence = img.flatten()
sequence = np.sort(sequence)

j=0
for i in range(256):
    while(sequence[j]==i and j<(sequence.size-1)):
        histogram[i]+=1
        j+=1

histogram[255]+=1

sumF = np.dot(range(256), histogram)
sumB = 0
Wb=0
Wf=0
Max=0
threshold = 0;

for t in range(256):
    Wb+=histogram[t]
    if(Wb==0):
        continue
    Wf= sequence.size - Wb
    if(Wf==0):
        break
        
    sumB += t * histogram[t];
    Mb = sumB/Wb
    Mf = (sumF - sumB)/Wf
    Var = Wb*Wf*np.square(Mb-Mf)
    if(Var > Max):
       Max = Var
       threshold = t
       
       
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
plt.hist(sequence, bins=256, facecolor="green")
plt.axvline(threshold, color="black")
plt.show()
