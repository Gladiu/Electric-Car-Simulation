import imageio
import numpy as np
import matplotlib.pyplot as plot

def convert_image_to_array_of_points(image):
    # Fliping image to have point 0,0 be at bottom left corner
    flipped_image = np.flipud(image)

    return_array = np.array([])
    # If point isnt full of zeroes then add it to
    for y in range(flipped_image.shape[0]):
        for x in range(flipped_image.shape[1]):
            current_point = flipped_image[y][x]
            index_array= np.where(current_point == 0)
            if index_array[0].size != 0:
                np.append(return_array, (x,y))

def main():
    image = imageio.imread('image/test.png')
    image = np.array(image) # Converting python array to numpy array
    
    my_array = convert_image_to_array_of_points(image)
    print(my_array)

    #plot.imshow(image)
    #plot.show()
    

if __name__=="__main__":
    main()
