import os
from tkinter import *
from tkinter import filedialog
from pygame import mixer

playlist = []
mixer.init()
current_index = 0
is_paused = False
fd = None
current_image_size = "small"


def select_music_folder():
    folder_path = filedialog.askdirectory(
        title="Выберите папку с музыкой",
        initialdir=os.path.expanduser("~"),
        mustexist=True
    )
    if folder_path:
        audio_files = [f for f in os.listdir(folder_path)
                       if f.lower().endswith(('.mp3', '.wav', '.ogg', '.flac', '.m4a'))]
        if not audio_files:
            return None
    return folder_path


def browse_folder():
    global fd, current_index, playlist
    selected_folder = select_music_folder()
    if selected_folder is not None:
        fd = selected_folder
        playlist = []
        current_index = 0
        playlist = os.listdir(fd)
        for file in playlist:
            mixer.music.load(os.path.join(fd, file))
        update_track_label()
    else:
        lbl_track.config(text='Треков в этой папке нет!')


def load_and_play():
    global current_index, is_paused
    if is_paused:
        mixer.music.unpause()
        is_paused = False
        btn_pause.config(relief='raised')
    else:
        if playlist and fd:
            track_path = os.path.join(fd, playlist[current_index])
            mixer.music.load(track_path)
            mixer.music.play()
            update_track_label()
        else:
            lbl_track.config(text='Выберите папку!')


def update_track_label():
    if playlist and current_index < len(playlist):
        track_name = playlist[current_index]
        if '.' in track_name:
            track_name = track_name[:track_name.rindex('.')]
        lbl_track.config(text=track_name)
    elif not playlist:
        lbl_track.config(text='Выберите папку с музыкой')


def next_track():
    global current_index
    if playlist:
        current_index = (current_index + 1) % len(playlist)
        load_and_play()


def previous_track():
    global current_index
    if playlist:
        current_index = (current_index - 1) % len(playlist)
        load_and_play()


def pause():
    global is_paused
    mixer.music.pause()
    btn_pause.config(relief='sunken')
    is_paused = True


def stop():
    global is_paused
    mixer.music.stop()
    is_paused = False
    btn_pause.config(relief='raised')


def on_resize(event=None):
    window_width = mp.winfo_width()
    window_height = mp.winfo_height()
    canvas.delete('all')
    canvas.config(bg='#363d4d')
    line_y = window_height * 0.90
    canvas.create_line(0, line_y, window_width, line_y,width=4, fill='#1f232e')

    canvas.create_polygon(0, window_height, 0, line_y,window_width, line_y, window_width, window_height,fill='#2b3140')
    global current_image_size
    if window_width >= 1400:
        if current_image_size != "large":
            current_image_size = "large"
        current_pic = music_pic_large
    else:
        if current_image_size != "small":
            current_image_size = "small"
        current_pic = music_pic_small
    img_x = window_width * 0.206
    img_y = window_height * 0.417
    canvas.create_image(img_x, img_y, image=current_pic, anchor='center')
    update_button_positions(window_width, window_height)


def update_button_positions(window_width, window_height):
    base_y = window_height * 0.90
    start_x = (window_width - 325) / 2
    lbl_track.place(x=start_x - 135, y=base_y + 25, anchor='center', width=200, height=40)
    btn_stop.place(x=start_x + 20, y=base_y + 25, anchor='center')
    btn_previous.place(x=start_x + 85, y=base_y + 25, anchor='center')
    btn_play.place(x=start_x + 150, y=base_y + 25, anchor='center')
    btn_pause.place(x=start_x + 215, y=base_y + 25, anchor='center')
    btn_next.place(x=start_x + 280, y=base_y + 25, anchor='center')
    btn_folder.place(x=start_x + 345, y=base_y + 25, anchor='center')

mp = Tk()
mp.geometry("800x540+250-100")
mp.minsize(800, 540)
mp.title("Music Player")

mp.iconbitmap(default='images/icon.ico')
music_pic_small = PhotoImage(file='images/picture.png')
music_pic_large = PhotoImage(file='images/picture_large.png')

play_button = PhotoImage(file='images/play-button.png')
stop_button = PhotoImage(file='images/stop-button.png')
pause_button = PhotoImage(file='images/pause-button.png')
forward_button = PhotoImage(file='images/forward-button.png')
back_button = PhotoImage(file='images/back-button.png')
folder_button = PhotoImage(file='images/folder-button.png')

canvas = Canvas(mp, bg='#363d4d', highlightthickness=0)
canvas.pack(fill='both', expand=YES)

lbl_track = Label(mp, text='Выберите папку с музыкой', font=('Arial', 11, 'bold'), bg='#2b3140', fg='white',relief='flat', anchor='center', wraplength=180)
btn_play = Button(mp, image=play_button, bg='#363d4d', height=50, width=50, command=load_and_play, relief='raised',borderwidth=0)
btn_pause = Button(mp, image=pause_button, bg='#363d4d', height=50, width=50, command=pause, relief='raised',borderwidth=0)
btn_stop = Button(mp, image=stop_button, bg='#363d4d', height=50, width=50, command=stop, relief='raised', borderwidth=0)
btn_next = Button(mp, image=forward_button, bg='#363d4d', height=50, width=50, command=next_track, relief='raised',borderwidth=0)
btn_previous = Button(mp, image=back_button, bg='#363d4d', height=50, width=50, command=previous_track, relief='raised',borderwidth=0)
btn_folder = Button(mp, image=folder_button, bg='#363d4d', height=50, width=50, command=browse_folder, relief='raised',borderwidth=0)
mp.bind('<Configure>', on_resize)
mp.mainloop()