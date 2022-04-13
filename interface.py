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
from tkinter import ttk
from PIL import Image
from PIL import ImageTk
from tkinter import filedialog
matplotlib.use('TkAgg')
__author__ = 'Melek'

def alert():
    pass

class Interface:
    def __init__(self, window):
        self.window = window
        self.window.iconphoto(False, tk.PhotoImage(file='icons/imgicn.png'))
        self.window.title('Image Processing Tool')
        self.menu_initialisation()
        self.window.geometry(f'{self.window.winfo_screenwidth() - 100}x{self.window.winfo_screenheight() - 100}+10+10')
        self.currentimage=[]


    def menu_initialisation(self):
        menubar = tk.Menu(self.window)

        menuContrast = tk.Menu(menubar, tearoff=0)
        menuContrast.add_command(label="Equalisation", command=alert)
        menuContrast.add_command(label="Local Equalisation", command=alert)
        menuContrast.add_separator()
        menuContrast.add_command(label="Dark Dilatation", command=alert)
        menuContrast.add_command(label="Light Dilatation", command=alert)
        menuContrast.add_command(label="Middle Dilatation", command=alert)
        menuContrast.add_command(label="Inverse", command=alert)
        menubar.add_cascade(label="Contrast", menu=menuContrast)

        menuFilter = tk.Menu(menubar, tearoff=0)
        menuFilter.add_command(label="Median", command=alert)
        menuFilter.add_command(label="Average", command=alert)
        menuFilter.add_command(label="Gaussian", command=alert)
        menuFilter.add_separator()
        menuFilter.add_command(label="High_boost", command=alert)
        menuFilter.add_command(label="Laplace", command=alert)
        menuFilter.add_separator()
        menuFilter.add_command(label="Prewitt H", command=alert)
        menuFilter.add_command(label="Prewitt V", command=alert)
        menubar.add_cascade(label="Filters", menu=menuFilter)

        menuBinary = tk.Menu(menubar, tearoff=0)
        menuBinary.add_command(label="Thresholding", command=alert)
        menuBinary.add_separator()
        menuBinary.add_command(label="Dilatation", command=alert)
        menuBinary.add_command(label="Erosion", command=alert)
        menuBinary.add_command(label="Closing", command=alert)
        menuBinary.add_command(label="Opening", command=alert)
        menubar.add_cascade(label="Binary", menu=menuBinary)

        menuOther = tk.Menu(menubar, tearoff=0)
        menuOther.add_command(label="Add noise", command=alert)
        menuOther.add_command(label="Generate Ascii art", command=alert)
        menubar.add_cascade(label="Other", menu=menuOther)

        menubar.add_command(label="Quit", command=self.QuitMenuButton_callback)

        self.window.config(menu=menubar)

        Frametools = tk.Frame(self.window,width=self.window.winfo_screenwidth()*0.2)
        Frametools.pack_propagate(0)
        Frametools.pack(anchor=tk.W, side=tk.LEFT,fill=tk.Y, expand=tk.YES)

        FrameFile = tk.Frame(Frametools, height=100, width=100, pady=5)
        tk.Label(FrameFile, text="Image Path:").grid(row=0, column=0, padx=2)
        self.entry_text = tk.StringVar()
        self.entry_text.set("input/melek.pgm")
        tk.Entry(FrameFile, width=30, textvariable = self.entry_text).grid(row=0, column=1, padx=10)
        FrameFile.pack(anchor=tk.NW)

        Frameopensave = tk.Frame(Frametools, height=100, width=100, pady=5)
        tk.Button(Frameopensave, text="Open", padx=10, pady=5, command=self.importButton_callback).grid(row=0,column=0,padx=10)
        tk.Button(Frameopensave, text="Save", padx=10, pady=5, command=self.saveButton_callback).grid(row=0,column=1,padx=10)
        Frameopensave.pack(anchor=tk.NW)

        ttk.Separator(Frametools,orient='horizontal').pack(fill='x',pady=5)

        Framewidth = tk.Frame(Frametools, height=100, width=100, pady=5)
        tk.Label(Framewidth, text="Width:").grid(row=0, column=0, padx=10)
        self.width_text = tk.Label(Framewidth, text="0", width=15, relief=tk.SUNKEN)
        self.width_text.grid(row=0, column=2)
        Framewidth.pack(anchor=tk.NW)

        Frameheight = tk.Frame(Frametools, height=100, width=100, pady=5)
        tk.Label(Frameheight, text="Length:").grid(row=0, column=0, padx=10)
        self.height_text = tk.Label(Frameheight, text="0", width=15, relief=tk.SUNKEN)
        self.height_text.grid(row=0, column=2)
        Frameheight.pack(anchor=tk.NW)

        Framepixel = tk.Frame(Frametools, height=100, width=100, pady=5)
        tk.Label(Framepixel, text="Number of pixels:").grid(row=0, column=0, padx=10)
        self.pixel_text=tk.Label(Framepixel, text="0", width=15, relief=tk.SUNKEN)
        self.pixel_text.grid(row=0, column=2)
        Framepixel.pack(anchor=tk.NW)

        Frameaverage = tk.Frame(Frametools, height=100, width=100, pady=5)
        tk.Label(Frameaverage, text="Average:").grid(row=0, column=0, padx=10)
        self.average_text=tk.Label(Frameaverage, text="0", width=25, relief=tk.SUNKEN)
        self.average_text.grid(row=0, column=2)
        Frameaverage.pack(anchor=tk.NW)

        Framedeviation = tk.Frame(Frametools, height=100, width=100, pady=5)
        tk.Label(Framedeviation, text="Standard deviation:").grid(row=0, column=0, padx=10)
        self.deviation_text=tk.Label(Framedeviation, text="0", width=25, relief=tk.SUNKEN)
        self.deviation_text.grid(row=0, column=2)
        Framedeviation.pack(anchor=tk.NW)

        Frameentropy = tk.Frame(Frametools, height=100, width=100, pady=5)
        tk.Label(Frameentropy, text="Entropy:").grid(row=0, column=0, padx=10)
        self.entropy_text=tk.Label(Frameentropy, text="0", width=25, relief=tk.SUNKEN)
        self.entropy_text.grid(row=0, column=2)
        Frameentropy.pack(anchor=tk.NW)

        FrameSNR = tk.Frame(Frametools, height=100, width=100, pady=5)
        tk.Label(FrameSNR, text="SNR:").grid(row=0, column=0, padx=10)
        self.SNR_text=tk.Label(FrameSNR, text="0", width=25, relief=tk.SUNKEN)
        self.SNR_text.grid(row=0, column=2)
        FrameSNR.pack(anchor=tk.NW)

        FrameHistogram= tk.Frame(Frametools, height=100, width=100, pady=5)
        tk.Label(FrameHistogram, text="Histogram:").grid(row=0, column=0, padx=10)
        self.histogram= tk.Label(FrameHistogram, text="0", width=10, relief=tk.SUNKEN).grid(row=0, column=2)
        FrameHistogram.pack(anchor=tk.NW)

        FrameConsole = tk.Frame(Frametools, height=100, width=100, pady=5)
        tk.Label(FrameConsole, text="Console:").pack()
        self.console=tk.Text(FrameConsole, height=10, width=55,fg="red")
        self.console.pack()
        FrameConsole.pack(anchor=tk.S,side=tk.BOTTOM)

        imageframe = tk.Frame(self.window,width=self.window.winfo_screenwidth()*0.8)
        imageframe.pack_propagate(0)
        imageframe.pack(side=tk.RIGHT,fill=tk.Y)
        self.canvas = tk.Canvas(imageframe, bg="gray",width=self.window.winfo_screenwidth()*0.7,height=self.window.winfo_screenheight())
        self.canvas.pack(expand=tk.YES,anchor=tk.CENTER,pady=20, padx=20)

    def updateStats(self):
        self.width_text.config(text=str(s.width))
        self.height_text.config(text=str(s.height))
        self.pixel_text.config(text=str(st.nbPixels()))
        self.average_text.config(text=str(st.average(self.currentimage)))
        self.deviation_text.config(text=str(st.deviation(self.currentimage)))
        self.entropy_text.config(text=str(st.entropy(self.currentimage)))
        self.SNR_text.config(text=str(st.SNR(self.currentimage)))
        self.displayImage(self.currentimage)

    def displayImage(self,pixels):
        arrayimg = np.array(pixels, dtype=np.uint8)
        displayimage = Image.fromarray(arrayimg)
        ImagetoDisplay = ImageTk.PhotoImage(displayimage)
        self.window.ImagetoDisplay=ImagetoDisplay
        self.canvas.config(width=s.width, height=s.height)
        self.canvas.create_image(
            s.width/2, s.height/2,anchor=tk.CENTER, image=ImagetoDisplay)

    def importButton_callback(self):
        io.read(self.entry_text.get())
        self.currentimage=s.image_orig.copy()
        self.updateStats()

    def saveButton_callback(self):
        io.write(self.entry_text.get(),self.currentimage)
        self.writeConsole("Image saved successfully.\n")

    def writeConsole(self,text):
        self.console.config(state=tk.NORMAL)
        self.console.insert(tk.END, text)
        self.console.config(state=tk.NORMAL)

    def QuitMenuButton_callback(self):
        self.window.destroy()






def showimage(image,title):
    plt.imshow(image, cmap='gray')
    plt.title(title)
    plt.show()