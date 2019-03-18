from PIL import Image, ImageFilter
from ImageHelper.ImageFilter import ImageUserFilters, PILFilters, CV2Filters
from numpy import ndarray
import numpy as np
import os
import cv2

class Primitives:
    def __init__(self):
        self.PIL = PILBase()
        self.CV2 = CV2Base()

class PILBase:
    def __init__(self):
        return
class CV2Base:
    def __init__(self):
        return

class Observer:
    def __init__(self, objectToObserve):
        self.parrentObject = objectToObserve
        self.object = objectToObserve.image
        self.state = objectToObserve.mode
        self.Primitives = Primitives()

    def ReOpenInBaseMode(self):
        if type(self.state) is type(self.Primitives.CV2):
            self.ImageSave('intermidiate')
            self.object = Image.open('intermidiate.jpg').convert('RGB')
            self.state = self.Primitives.PIL
            os.remove('intermidiate.jpg')
        else:
            print(self.state)
            print('it is already in Base Mode')
    def ReOpenInColorMode(self):
        if type(self.state) is type(self.Primitives.PIL):
            self.ImageSave('intermidiate')
            self.object = np.copy( cv2.imread('intermidiate.jpg'))
            self.state = self.Primitives.CV2
            os.remove('intermidiate.jpg')
        else:
            print(self.state)
            print('it is already in Color Mode')
    def ImageSave(self, name):
        if type(self.state) is type(self.Primitives.PIL):
            self.object.save(name + '.jpg', 'JPEG')
            return
        elif type(self.state) is type(self.Primitives.CV2):
            cv2.imwrite(name + '.jpg',self.object)
            return
    def ApplyFilterSettings(self, filterType):
        if filterType._value_ == 1:
            print('1')
            self.ReOpenInColorMode()
        elif filterType._value_ == 0:
            print('2')

            self.ReOpenInBaseMode()
        
    def ApplyFilter(self, callMethod):
        self.ApplyFilterSettings(callMethod)
        try:
            filters = ImageUserFilters()
            filters.setupImage(self.object)
            getattr(filters, callMethod._name_)()
            self.object = filters.image
            self.parrentObject.image = filters.image
            self.parrentObject.mode = self.state

        except Exception as ex:
            print(str(ex))
            print('this method is not implemented')
