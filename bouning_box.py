import os 
import numpy as np
import cv2

class BBox2D: 
    def __init__(self, 
                 x1: float, 
                 y1: float, 
                 x2: float, 
                 y2: float
        ):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def width(self):
        return abs(self.x2 - self.x1)

    def height(self):
        return abs(self.y2 - self.y1)
    
    def center(self):
        return (
            self.x1 + self.width()/2, 
            self.y1 + self.height()/2
        )
    

        

    