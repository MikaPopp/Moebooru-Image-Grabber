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

def start_grabbing():
    source = value_option_source.get()
    rating = value_option_rating.get()
    tags = entry_tags.get()
    count = entry_count.get()
    if rating == rating_list[0]:
        grab(tags, grab_count=count, source=source)
    elif rating == rating_list[1]:
        tags += " rating:e"
        grab(tags, grab_count=count, source=source)
    elif rating == rating_list[2]:
        tags += " rating:q"
        grab(tags, grab_count=count, source=source)
    elif rating == rating_list[3]:
        tags += " rating:s"
        grab(tags, grab_count=count, source=source)

window = Tk()
window.geometry("500x500")
window.title("Moebooru grabber - MikaPopp")
window.resizable(False, False)

source_list = ["Yande.re", "Konachan.com"]
value_option_source = StringVar()
value_option_source.set(source_list[0])
rating_list = ["All" ,"Explicit", "Questionable", "Safe"]
value_option_rating = StringVar()
value_option_rating.set(rating_list[0])

background_picture = PhotoImage(file=os.getcwd()+"/resources/bg.png")
background_label = Label(image=background_picture)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
label_source = Label(text="Source:")
label_source.grid(row=0)
dropdown_source = OptionMenu(window, value_option_source, *source_list)
dropdown_source.grid(row=1)
label_rating = Label(text="Rating:")
label_rating.grid(row=2)
dropdown_rating = OptionMenu(window, value_option_rating, *rating_list)
dropdown_rating.grid(row=3)
label_tags = Label(text="Tags:")
label_tags.grid(row=4)
entry_tags = Entry()
entry_tags.grid(row=5)
label_count = Label(text="Grab Count:")
label_count.grid(row=6)
entry_count = Entry()
entry_count.grid(row=7)
button_start = Button(text="Start Grabbing", width=12, command=lambda:start_grabbing())
button_start.grid(row=8)

window.mainloop()