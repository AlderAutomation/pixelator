from typing import Text
from PIL import Image, ImageTk
import tkinter as tk 


class application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.size = 0
        self.path = "/media/matthew/BigOlUSB/Code/2021_Project/Pixel Art Generator/guns.png"


    def create_widgets(self):
        # test_image = ImageTk.PhotoImage(Image.open("/media/matthew/BigOlUSB/Code/2021_Project/Pixel Art Generator/guns.png"))
        # self.image_viewer =  tk.Label(image=test_image)
        # self.image_viewer.grid(row=0, column=0, columnspan=2)

        self.button_32 = tk.Button(self, text="32 X 32", command=self.set_size_32)
        self.button_32.grid(row=1, column=0)

        self.button_64 = tk.Button(self, text="64 X 64", command=self.set_size_64)
        self.button_64.grid(row=1, column=1)

        self.test_button = tk.Button(self, text="Test Image", command=self.show_image)
        self.test_button.grid(row=2, column=0)

        self.save_button = tk.Button(self, text="Save Image", command=self.save_image)
        self.save_button.grid(row=2, column=1)


    def set_size_32(self):
        self.size = (32,32)


    def set_size_64(self):
        self.size = (64,64)


    def save_image(self):
        pass


    def show_image(self):
        img = self.load_image()
        self.convert_to_pixel(img)


    def load_image(self):
        img = Image.open(self.path)
        
        return img


    def convert_to_pixel(self, img):
        img_32x32 = img.resize((self.size), resample=Image.NEAREST)
        result = img_32x32.resize(img.size, Image.NEAREST)

        print (result.show())


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x600")
    root.title("Pixelator")
    app = application(master=root)

    app.mainloop()
