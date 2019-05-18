# coding=utf8

import sys
from ImageHelper.ImageFilter import ImageUserFilters, PILFilters, CV2Filters, Filters
from ImageHelper.ImageHelper import ImageHelper, Primitives
from Observer import Observer
from tkinter import *
from Interface import Interface

class Application:
    def main(self, args):
        interface = Interface().getInstance()
        interface.CreateInterface()
        
        '''
        if len(args) <= 1:
            return 0
        if len(args) == 3:
            img = ImageHelper(args[1], args[2])
        else:
            img = ImageHelper(args[1],"color")
        observer = Observer(img)
        window = Tk()
        window.title("Photoeditor")
        window.mainloop()
        observer.ApplyFilter(Filters.AddSharpness)
        img.OpenImage()

        observer.ImageSave('result')
        '''
        return

Application().main(sys.argv)
