import screen_brightness_control as sbc
from tkinter import *
import tkinter as tk
from tkinter import ttk
import threading

brightness = sbc.get_brightness()
stop_event = threading.Event()

def change_brightness():
    global scale_int
    global brightness
    if brightness != scale_int:
        master.after(100, sbc.set_brightness(scale_int.get()))

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

# slider
scale_int = IntVar(value=brightness)
slider = ttk.Scale(master, 
                   command = lambda value: change_brightness(), 
                   from_= 0, 
                   to = 100,
                   length = 300,
                   orient = 'vertical',
                   variable = scale_int)
slider.pack()


tk.mainloop()