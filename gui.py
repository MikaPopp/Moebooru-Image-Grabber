import os
from tkinter import Label
from tkinter import StringVar
from tkinter import Grid
from tkinter import Tk
from tkinter import OptionMenu
from tkinter import Entry
from tkinter import Button
from tkinter import PhotoImage
from grabber import grab
from tkinter import *
from tkinter.ttk import *
from ttkthemes import themed_tk as tk

def start_grabbing():
    source = value_option_source.get()
    tags = entry_tags.get()
    count = entry_count.get()
    if var_one.get() == 1:
        tags += ""
    elif var_four.get() == 1:
        tags += " rating:s"
    else:
        if var_two.get() == 1:
            tags += " rating:e "
        if var_three.get() == 1:
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
label_source = Label(text="Source:")
label_source.grid(row=0)
dropdown_source = OptionMenu(window, value_option_source, source_list[0], *source_list)
dropdown_source.grid(row=1)
label_rating = Label(text="Rating:")
label_rating.grid(row=2)
var_one = IntVar(value=1)
var_two = IntVar()
var_three = IntVar()
var_four = IntVar()
check_rating_all = Checkbutton(window, text="All", variable=var_one)
check_rating_all.grid(row=3)
check_rating_explicit = Checkbutton(window, text="Explicit", variable=var_two)
check_rating_explicit.grid(row=4)
check_rating_questionable = Checkbutton(window, text="Questionable", variable=var_three)
check_rating_questionable.grid(row=5)
check_rating_safe = Checkbutton(window, text="Safe", variable=var_four)
check_rating_safe.grid(row=6)
label_tags = Label(text="Tags:")
label_tags.grid(row=7)
entry_tags = Entry()
entry_tags.grid(row=8)
label_count = Label(text="Count:")
label_count.grid(row=9)
entry_count = Entry(window)
reg = window.register(callback)
entry_count.config(validate="key", validatecommand=(reg, "%P"))
entry_count.grid(row=10)
button_start = Button(text="Start", width=4, command=lambda:start_grabbing())
button_start.grid(row=11)

window.mainloop()