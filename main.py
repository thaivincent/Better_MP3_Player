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
root.geometry("1150x650+290+85")
root.configure(background='#212121')
mixer.init()

global current_playing_song
current_playing_song = -1

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
    songnum = 0
    for i in song_list:
        if i[-4:] == ".mp3":
            songnum += 1
            song_listbox.insert(index,i)
            index += 1
    songcount.set(songnum)
    song_listbox.place(x = 450, y = 50)   


def PlayMusic():
    global current_playing_song
    current_curse_selection = song_listbox.curselection()[0] 
    if current_playing_song == -1 or current_playing_song != current_curse_selection:
        song_file = song_listbox.get(song_listbox.curselection())
        play_file = os.path.join(folder_path,song_file)
        mixer.music.load(play_file)
        mixer.music.play()
        play_pause_button.config(image=spotify_pause_image) # Updating the Play/Pause button
        current_playing_song = song_listbox.curselection()[0] # Updating current song selection  
    else:
        mixer.music.pause()
        current_playing_song = -1
        play_pause_button.config(image=spotify_play_image)
        
 
    
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
button_resume = PhotoImage(file="Images/resume_button.png")


button_pause = PhotoImage(file="Images/pause_button.png")

#Placing the File Button
file_image = Image.open(r"Images/file_logo.png")
file_image = file_image.resize((200,200))
button_file = ImageTk.PhotoImage(file_image)    
Button(root, image=button_file, bg="#0f1a2b",bd=0, command = SelectFolder).place(x=50, y=350)

# Place the play music button
play_image = Image.open(r"C:\Users\vince\VS Code\Better_MP3_Player\Images\resume_button.png")
play_image = play_image.resize((100,100))
spotify_play_image = ImageTk.PhotoImage(play_image)

pause_image = Image.open(r"C:\Users\vince\VS Code\Better_MP3_Player\Images\pause_button.png")
pause_image = pause_image.resize((100,100))
spotify_pause_image = ImageTk.PhotoImage(pause_image)

global play_pause_button
play_pause_button = Button(root, image = spotify_play_image, command = PlayMusic)
play_pause_button.place(x=700, y = 450)

# Placing the song count
global songcount
songcount = StringVar(value="0")
Label(root, text="Song Count: ").place(x=540, y=10)
Label(root, textvariable=songcount).place(x=620, y=10)



root.resizable(0,0)
# Runs the application
root.mainloop()

