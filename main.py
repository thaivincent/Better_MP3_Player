# Must install Python
# Then pip install pygame
#      pip install tk 
#      pip install Pillow

import os

from tkinter import *
from tkinter import ttk
from tkinter import filedialog

from pygame import mixer

from PIL import Image, ImageTk

# Initalize window for the music player
root = Tk()
root.title("Music Player")
root.geometry("1150x650+290+85")
root.configure(background='#212121')
root.resizable(0,0)
mixer.init()

# GLOBAL Variables
# Represents the INDEX of the current playing song
current_playing_song = -1
last_playing_song = -1
paused = True


# Create a function to select a music directory
def SelectFolder():
    # Asks the user to select a directory
    global folder_path
    folder_path = filedialog.askdirectory(initialdir=r"C:\Users\vince\VS Code\Better_MP3_Player", title="Dialog Box")

    # Displays the appropriate directory
    Label(root, text = folder_path).place(x=50, y=700)

    song_listbox.delete(0,END)

    # Loop through the elements in the list to add them to the listbox
    # The list box is the element inside the interface which displays the list of songs 
    song_list = os.listdir(folder_path)
    index = 0
    global songnum
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
    global last_playing_song
    global paused
  
    #Plays highlighed Song in the list box
    def playSelectedSong():
        global current_playing_song
        song_file = song_listbox.get(song_listbox.curselection())
        play_file = os.path.join(folder_path,song_file)
        mixer.music.load(play_file)
        mixer.music.play()
        play_pause_button.config(image=spotify_pause_image) # Updating the Play/Pause button
        current_playing_song = song_listbox.curselection()[0] # Updating current song selection

    #Plays song at selected index in the listbox
    def PlaySong(index):
        global current_playing_song
        song_file = song_listbox.get(index)
        play_file = os.path.join(folder_path,song_file)
        mixer.music.load(play_file)
        mixer.music.play()
        play_pause_button.config(image=spotify_pause_image) # Updating the Play/Pause button
        current_playing_song = index # Updating current song selection        



    if len(song_listbox.curselection()) == 0:
        print("No song selected")
        return()
    current_curse_selection = song_listbox.curselection()[0]
    
    if paused:
        #If the current song is being unpaused
        if last_playing_song == current_curse_selection:
            mixer.music.unpause()
            paused = False
            play_pause_button.config(image=spotify_pause_image) # Updating the Play/Pause button
            current_playing_song = song_listbox.curselection()[0] # Updating current song selection

            print("current song being unpaused")
            print(current_curse_selection, current_playing_song)
        #If there is no song currently playing or a different is selected

        elif current_playing_song != current_curse_selection:
            playSelectedSong()
            paused = False
            last_playing_song = current_playing_song
            print("change to different song")
            print(current_curse_selection, current_playing_song)

    elif not paused:
        print("music paused")
        paused = True
        mixer.music.pause()
        last_playing_song = current_playing_song
        current_playing_song = -1
        play_pause_button.config(image=spotify_play_image)
        
algorithms = ["True Random", "Random No Repeats", "No Shuffle" ]   
combo = ttk.Combobox(state = "readonly", values = algorithms)
combo.place(x=340,y=550)
combo.set("No Shuffle")

def NextSong():
    global current_playing_song

    songcurrent = current_playing_song + 1
    if songcurrent < songnum:
        song_file = song_listbox.get(songcurrent)
        play_file = os.path.join(folder_path,song_file)
        mixer.music.load(play_file)
        mixer.music.play()
        current_playing_song += 1
        song_listbox.select_clear(0,END)
        song_listbox.selection_set(current_playing_song)
    elif songcurrent == songnum:
        song_file = song_listbox.get(0)
        play_file = os.path.join(folder_path,song_file)
        mixer.music.load(play_file)
        mixer.music.play()
        current_playing_song = 0
        song_listbox.select_clear(0,END)
        song_listbox.selection_set(current_playing_song)

def PrevSong():
    global current_playing_song
    if current_playing_song > 0:
        song_file = song_listbox.get(current_playing_song - 1)
        play_file = os.path.join(folder_path,song_file)
        mixer.music.load(play_file)
        mixer.music.play()
        current_playing_song -= 1
        song_listbox.select_clear(0,END)
        song_listbox.selection_set(current_playing_song)
    elif current_playing_song == 0:
        song_file = song_listbox.get(songnum - 1)
        play_file = os.path.join(folder_path,song_file)
        mixer.music.load(play_file)
        mixer.music.play()
        current_playing_song = songnum - 1
        song_listbox.select_clear(0,END)
        song_listbox.selection_set(current_playing_song)

def SelectChange(event):
    play_pause_button.config(image=spotify_play_image)

def Debug():
    print("Current Playing Song:", current_playing_song)
    print("Song Selection:", song_listbox.curselection())
    
# Sets the Icon photo
spotify_iconlogo = PhotoImage(file="Images/spotify_logo.png")
root.iconphoto(False, spotify_iconlogo)

# Loads the image
wide_logo = Image.open(r"Images/spotify_logo_wide.png")

# Resizes, and sets the banner photo
wide_logo = wide_logo.resize((200,115))
spotify_widelogo = ImageTk.PhotoImage(wide_logo)
Label(root, image = spotify_widelogo).pack(anchor = "n", side = "left")


# Initializing the pictures for the buttons
button_resume = PhotoImage(file="Images/resume_button.png")
button_pause = PhotoImage(file="Images/pause_button.png")
prev_image = PhotoImage(file="Images/prev_button.png")
next_image = PhotoImage(file="Images/next_button.png")

#Placing the File Button
file_image = Image.open(r"Images/file_logo.png")
file_image = file_image.resize((200,200))
button_file = ImageTk.PhotoImage(file_image)    
Button(root, image=button_file, bg="#0f1a2b",bd=0, command = SelectFolder).place(x=50, y=350)

# Placing the play/pause music button
play_image = Image.open(r"Images\resume_button.png")
play_image = play_image.resize((100,100))
spotify_play_image = ImageTk.PhotoImage(play_image)

pause_image = Image.open(r"Images\pause_button.png")
pause_image = pause_image.resize((100,100))
spotify_pause_image = ImageTk.PhotoImage(pause_image)

global play_pause_button
play_pause_button = Button(root, image = spotify_play_image, command = PlayMusic)
play_pause_button.place(x=700, y=450)

# Displaying the song count
global songcount
songcount = StringVar(value="0")
Label(root, text="Song Count: ").place(x=540, y=10)
Label(root, textvariable=songcount).place(x=620, y=10)

# Placing the Next and Prev Buttons
prev_button = Button(root, image=prev_image,command=PrevSong)
prev_button.place(x=540, y=450)

next_button = Button(root, image=next_image,command=NextSong)
next_button.place(x=810,y=450)

Button(root,text="Debug",command=Debug).pack()

# Initializing the songlist
song_listbox = Listbox(root, height= 20, width = 100, selectmode=SINGLE)
song_listbox.bind("<<ListboxSelect>>", SelectChange) 

# Runs the application
root.mainloop()

