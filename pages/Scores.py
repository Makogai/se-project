# from tkinter import *
# from PIL import ImageTk ,Image

# base = Tk()
# base.title('Start Button')

# img=ImageTk.PhotoImage(Image.open ("c:/Users/mares/Desktop/it-projekat/assets/images/link2.png"))
# lab=Label(image=img)
# lab.pack()

# button=Button(base,text='exit',command=base.quit)
# button.pack()
# base.mainloop()


import tkinter as tk

def mmWindow():
    mmWindow = tk.Tk()
    mmWindow.geometry('600x600')

mWindow = tk.Tk()
# You can set any size you want
mWindow.geometry('500x500+0+0')
mWindow.title('DMX512 Controller')

wtitle = tk.Label(mWindow, text="Pi DMX", fg='blue')
wtitle.grid(row=0, column=1)

# You can set any height and width you want
mmbutton = tk.Button(mWindow, height=5, width=20, text="Main Menu", command=mmWindow)
mmbutton.grid(row=1, column=1)

mWindow.mainloop()