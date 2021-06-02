import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

def popup_bonus():
    win = tk.Toplevel()
    win.wm_title("Window")
    win.wm_geometry("200x200")

    l = tk.Label(win, text="This program was made by:")
    l.place(x=10, y=10)
    l = tk.Label(win, text="Marko Pejanovic 49/19")
    l.place(x=10, y=30)
    l = tk.Label(win, text="Marko Pejanovic 49/19")
    l.place(x=10, y=60)
    l = tk.Label(win, text="Marko Pejanovic 49/19")
    l.place(x=10, y=90)

    b = ttk.Button(win, text="Close", command=win.destroy)
    b.place(x=10, y=130)

def popup_showinfo():
    showinfo("Creators", "This program was made by:\n Marko Pejanovic 49/19")