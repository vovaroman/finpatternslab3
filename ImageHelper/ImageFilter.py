#coding=utf8
from PIL import Image, ImageFilter
import cv2
import os
from enum import Enum


class Filters(Enum):
    AddSharpness = 0
    AddBlur = 0
    AddSMOOTH = 0
    ColorizeImage = 1


class PILFilters():
    def AddSharpness(self):
        self.image = self.image.filter( ImageFilter.SHARPEN )
    def AddBlur(self):
        self.image = self.image.filter( ImageFilter.BLUR )
    def AddSMOOTH(self):
        self.image = self.image.filter( ImageFilter.SMOOTH )

class CV2Filters():
    def ColorizeImage(self):
        data = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        self.image = data

class ImageUserFilters(PILFilters, CV2Filters):
    def __init__(self):
        self.image = None
        pass
    def setupImage(self, img):
        self.image = img
        pass
