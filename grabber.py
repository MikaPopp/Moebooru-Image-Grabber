import os
from tkinter import Label
from tkinter import StringVar
from tkinter import Grid
from tkinter import Tk
from tkinter import OptionMenu
from tkinter import Entry
from tkinter import Button
from tkinter import PhotoImage
from misc import *
from tkinter import *
from tkinter.ttk import *
from ttkthemes import themed_tk as tk
from pybooru import Moebooru
import requests

def grab(*grab_tags:str, grab_count:int, source:str):
    client = Moebooru(site_url="https://"+source)
    posts = client.post_list(tags=grab_tags, limit=grab_count)
    count = 0
    printAwesomeASCII()
    if(len(grab_count) == 0):
            print("No grab count specified!")
            print("returning...")
            gui()
    else:
        if((float(checkDiskSpace())-(float(grab_count)*5/1024)) >= 0):
            if(not posts):
                print("There wasn't any post to grab!")
                print("returning...")
                gui()
            else:
                print("=============================================================")
                printProgressBar(0, int(grab_count), prefix = 'Progress:', suffix = 'Complete', length = 50)
                for post in posts:
                    image_url = post["file_url"]
                    image_name = image_url.split("/")[-1]
                    image_path = os.getcwd()+"/pictures/"
                    img_data = requests.get(image_url).content
                    with open(image_path+image_name, "wb") as handler:
                        handler.write(img_data)
                        count+=1
                        printProgressBar(count, int(grab_count), prefix="Progress:", suffix="Complete", length=50)
                print("=============================================================")
                print("Finished grabbing")
                gui()
        else:
            print("Not enough disk space!")
            print("returning...")
            gui()

def start_grabbing(window, source, tags, count, c1, c2, c3):
    window.destroy()  
    if c3 == 1:
        tags += " rating:s"
    else:
        if c1 == 1:
            tags += " rating:e "
        if c2 == 1:
            tags += "rating:q "
    grab(tags, grab_count=count, source=source)

def callback(input):
        if str.isdigit(input) or input == "":
            maxlength = 5
            if len(input) is None or len(input) <= maxlength:
                return True
            else:
                return False
        else:
            return False

def gui():
    window = tk.ThemedTk()
    window.get_themes()
    window.set_theme("black")
    window.geometry("400x400")
    window.title("Moebooru Image Grabber - MikaPopp")
    window.resizable(False, False)

    source_list = ["Yande.re", "Konachan.com"]
    value_option_source = StringVar()

    background_picture = PhotoImage(file=os.getcwd()+"/resources/bg.png")
    background_label = Label(image=background_picture)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    label_source = Label(text="Source:", background="black")
    label_source.grid(row=0)
    dropdown_source = OptionMenu(window, value_option_source, source_list[0], *source_list)
    dropdown_source.grid(row=1)
    label_rating = Label(text="Rating (optional):", background="black")
    label_rating.grid(row=2)
    var_one = IntVar()
    var_two = IntVar()
    var_three = IntVar()
    check_rating_explicit = Checkbutton(window, text="Explicit", variable=var_one)
    check_rating_explicit.grid(row=3)
    check_rating_questionable = Checkbutton(window, text="Questionable", variable=var_two)
    check_rating_questionable.grid(row=4)
    check_rating_safe = Checkbutton(window, text="Safe", variable=var_three)
    check_rating_safe.grid(row=5)
    label_tags = Label(text="Tags (optional):", background="black")
    label_tags.grid(row=6)
    entry_tags = Entry(width=15)
    entry_tags.grid(row=7, padx=15)
    label_count = Label(text="Count:", background="black")
    label_count.grid(row=8)
    entry_count = Entry(window, width=15)
    reg = window.register(callback)
    entry_count.config(validate="key", validatecommand=(reg, "%P"))
    entry_count.grid(row=9)
    button_start = Button(text="Start", state=ACTIVE, width=4, command=lambda:start_grabbing(window=window, source=value_option_source.get(), tags=entry_tags.get(),
     count=entry_count.get(), c1=var_one.get(), c2=var_two.get(), c3=var_three.get()))
    button_start.grid(row=10)
    window.mainloop()

gui()