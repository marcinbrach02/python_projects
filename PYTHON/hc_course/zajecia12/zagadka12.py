import tkinter as tk
gui = tk.Tk()
letters = "xxamkt"
def show():
    for i in reversed(letters):
            tk.Label(text=i).pack()
    tk.Label(text="and add lowercase name of this widget below:").pack()
    tk.Entry().pack()

button = tk.Button(text="Show password", command=show).pack()
