from tkinter import *
from PIL import Image, ImageTk, ImageEnhance, ImageOps, ImageDraw, ImageFilter
import random
import os

root = Tk()
root.title("Photoshoppe")
root.geometry("1000x420")
root.config(bg="teal")

''' MODEL - Functions and Data'''
def load_image():
    global loaded_image
    file_name = pic_entry.get()
    try:
        img = Image.open(file_name)
        width, height = img.size
        if width > height:
            loaded_image = img.resize((600, 400), Image.LANCZOS)
        else: 
            multiplier = 400 / height
            loaded_image = img.resize((int(width * multiplier), 400), Image.LANCZOS)
        display_image(loaded_image)
    except FileNotFoundError:
        print("File not found. Please check the file name.")

def display_image(image):
    global loaded_image
    loaded_image = image
    root.photo_image = ImageTk.PhotoImage(loaded_image)
    canvas.create_image(300, 200, image=root.photo_image)

def apply_black_and_white():
    if load_image:
        pixels = load_image.load()
        for y in range(load_image.height):
            for x in range(load_image.width):
                r,g,b = pixels[x,y]
                avg = int((r+g+b)/3)
                pixels[x,y]=(avg,avg,avg)
        display_image(load_image)

# Save the modified image
def save_image():
    if loaded_image:
        file_name = pic_entry.get()
        base, ext = os.path.splitext(file_name)
        modified_file_name = f"{base}_modified.png"
        loaded_image.save(modified_file_name)
        print(f"Image saved as {modified_file_name}")

''' CONTROLLERS - Widgets That Users Interact With'''



''' VIEW - Widgets That Display Visuals'''

root.mainloop()
