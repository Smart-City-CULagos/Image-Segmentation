# -*- coding: utf-8 -*-
"""
K-Means

@author: Christian Quintanar
"""

from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans

img = Image.open("")
img = np.asarray(img)/255

img_n =img.reshape(img.shape[0]*img.shape[1], img.shape[2])

kmeans = KMeans(n_clusters=5, random_state=0).fit(img_n)
pic2show = kmeans.cluster_centers_[kmeans.labels_]

cluster_pic = pic2show.reshape(img.shape[0], img.shape[1], img.shape[2])


plt.subplot(121)
plt.title("Original")
plt.imshow(img)
plt.subplot(122)
plt.title("K-Means")
plt.imshow(cluster_pic)
plt.show()
