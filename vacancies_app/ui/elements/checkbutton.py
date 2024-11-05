import ttkbootstrap as ttk


class CheckButton:
    def __init__(self, window, text, relx, rely, anchor):
        self.window = window
        self.check_var = ttk.BooleanVar()
        self.button = self.create(text, relx, rely, anchor)
        self.text = text

    def create(self, text, relx, rely, anchor):

        button = ttk.Checkbutton(
            self.window,
            text=text,
            variable=self.check_var,
            bootstyle="danger-round-toggle",

        )

        button.place(relx=relx, rely=rely, anchor=anchor)
        return button

    def get_query_value(self):
        exp_dict = {
            'Без опыта': 'noExperience',
            'Опыт от 1 до 3 лет': 'between1And3'
        }

        value = exp_dict[self.text] if self.check_var.get() else None
        return value

    def remove(self):
        self.button.place_forget()
