import imageio
import numpy as np
import matplotlib.pyplot as plot

def check_if_zero(array):
    for i in range(len(array)):
        if array[i] != 0:
            return False
    return True


im = imageio.imread('image/test.png')
im = np.array(im)

x_array = []
y_array = []

for x in range(im.shape[0]):
    for y in range(im.shape[1]):
        if check_if_zero(im[x][y]) == False:
            x_array.append(x)
            y_array.append(y)
plot.plot(x_array, y_array)
plot.show()
