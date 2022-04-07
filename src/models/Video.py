from fileinput import filename
import os
from turtle import title
import cv2
from tkinter import filedialog

dirname = os.path.dirname(__file__)

class Video:

    def __init__(self):
        self.videoFrames = []
        self.currentFrame = 0

    def open_file(self):
        self.pause = False
        self.filename = filedialog.askopenfile(initialdir=os.path.join(dirname, '../../ressources'),mode='rb', title='choose a video to load', filetypes=(("mp4 files","*.mp4"), ("gif files","*.gif")))
        self.cap = cv2.VideoCapture(self.filename.name)
        self.width = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        self.saveFrames()
        
    def saveFrames(self):
        while self.get_frame() != False:
            self.videoFrames.append(self.get_frame())
            
        
    # get only one frame    
    def get_frame(self):   
        try:
            if self.cap.isOpened():
                ret, frame = self.cap.read()
                return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        except:
            return False
            