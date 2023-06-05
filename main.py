import os

from tkinter import *
from tkinter import Tk
from tkinter import filedialog

from pygame import mixer

from PIL import Image, ImageTk

# Initalize window for the music player
root = Tk()
root.title("Music Player")
root.geometry("920x600+290+85")
root.configure(background='#212121')
mixer.init()


label = Label(root, text="Testing")
label.pack(side = BOTTOM)

# Create a function to open a file
def AddMusic():
    path = filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs = os.listdir(path)
        for song in songs:
            if song.endswith(".mp3"):
                Playlist.insert(END, song)

def PlayMusic():
    Music_Name = Playlist.get(ACTIVE)
    print(Music_Name[0:-4])
    mixer.music.load(Playlist.get(ACTIVE))
    mixer.music.play()

# Sets the Icon photo
spotify_iconlogo = PhotoImage(file="Images/spotify_logo.png")
root.iconphoto(False, spotify_iconlogo)


# Loads the image
wide_logo = Image.open(r"Images/spotify_logo_wide.png")

# Resizes, and sets the banner photo
wide_logo = wide_logo.resize((400,225))
spotify_widelogo = ImageTk.PhotoImage(wide_logo)
Label(root, image = spotify_widelogo).pack(anchor = "n", side = "left")

# Initializing the pictures for the buttons
add = Image.open(r"Images/add_button.png")
add = add.resize((200,200))
button_Add = ImageTk.PhotoImage(add)    
Button(root, image=button_Add, bg="#0f1a2b",bd=0, command=PlayMusic).place(x=100, y=500)


button_Resume = PhotoImage(file="Images/resume_button.png")

button_Pause = PhotoImage(file="Images/pause_button.png")



# Runs the application
root.mainloop()

