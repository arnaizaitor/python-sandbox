import numpy as np
from numpy import asarray
from PIL import Image
from primeFunctionalities import *
import matplotlib.pyplot as plt

class Pyxelator():

    ################################################################################
    # arguments: image: image we want to pixelate passed as a pillow Image
    # returns: pre_pyxel: list of lists with pixels to make average of them
    ################################################################################
    def relocate_pixels(this, image, pyxel_len):
        size = image.size
        # Store the image data as a numpy array
        image_arr = asarray(image)

        # Void list to remply with new pixels
        pre_pyxel = list([] for i in range(int((size[0]/pyxel_len)*(size[1]/pyxel_len))))

        current_pixel = 0
        # Double loop to locate pointer on pre_pyxel matrix
        for i in range(0, size[0], pyxel_len):
            for j in range(0, size[1], pyxel_len):
                # Double loop to add pixels to form new pixels
                for i_p in range(pyxel_len):
                    for j_p in range(pyxel_len):
                        # We add the pixels to average them to pyxelize
                        pre_pyxel[current_pixel].append(image_arr[j + j_p][i + i_p])
                current_pixel += 1

        return pre_pyxel

    ################################################################################
    # arguments: pre_pyxel: list of lists with pixels to make average of them
    # returns: avg_pixels: list of averaged pixels
    ################################################################################
    def average_pixels(this, pre_pyxel):
        avg_pixels = []
        for new_pixel in pre_pyxel:
            r_acc, g_acc, b_acc = 0, 0, 0
            pre_pyxels_count = 0
            for r, g, b in new_pixel:
                r_acc += r
                g_acc += g
                b_acc += b
                pre_pyxels_count += 1
            # We make the average colour of previous pixels 
            avg_pixels.append(list((int(r_acc/pre_pyxels_count), int(g_acc/pre_pyxels_count), int(b_acc/pre_pyxels_count))))
            
        return avg_pixels

    ################################################################################
    # arguments: avg_pixels: list of averaged pixels
    #            new_x: new x_dimension of the matrix
    #            new_y: new y_dimension of the matrix
    # returns:   relocated_pixels: matrix of new averaged pixels in correct position
    ################################################################################
    def pixelate_image(this, avg_pixels, new_x, new_y):
        relocated_pixels = list([] for i in range(new_x))
        acc = 0
        y_pointer = 0
        for px in avg_pixels:
            relocated_pixels[y_pointer].append(px)
            acc += 1
            if(acc == new_y):
                acc = 0
                y_pointer += 1

        return relocated_pixels

    def rotate(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        
        # Preste atención al alcance y subíndice
        for i in range(n//2):
            for j in range(i, n-1-i):
                matrix[i][j], matrix[j][n-1-i], matrix[n-1-i][n-1-j], matrix[n-1-j][i] = \
                matrix[n-1-j][i], matrix[i][j], matrix[j][n-1-i], matrix[n-1-i][n-1-j]

    ################################################################################
    # arguments: new_pixels: list of pixels in correct position
    # returns: None 
    ################################################################################
    def save_pixelyzed_image(this, new_pixels):
        plt.axis('off')
        plt.imshow(asarray(new_pixels))
        plt.savefig('../images/try.png', transparent=True)
        return


# We create an instance of the Pyxelator
px = Pyxelator()
# We create an instance of the PrimeFunctionalities
pf = PrimeFunctionalities()
# load the image
image = Image.open('../images/parrots.jpeg')
# We store its dimensions
old_x = image.size[0]
old_y = image.size[1]
# We calculate the new pixel length
pixel_len = pf.MCD(list(image.size))
pixel_len = int(pixel_len/6)
# We calculate the new dimensions of the image
new_x = int(old_x/pixel_len)
new_y = int(old_y/pixel_len)

####################
# IMAGE PROCESSING #
####################
# We relocate the image pixels in order to pixelyze the image
relocated_pixels = px.relocate_pixels(image, pixel_len) 
# We make the average pixels of the previous image in order to pixelyze it
avg_pixels = px.average_pixels(relocated_pixels)
# We relocate the average pixels in their correct positions in order to remake the image
final_pixels = px.pixelate_image(avg_pixels, new_x, new_y)
# We rotate the matrix 270 degrees
final_pixels = np.rot90(np.rot90(np.rot90(final_pixels)))
# We flip the rows
final_pixels = [row[::-1] for row in final_pixels]
# We store the final image
px.save_pixelyzed_image(final_pixels)
