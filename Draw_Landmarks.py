# -*- coding: utf-8 -*-
"""
Plot circular landmarks in image given corresponding centers.
Centers are some hyperparameters given by the user.
Freely change it to draw you own maps.

@author: Riemann Lee
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

img = plt.imread('img/Canvas.png')

fig,ax = plt.subplots(1)
ax.spines['left'].set_position('zero')
ax.spines['right'].set_position(('data', 800))
ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_position(('data', 600))
# Create a figure. Equal aspect so circles look circular
ax.set_aspect('equal')

# Don't use any ticks to make the image more visible
plt.xticks([])
plt.yticks([])

# Show the image
ax.imshow(img)

# Given centers of cicular landmarks and it's radius
# Note that the more landmarks we are creating, then the more computation time we require.


# Version 1: 5 landmarks
Centers = np.array([ [336,175], [718,159], [510,43], [167, 333], [472, 437] ])
Radius = np.array([ [12], [6], [7], [18], [9] ])

# Version 2: 10 landmarks
# Centers = np.array([ [144,73], [510,43], [336,175], [718,159], [178,484], [665,464], [267, 333], [541, 300], [472, 437], [100, 533] ])
# Radius=np.array([ [12], [32], [7], [8], [13], [6], [7], [8], [9], [10] ])

if len(Centers) != len(Radius):
    raise ValueError("Centers and Radius must have the same size!")
# Now, loop through coord arrays, and create a circle at center
for count, value in enumerate(Centers):
    circ = Circle(value,Radius[count])
    ax.add_patch(circ)

# Show the map with landmarks
plt.show()
fig.savefig("./img/Map_With_Landmarks_1.png")