from vacancies_app.services.vacancies import get_filtered_vacancies
from vacancies_app.ui.elements.buttons import MainButton, ActiveButton
from vacancies_app.ui.elements.checkbutton import CheckButton
from vacancies_app.ui.elements.gif import Gif
from vacancies_app.ui.elements.image import Image
from vacancies_app.ui.elements.music import Music
from vacancies_app.ui.elements.scrolled_text import ScrolledText
from vacancies_app.ui.elements.text import Text


class Layout:
    def __init__(self, window):
        self.window = window
        self.main_button = MainButton(window, self.action)
        self.no_experience_btn = CheckButton(window, 'Без опыта', 0.5, 0.7, "center")
        self.experience_btn = CheckButton(window, 'Опыт от 1 до 3 лет', 0.5, 0.75, "center")
        self.music = Music(r'./media/music/music.mp3')
        self.active_button = ActiveButton(self.window)
        self.congrats_gif = Gif(r'./media/gif/congrats.gif', self.window, 0.5, 0.3, "center")
        self.cat_gif = Gif(r'./media/gif/cat.gif', self.window, 0.5, 0.3, "center")
        self.image = Image(r'./media/image/cat.png', window, 0.5, 0.4, "center")

    def action(self):
        self.image.remove()
        self.main_button.remove()
        self.experience_btn.remove()
        self.no_experience_btn.remove()

        experience = [self.no_experience_btn.get_query_value(), self.experience_btn.get_query_value()]
        filtered_experience = list(filter(lambda exp: exp is not None, experience))

        self.cat_gif.show()
        self.music.play()
        self.active_button.show()

        vacancies = get_filtered_vacancies(self.active_button, filtered_experience)
        Text(self.window, "Готово!\nВы откликнулись на:", 0.5, 0.55, "center")
        ScrolledText(self.window, vacancies)

        self.cat_gif.remove()
        self.active_button.remove()
        self.congrats_gif.show()
        self.music.stop()
