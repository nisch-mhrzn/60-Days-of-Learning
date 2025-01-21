 #install moviepy
from moviepy.editor import *

video = VideoFileClip("venisha.mp4").subclip(00,7)
video.write_gif("veni.gif")

from moviepy.video.fx.all import blackwhite

# Apply black and white effect
bw_video = blackwhite(video)
bw_video.write_videofile("bw_video.mp4")

rotated_video = video.rotate(90)  # rotate 90 degrees
rotated_video.write_videofile("rotated_video.mp4")

resized_video = video.resize(height=360)  # resize to 360p height
resized_video.write_videofile("resized_video.mp4")
# Apply a fade-in effect
video_with_fadein = video.fadein(2)  # 2 seconds fade-in
video_with_fadein.write_videofile("video_with_fadein.mp4")
#speed up
sped_up_video = video.speedx(factor=1.25)  # speed up by a factor of 2
sped_up_video.write_videofile("sped_up_video.mp4")