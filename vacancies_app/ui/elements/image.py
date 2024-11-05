import ttkbootstrap as ttk
from PIL import Image as Img, ImageTk


class Image:
    def __init__(self, path, window, relx, rely, anchor):
        self.window = window
        self.path = path
        self.label = self.create_label(relx, rely, anchor)

    def create_label(self, relx, rely, anchor):
        image = Img.open(self.path)
        resized_image = image.resize((400, 400))
        photo = ImageTk.PhotoImage(resized_image)
        label = ttk.Label(self.window, image=photo)
        label.image = photo
        label.place(relx=relx, rely=rely, anchor=anchor)
        return label

    def remove(self):
        self.label.place_forget()



