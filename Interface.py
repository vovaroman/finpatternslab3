from tkinter import  *
from tkinter import filedialog
from tkinter import Label, Canvas
import tkinter as tk
from PIL import ImageTk, Image
import sys
import os
from ImageHelper.ImageFilter import ImageUserFilters, PILFilters, CV2Filters, Filters
from ImageHelper.ImageHelper import ImageHelper, Primitives
from Observer import Observer


class Interface:
    def __init__(self):
        self.interface = None
        self.window = None
        self.img = None
        self.observer = None
        pass
    def getInstance(self):
        if self.interface != None:
            return self.interface
        else:
            self.interface = Interface()
            return self.interface
    def OpenFile(self):
        self.img = tk.filedialog.askopenfilename()
        self.window.destroy()
        self.CreateInterface()
    def SaveFile(self):
        if self.observer != None:
            print('save')
            self.observer.ImageSave('final')
    def ApplyFilter(self, filter):
        print(self.observer)
        if self.observer != None:
            print('apply')
            self.observer.ApplyFilter(filter)
            self.observer.ImageSave('filterversion')
            self.img = os.getcwd() + '/filterversion.jpg'
            print(self.img)
            self.window.destroy()
            self.CreateInterface()
    def CreateInterface(self):
        self.window = Tk()
        self.window.geometry('500x600')
        self.window.title("Photoeditor")
        menu = Menu(self.window)
        menuitems = Menu(menu)
        menuitems.add_command(label='Open', command=self.OpenFile)
        menuitems.add_command(label='Save', command=self.SaveFile)
        filterMenu = Menu(menu)
        filterMenu.add_command(label='AddSharpness', command=lambda: self.ApplyFilter(Filters.AddSharpness))
        filterMenu.add_command(label='AddBlur', command=lambda: self.ApplyFilter(Filters.AddBlur))
        filterMenu.add_command(label='AddSMOOTH', command=lambda: self.ApplyFilter(Filters.AddSMOOTH))
        filterMenu.add_command(label='DetailFilter', command=lambda: self.ApplyFilter(Filters.DetailFilter))
        filterMenu.add_command(label='CountourFilter', command=lambda: self.ApplyFilter(Filters.CountourFilter))
        filterMenu.add_command(label='GaussianBlur2Filter', command=lambda: self.ApplyFilter(Filters.GaussianBlur2Filter))
        filterMenu.add_command(label='GaussianBlur5Filter', command=lambda: self.ApplyFilter(Filters.GaussianBlur5Filter))
        filterMenu.add_command(label='GaussianBlur10Filter', command=lambda: self.ApplyFilter(Filters.GaussianBlur10Filter))
        filterMenu.add_command(label='DiscolorImage', command=lambda: self.ApplyFilter(Filters.DiscolorImage))
        filterMenu.add_command(label='AutumnFilter', command=lambda: self.ApplyFilter(Filters.AutumnFilter))
        filterMenu.add_command(label='OceanFilter', command=lambda: self.ApplyFilter(Filters.OceanFilter))
        filterMenu.add_command(label='JetFilter', command=lambda: self.ApplyFilter(Filters.JetFilter))
        filterMenu.add_command(label='LuvFilter', command=lambda: self.ApplyFilter(Filters.LuvFilter))
        filterMenu.add_command(label='FullRGBHLSFilter', command=lambda: self.ApplyFilter(Filters.FullRGBHLSFilter))
        filterMenu.add_command(label='BGR2XYZFilter', command=lambda: self.ApplyFilter(Filters.BGR2XYZFilter))
        filterMenu.add_command(label='Resize200', command=lambda: self.ApplyFilter(Filters.Resize200))
        filterMenu.add_command(label='Resize50', command=lambda: self.ApplyFilter(Filters.Resize50))
        if self.img != None:
            print('here')
            img = ImageTk.PhotoImage(Image.open(self.img))
            panel = tk.Label(self.window, image = img)
            panel.pack(side = "bottom", fill = "both", expand = "yes")
            image = ImageHelper(self.img,"color")
            self.observer = Observer(image)

        menu.add_cascade(label='File', menu=menuitems)
        menu.add_cascade(label='Filters', menu=filterMenu)
        self.window.config(menu=menu)
        self.window.mainloop()
