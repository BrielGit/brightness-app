import screen_brightness_control as sbc
from tkinter import *
import tkinter as tk
from tkinter import ttk
import threading

brightness = sbc.get_brightness()
stop_event = threading.Event()

def change_brightness(event=None):
    global brightness
    new_brightness = int(slider.get())
    if brightness != new_brightness:
        master.after(100, sbc.set_brightness(new_brightness))

def center_window(master, width, height):
    screen_width = master.winfo_screenwidth()
    screen_height = master.winfo_screenheight()
    x1 = width / 2
    y1 = height / 2
    x2 = screen_width / 2
    y2 = screen_height / 2
    x3 = int(x2 - x1)
    y3 = int(y2 - y1)
    master.geometry(f'{width}x{height}+{x3}+{y3}')

master = tk.Tk()
center_window(master, 300, 350)
master.title('Brightness Controller')

slider = Scale(master, from_=0, to=100, orient=HORIZONTAL, command=change_brightness)
# slider = ttk.Scale(master, command = lambda value: print(slider.get()), from_= 0, to = 100)
slider.set(brightness)
slider.pack()


tk.mainloop()