from __future__ import unicode_literals
from pybooru import Moebooru
import requests
import os
import psutil

def checkDiskSpace():
    path = "/"
    bytes_avail = psutil.disk_usage(path).free
    gigabytes_avail = bytes_avail / 1024 / 1024 / 1024
    return gigabytes_avail

def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    if iteration == total: 
        print()

def grab(*grab_tags:str, grab_count:int, source:str):
    client = Moebooru(site_url="https://"+source)
    posts = client.post_list(tags=grab_tags, limit=grab_count)
    count = 0
    os.system("cls")
    print("\u001b[31;1m" + " __ __  _  _         ___                 ")
    print("\u001b[31;1m" + "|  \  \<_>| |__ ___ | . \ ___  ___  ___  ")
    print("\u001b[31;1m" + "|     || || / /<_> ||  _// . \| . \| . \ ")
    print("\u001b[31;1m" + "|_|_|_||_||_\_\<___||_|  \___/|  _/|  _/ ")
    print("\u001b[31;1m" + "                              |_|  |_|   ")
    print("\u001b[32m" + "Start grabbing...")
    if(len(grab_count) == 0):
            print("No grab count specified!")
            print("returning...")
            os.system('python gui.py')
    else:
        if((float(checkDiskSpace())-(float(grab_count)*5/1024)) >= 0):
            if(not posts):
                print("There wasn't any post to grab!")
                print("returning...")
                os.system('python gui.py')
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
                os.system('python gui.py')
        else:
            print("Not enough disk space!")
            print("returning...")
            os.system('python gui.py')