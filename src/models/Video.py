from fileinput import filename
import os
import cv2
from tkinter import messagebox

dirname = os.path.dirname(__file__)

class Video:

    def __init__(self):
        pass

    def open_file(self, videoFile):
        self.pause = False
        self.filename = os.path.join(dirname, videoFile)
        print(self.filename)
        self.cap = cv2.VideoCapture(self.filename)
        self.width = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        
    
    # get only one frame    
    def get_frame(self):   
        try:
            if self.cap.isOpened():
                ret, frame = self.cap.read()
                return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        except:
            messagebox.showerror(title='Alert', message='End of the video.')