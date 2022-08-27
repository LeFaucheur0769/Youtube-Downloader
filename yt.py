from pytube import YouTube

# https://www.youtube.com/watch?v=Usw0IlGbkC4
url = input("\nPlease insert the url : ")
video = YouTube(url)
print("\nTitle : " + video.title)

mp34 = input("\nWould you download the video or the audio : ")
path = input(
    "\nPlease insert the path where you would your download goes (Enter = default) : "
)
try:
    if mp34 == "video":
        print("\n\nGetting the video file")
        stream = video.streams.get_highest_resolution()
        print("\n\nDownload...")
        stream.download(path)
        print("\ndone")
    if mp34 == "audio":
        print("\n\nGetting the audio file")
        stream = video.streams.get_audio_only()
        print("\n\nDownload...")
        stream.download(path)
        print("\ndone")

    else:
        print("\nError")
except:
    print("\nError")
