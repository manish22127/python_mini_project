
from pytube import YouTube
vedio = None
link = input("enter the url")
vedio = YouTube(link)
stream = vedio.streams.get_highest_resolution()
stream.download()
