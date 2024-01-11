import tkinter as tk
import time

def clock():
    time_current = time.strftime("%H:%M:%S")
    timeclock.config(text=time_current)
    timeclock.after(1000, clock)

window = tk.Tk()
window.title("Time")

timeclock = tk.Label(window, text="", font=("Mali", 36))
timeclock.pack()

clock()
window.mainloop()