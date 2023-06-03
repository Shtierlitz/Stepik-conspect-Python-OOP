from moviepy.editor import *
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.fx.resize import resize
import pygame as ga


def duration(clip):
    """Показывает длительность видео в формате hh:mm:ss"""
    s = clip.duration
    hours = s // 60 // 60
    minutes = s // 60 % 60
    secs = s % 60 % 60
    print(f'{int(hours):02} : {int(minutes):02} : {secs}')



clip_1 = VideoFileClip("E:\Payne audio.mp4")

clip_1.memoize_frame

final_clip = clip_1.subclip(3, 9)
w, h = final_clip.size
print(w, h)

final_clip.write_videofile("E:/test_1.mp4")


# clip_1.size = [640, 480]

# print(w,h)
# clip_1.show(10.5, interactive=True)
# clip_1.fx( resize, width=1270)

# clip_1.preview(fps=25)



# duration(clip_1)
