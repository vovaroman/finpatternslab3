from PIL import Image, ImageFilter
import cv2
import os
from Observer import Primitives

class ImageHelper:

    def __openInBaseMode(self):
        self.image = Image.open(self.pathToFile).convert('RGB')
        self.mode = Primitives().PIL
    def __openInColorMode(self):
        self.image = cv2.imread(self.pathToFile)
        self.mode = Primitives().CV2
    
    def __init__(self, path, mode):
        self.pathToFile = path
        self.image = None
        self.mode = None
        if mode == 'base':
            self.__openInBaseMode()
        elif mode == 'color':
            self.__openInColorMode()

    def OpenImage(self):
        if type(self.mode) is type(Primitives().PIL):
            self.image.show()
        elif type(self.mode) is type(Primitives().CV2):
            cv2.imshow('image',self.image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()



