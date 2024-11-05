import threading
import ttkbootstrap as ttk


class MainButton:
    def __init__(self, window, action):
        self.window = window
        self.button = ttk.Button(self.window,
                                 text='Откликнуться',
                                 padding=(10, 10),
                                 width=50,
                                 bootstyle="danger",
                                 command=lambda: threading.Thread(target=action).start()
                                 )
        self.button.place(relx=0.5, rely=0.85, anchor="center")

    def remove(self):
        self.button.place_forget()


class ActiveButton:
    def __init__(self, window):
        self.window = window
        self.active_button = ttk.Floodgauge(self.window,
                                            bootstyle="danger",
                                            length=300,
                                            font=("Helvetica", 16),
                                            value=0,
                                            text="В процессе..."
                                            )

    def show(self):
        self.active_button.place(relx=0.5, rely=0.7, anchor="center")

    def update(self, step):
        self.active_button.step(step)
        if self.active_button["value"] >= 100:
            self.active_button.configure(text="Завершено!", bootstyle="info")

    def remove(self):
        self.active_button.place_forget()
