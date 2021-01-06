from moviepy.editor import *

numberOfVideo = int(input("Please enter number of video: "))
list_of_video = []

for i in range(1, numberOfVideo):
    name = input("Please enter path of video number " + str(i) + ": ")
    clip = VideoFileClip(name)
    list_of_video += clip

final_clip = concatenate_videoclips(list_of_video)
final_clip.write_videofile("new.mp4")
