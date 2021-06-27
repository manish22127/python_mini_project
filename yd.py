
print("welcome to youtube downloader")

from pytube import YouTube
link = input("enter the url")
vedio = YouTube(link)
stream = vedio.streams.get_highest_resolution()
print("Download initialised")
stream.download()
print("Thankyou for downloading \nProgram wirtten by Manish");
