# 开发时间：2023-01-19 19:07
# 开发人员：林坚洪
from moviepy.editor import AudioFileClip
my_audio_clip = AudioFileClip(r'C:\Users\林坚洪\Downloads\华晨宇-假如逃离我.mp4')
my_audio_clip.write_audiofile(r'C:\Users\林坚洪\Downloads\华晨宇-假如逃离我.mp3')
""""""