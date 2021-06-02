from tkinter import *
from pathlib import Path
# from tkinter.ttk import *
from tkinter.messagebox import showinfo
from PIL import ImageTk ,Image

# Import pages
from pages import Help
from pages import Short

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        menu = Menu(self.master)
        self.master.config(menu=menu)

        fileMenu = Menu(menu, tearoff=0)
        fileMenu.add_command(label="Home", command=self.openDashboard)
        fileMenu.add_command(label="Exit", command=self.exitProgram)
        menu.add_cascade(label="File", menu=fileMenu)

        editMenu = Menu(menu, tearoff=0)
        editMenu.add_command(label="About", command=Help.popup_showinfo)
        menu.add_cascade(label="Help", menu=editMenu)

        # Dashvboard
        page_title = Label(text="Welcome to Dashbaord", font=("Roboto", 21))
        page_title.pack(side = TOP)

        # Buttons
        shortener_btn = Button(height=4,text="Link Shortener", command=Short.url_shortner).place(x=20, y=40)
        shortener_btn2 = Button(text="Link Shortener").place(x=120, y=40)


    def exitProgram(self):
        exit()
    def openDashboard(self):
        exit()
        
root = Tk()
app = Window(root)
root.title('PyFy - Python toolkit')
iconPath = Path(__file__).parent / "./assets/images/icon.ico"
root.iconbitmap(iconPath)
root.geometry("700x400")
root.mainloop()
