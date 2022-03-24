import tkinter as tk
import PIL.Image, PIL.ImageTk


from models.Video import Video
from view.view import View

class Controller:

    def __init__(self, video, view):
        
        self.video = video
        self.view = view
        
        self.width = self.view.parent.winfo_screenwidth()               
        self.height = self.view.parent.winfo_screenheight()               

        self.pause = False
           
        self.video.open_file('../../ressources/videos/bmo-video-1-1.mp4')
        
        self.isVideoLoaded = True
        self.view.canvas.config(width = 1440, height =self.height)
        self.play_video()
        
    def play_video(self):
        # Get a frame from the video source, and go to the next frame automatically
        ret, frame = self.video.get_frame()
        if ret:
            self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
            self.view.canvas.create_image((self.view.canvas.winfo_width()-self.video.width)/2, 0, image = self.photo, anchor = ['nw'])
        if not self.pause:
            self.view.parent.after(self.view.delay, self.play_video)

    def pauseVideo(self):
        self.pause = not self.pause
        if not self.pause:
            self.view.parent.after(self.view.delay, self.play_video)
            
    def __del__(self):
       if self.video.cap.isOpened():
          self.video.cap.release()