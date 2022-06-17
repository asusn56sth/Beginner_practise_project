from pytube import YouTube
from pytube import Search
import requests
from bs4 import BeautifulSoup

url = 'https://www.youtube.com/watch?v=GaYgqF8TzB4'
video = YouTube(url)

if video.check_availability() != None:
    print("Video not available")
else:
    # get the title of the youtube video
    title = video.title
    print("Title of the video : ", title)

    # get the thumbnail url of the youtube video
    thumbnail = video.thumbnail_url
    print("Thumbnails : ", thumbnail)


choice = input(
    "Do you want audio or video?\nPress 'V' for video or 'A' for audio : ")

if choice == 'V' or choice == 'v':
    # get the list of all the streams available of the given youtube video
    # progressive streams have the video and audio in a single file, but typicallly do not provide the highest quality media
    # adaptive streams split the video and audio tracks but can provide much higher quality
    stream = video.streams.filter(
        only_video=True, file_extension='mp4')
    print("Total Streams available : ")
    for i, strm in enumerate(stream):
        print(f"Stream {i} : ", strm)

    print('')
    # to download the youtube stream
    choice = input("Do you want to download? Y/N : ")
    if choice == 'y' or choice == 'Y':
        stream.first().download().on_progress()

elif choice == 'A' or choice == 'a':
    # get the list of all the streams available of the given youtube video
    stream = video.streams.filter(only_audio=True, file_extension='mp4')
    print("Total Streams available : ")
    for i, strm in enumerate(stream):
        print(f"Stream {i} : ", strm)

    # to download the youtube stream
    choice = input("Do you want to download? Y/N : ")
    if choice == 'y' or choice == 'Y':
        stream.get_audio_only().download().on_progress()


choice = input("Do you want to download caption also? Y/N : ")
if choice == 'y' or choice == 'Y':
    caption = video.caption
    print(caption)
