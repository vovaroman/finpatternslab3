# coding=utf8

import sys
from ImageHelper.ImageFilter import ImageUserFilters, PILFilters, CV2Filters, Filters
from ImageHelper.ImageHelper import ImageHelper, Primitives
from Observer import Observer


class Application:
    def main(self, args):
        if len(args) <= 1:
            return 0
        img = ImageHelper(args[1], args[2])  #imgFilter.ImageUserFilters(args[1], args[2])
        observer = Observer(img)
        observer.ApplyFilter(Filters.ColorizeImage)
        observer.ApplyFilter(Filters.AddSharpness)
        observer.ApplyFilter(Filters.AddSharpness)

        img.OpenImage()
        observer.ImageSave('result')
        return

Application().main(sys.argv)
