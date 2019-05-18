#coding=utf8
from PIL import Image, ImageFilter
import cv2
import os
from enum import Enum
import numpy as np


class Filters(Enum):
    AddSharpness = 0
    AddBlur = 1
    AddSMOOTH = 2
    DiscolorImage = 3
    AutumnFilter = 4
    OceanFilter = 5
    LuvFilter = 6
    JetFilter = 7
    FullRGBHLSFilter = 8
    BGR2XYZFilter = 9
    DetailFilter = 10
    CountourFilter = 11
    GaussianBlur2Filter = 12
    GaussianBlur5Filter = 13
    GaussianBlur10Filter = 14
    Resize200 = 15
    Resize50 = 16

class PILFilters():
    def AddSharpness(self):
        self.image = self.image.filter( ImageFilter.SHARPEN )
    def AddBlur(self):
        self.image = self.image.filter( ImageFilter.BLUR )
    def AddSMOOTH(self):
        self.image = self.image.filter( ImageFilter.SMOOTH )
    def DetailFilter(self):
        self.image = self.image.filter(ImageFilter.DETAIL)
    def CountourFilter(self):
        self.image = self.image.filter(ImageFilter.CONTOUR)
    def GaussianBlur2Filter(self):
        self.image = self.image.filter(ImageFilter.GaussianBlur(radius=2))
    def GaussianBlur5Filter(self):
        self.image = self.image.filter(ImageFilter.GaussianBlur(radius=5))
    def GaussianBlur10Filter(self):
        self.image = self.image.filter(ImageFilter.GaussianBlur(radius=10))
class CV2Filters():

    def DiscolorImage(self):
        data = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        self.image = data
    def AutumnFilter(self):
        data = cv2.cvtColor(self.image, cv2.COLORMAP_AUTUMN)
        self.image = data
    def OceanFilter(self):
        data = cv2.cvtColor(self.image, cv2.COLORMAP_OCEAN)
        self.image = data
    def JetFilter(self):
        data = cv2.cvtColor(self.image, cv2.COLORMAP_JET)
        self.image = data
    def LuvFilter(self):
        data = cv2.cvtColor(self.image, cv2.COLOR_LBGR2Luv)
        self.image = data
    def FullRGBHLSFilter(self):
        data = cv2.cvtColor(self.image, cv2.COLOR_RGB2HLS_FULL)
        self.image = data
    def BGR2XYZFilter(self):
        data = cv2.cvtColor(self.image, cv2.COLOR_BGR2XYZ)
        self.image = data
    def Resize200(self):
        scale_percent = 200 # percent of original size
        width = int(self.image.shape[1] * scale_percent / 100)
        height = int(self.image.shape[0] * scale_percent / 100)
        dim = (width, height)
        # resize image
        self.image = cv2.resize(self.image, dim, interpolation = cv2.INTER_AREA)
    def Resize50(self):
        scale_percent = 50 # percent of original size
        width = int(self.image.shape[1] * scale_percent / 100)
        height = int(self.image.shape[0] * scale_percent / 100)
        dim = (width, height)
        # resize image
        self.image = cv2.resize(self.image, dim, interpolation = cv2.INTER_AREA)
    

class ImageUserFilters(PILFilters, CV2Filters):
    def __init__(self):
        self.image = None
        pass
    def setupImage(self, img):
        self.image = img
        pass
