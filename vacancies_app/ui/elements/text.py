from tkinter import ttk


class Text:
    def __init__(self, window, text, relx, rely, anchor):
        self.window = window
        self.text = self.create(text, relx, rely, anchor)

    def create(self, text, relx, rely, anchor):
        text_label = ttk.Label(self.window, text=text, justify="center", font=("Helvetica", 25))
        text_label.place(relx=relx, rely=rely, anchor=anchor)
        return text_label

