# Must install Python
# Then pip install pygame
#      pip install tk 
#      pip install Pillow

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

# Create a function to select a music directory
def SelectFolder():
    # Asks the user to select a directory
    global folder_path
    folder_path = filedialog.askdirectory(initialdir=r"C:\Users\vince\VS Code\Better_MP3_Player", title="Dialog Box")

    # Displays the appropriate directory
    Label(root, text = folder_path).place(x=50, y=700)

    #Initialize a listbox
    global song_listbox
    song_listbox = Listbox(root, height= 20, width = 100, selectmode=SINGLE)

    # Loop through the elements in the list to add them to the listbox
    song_list = os.listdir(folder_path)
    index = 0
    for i in song_list:
        song_listbox.insert(index,i)
        index += 1

    song_listbox.place(x = 450, y = 50)   


def PlayMusic():
    for i in song_listbox.curselection():
        song_file = song_listbox.get(i)
        mixer.music.load(folder_path + "/" + song_file)
        



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
file_image = Image.open(r"Images/file_logo.png")
file_image = file_image.resize((200,200))
button_File = ImageTk.PhotoImage(file_image)    
Button(root, image=button_File, bg="#0f1a2b",bd=0, command = SelectFolder).place(x=50, y=500)

button_Resume = PhotoImage(file="Images/resume_button.png")

button_Pause = PhotoImage(file="Images/pause_button.png")


# Place the play music button

play_image = Image.open(r"C:\Users\vince\VS Code\Better_MP3_Player\Images\resume_button.png")
play_image = play_image.resize((100,100))
spotify_play_image = ImageTk.PhotoImage(play_image)
Button(root, image = spotify_play_image, command = PlayMusic).place(x=460, y = 550)


# Runs the application
root.mainloop()

