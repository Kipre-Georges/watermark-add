from fileinput import filename
import os
from pydoc import cli
from turtle import width
from unittest import result 
from moviepy.editor import *
from os import *
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from notifypy import Notify
import moviepy.editor as me





var_path=str(input("Enter the path of the video : "))
watermark=input("Write your Watermark : ")
fontsize_choice=int(input("Enter a font size : "))


l=os.listdir(var_path)
VIDEO_LIST=[]


for i in l:
    if i.endswith('.mp4') or i.endswith(".MP4"):
        VIDEO_LIST.append(i)



for i in VIDEO_LIST:
    filename=i

    clip=VideoFileClip(i)

    

    time_clip=clip.duration

    txt_clip=TextClip(watermark,fontsize=fontsize_choice,color='white')
    txt_clip=txt_clip.set_pos('bottom').set_duration(time_clip)


    result=CompositeVideoClip([clip,txt_clip])

    result.write_videofile(i+"new.mp4")

notification = Notify()
notification.title = "ADD WATERMARK"
notification.message = "The processing of your videos is complete."
notification.send()
