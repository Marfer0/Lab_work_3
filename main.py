import os
from tkinter import *
from tkinter import filedialog, messagebox
from pygame import mixer


fd = 'C:/Users/PC/PycharmProjects/Lab_work_3/playlist'
playlist = os.listdir(fd)
mixer.init()
current_index = 0
for file in playlist:
    mixer.music.load(os.path.join(fd, file))


def select_music_folder():
    folder_path = filedialog.askdirectory(
        title="Выберите папку с музыкой",
        initialdir=os.path.expanduser("~"),
        mustexist=True
    )
    print(folder_path)
    return folder_path


def load_and_play():
    global current_index
    if playlist:
        track_path = os.path.join(fd, playlist[current_index])
        mixer.music.load(track_path)
        mixer.music.play()
        canvas.create_text(185, 485, text=playlist[current_index][:-4], font=('Arial', 12, 'bold'), fill='white', tags='label')

def next_track():
    global current_index
    if (current_index + 1) < len(playlist):
        current_index = (current_index + 1)
    else:
        current_index = 0
    canvas.delete('label')
    load_and_play()

def previous_track():
    global current_index
    if (current_index - 1) >= 0:
        current_index = (current_index - 1)
    else:
        current_index = len(playlist) - 1
    canvas.delete('label')
    load_and_play()


def toggle_pause():
    if btn_pause['relief'] == SUNKEN:
        mixer.music.unpause()
        btn_pause.config(relief=RAISED)
    else:
        mixer.music.pause()
        btn_pause.config(relief=SUNKEN)


mp = Tk()
mp.geometry("800x540+250-100")
mp.minsize(800,540)
mp.maxsize(800,540)
mp.title("Music Player")
mp.iconbitmap(default='images/icon.ico')
canvas = Canvas(bg='#363d4d', width=800, height=540)
canvas.pack(anchor=CENTER, expand=1)
canvas.create_line(0, 400, 800, 400, width=4, fill='#1f232e')
canvas.create_polygon(0, 540, 0, 400, 800, 400, 800, 540, fill='#2b3140')
music_pic = PhotoImage(file='images/picture.png')
canvas.create_image(165, 225, image=music_pic)
play_button = PhotoImage(file='images/play-button.png')
stop_button = PhotoImage(file='images/stop-button.png')
pause_button = PhotoImage(file='images/pause-button.png')
forward_button = PhotoImage(file='images/forward-button.png')
back_button = PhotoImage(file='images/back-button.png')
folder_button = PhotoImage(file='images/folder-button.png')
btn_play = Button(mp, image=play_button, bg='#363d4d', height=50, width=50, command=load_and_play)
btn_play.place(x=495, y=460)
btn_pause = Button(mp, image=pause_button, bg='#363d4d', height=50, width=50, command=toggle_pause)
btn_pause.place(x=560, y=460)
btn_stop = Button(mp, image=stop_button, bg='#363d4d', height=50, width=50, command=mixer.music.stop)
btn_stop.place(x=430, y=460)
btn_next = Button(mp, image=forward_button, bg='#363d4d', height=50, width=50, command=next_track)
btn_next.place(x=625, y=460)
btn_previous = Button(mp, image=back_button, bg='#363d4d', height=50, width=50, command=previous_track)
btn_previous.place(x=365, y=460)
btn_folder = Button(mp, image=folder_button, bg='#363d4d', height=50, width=50, command=select_music_folder)
btn_folder.place(x=690, y=460)
mp.mainloop()