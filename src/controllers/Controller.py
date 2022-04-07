import tkinter as tk
import PIL.Image, PIL.ImageTk
from tkinter import messagebox
from models.Video import Video
from view.view import View

class Controller:

    def __init__(self, video, view):
        
        self.video = video
        self.view = view
        
        self.width = self.view.parent.winfo_screenwidth()               
        self.height = self.view.parent.winfo_screenheight()         
        self.view.canvas.config(width=self.width, height=self.height-100)
        self.pause = True
        
    def LoadVideo(self):
        self.video.open_file()
        self.play_video()
        
    def play_video(self):
        # Get a frame from the video source, and go to the next frame automatically
        ret, frame = self.video.videoFrames[self.video.currentFrame]
        if ret:
            self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
            self.view.canvas.create_image((self.view.canvas.winfo_width()-self.video.width)/2, 0, image = self.photo, anchor = ['nw'])
        if not self.pause:
            self.video.currentFrame += 1
            self.view.parent.after(self.view.delay, self.play_video)
            
        if self.video.currentFrame == len(self.video.videoFrames):
            messagebox.showerror(title='Alert', message='End of the video.')

    def pauseVideo(self):
        self.pause = not self.pause
        if not self.pause:
            self.view.parent.after(self.view.delay, self.play_video)
            
    def NextFrame(self):
        if self.pause:
            ret, frame = self.video.videoFrames[self.video.currentFrame+1]
            if ret:
                self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
                self.view.canvas.create_image((self.view.canvas.winfo_width()-self.video.width)/2, 0, image = self.photo, anchor = ['nw'])
                self.video.currentFrame += 1
    
    def PreviousFrame(self):
        if self.pause:
            ret, frame = self.video.videoFrames[self.video.currentFrame-1]
            if ret:
                self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
                self.view.canvas.create_image((self.view.canvas.winfo_width()-self.video.width)/2, 0, image = self.photo, anchor = ['nw'])
                self.video.currentFrame -= 1
    
    def FirstFrame(self):
        if self.pause:
            ret, frame = self.video.videoFrames[0]
            if ret:
                self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
                self.view.canvas.create_image((self.view.canvas.winfo_width()-self.video.width)/2, 0, image = self.photo, anchor = ['nw'])
                
    def LastFrame(self):
        if self.pause:
            ret, frame = self.video.videoFrames[len(self.video.videoFrames)-1]
            if ret:
                self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
                self.view.canvas.create_image((self.view.canvas.winfo_width()-self.video.width)/2, 0, image = self.photo, anchor = ['nw'])
                
    def __del__(self):
       if self.video.cap.isOpened():
          self.video.cap.release()