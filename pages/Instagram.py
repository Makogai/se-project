import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from urllib.request import urlopen
from io import BytesIO
import instaloader
from datetime import datetime
from tkinter import messagebox
from pathlib import Path
import json

class InstagramData:

    def __init__(self):
        self.root = tk.Toplevel()
        self.root.geometry('700x400')
        iconPath = Path(__file__).parent / "../assets/images/instagram.ico"
        self.root.iconbitmap(iconPath)
        self.root.maxsize(700, 400)
        self.root.minsize(700, 400)

        self.root.title('PyFy - Instagram data')
        self.root['bg'] = "white"

        self.title = Label(self.root, text="Instagram Data", font=(
            'verdana', 15, 'bold'), bg="white", fg="#f56132")
        self.title.place(x=280, y=5)

        self.date = Label(self.root, text=datetime.now().date(),
                          fg="#f56132", font=('verdana', 10, 'bold'))
        self.date.place(x=600, y=5)

        Label(self.root, text="Enter username here", font=(
            'verdana', 10, 'bold'), fg="#f56132").place(x=100, y=50)

        self.url = Entry(self.root, width=50, bg="lightgrey",
                         relief=GROOVE, borderwidth=2, border=2)
        self.url.place(x=100, y=80)

        self.button = Button(self.root, relief=GROOVE, text="Get", font=(
            'verdana', 8, 'bold'), bg="#f56132", fg="white", command=self.getData)
        self.button.place(x=420, y=78)

        # Placeholder image for profile photo
        ph_profile_path = Path(__file__).parent / \
            "../assets/images/profile_ph.png"
        im_ph = Image.open(ph_profile_path)
        profileImage_ph = im_ph.resize((250, 250), Image.ANTIALIAS)
        photo_ph = ImageTk.PhotoImage(profileImage_ph)

        self.label_profile_ph = Label(self.root, image=photo_ph)
        self.label_profile_ph.image = photo_ph
        self.label_profile_ph.place(x=0, y=120)
        # End of the placeholder for profile

        # Image for followers
        ph_profile_path = Path(__file__).parent / \
            "../assets/images/followers.png"
        im_ph = Image.open(ph_profile_path)
        profileImage_ph = im_ph.resize((25, 25), Image.ANTIALIAS)
        photo_ph = ImageTk.PhotoImage(profileImage_ph)

        self.label_profile_ph = Label(self.root, image=photo_ph)
        self.label_profile_ph.image = photo_ph
        self.label_profile_ph.place(x=260, y=190)
        # End of followers image

        # Image for following
        ph_profile_path = Path(__file__).parent / \
            "../assets/images/following.png"
        im_ph = Image.open(ph_profile_path)
        profileImage_ph = im_ph.resize((25, 25), Image.ANTIALIAS)
        photo_ph = ImageTk.PhotoImage(profileImage_ph)

        self.label_profile_ph = Label(self.root, image=photo_ph)
        self.label_profile_ph.image = photo_ph
        self.label_profile_ph.place(x=260, y=220)
        # End of following image

        self.username_lb = Label(self.root, font=(
            'verdana', 15, 'bold'), bg="white", fg="#f56132", text="username")
        self.username_lb.place(x=260, y=120)

        self.name_lb = Label(self.root, font=(
            'verdana', 15, 'normal'), bg="white", fg="#f56132", text="Full Name")
        self.name_lb.place(x=260, y=150)

        self.followers_lb = Label(self.root, font=(
            'verdana', 12, 'bold'), bg="white", fg="#f56132", text="0000000")
        self.followers_lb.place(x=290, y=192)

        self.following_lb = Label(self.root, font=(
            'verdana', 12, 'bold'), bg="white", fg="#f56132", text="0000000")
        self.following_lb.place(x=290, y=222)

        self.bio_lb = Label(self.root, font=(
            'verdana', 11, 'normal'), bg="white", fg="#f56132", text="Biography")
        self.bio_lb.place(x=260, y=250)

        self.root.mainloop()

    def getData(self):
        if self.url.get() == "":
            messagebox.showerror("Error", "Please enter an username")
        else:
            L = instaloader.Instaloader()
            profile = instaloader.Profile.from_username(
                L.context, self.url.get())

            profile_pic = profile.profile_pic_url
            username = profile.username
            followers = profile.followers
            following = profile.followees
            name = profile.full_name
            bio = profile.biography

            URL = profile_pic
            u = urlopen(URL)
            raw_data = u.read()
            u.close()

            im = Image.open(BytesIO(raw_data))
            image = im.resize((250, 250), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(image)

            self.label = Label(self.root, image=photo)
            self.label.image = photo
            self.label.place(x=0, y=120)
            self.username_lb['text'] = username
            self.following_lb['text'] = following
            self.followers_lb['text'] = followers
            self.name_lb['text'] = name if name != "" else "[NO NAME]"
            self.bio_lb['text'] = bio if bio != "" else "[NO BIO]"
            
            data = {}
            # data['profile'] = []
            data['profile']=({
                'username': username,
                'followers': followers,
                'following': following,
                'full_name': name,
                'bio': bio
            })
            with open('instagram_data/'+username+'.json', 'w') as outfile:
                json.dump(data, outfile)
            # self.write_json(data_current)



        
# InstagramData()
