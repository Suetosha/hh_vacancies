import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import scrolledtext
import tkinter as tk


class ScrolledText:
    def __init__(self, window, text):
        self.window = window
        self.text_area = self.create(text)

    def create(self, text):
        scrolled_text = scrolledtext.ScrolledText(self.window,
                                                  font=("Helvetica", 14),
                                                  width=70,
                                                  height=13
                                                  )
        scrolled_text.place(relx=0.5, rely=0.8, anchor="center")
        scrolled_text.insert(tk.INSERT, text)
        scrolled_text.configure(state='disabled')
        return scrolled_text


