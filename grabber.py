from __future__ import unicode_literals
from pybooru import Moebooru
import requests
import os

def grab(*grab_tags:str, grab_count:int, source:str):
    client = Moebooru(site_url="https://"+source)
    posts = client.post_list(tags=grab_tags, limit=grab_count)
    for post in posts:
        image_url = post["file_url"]
        image_name = image_url.split("/")[-1]
        image_path = os.getcwd()+"/pictures/"
        img_data = requests.get(image_url).content
        with open(image_path+image_name, "wb") as handler:
            handler.write(img_data)