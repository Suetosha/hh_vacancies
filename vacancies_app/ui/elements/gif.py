from PIL import Image, ImageTk, ImageSequence
import ttkbootstrap as ttk


class Gif:
    def __init__(self, path, window, relx, rely, anchor):
        self.path = path
        self.window = window
        self.label, self.frames = self.create_label(relx, rely, anchor), self.create_frames()

    def create_frames(self):
        gif = Image.open(self.path)
        frames = [ImageTk.PhotoImage(frame.copy().resize((500, 300))) for frame in ImageSequence.Iterator(gif)]
        return frames

    def create_label(self, relx, rely, anchor):
        label = ttk.Label(self.window)
        label.place(relx=relx, rely=rely, anchor=anchor)
        label.lower()
        return label

    def show(self):
        self.label.lift()
        self.update_frame(0)

    def update_frame(self, index):
        frame = self.frames[index]
        self.label.config(image=frame)
        self.window.after(100, self.update_frame, (index + 1) % len(self.frames))

    def remove(self):
        self.label.place_forget()

