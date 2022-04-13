import settings as s
import filters as f
import imageIO as io
import contrast as c
import stats as st
import binary as b


import matplotlib.pyplot as plt
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
import tkinter as tk
from PIL import Image
from PIL import ImageTk
from PIL import ImageEnhance
from tkinter import filedialog
matplotlib.use('TkAgg')
__author__ = 'Melek'


class Interface:
    def __init__(self, window):
        self.window = window
        self.currentimage=[]
        self.menu_initialisation()

    def menu_initialisation(self):
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        self.window.title('Photo Editing App with Python (Tkinter and OpenCV)')

        self.window.geometry(f'{screen_width}x{screen_height}')

        Frametools = tk.Frame(self.window, height=20, width=200)
        Frametools.grid(row=0, column=0)
        Frametools.pack(anchor=tk.W)

        Frame1 = tk.Frame(Frametools, height=20, width=200)
        Frame1.pack(anchor=tk.N)

        Frame2 = tk.Frame(Frametools, height=20)
        Frame2.pack(anchor=tk.W)

        Frame3 = tk.Frame(Frametools, height=20)
        Frame3.pack(anchor=tk.E)
        self.label = tk.Label(Frame3, text="average here")
        self.label.pack(pady=10, padx=10)

        imageframe = tk.Frame(self.window, width=screen_width*0.7)
        self.canvas = tk.Canvas(imageframe, bg="gray", width=1280, height=720)
        imageframe.pack(anchor=tk.E,fill=tk.Y)
        self.canvas.grid(row=0, column=1)
        self.canvas.pack(expand=tk.YES, fill=tk.BOTH,anchor=tk.CENTER,pady=10, padx=10)
        importButton = tk.Button(Frame1, text="Import", padx=10, pady=5, command=self.importButton_callback)
        importButton.grid(row=0, column=0)

        saveButton = tk.Button(Frame1, text="Save", padx=10, pady=5, command=self.saveButton_callback)
        saveButton.grid(row=0, column=1)

        closeButton = tk.Button(Frame1, text="Close", padx=10, pady=5, command=self.closeButton_callback)
        closeButton.grid(row=0, column=2)

        averageButton = tk.Button(Frame1, text="Average", padx=10, pady=5, command=self.average_callback)
        averageButton.grid(row=0, column=3)

        brightnessSlider = tk.Scale(Frame2, label="Brightness", from_=0, to=2, orient=tk.HORIZONTAL,
                                    length=screen_width,
                                    resolution=0.1, command=self.brightness_callback)
        brightnessSlider.set(1)
        brightnessSlider.pack(anchor=tk.N)

    def yellowButton_callback(self):
        pass

    def blueButton_callback(self):
        pass

    def pinkButton_callback(self):
        pass

    def orangeButton_callback(self):
        pass

    def noneButton_callback(self):
        pass

    def displayImage(self,pixels):
        self.currentimage=pixels.copy()
        arrayimg = np.array(pixels, dtype=np.uint8)
        displayImage = Image.fromarray(arrayimg)
        ImagetoDisplay = ImageTk.PhotoImage(displayImage)
        self.window.ImagetoDisplay=ImagetoDisplay
        self.canvas.config(width=s.width, height=s.height)
        self.canvas.create_image(
            s.width/2, s.height,anchor=tk.S, image=ImagetoDisplay)
        self.canvas.anchor=tk.CENTER
        #self.canvas.pack(expand=tk.YES, fill=tk.BOTH,anchor=tk.CENTER)

    def importButton_callback(self):
        io.read("input\\mona.pgm")
        self.displayImage(s.image_orig)

    def saveButton_callback(self):
        io.read("input\\melek.pgm")
        self.displayImage(s.image_orig)
        #savefile = filedialog.asksaveasfile(defaultextension=".jpg")
        #outputImage.save(savefile)

    def average_callback(self):
        self.label.config(text=(st.average(self.currentimage)))

    def closeButton_callback(self):
        self.window.destroy()

    def brightness_callback(self,brightness_pos):
        pass





def showimage(image,title):
    plt.imshow(image, cmap='gray')
    plt.title(title)
    plt.show()