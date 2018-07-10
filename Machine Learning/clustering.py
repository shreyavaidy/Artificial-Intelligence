# %matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
import seaborn
import imageio

np.random.seed(sum(map(ord, "aesthetics")))
seaborn.set_context('notebook')

# Color image clustering using KMeans
from sklearn.cluster import KMeans
with seaborn.axes_style('dark'):
    original_image = imageio.imread('trees.png')
    # plt.imshow(original_image)
    # plt.show()


image_rescale = (original_image).reshape(-1,3)

print image_rescale.shape
# print image_rescale.min(axis=0)


i = 5
while(i <= 15):
    # Shuffle the image array
    from sklearn.utils import shuffle

    shuffled_image = shuffle(image_rescale, n_samples=i, random_state=0)

    k_colors = KMeans(init='k-means++', random_state=0, n_clusters=i)
    k_colors.fit(image_rescale)
    i=i+5

    # Predict the y-labels
    y_pred = k_colors.predict(shuffled_image)
    # print k_colors.cluster_centers_.shape

    # Find the new image with labels
    new_image = k_colors.cluster_centers_[k_colors.labels_]
    # print new_image.shape

    new_image = np.reshape(new_image, (original_image.shape))
    # print new_image.shape

    # Now plot the two images side by side to see the difference
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(1, 2, 1, xticks=[], yticks=[], title='Original Trees')
    ax.imshow(original_image)

    ax = fig.add_subplot(1, 2, 2, xticks=[], yticks=[], title='Clustered Trees Using K-Means')
    ax.imshow(new_image)
    plt.show()

