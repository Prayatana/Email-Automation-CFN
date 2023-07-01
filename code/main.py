from PIL import Image, ImageDraw, ImageFont, ImageColor
import time
import os
import pandas as pd


try:
    os.mkdir("out")
except:
    pass

df = pd.read_csv("email.csv")

for _, row in df.iterrows():
    img = Image.open(os.getcwd() + "/Selected.png")

    draw = ImageDraw.Draw(img)

    text = str(row["name"])
    
    first_name = " ".join(text.split(" ")[:-1])
    first_name = first_name


    last_name = text.split(" ")[-1]

    font = ImageFont.truetype('font/NexaScriptLight.ttf', 600)

    _, _, w_f, h_f = draw.textbbox((0, 0), first_name, font=font)

    _, _, w_l, h_l = draw.textbbox((0,0), last_name, font=font)

    if (w_f > img.size[0] or w_l > img.size[0]):
        print(text)
        continue


    draw.text(((img.size[0] - w_f) / 2, 2100 - h_l - 10), first_name, font=font, fill="#fff")
    draw.text(((img.size[0] - w_l) / 2, 2100), last_name, font=font, fill="#fff")

    img.save(f"out/{'_'.join(text.lower().split())}.png")

