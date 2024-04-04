import tkinter as tk
import time

def time_counter():
    second = int(entry.get())
    while 0 < second:
        label.config(text="Time left:{}".format(second))
        time.sleep(1)
        second -= 1
        window.update()
    label.config(text='Your time is over !!')

window = tk.Tk()
window.title('Time Counter !!')
label = tk.Label(window,text='Enter the seconds:')
label.pack()
entry = tk.Entry(window)
entry.pack()
start_button = tk.Button(window,text='Start',command=time_counter)
start_button.pack()
window.mainloop()

