"""
    Author: PEMPEME MOHAMED CHAMSOUDINE
    link github : https://github.com/pemochamdev
"""

import yt_dlp

# Enter  the url for the download

url = input('Enter video url')

ydl_opts = {}

with yt_dlp.YoutubeDL(ydl_opts) as ydl :
    
    ydl.download([url])

print('Video download sucessfully')