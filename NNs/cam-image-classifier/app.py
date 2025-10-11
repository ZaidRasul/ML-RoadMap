import tkinter as tk
from tkinter import simpledialog
import PIL.Image, PIL.ImageTk
import os
import cv2 as cv
import camera

class App:
    def __init__(self, window=tk.Tk(), window_title="Cam-Image_Classifier"):
        self.window = window
        self.window_title = window_title

        self.counters = [1, 1]
        #self.model = something
        self.auto_predict = False

        self.camera = camera.Camera()
        #self.init_gui()
        self.delay = 15
        #self.update()
        self.window.attributes('-topmost', True)
        self.window.mainloop()

    
        