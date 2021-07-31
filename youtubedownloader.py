#Creating an Youtube installer
#First start off by importing the required libraries

from pytube import YouTube

Video_url = input("Please enter the Youtube video URL: ")
video = YouTube(Video_url)
print(video.streams)
stream = video.streams.get_highest_resolution()
stream.download()

