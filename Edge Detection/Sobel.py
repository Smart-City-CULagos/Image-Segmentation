# -*- coding: utf-8 -*-
"""
Sobel

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

Gx = np.array(
      [[-1,0,1],
      [-2,0,2],
      [-1,0,1]])
Gy = np.array(
    [[-1,-2,-1],
      [0,0,0],
      [1,2,1]])
	
width, height = img.shape
maskM, maskN = (3,3)

SobelX = cv2.filter2D(img,-1,Gx)
SobelY = cv2.filter2D(img,-1,Gy)

SobelX = SobelX.astype(np.int32)
SobelY = SobelY.astype(np.int32)

Mag = np.sqrt(np.square(SobelX)+np.square(SobelY))
      
plt.subplot(121)
plt.title("Original")
plt.imshow(img, cmap="Greys_r")
plt.subplot(122)
plt.title("Sobel")
plt.imshow(Mag, cmap="Greys_r")
plt.show()
