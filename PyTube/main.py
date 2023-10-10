from pytube import YouTube


link = input("Insert the link of youtube to download the video: ")
yt = YouTube(link)

#this code download the video
yd = yt.streams.get_highest_resolution()
yd.download()


print("Title: ", yt.title)
print("View: ", yt.views)
