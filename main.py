from tkinter import *

mp = Tk()
mp.geometry("800x540+250-100")
mp.minsize(800,540)
mp.maxsize(800,540)
mp.title("Music Player")
mp.iconbitmap(default='C:/Users/PC/PycharmProjects/Lab_work_3/icon.ico')
# mp['bg'] = '#363d4d'
canvas = Canvas(bg='#363d4d', width=800, height=540)
canvas.pack(anchor=CENTER, expand=1)
canvas.create_line(0, 400, 800, 400, width=4, fill='#1f232e')
canvas.create_polygon(0, 540, 0, 400, 800, 400, 800, 540, fill='#2b3140')
python_image = PhotoImage(file='C:/Users/PC/PycharmProjects/Lab_work_3/picture.png')
canvas.create_image(165, 225, image=python_image)
mp.mainloop()