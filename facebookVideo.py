import os
# from __future__ import unicode_literals
import youtube_dl

print("Enter download location/path : ")
path = str(input())
os.chdir(path)


options ={

}
print("Facebook url: ")
url = str(input())
with youtube_dl.YoutubeDL(options) as u:
    info = u.extract_info(url, download=True)
    audio_title = info.get('title', None)
    print(audio_title)
    print("Downloading....." + url)
    u.download([url])
