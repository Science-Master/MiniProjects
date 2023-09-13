# from tkinter import *
# from pytube import YouTube
#
# # Creat a display window for the app using tkinter
# root = Tk()
# root.geometry('500x350')
# root.resizable(0, 0)
# root.title("SERITECH'S YOUTUBE VIDEO DOWNLOADER")
#
# Label(root, text="Youtube video downloader", font="arial 20 bold").pack()
#
# # Link accepter
# link = StringVar()
#
# Label(root, text="Paste link to video here: ", font="arial 15 italic").place(x=130, y=60)
# link_enter = Entry(root, width=70, textvariable=link).place(x=32, y=90)
#
#
# # Function to download the video
# def downloader():
#     url = YouTube(str(link.get()))
#     video = url.streams.get_highest_resolution()
#     video.download('C:\\Users\\pc\\Downloads')
#
#     # Display details of the video
#     Label(root, text="Title: " + str(YouTube(str(link.get())).title), font="arial 8 italic").place(x=40, y=60)
#     Label(root, text="Views: " + str(YouTube(str(link.get())).views), font="arial 8 italic").place(x=40, y=60)
#     #Label(root, text="Streams: " + str(YouTube(str(link.get_highest_resolution())).streams), font="arial 8 italic").place(x=40, y=60)
#
#     Label(root, text="VIDEO DOWNLOADED!", font="arial 25").place(x=150, y=150)
#     print("video downloaded!")
#
#
# Button(root, text="DOWNLOAD", font="arial 15 bold", bg="black", fg="white", padx=2, command=downloader).place(x=180,
#                                                                                                               y=200)
#
# root.mainloop()
#
# '''
# # importing the module
# from pytube import YouTube
#
# # where to save
# SAVE_PATH = "E:/" #to_do
#
# # link of the video to be downloaded
# link="https://www.youtube.com/watch?v=xWOoBJUqlbI"
#
# try:
# 	# object creation using YouTube
# 	# which was imported in the beginning
# 	yt = YouTube(link)
# except:
# 	print("Connection Error") #to handle exception
#
# # filters out all the files with "mp4" extension
# mp4files = yt.filter('mp4')
#
# #to set the name of the file
# yt.set_filename('GeeksforGeeks Video')
#
# # get the video with the extension and
# # resolution passed in the get() function
# d_video = yt.get(mp4files[-1].extension,mp4files[-1].resolution)
# try:
# 	# downloading the video
# 	d_video.download(SAVE_PATH)
# except:
# 	print("Some Error!")
# print('Task Completed!')
# '''


# importing the module
from pytube import YouTube

# where to save
SAVE_PATH = "C:\\Users\\pc\\Downloads//" #to_do

# link of the video to be downloaded
link="https://youtu.be/R2TGEVL_1LI"

try:
	# object creation using YouTube
	# which was imported in the beginning
	yt = YouTube(link)
except:
	print("Connection Error") #to handle exception

# filters out all the files with "mp4" extension
mp4files = yt.filter('mp4')

#to set the name of the file
yt.set_filename("Event handling VB")

# get the video with the extension and
# resolution passed in the get() function
d_video = yt.get(mp4files[-1].extension,mp4files[-1].resolution)
try:
	# downloading the video
	d_video.download(SAVE_PATH)
except:
	print("Some Error!")
print('Task Completed!')
