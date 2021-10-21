import os
import numpy as np
from PIL import Image
from numpy import asarray
from matplotlib import image
from utils import natural_keys
import matplotlib.pyplot as plt
from primeFunctionalities import *


class Pyxelator():

    ################################################################################
    # arguments: image: image we want to pixelate passed as a pillow Image
    #            pyxel_len: length of the new pixel for the image to pixelate
    # returns:   pre_pyxel: list of lists with pixels to make average of them
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
    # returns:   avg_pixels: list of averaged pixels
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


    ################################################################################
    # arguments: new_pixels: list of pixels in correct position
    # returns:   None 
    ################################################################################
    def save_pixelyzed_image(this, new_pixels, output_route):
        plt.axis('off')
        plt.imshow(asarray(new_pixels))
        plt.savefig(output_route, transparent=True)
        return


    ################################################################################
    # arguments: input_route: route of the image to pixelize
    #            output_route: route of the pixelyzed image
    #            pixel-len: length of the new pixels
    # returns:   None 
    ################################################################################
    def pyxelize(this, input_route, output_route, pixel_len=2):
        # load the image
        image = Image.open(input_route)
        # We store its dimensions
        old_x = image.size[0]
        old_y = image.size[1]
        # We calculate the new dimensions of the image
        new_x = int(old_x/pixel_len)
        new_y = int(old_y/pixel_len)
        ####################
        # IMAGE PROCESSING #
        ####################
        # We relocate the image pixels in order to pixelyze the image
        relocated_pixels = this.relocate_pixels(image, pixel_len) 
        # We make the average pixels of the previous image in order to pixelyze it
        avg_pixels = this.average_pixels(relocated_pixels)
        # We relocate the average pixels in their correct positions in order to remake the image
        final_pixels = this.pixelate_image(avg_pixels, new_x, new_y)
        # We rotate the matrix 270 degrees
        final_pixels = np.rot90(np.rot90(np.rot90(final_pixels)))
        # We flip the rows
        final_pixels = [row[::-1] for row in final_pixels]
        # We store the final image
        this.save_pixelyzed_image(final_pixels, output_route)


    ################################################################################
    # arguments: input_route: route of the image to pixelize
    #            output_route_dir: route of the dir where we will store the pixelyzed images
    # returns:   None 
    ################################################################################
    def pyxelize_several(this, input_route, output_route_dir):
        # We create an instance of the PrimeFunctionalities
        pf = PrimeFunctionalities()

        # If the output dir doesnt exist, we create it
        if(not os.path.exists(output_route_dir)):
            os.makedirs(output_route_dir)
        
        # We calculate the max possible pyxel length
        # load the image
        image = Image.open(input_route)
        # We calculate the max pixel length
        pixel_len = pf.MCD(list(image.size))
        # We calculate the possible pixel lengths
        pixel_lens_list = sorted(pf.divisors(pixel_len))

        # To pixelize with several pixel lengths
        image_index = 1
        for length in pixel_lens_list:
            this.pyxelize(input_route, 
                          os.path.join(output_route_dir, 
                                       str(image_index) + '_' + input_route[input_route.rfind('/') + 1 : input_route.rfind('.')] + '_' + str(length) + 'px.png'),
                          length)
            image_index += 1

        return


    ################################################################################
    # arguments: images_dir: directory of the images to make a gif of
    #            output_gif_dir: route of the dir where we will store the gif
    # returns:   None 
    ################################################################################
    def generate_gif(this, images_dir, output_gif_dir):
        # If the output dir doesnt exist, we create it
        if(not os.path.exists(output_gif_dir)):
            os.makedirs(output_gif_dir)

        img, *imgs = [Image.open(os.path.join(images_dir, f)) for f in sorted(os.listdir(images_dir), key=natural_keys)]
        img.save(fp=str(os.path.join(output_gif_dir, images_dir[images_dir.rfind('/') + 1 : ]) + '.gif'), format='GIF', append_images=imgs,
                 save_all=True, duration=100, loop=0)

        return


    ################################################################################
    # arguments: input_image_route: directory of the images to pixelate and make a gif of
    # returns:   None 
    ################################################################################
    def generate_pixels_and_gif(this, input_image_route):
        # We calculate the output dir 
        # '../images/input/parrots/parrots.jpeg' '../images/output/parrots'
        pixelated_images_route = os.path.join('../images/output/',
                                    input_image_route[input_image_route.rfind('/') + 1 : input_image_route.rfind('.')])
        # We pixelate the image
        this.pyxelize_several(input_image_route, pixelated_images_route)

        # We calculate the gif dir
        output_gif_route = os.path.join('../images/gifs/',
                                    input_image_route[input_image_route.rfind('/') + 1 : input_image_route.rfind('.')])
        # We generate the gif with the pixelated images
        this.generate_gif(pixelated_images_route, output_gif_route)

        return



if(__name__ == '__main__'):
    # We create an instance of the Pyxelator
    px = Pyxelator()
    # We pixelate the image and create the gif
    px.generate_pixels_and_gif('../images/input/parrots/parrots.jpeg')