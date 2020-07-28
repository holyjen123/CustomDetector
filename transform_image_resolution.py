from PIL import Image
import os 
import argparse
import easydict


def rescale_images(directory, size):
    for img in os.listdir(directory):
        print(img)
        im = Image.open(directory+img)
        im_resized = im.resize(size, Image.ANTIALIAS)
        im_resized.save(directory+img)
        

size = 800, 600
rescale_images("images/", size)
