from genericpath import exists
import os
import tkinter as tk
from tkinter import LEFT, messagebox
from turtle import width
import PIL.Image, PIL.ImageTk
from tkinter import ttk
from click import command
from models.Video import Video
from controllers import Controller
import cv2


class View(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.pause = False
        #------------------resizing the window to match screensize--------------#  
        width = self.parent.winfo_screenwidth()               

        height = self.parent.winfo_screenheight()               

        self.parent.geometry("%dx%d" % (width, height))

        #------------------Menu bar--------------#
        menubar = tk.Menu(self.parent, background='white', foreground='black', activebackground='white', activeforeground='black')  
        file = tk.Menu(menubar, tearoff=1, background='white', foreground='black')    
        file.add_command(label="Open")  
        file.add_command(label="Save")  
        file.add_command(label="Save as")    
        file.add_separator()  
        file.add_command(label="Exit", command=self.parent.quit)  
        menubar.add_cascade(label="File", menu=file)  

        edit = tk.Menu(menubar, tearoff=0)  
        edit.add_command(label="Undo")  
        edit.add_separator()     
        edit.add_command(label="Cut")  
        edit.add_command(label="Copy")  
        edit.add_command(label="Paste")  
        menubar.add_cascade(label="Edit", menu=edit)  

        help = tk.Menu(menubar, tearoff=0)    
        menubar.add_cascade(label="Help", menu=help)  
            
        self.parent.config(menu=menubar)

        #-----------------video part----------#
        
        videoLabelFrame = tk.LabelFrame(self.parent, text = "video To track :", bg = "white",relief = tk.SUNKEN, bd=4)
        videoLabelFrame.pack(side = LEFT)
        self.canvas = tk.Canvas(videoLabelFrame)
        self.canvas.pack()
        self.pauseButton = tk.Button(videoLabelFrame,text = "▶", command = lambda:self.controller.pauseVideo())
        self.pauseButton.pack()
        self.delay = 15   # ms
        
    def setController(self, controller):
        self.controller = controller

    # Release the video source when the object is destroyed