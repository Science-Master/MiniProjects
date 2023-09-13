import pygame
import tkinter as tkr
from tkinter.filedialog import askdirectory # this allows to select directory
import os # allows inereaction with the os
from tkinter import Toplevel, Button, Tk, Menu



music_player = tkr.Tk()
music_player.title("SERIPLAY")
music_player.geometry("450x350")
music_player.iconbitmap(r'D:\SERINYE RECOVERED\STUFF\img rses\ICONS\My-Music.ico')

directory = askdirectory()
os.chdir(directory)  # allows for change of directory
song_list = os.listdir()

play_list = tkr.Listbox(music_player, font = "Helvetica 12 bold", bg = "yellow", selectmode = tkr.SINGLE)
for item in song_list:
    pos = 0
    play_list.insert(pos, item)
    pos += 1


pygame.init()
pygame.mixer.init()

# Functions to control buttons

def play():
    pygame.mixer.music.load(play_list.get(tkr.ACTIVE))
    var.set(play_list.get(tkr.ACTIVE))
    pygame.mixer.music.play()

def next():
    pygame.mixer.music.next()

def pause():
    pygame.mixer.music.pause()

def replay():
    pygame.mixer.music.rewind()


#interactive buttons for controls

Button1 = tkr.Button(music_player, width = 5, height = 3, font = "Helvetica 12 bold", text = "PLAY", command = play, bg = "#303a52", fg = "blue", bd ="1px")
Button2 = tkr.Button(music_player, width = 5, height = 3, font = "Helvetica 12 bold", text = "NEXT", command = next, bg = "#303a52", fg = "red", bd ="1px")
Button3 = tkr.Button(music_player, width = 5, height = 3, font = "Helvetica 12 bold", text = "PAUSE", command = pause, bg = "#303a52", fg = "purple", bd ="1px")
Button4 = tkr.Button(music_player, width = 5, height = 3, font = "Helvetica 12 bold", text = "REPLAY", command = replay, bg = "#303a52", fg = "orange", bd ="1px")


# Displaying the running song at the top of the app

var = tkr.StringVar()
song_title = tkr.Label(music_player, font = "Helvetica 12 bold", textvariable = var)

# Arranging the buttons in a horizontal format

song_title.pack()
Button1.pack(fill = "x")
Button2.pack(fill = "x")
Button3.pack(fill = "x")
Button4.pack(fill = "x")
play_list.pack(fill = "both", expand = "yes")


# Menu bar
menubar = Menu(music_player)
file = Menu(menubar, tearoff=0)
file.add_command(label="New")
file.add_command(label="Open")
file.add_command(label="Create playlist")
file.add_command(label="Share")

file.add_separator()
file.add_command(label="Exit", command=music_player.quit)

menubar.add_cascade(label="FILE", menu=file)
edit = Menu(menubar, tearoff=0)
edit.add_command(label="Undo")
edit.add_separator()

music_player.config(menu=menubar)



music_player.mainloop()