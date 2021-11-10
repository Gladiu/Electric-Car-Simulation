import imageio
import numpy as np

im = imageio.imread('test.png')
im = np.array(im)
print(im[1])
