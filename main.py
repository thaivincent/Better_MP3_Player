import os
from tkinter import *
from tkinter import Tk
from tkinter import filedialog
from pygame import mixer

# Create a function to open a file
def AddMusic():
    path = filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs = os.listdir(path)
        for song in songs:
            if song.endswith(".mp3"):
                Playlist.insert(END, song)
# Create a function to play file
def PlayMusic():
    Music_Name = Playlist.get(ACTIVE)
    print(Music_Name[0:-4])
    mixer.music.load(Playlist.get(ACTIVE))
    mixer.music.play()

root = Tk()

label = Label(root, text="hello")
label.pack()
root.mainloop()