import os
from tkinter import *
from tkinter import Tk
from tkinter import filedialog
from pygame import mixer

# Initalize window for the music player
root = Tk()
root.title("Music Player")
root.geometry("920x600+290+85")
root.configure(background='#212121')


label = Label(root, text="Testing")
label.pack()

# Sets the iconphoto
spotify_logo = PhotoImage(file="Images\spotify_logo.png")
root.iconphoto(False, spotify_logo)

root.mainloop()

mixer.init()