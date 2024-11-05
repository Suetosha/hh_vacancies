from vacancies_app.ui.layout import Layout
from vacancies_app.ui.window import init_window


def main():
    current_window = init_window()
    Layout(current_window)
    current_window.mainloop()


if __name__ == '__main__':
    main()



