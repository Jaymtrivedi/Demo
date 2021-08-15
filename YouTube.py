# Download Youtube Video using python
# @curious_.programmer
# pip install pytube
from pytube import YouTube

link = input("insert link here : ")
url = YouTube(link)
print("Downloading.....")
video = url.streams.first()
video.download()
print("Downloaded !")
