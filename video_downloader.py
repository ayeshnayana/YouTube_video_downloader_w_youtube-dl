from __future__ import unicode_literals
import youtube_dl
import os

video_url = 'https://www.youtube.com/watch?v=RTADKe7VNUM'

try:
    with youtube_dl.YoutubeDL() as ydl:
        ydl.download([video_url])
except:
    os.system(f"""youtube-dl -o "song.%(ext)s" --extract-audio -x --audio-format mp3 {video_url}""")

 # In pycharm install web-youtube-dl



