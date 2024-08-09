import screen_brightness_control as sbc
from tkinter import *
import tkinter as tk
import threading

brightness = sbc.get_brightness()

def change_brightness(value):
    global idk
    threading.Thread(target=lambda: sbc.set_brightness(idk.get())).start()

def center_window(width, height):
    screen_width = master.winfo_screenwidth()
    screen_height = master.winfo_screenheight()
    x1 = width / 2
    y1 = height / 2
    x2 = screen_width / 2
    y2 = screen_height / 2
    x3 = int(x2 - x1)
    y3 = int(y2 - y1)
    master.geometry(f'{width}x{height}+{x3}+{y3}')

def jump_to_position(event):
    # Calculate the new slider value based on the click position
    slider_length = slider.winfo_width()
    click_position = event.x
    new_value = (click_position / slider_length) * 100
    slider.set(new_value)
    change_brightness(new_value)

def display_entry_value(event=None):
    global idk
    entry_value.delete(0, tk.END)
    entry_value.insert(0, str(slider.get()))

def entry_useful(event):
    global idk
    idk.set(entry_value.get())
    change_brightness(idk.get())

def validate_entry(value):
    return value.isdigit() or value == ''

master = tk.Tk()
center_window(400, 150)
master.title('Brightness Controller')
master.configure(bg="#2b2b2b")
idk = tk.IntVar(value=0)

label_sun = Label(master, text="☀",background='#2b2b2b', fg='white', font=("Arial", 24))
label_sun.pack(pady=(10, 8), padx=(7, 0))

slider = Scale(master, from_=0, to=100, orient=HORIZONTAL, showvalue=False, variable=idk, command=display_entry_value, length=300, sliderlength=20, bd=0)
slider.set(brightness)
slider.pack()

vcmd = (master.register(validate_entry), '%P')
entry_value = Entry(master, validate='key', validatecommand=vcmd, width=8, justify='center', font=('Courier', 12), bd=4)
# entry_value.insert(0, brightness)
entry_value.pack(pady=(15, 0))

# Bind the brightness change to slider release
slider.bind("<ButtonRelease-1>", change_brightness)

# Bind mouse click on slider to jump to the clicked position
slider.bind("<Button-1>", jump_to_position)
entry_value.bind("<Return>", entry_useful)  # Bind the "Enter" key to the entry box


# Being a cringe simp

master.mainloop()
