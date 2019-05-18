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
        with open('./basefilters.txt') as f:
            content = f.readlines()
        baseModeFilters = [x.strip() for x in content]
        with open('./colorfilters.txt') as f:
            content = f.readlines()
        colorFilters = [x.strip() for x in content]
        if filterType._name_ in colorFilters:
            self.ReOpenInColorMode()
        else:
            self.ReOpenInBaseMode()
    def ApplyFilter(self, callMethod):
        self.ApplyFilterSettings(callMethod)
        try:
            print(callMethod._name_)
            filters = ImageUserFilters()
            filters.setupImage(self.object)
            getattr(filters, callMethod._name_)()
            self.object = filters.image
            self.parrentObject.image = filters.image
            self.parrentObject.mode = self.state

        except Exception as ex:
            print(str(ex))
            print('this method is not implemented')
