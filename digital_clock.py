#!/usr/bin/env python3

import tkinter as tk
import time as tm

def show_time():
    current_time = tm.strftime("%I:%M:%S %P")
    clock_label['text'] = current_time
    clock_label.after(200, show_time)

window = tk.Tk()
window.title("Digtal_Clock")
clock_label=tk.Label(window, font='ariel 80', bg='black', fg='red')
clock_label.grid(column=0, row=0)
show_time()
window.mainloop()