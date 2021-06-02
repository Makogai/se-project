

import instaloader
L = instaloader.Instaloader()
profile = instaloader.Profile.from_username(L.context, 'makogai')
profile_pic = profile.profile_pic_url

# import tkinter
# from tkinter import *
# from PIL import ImageTk, Image 

# root = Tk()
# # Create a photoimage object of the image in the path
# image1 = Image.open(profile_pic)
# test = ImageTk.PhotoImage(image1)

# label1 = tkinter.Label(image=test)
# label1.image = test

# # Position image
# label1.pack()
# root.mainloop()




import tkinter as tk
from PIL import Image, ImageTk
from urllib.request import urlopen
from io import BytesIO

root = tk.Tk()

URL = profile_pic
u = urlopen(URL)
raw_data = u.read()
u.close()

im = Image.open(BytesIO(raw_data))
photo = ImageTk.PhotoImage(im)

label = tk.Label(image=photo)
label.image = photo
label.pack()

root.mainloop()