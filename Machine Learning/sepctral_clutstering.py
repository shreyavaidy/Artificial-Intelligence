# Assignment 3: Machine Learning
# Problem 3 - Bonus - Spectral Clustering
##############################################

import numpy as np
import matplotlib.pyplot as plt
from sklearn.feature_extraction import image
from sklearn.cluster import spectral_clustering

l = 100
x, y = np.indices((l, l))

center1 = (20, 24)
center2 = (40, 50)
center4 = (24, 70)

radius1, radius2, radius3, radius4 = 16, 14, 15, 14

circ1 = (x - center1[0]) ** 2 + (y - center1[1]) ** 2 < radius1 ** 2
circ2 = (x - center2[0]) ** 2 + (y - center2[1]) ** 2 < radius2 ** 2
circ3 = (x - center4[0]) ** 2 + (y - center4[1]) ** 2 < radius4 ** 2

# Making 3 circles of the new image from the computed values
newspec_image = circ1 + circ2 + circ3

mask = newspec_image.astype(bool)

newspec_image = newspec_image.astype(float)
newspec_image += 1 + 0.2 * np.random.randn(*newspec_image.shape)

# Converting the image into a graph
graphed = image.img_to_graph(newspec_image, mask=mask)

graphed.data = np.exp(-graphed.data / graphed.data.std())

labels = spectral_clustering(graphed, n_clusters=4, eigen_solver='arpack')
label_im = -np.ones(mask.shape)
label_im[mask] = labels

plt.matshow(newspec_image)
plt.matshow(label_im)
plt.show()


