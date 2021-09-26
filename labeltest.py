from typing import Text
from PIL import Image, ImageTk
import tkinter as tk 
from tkinter import filedialog as fd



root = tk.Tk()

logo = Image.open("/media/matthew/BigOlUSB/Code/2021_Project/Pixel Art Generator/Logo Transparent.png")
logoimg = ImageTk.PhotoImage(logo)

root.image_viewer =  tk.Label(root, image=logoimg)
root.image_viewer.grid(row=1, column=0)



root.mainloop()