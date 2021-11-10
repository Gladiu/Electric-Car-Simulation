import imageio
import numpy as np

im = imageio.imread('image/50opacity.png')
im = np.array(im)
print(im)
