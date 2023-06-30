# py demosaic.py --input_dir testdata\mishka_mosaic


import os 
import numpy as np
import cv2
import argparse
from bouning_box import BBox2D
from image_search import image_search

class Snippet2D:
    '''
    for recognized object on bigger source image
    '''

    def __init__(self, snippet_path, original_image_path):
        self.snippet_path = os.path.abspath(snippet_path)
        self.original_image_path = os.path.abspath(original_image_path)
        # self.bbox = 

    # def bbox_from_name(self) -> BBox2D

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_dir')
    opts = parser.parse_args()
    input_dir = os.path.abspath(opts.input_dir)
    print(input_dir)
    images_path = image_search(input_dir, ['.jpg'])
    print(images_path)



