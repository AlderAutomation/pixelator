from typing import Text
from PIL import Image, ImageTk
import tkinter as tk 
from tkinter import filedialog as fd


class application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()
        self.grid()
        self.size = 0
        self.path = ""
        self.img = ""


    def create_widgets(self):
        self.load_button = tk.Button(self, text="Load Image", command=self.load_image)
        self.load_button.grid(row=0, column=0)

        self.logo = Image.open("/media/matthew/BigOlUSB/Code/2021_Project/Pixel Art Generator/logo.png")
        self.logoimg = ImageTk.PhotoImage(self.logo)

        self.image_viewer = tk.Label(self, image=self.logoimg)
        self.image_viewer.grid(row=1, column=0, columnspan=2)

        self.button_32 = tk.Button(self, text="32 X 32", command=self.set_size_32)
        self.button_32.grid(row=2, column=0)

        self.button_64 = tk.Button(self, text="64 X 64", command=self.set_size_64)
        self.button_64.grid(row=2, column=1)

        self.test_button = tk.Button(self, text="Test Image", command=self.show_image)
        self.test_button.grid(row=3, column=0)

        self.save_button = tk.Button(self, text="Save Image", command=self.save_image)
        self.save_button.grid(row=3, column=1)


    def set_size_32(self):
        self.size = (32,32)


    def set_size_64(self):
        self.size = (64,64)


    def save_image(self):
        pass


    def show_image(self):
        self.convert_to_pixel()


    def load_image(self):
        self.path = fd.askopenfilename()
        self.img = Image.open(self.path)
        

    def convert_to_pixel(self):
        img_32x32 = self.img.resize((self.size), resample=Image.NEAREST)
        result = img_32x32.resize(self.img.size, Image.NEAREST)
        self.image_viewer.image=result

        print (result.show())


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1600x1200")
    root.title("Pixelator")
    app = application(master=root)
    app.mainloop()
