import os
import tkinter as tk
from tkinter import messagebox
import PIL.Image, PIL.ImageTk
from tkinter import ttk
import cv2

dirname = os.path.dirname(__file__)
class View(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent


        #------------------resizing the window to match screensize--------------#  
        width = self.parent.winfo_screenwidth()               

        height = self.parent.winfo_screenheight()               

        self.parent.geometry("%dx%d" % (width, height))

        #------------------Menu bar--------------#
        menubar = tk.Menu(self.parent, background='#ff8000', foreground='black', activebackground='white', activeforeground='black')  
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
        videoLabelFrame.pack(padx=3)
        message = tk.Label(videoLabelFrame, text="Hello, World!")
        message.pack()
        self.canvas = tk.Canvas(videoLabelFrame)
        self.canvas.pack()
        self.delay = 15   # ms
        self.open_file()
        self.play_video()
    
    def setController(self, controller):
        self.controller = controller

    def open_file(self):
        self.pause = False
        self.filename = os.path.join(dirname, '../../ressources/bmo-video-1-1.mp4')
        print(self.filename)
        self.cap = cv2.VideoCapture(self.filename)
        self.width = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        self.canvas.config(width = self.width, height = self.height)


    # get only one frame    
    def get_frame(self):   
        try:
            if self.cap.isOpened():
                ret, frame = self.cap.read()
                return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        except:
            messagebox.showerror(title='Alert', message='End of the video.')


    def play_video(self):
        # Get a frame from the video source, and go to the next frame automatically
        ret, frame = self.get_frame()
        if ret:
            self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
            self.canvas.create_image(0, 0, image = self.photo, anchor = ['nw'])
        if not self.pause:
            self.parent.after(self.delay, self.play_video)


    # Release the video source when the object is destroyed
    def __del__(self):
        if self.cap.isOpened():
            self.cap.release()