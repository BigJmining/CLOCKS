#!/usr/bin/env python3
'''
Task management is an issue for many, this app allows you to create a timer for an event.
The timer can be labled
'''

import tkinter as tk
from time import sleep 
import sys, random


commands = sys.argv[1::]

# if the user inputs a command (time) from command line
if len(commands) > 0:
    commands_time = str(commands[0]).split(":")
    timer_hour = commands_time[0]
    timer_minute = commands_time[1]
    timer_second = commands_time[2]
    length_of_timer = int(timer_second) + (int(timer_minute)*60) + ((int(timer_hour)*60)*60)
    my_window_lable = str(commands[1])
    
else:
    # get desired time for timer from user    
    new_timer = input('>>(HR:MIN:SEC)<<: ')
    commands_time = str(new_timer).split(":")
    timer_hour = commands_time[0]
    timer_minute = commands_time[1]
    timer_second = commands_time[2]
    length_of_timer = int(timer_second) + (int(timer_minute)*60) + ((int(timer_hour)*60)*60)
    # lable the timer 
    my_window_lable = input("Name of Countdown?:: ")

global counter
counter = int(length_of_timer)



def show_timer():
    global counter
    minutes, seconds = divmod(counter, 60)
    hours, minutes = divmod(minutes, 60)
    count = (str(hours).zfill(2)+':'+str(minutes).zfill(2)+':'+str(seconds).zfill(2))
    
    countdown['text'] = count
    counter -= 1
    sleep(.8)
    countdown.after(200, show_timer)
    
    if hours < 0:
        boom()
        # uncomment next 2 lines if user wants the window to auto close after 5 sec
        # if seconds < 50:    
            # sys.exit(0)
            

def change_color():
    # give different colors to timers should user want to run multi incidents of app
    number_color = ['green', 'yellow', 'pink', 'blue', 'purple', 'grey', 'white', 'orange','red']
    return random.choice(number_color)


def boom():
    # once the timer completes blink its color to alert user
    countdown = tk.Label(window, font='ariel 80', bg='black', fg=change_color(), text='  BOOM  ')
    countdown.grid(column=0, row=0)
    

window = tk.Tk()
if len(my_window_lable) > 0:
    window.title(my_window_lable.upper())
else:    
    window.title("Digtal_Countdown_Timer")
countdown = tk.Label(window, font='ariel 80', bg='black',fg=change_color())
countdown.grid(column=0, row=0)

show_timer()

window.mainloop()





