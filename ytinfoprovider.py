from pytube import YouTube
link=input("what is the link for your video:")#taking the video link as input
yt=YouTube(link)
print("title:",yt.title)#prints title of the video
print("posted by:",yt.author)#which channel posted this video
print("views",yt.views)#number of views in the video
print("description is:",yt.description)#shows description f the video
print("video length is",yt.length,"seconds")#length of the video in seconds
print("age restricted or not",yt.age_restricted)#prints true when video is age restricted and false when not

# downloadingthe video
print("Do you want to download this video(y/n):")
a=input()#whether to download this video or not
if a=="y":
    print("what should be the resolution of the video(h/l)")#h for highest and l for lowest
    b=input()
    if b=="h":
        ys=yt.streams.get_highest_resolution()
        ys.download()# downloads the video in the current open file
    elif b=="l":
        ys=yt.streams.get_lowest_resolution()
        ys.download()# downloads the video in the current open file
    else:
        print("error!")
elif a== "n":
    print("it's okay")
else:
    print("error!!")
print("task complete")
